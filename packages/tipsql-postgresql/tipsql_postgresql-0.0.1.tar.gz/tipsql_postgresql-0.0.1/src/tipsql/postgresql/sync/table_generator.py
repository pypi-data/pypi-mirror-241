from dataclasses import dataclass
from pathlib import Path
from typing import Any

import psycopg
from tipsql.core.utils.jinja import render_template
from tipsql.postgresql.information_schema.columns import (
    ColumnInformation,
    get_table_column_infos,
)
from tipsql.postgresql.information_schema.tables import (
    TableInformation,
    get_table_infos,
)


class TableGenerator:
    def __init__(self, connection: psycopg.Connection) -> None:
        self.connection = connection

    def generate(self, template_path: Path | None = None) -> str:
        tables = []
        for table in get_table_infos(self.connection):
            columns = get_table_column_infos(self.connection, table)
            if table.type == "BASE TABLE":
                tables.append(make_table(table, columns))

        return render_template(
            template_path or Path(__file__).parent / "table_generator.py.jinja",
            tables=tables,
            views=[],
        )


@dataclass(frozen=True, slots=True)
class Table:
    schema: str
    name: str
    comment: str | None
    columns: list["Column"]

    @property
    def class_name(self) -> str:
        from inflection import camelize, singularize

        return singularize(camelize(self.name))


@dataclass(frozen=True, slots=True)
class Column:
    name: str
    database_type: str
    python_type: str
    comment: str | None


def make_table(table: TableInformation, columns: list[ColumnInformation]) -> Table:
    return Table(
        schema=table.schema,
        name=table.name,
        comment=table.comment,
        columns=[make_column(column) for column in columns],
    )


def make_column(column: ColumnInformation) -> Column:
    match column.data_type:
        case "bigint":
            database_type = f"Bigint[Literal[{column.numeric_precision}], Literal[{column.numeric_scale}]]"
            python_type = int
        case "character varying":
            database_type = f"Varchar[Literal[{column.character_octet_length}]]"
            python_type = str
        case _:
            database_type = Any.__name__
            python_type = Any

    return Column(
        name=column.column_name,
        database_type=database_type,
        python_type=python_type.__name__,
        comment=column.comment,
    )
