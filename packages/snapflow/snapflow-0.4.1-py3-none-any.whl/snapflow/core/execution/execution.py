from __future__ import annotations

import traceback
from collections import abc, defaultdict
from contextlib import contextmanager
from dataclasses import dataclass, field
from enum import Enum
from io import IOBase
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    Iterator,
    List,
    Optional,
    Set,
    Tuple,
)

import dcp
import sqlalchemy
from commonmodel.base import Schema, SchemaLike
from dcp.data_format.base import DataFormat, get_format_for_nickname
from dcp.data_format.handler import get_handler_for_name, infer_format_for_name
from dcp.storage.base import Storage
from dcp.utils.common import rand_str, utcnow
from loguru import logger
from snapflow.core.data_block import (
    Alias,
    DataBlockMetadata,
    ManagedDataBlock,
    StoredDataBlockMetadata,
    get_datablock_id,
    get_stored_datablock_id,
)
from snapflow.core.environment import Environment
from snapflow.core.execution.executable import (
    CumulativeExecutionResult,
    Executable,
    ExecutionContext,
    ExecutionResult,
)
from snapflow.core.metadata.api import MetadataApi
from snapflow.core.node import DataBlockLog, Direction, Node, SnapLog, get_state
from snapflow.core.snap import (
    DEFAULT_OUTPUT_NAME,
    DataInterfaceType,
    InputExhaustedException,
    _Snap,
)
from snapflow.core.snap_interface import (
    BoundInterface,
    NodeInterfaceManager,
    StreamInput,
)
from snapflow.core.typing.casting import cast_to_realized_schema
from snapflow.utils.output import cf, error_symbol, success_symbol
from sqlalchemy.sql.expression import select


class ImproperlyStoredDataBlockException(Exception):
    pass


def validate_data_blocks(env: Environment):
    # TODO: More checks?
    env.md_api.flush()
    for obj in env.md_api.active_session.identity_map.values():
        if isinstance(obj, DataBlockMetadata):
            urls = set([sdb.storage_url for sdb in obj.stored_data_blocks])
            if all(u.startswith("python") for u in urls):
                fmts = set([sdb.data_format for sdb in obj.stored_data_blocks])
                if all(not f.is_storable() for f in fmts):
                    raise ImproperlyStoredDataBlockException(
                        f"DataBlock {obj} is not properly stored (no storeable format(s): {fmts})"
                    )


@dataclass(frozen=True)
class SnapContext:  # TODO: (Generic[C, S]):
    env: Environment
    snap: _Snap
    node: Node
    executable: Executable
    metadata_api: MetadataApi
    inputs: List[StreamInput]
    bound_interface: BoundInterface
    snap_log: SnapLog
    execution_context: ExecutionContext
    input_blocks_processed: Dict[str, Set[DataBlockMetadata]] = field(
        default_factory=lambda: defaultdict(set)
    )
    output_blocks_emitted: Dict[str, StoredDataBlockMetadata] = field(
        default_factory=dict
    )

    @contextmanager
    def as_tmp_local_object(self, obj: Any) -> str:
        tmp_name = "_tmp_obj_" + rand_str()
        self.execution_context.local_storage.get_api().put(tmp_name, obj)
        yield tmp_name
        self.execution_context.local_storage.get_api().remove(tmp_name)

    def ensure_log(self, block: DataBlockMetadata, direction: Direction, name: str):
        if self.metadata_api.execute(
            select(DataBlockLog).filter_by(
                snap_log_id=self.snap_log.id,
                stream_name=name,
                data_block_id=block.id,
                direction=direction,
            )
        ).scalar_one_or_none():
            return
        drl = DataBlockLog(  # type: ignore
            snap_log_id=self.snap_log.id,
            stream_name=name,
            data_block_id=block.id,
            direction=direction,
            processed_at=utcnow(),
        )
        self.metadata_api.add(drl)

    def finish_execution(self):
        logger.debug("Finishing execution")
        self.log_all()
        # TODO: multiple aliases support?
        sdb = self.output_blocks_emitted.get(DEFAULT_OUTPUT_NAME)
        if sdb is not None:
            self.create_alias(sdb)
        self.metadata_api.flush()

    # def create_aliases(self):
    #     for output_name, sdb in self.output_blocks_emitted.items():
    #         if output_name
    #         self.create_alias(sdb)

    def log_all(self):
        # Do this one last time (in case no output emitted, like an exporter):
        self.log_processed_input_blocks()
        for input_name, blocks in self.input_blocks_processed.items():
            for block in blocks:
                self.ensure_log(block, Direction.INPUT, input_name)
                logger.debug(f"Input logged: {block}")
        for output_name, sdb in self.output_blocks_emitted.items():
            self.metadata_api.add(sdb.data_block)
            self.metadata_api.add(sdb)
            logger.debug(f"Output logged: {sdb.data_block}")
            self.ensure_log(sdb.data_block, Direction.OUTPUT, output_name)

    def get_snap_args(self) -> Tuple[List, Dict]:
        snap_args = []
        if self.bound_interface.context:
            snap_args.append(self)
        snap_inputs = self.bound_interface.inputs_as_kwargs()
        snap_kwargs = snap_inputs
        return (snap_args, snap_kwargs)

    def get_param(self, key: str, default: Any = None) -> Any:
        if default is None:
            try:
                default = self.snap.get_param(key).default
            except KeyError:
                pass
        return self.node.params.get(key, default)

    def get_params(self, defaults: Dict[str, Any] = None) -> Dict[str, Any]:
        final_params = {p.name: p.default for p in self.snap.params}
        final_params.update(defaults or {})
        final_params.update(self.node.params)
        return final_params

    def get_state_value(self, key: str, default: Any = None) -> Any:
        assert isinstance(self.snap_log.node_end_state, dict)
        return self.snap_log.node_end_state.get(key, default)

    def get_state(self) -> Dict[str, Any]:
        return self.snap_log.node_end_state

    def emit_state_value(self, key: str, new_value: Any):
        new_state = self.snap_log.node_end_state.copy()
        new_state[key] = new_value
        self.snap_log.node_end_state = new_state

    def emit_state(self, new_state: Dict):
        self.snap_log.node_end_state = new_state

    def emit(
        self,
        records_obj: Any = None,
        name: str = None,
        storage: Storage = None,
        output: str = DEFAULT_OUTPUT_NAME,
        data_format: DataFormat = None,
        schema: SchemaLike = None,
        update_state: Dict[str, Any] = None,
        replace_state: Dict[str, Any] = None,
    ):
        assert records_obj is not None or (
            name is not None and storage is not None
        ), "Emit takes either records_obj, or name and storage"
        if schema is not None:
            schema = self.env.get_schema(schema)
        if data_format is not None:
            if isinstance(data_format, str):
                data_format = get_format_for_nickname(data_format)
        self.handle_emit(
            records_obj, name, storage, output, data_format=data_format, schema=schema
        )
        if update_state is not None:
            for k, v in update_state.items():
                self.emit_state_value(k, v)
        if replace_state is not None:
            self.emit_state(replace_state)
        # Commit input blocks to db as well, to save progress
        self.log_processed_input_blocks()

    def create_alias(self, sdb: StoredDataBlockMetadata) -> Optional[Alias]:
        self.metadata_api.flush([sdb.data_block, sdb])
        alias = sdb.create_alias(self.env, self.node.get_alias())
        self.metadata_api.flush([alias])
        return alias

    def create_stored_datablock(self) -> StoredDataBlockMetadata:
        block = DataBlockMetadata(
            id=get_datablock_id(),
            inferred_schema_key=None,
            nominal_schema_key=None,
            realized_schema_key="Any",
            record_count=None,
            created_by_node_key=self.node.key,
        )
        sdb = StoredDataBlockMetadata(  # type: ignore
            id=get_stored_datablock_id(),
            data_block_id=block.id,
            data_block=block,
            storage_url=self.execution_context.local_storage.url,
            data_format=None,
        )
        return sdb

    def get_stored_datablock_for_output(self, output: str) -> StoredDataBlockMetadata:
        sdb = self.output_blocks_emitted.get(output)
        if sdb is None:
            self.output_blocks_emitted[output] = self.create_stored_datablock()
            return self.get_stored_datablock_for_output(output)
        return sdb

    def handle_emit(
        self,
        records_obj: Any = None,
        name: str = None,
        storage: Storage = None,
        output: str = DEFAULT_OUTPUT_NAME,
        data_format: DataFormat = None,
        schema: SchemaLike = None,
    ):
        logger.debug(
            f"HANDLING EMITTED OBJECT (of type '{type(records_obj).__name__}')"
        )
        # TODO: can i return an existing DataBlock? Or do I need to create a "clone"?
        #   Answer: ok to return as is (just mark it as 'output' in DBL)
        if isinstance(records_obj, StoredDataBlockMetadata):
            # TODO is it in local storage tho? we skip conversion below...
            # This is just special case right now to support SQL snap
            # Will need better solution for explicitly creating DB/SDBs inside of snaps
            return records_obj
        elif isinstance(records_obj, DataBlockMetadata):
            raise NotImplementedError
        elif isinstance(records_obj, ManagedDataBlock):
            raise NotImplementedError
        nominal_output_schema = schema
        if nominal_output_schema is None:
            nominal_output_schema = self.bound_interface.resolve_nominal_output_schema(
                self.env
            )  # TODO: could check output to see if it is LocalRecords with a schema too?
        if nominal_output_schema is not None:
            nominal_output_schema = self.env.get_schema(nominal_output_schema)
        sdb = self.get_stored_datablock_for_output(output)
        sdb.data_format = data_format
        db = sdb.data_block
        if db.nominal_schema_key and db.nominal_schema_key != nominal_output_schema.key:
            raise Exception(
                "Mismatch nominal schemas {db.nominal_schema_key} - {nominal_output_schema.key}"
            )
        db.nominal_schema_key = nominal_output_schema.key
        if records_obj is not None:
            name = "_tmp_obj_" + rand_str(10)
            storage = self.execution_context.local_storage
            storage.get_api().put(name, records_obj)
            if nominal_output_schema is not None:
                # TODO: still unclear on when and why to do this cast
                handler = get_handler_for_name(name, storage)
                handler().cast_to_schema(name, storage, nominal_output_schema)
        sdb.storage_url = storage.url
        assert name is not None
        assert storage is not None
        self.append_records_to_stored_datablock(name, storage, sdb)
        return sdb

    def resolve_new_object_with_data_block(
        self, sdb: StoredDataBlockMetadata, name: str, storage: Storage
    ):
        handler = get_handler_for_name(name, storage)
        inferred_schema = handler().infer_schema(name, storage)
        self.env.add_new_generated_schema(inferred_schema)
        if sdb.data_block.realized_schema_key in (None, "Any"):
            # Cast to nominal if no existing realized schema
            realized_schema = cast_to_realized_schema(
                self.env,
                inferred_schema=inferred_schema,
                nominal_schema=sdb.nominal_schema(self.env),
            )
        else:
            # If already a realized schema, conform new inferred schema to existing realized
            realized_schema = cast_to_realized_schema(
                self.env,
                inferred_schema=inferred_schema,
                nominal_schema=sdb.data_block.realized_schema(self.env),
            )
        self.env.add_new_generated_schema(realized_schema)
        sdb.data_block.realized_schema_key = realized_schema.key
        logger.debug(
            f"Inferred schema: {inferred_schema.key} {inferred_schema.fields_summary()}"
        )
        logger.debug(
            f"Realized schema: {realized_schema.key} {realized_schema.fields_summary()}"
        )
        if sdb.data_block.nominal_schema_key:
            logger.debug(
                f"Nominal schema: {sdb.data_block.nominal_schema_key} {sdb.data_block.nominal_schema(self.env).fields_summary()}"
            )

    def append_records_to_stored_datablock(
        self, name: str, storage: Storage, sdb: StoredDataBlockMetadata
    ):
        self.resolve_new_object_with_data_block(sdb, name, storage)
        if sdb.data_format is None:
            fmt = infer_format_for_name(name, storage)
            # if sdb.data_format and sdb.data_format != fmt:
            #     raise Exception(f"Format mismatch {fmt} - {sdb.data_format}")
            if fmt is None:
                raise Exception(f"Could not infer format {name} on {storage}")
            sdb.data_format = fmt
        # TODO: to_format
        # TODO: make sure this handles no-ops (empty object, same storage)
        # TODO: copy or alias? sometimes we are just moving temp obj to new name, dont need copy
        result = dcp.copy(
            from_name=name,
            from_storage=storage,
            to_name=sdb.get_name_for_storage(),
            to_storage=sdb.storage,
            to_format=sdb.data_format,
            available_storages=self.execution_context.storages,
            if_exists="append",
        )
        logger.debug(f"Copied {result}")
        logger.debug(f"REMOVING NAME {name}")
        storage.get_api().remove(name)

    def log_processed_input_blocks(self):
        for input in self.bound_interface.inputs:
            if input.bound_stream is not None:
                for db in input.bound_stream.get_emitted_blocks():
                    self.input_blocks_processed[input.name].add(db)

    def should_continue(self) -> bool:
        """
        Long running snaps should check this function periodically
        to honor time limits.
        """
        if not self.execution_context.execution_timelimit_seconds:
            return True
        seconds_elapsed = (utcnow() - self.snap_log.started_at).total_seconds()
        return seconds_elapsed < self.execution_context.execution_timelimit_seconds

    def as_execution_result(self) -> ExecutionResult:
        input_block_counts = {}
        for input_name, dbs in self.input_blocks_processed.items():
            input_block_counts[input_name] = len(dbs)
        output_blocks = {}
        for output_name, sdb in self.output_blocks_emitted.items():
            alias = sdb.get_alias(self.env)
            output_blocks[output_name] = {
                "id": sdb.data_block_id,
                "record_count": sdb.record_count(),
                "alias": alias.alias if alias else None,
            }
        return ExecutionResult(
            inputs_bound=list(self.bound_interface.inputs_as_kwargs().keys()),
            non_reference_inputs_bound=self.bound_interface.non_reference_bound_inputs(),
            input_block_counts=input_block_counts,
            output_blocks=output_blocks,
            error=self.snap_log.error.get("error")
            if isinstance(self.snap_log.error, dict)
            else None,
            traceback=self.snap_log.error.get("traceback")
            if isinstance(self.snap_log.error, dict)
            else None,
        )


class ExecutionManager:
    def __init__(self, exe: Executable):
        self.exe = exe
        self.env = exe.execution_context.env
        self.logger = exe.execution_context.logger
        self.node = self.exe.node

    def execute(self) -> ExecutionResult:
        # Setup for run
        base_msg = (
            f"Running node {cf.bold(self.node.key)} {cf.dimmed(self.node.snap.key)}\n"
        )
        logger.debug(
            f"RUNNING NODE {self.node.key} {self.node.snap.key} with params `{self.node.params}`"
        )
        self.logger.log(base_msg)
        with self.logger.indent():
            result = self._execute()
            self.log_execution_result(result)
            if not result.error:
                self.logger.log(cf.success("Ok " + success_symbol + "\n"))  # type: ignore
            else:
                error = result.error or "Snap failed (unknown error)"
                self.logger.log(cf.error("Error " + error_symbol + " " + cf.dimmed(error[:80])) + "\n")  # type: ignore
                if result.traceback:
                    self.logger.log(cf.dimmed(result.traceback), indent=2)  # type: ignore
            logger.debug(f"Execution result: {result}")
            logger.debug(f"*DONE* RUNNING NODE {self.node.key} {self.node.snap.key}")
        return result

    def _execute(self) -> ExecutionResult:
        with self.env.md_api.begin():
            interface_mgr = NodeInterfaceManager(self.exe)
            try:
                bound_interface = interface_mgr.get_bound_interface()
            except InputExhaustedException as e:
                logger.debug(f"Inputs exhausted {e}")
                raise e
                # return ExecutionResult.empty()
            with self.start_snap_run(self.node, bound_interface) as snap_ctx:
                # snap = executable.compiled_snap.snap
                # local_vars = locals()
                # if hasattr(snap, "_locals"):
                #     local_vars.update(snap._locals)
                # exec(snap.get_source_code(), globals(), local_vars)
                # output_obj = local_vars[snap.snap_callable.__name__](
                snap_args, snap_kwargs = snap_ctx.get_snap_args()
                output_obj = snap_ctx.snap.snap_callable(*snap_args, **snap_kwargs,)
                if output_obj is not None:
                    self.emit_output_object(output_obj, snap_ctx)
            result = snap_ctx.as_execution_result()
        logger.debug(f"EXECUTION RESULT {result}")
        return result

    def emit_output_object(
        self, output_obj: DataInterfaceType, snap_ctx: SnapContext,
    ):
        assert output_obj is not None
        if isinstance(output_obj, abc.Generator):
            output_iterator = output_obj
        else:
            output_iterator = [output_obj]
        i = 0
        for output_obj in output_iterator:
            logger.debug(output_obj)
            i += 1
            snap_ctx.emit(output_obj)

    @contextmanager
    def start_snap_run(
        self, node: Node, bound_interface: BoundInterface
    ) -> Iterator[SnapContext]:
        from snapflow.core.graph import GraphMetadata

        # assert self.current_runtime is not None, "Runtime not set"
        md = self.env.get_metadata_api()
        node_state_obj = node.get_state(self.env)
        if node_state_obj is None:
            node_state = {}
        else:
            node_state = node_state_obj.state
        new_graph_meta = node.graph.get_metadata_obj()
        graph_meta = md.execute(
            select(GraphMetadata).filter(GraphMetadata.hash == new_graph_meta.hash)
        ).scalar_one_or_none()
        if graph_meta is None:
            md.add(new_graph_meta)
            md.flush()  # [new_graph_meta])
            graph_meta = new_graph_meta

        snap_log = SnapLog(  # type: ignore
            graph_id=graph_meta.hash,
            node_key=node.key,
            node_start_state=node_state.copy(),  # {k: v for k, v in node_state.items()},
            node_end_state=node_state,
            snap_key=node.snap.key,
            snap_params=node.params,
            # runtime_url=self.current_runtime.url,
            started_at=utcnow(),
        )
        md.add(snap_log)
        md.flush([snap_log])
        snap_ctx = SnapContext(
            env=self.env,
            snap=self.exe.snap,
            node=self.exe.node,
            executable=self.exe,
            metadata_api=self.env.md_api,
            inputs=bound_interface.inputs,
            snap_log=snap_log,
            bound_interface=bound_interface,
            execution_context=self.exe.execution_context,
        )
        try:
            yield snap_ctx
            # Validate local memory objects: Did we leave any non-storeables hanging?
            validate_data_blocks(self.env)
        except Exception as e:
            # Don't worry about exhaustion exceptions
            if not isinstance(e, InputExhaustedException):
                logger.debug(f"Error running node:\n{traceback.format_exc()}")
                snap_log.set_error(e)
                snap_log.persist_state(self.env)
                snap_log.completed_at = utcnow()
                # TODO: should clean this up so transaction surrounds things that you DO
                #       want to rollback, obviously
                # md.commit()  # MUST commit here since the re-raised exception will issue a rollback
                if self.exe.execution_context.abort_on_snap_error:
                    raise e
        finally:
            snap_ctx.finish_execution()
            # Persist state on success OR error:
            snap_log.persist_state(self.env)
            snap_log.completed_at = utcnow()

    def log_execution_result(self, result: ExecutionResult):
        self.logger.log("Inputs: ")
        if result.input_block_counts:
            self.logger.log("\n")
            with self.logger.indent():
                for input_name, cnt in result.input_block_counts.items():
                    self.logger.log(f"{input_name}: {cnt} block(s) processed\n")
        else:
            if not result.non_reference_inputs_bound:
                self.logger.log_token("n/a\n")
            else:
                self.logger.log_token("None\n")
        self.logger.log("Outputs: ")
        if result.output_blocks:
            self.logger.log("\n")
            with self.logger.indent():
                for output_name, block_summary in result.output_blocks.items():
                    self.logger.log(f"{output_name}:")
                    cnt = block_summary["record_count"]
                    alias = block_summary["alias"]
                    if cnt is not None:
                        self.logger.log_token(f" {cnt} records")
                    self.logger.log_token(
                        f" {alias} " + cf.dimmed(f"({block_summary['id']})\n")  # type: ignore
                    )
        else:
            self.logger.log_token("None\n")


def execute_to_exhaustion(
    exe: Executable, to_exhaustion: bool = True
) -> Optional[CumulativeExecutionResult]:
    cum_result = CumulativeExecutionResult()
    while True:
        em = ExecutionManager(exe)
        try:
            result = em.execute()
        except InputExhaustedException:
            return cum_result
        cum_result.add_result(result)
        if (
            not to_exhaustion or not result.non_reference_inputs_bound
        ):  # TODO: We just run no-input DFs (sources) once no matter what
            # (they are responsible for creating their own generators)
            break
    return cum_result
