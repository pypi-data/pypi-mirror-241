from dataclasses import dataclass
from typing import Literal

import psycopg


@dataclass(frozen=True, slots=True)
class TableInformation:
    catalog: str
    schema: str
    name: str
    type: Literal["BASE TABLE", "VIEW", "LOCAL TEMPORARY"]
    comment: str | None


def get_table_infos(connection: psycopg.Connection) -> list[TableInformation]:
    return [
        TableInformation(*row)
        for row in connection.cursor().execute(
            """
            SELECT
                information_schema.tables.table_catalog,
                information_schema.tables.table_schema,
                information_schema.tables.table_name,
                information_schema.tables.table_type,
                pg_description.description AS comment
            FROM
                pg_stat_user_tables
            LEFT OUTER JOIN
                information_schema.tables
            ON
                information_schema.tables.table_schema = pg_stat_user_tables.schemaname
                AND information_schema.tables.table_name = pg_stat_user_tables.relname
            LEFT OUTER JOIN
                pg_description
            ON
                pg_stat_user_tables.relid = pg_description.objoid
                AND pg_description.objsubid = 0
            ORDER BY
                information_schema.tables.table_schema,
                information_schema.tables.table_name
            """
        )
    ]
