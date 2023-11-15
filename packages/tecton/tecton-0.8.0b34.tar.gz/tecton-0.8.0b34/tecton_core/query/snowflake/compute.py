import logging
import threading
import typing
from typing import Optional
from urllib.parse import urlparse

import attrs
import pandas as pd
import pyarrow
import snowflake.connector
import snowflake.snowpark
import sqlparse
from snowflake.snowpark.functions import col

from tecton_core import compute_mode
from tecton_core import conf
from tecton_core.errors import TectonValidationError
from tecton_core.query.dialect import Dialect
from tecton_core.query.errors import SQLCompilationError
from tecton_core.query.errors import UserDefinedTransformationError
from tecton_core.query.node_interface import NodeRef
from tecton_core.query.node_utils import get_batch_data_sources
from tecton_core.query.query_tree_compute import QueryTreeCompute
from tecton_core.snowflake_context import SnowflakeContext
from tecton_core.specs import SnowflakeSourceSpec
from tecton_core.time_utils import convert_pandas_df_for_snowflake_upload


_SNOWFLAKE_HOST_SUFFIX = ".snowflakecomputing.com"


def _get_single_field(sources: typing.List[SnowflakeSourceSpec], field: str) -> str:
    values = set()
    for spec in sources:
        values.add(getattr(spec, field))
    assert len(values) == 1, f"Conflicting values for `{field}` among Snowflake data sources: {values}"
    return values.pop()


@attrs.define
class SnowflakeCompute(QueryTreeCompute):
    session: snowflake.snowpark.Session
    lock: threading.RLock = threading.RLock()
    is_debug: bool = attrs.field(init=False)

    def __attrs_post_init__(self):
        self.is_debug = conf.get_bool("DUCKDB_DEBUG")

    @staticmethod
    def from_context() -> "SnowflakeCompute":
        return SnowflakeCompute(session=SnowflakeContext.get_instance().get_session())

    @staticmethod
    def for_connection(connection: snowflake.connector.SnowflakeConnection) -> "SnowflakeCompute":
        return SnowflakeCompute(session=snowflake.snowpark.Session.builder.configs({"connection": connection}).create())

    @staticmethod
    def for_query_tree(root: NodeRef) -> "SnowflakeCompute":
        """Initializes a connection based on the warehouse/url specified in the batch sources in the tree, and the
        user/password from tecton.conf.
        """
        user = conf.get_or_none("SNOWFLAKE_USER")
        password = conf.get_or_none("SNOWFLAKE_PASSWORD")
        if not user or not password:
            msg = "Snowflake user and password not configured. Instructions at https://docs.tecton.ai/docs/setting-up-tecton/connecting-data-sources/connecting-to-a-snowflake-data-source-using-spark"
            raise TectonValidationError(msg, can_drop_traceback=True)

        snowflake_sources: typing.List[SnowflakeSourceSpec] = get_batch_data_sources(root, SnowflakeSourceSpec)
        url = _get_single_field(snowflake_sources, "url")
        if url is None:
            msg = "Snowflake URL must be specified"
            raise TectonValidationError(msg, can_drop_traceback=True)

        host = urlparse(url).hostname
        if not host.endswith(_SNOWFLAKE_HOST_SUFFIX):
            msg = f"Snowflake URL host must end in {_SNOWFLAKE_HOST_SUFFIX}, but was {url}"
            raise TectonValidationError(msg, can_drop_traceback=True)

        account = host[: -len(_SNOWFLAKE_HOST_SUFFIX)]
        warehouse = _get_single_field(snowflake_sources, "warehouse")
        if warehouse is None:
            msg = "Snowflake warehouse must be specified"
            raise TectonValidationError(msg, can_drop_traceback=True)
        # The "database" parameter is not needed by the query itself,
        # but it's useful for error retrieval.
        # See `self.session.table_function("information_schema.query_history")` below.
        database = _get_single_field(snowflake_sources, "database")
        if database is None:
            msg = "Snowflake database must be specified"
            raise TectonValidationError(msg, can_drop_traceback=True)
        schema = _get_single_field(snowflake_sources, "schema")
        # Needed for register temp tables
        if schema is None:
            msg = "Snowflake schema must be specified"
            raise TectonValidationError(msg, can_drop_traceback=True)
        connection = snowflake.connector.connect(
            user=user,
            password=password,
            account=account,
            warehouse=warehouse,
            schema=schema,
            database=database,
        )
        return SnowflakeCompute.for_connection(connection)

    def run_sql(self, sql_string: str, return_dataframe: bool = False) -> Optional[pyarrow.Table]:
        sql_string = sqlparse.format(sql_string, reindent=True)
        if self.is_debug:
            logging.warning(f"SNOWFLAKE QT: run SQL {sql_string}")

        with self.monitoring_ctx(sql_string) as progress_logger:
            progress_logger(0.0)
            # Snowflake connections are not thread-safe. Launch Snowflake jobs without blocking the result. The lock is
            # released after the query is sent
            with self.lock:
                snowpark_df = self.session.sql(sql_string)
                if return_dataframe:
                    # TODO(TEC-16169): check types are converted properly
                    async_job = snowpark_df.toPandas(block=False)
                else:
                    async_job = snowpark_df.collect(block=False)

            if return_dataframe:
                try:
                    df = async_job.result(result_type="pandas")
                    progress_logger(1.0)
                except snowflake.connector.DatabaseError:
                    detailed_error = (
                        self.session.table_function("information_schema.query_history")
                        .where(col("query_id") == async_job.query_id)
                        .select("error_message")
                        .collect()[0][0]
                    )
                    if "SQL compilation error" in detailed_error:
                        raise SQLCompilationError(detailed_error.replace("\n", " "), sql_string) from None

                    msg = f"Snowflake query failed with: {detailed_error}"
                    raise UserDefinedTransformationError(msg) from None

                df = self._post_process_pandas(snowpark_df, df)
                return pyarrow.Table.from_pandas(df)
            else:
                async_job.result(result_type="no_result")
                return None

    @staticmethod
    def _post_process_pandas(snowpark_df: "snowflake.snowpark.DataFrame", pandas_df: pd.DataFrame) -> pd.DataFrame:
        """Converts a Snowpark DataFrame to a Pandas DataFrame while preserving types."""
        import snowflake.snowpark

        snowpark_schema = snowpark_df.schema

        def unquote(field_name: str) -> str:
            """If a column name was quoted, remove the enclosing quotes. Otherwise, return the original column name."""
            # Note that an unquoted column name cannot contain double quotes, so it is safe to return the original
            # column name if it is not wrapped in double quotes.
            # See https://docs.snowflake.com/en/sql-reference/identifiers-syntax for more details.
            return field_name[1:-1] if field_name[0] == field_name[-1] == '"' else field_name

        for field in snowpark_schema:
            # TODO(TEC-16169): Handle other types.
            if field.datatype == snowflake.snowpark.types.LongType():
                # The Snowpark schema may contain either quoted or unquoted identifiers. In general, Unified Tecton uses
                # quoted identifiers. However, certain queries (e.g. a data source scan) do a SELECT *, which results
                # in unquoted identifiers. The Pandas dataframe will not have quoted identifiers, and so sometimes need
                # to strip the surrounding double quotes.
                if field.name[0] == '"' and field.name[-1] == '"':
                    # NOTE: this condition is not actually accurate. For example if a user has a column that starts and
                    # ends with a double quote, and we do a SELECT *, that column will be returned as an unquoted
                    # identifier. However, this condition will mistakenly consider it a quoted identifier and strip the
                    # surrounding double quotes, which is wrong. In order to correctly address this, we would need to
                    # know whether the identifer was quoted or unquoted. However, this case is sufficiently rare that
                    # we will ignore it for now.
                    field_name = field.name[1:-1]
                else:
                    field_name = field.name
                pandas_df[field_name] = pandas_df[field_name].astype("int64")

        return pandas_df

    def get_dialect(self) -> Dialect:
        return Dialect.SNOWFLAKE

    def run_odfv(self, qt_node: NodeRef, input_df: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError

    def register_temp_table_from_pandas(self, table_name: str, pandas_df: pd.DataFrame) -> None:
        # Not quoting identifiers / keeping the upload case-insensitive to be consistent with the query tree sql
        # generation logic, which is also case-insensitive. (i.e. will upper case selected fields).
        df_to_write = pandas_df.copy()
        convert_pandas_df_for_snowflake_upload(df_to_write)
        self.session.write_pandas(
            df_to_write,
            table_name=table_name,
            auto_create_table=True,
            table_type="temporary",
            quote_identifiers=compute_mode.get_compute_mode() != compute_mode.ComputeMode.SNOWFLAKE,
            overwrite=True,
        )

    def register_temp_table(self, table_name: str, pa_table: pyarrow.Table) -> None:
        self.register_temp_table_from_pandas(table_name, pa_table.to_pandas())
