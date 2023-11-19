from dataclasses import dataclass
from typing import Literal

import psycopg
from tipsql.postgresql.information_schema.tables import TableInformation


@dataclass(frozen=True, slots=True)
class ColumnInformation:
    table_catalog: str
    table_schema: str
    table_name: str
    column_name: str
    ordinal_position: int
    column_default: str | None
    is_nullable: Literal["YES", "NO"]
    data_type: str
    character_maximum_length: int | None
    character_octet_length: int | None
    numeric_precision: int | None
    numeric_precision_radix: int | None
    numeric_scale: int | None
    datetime_precision: int | None
    domain_catalog: str | None
    domain_schema: str | None
    domain_name: str | None
    udt_catalog: str | None
    udt_schema: str | None
    udt_name: str | None
    comment: str | None


def get_table_column_infos(
    connection: psycopg.Connection, table: TableInformation
) -> list[ColumnInformation]:
    return [
        ColumnInformation(*row)
        for row in connection.cursor().execute(
            """
            SELECT
                information_schema.columns.table_catalog,
                information_schema.columns.table_schema,
                information_schema.columns.table_name,
                information_schema.columns.column_name,
                information_schema.columns.ordinal_position,
                information_schema.columns.column_default,
                information_schema.columns.is_nullable,
                information_schema.columns.data_type,
                information_schema.columns.character_maximum_length,
                information_schema.columns.character_octet_length,
                information_schema.columns.numeric_precision,
                information_schema.columns.numeric_precision_radix,
                information_schema.columns.numeric_scale,
                information_schema.columns.datetime_precision,
                information_schema.columns.domain_catalog,
                information_schema.columns.domain_schema,
                information_schema.columns.domain_name,
                information_schema.columns.udt_catalog,
                information_schema.columns.udt_schema,
                information_schema.columns.udt_name,
                pg_description.description AS comment
            FROM
                information_schema.columns
            LEFT OUTER JOIN
                pg_stat_user_tables
            ON
                information_schema.columns.table_schema = pg_stat_user_tables.schemaname
                AND information_schema.columns.table_name = pg_stat_user_tables.relname
            LEFT OUTER JOIN
                pg_description
            ON
                pg_stat_user_tables.relid = pg_description.objoid
                AND pg_description.objsubid = information_schema.columns.ordinal_position
            WHERE
                information_schema.columns.table_catalog = %s
                AND information_schema.columns.table_schema = %s
                AND information_schema.columns.table_name = %s
            ORDER BY
                ordinal_position
                ;
            """,
            [table.catalog, table.schema, table.name],
        )
    ]
