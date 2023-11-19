from logging import getLogger
from typing import Any, LiteralString, Sequence, cast, overload

import psycopg
from tipsql.core.query.builder import BuildProtcol
from tipsql.core.query.statement.insert import InsertQuery

logger = getLogger(__name__)


class Cursor:
    def __init__(self, cursor: psycopg.Cursor) -> None:
        self._cursor = cursor

    @property
    def description(
        self,
    ) -> tuple[tuple[str, None, None, None, None, None, None], ...] | Any:
        return self._cursor.description

    @property
    def rowcount(self) -> int:
        return self._cursor.rowcount

    def close(self) -> bool | None:
        return self._cursor.close()

    @overload
    def execute(
        self, operation: BuildProtcol, parameters: None = None
    ) -> psycopg.Cursor:
        ...

    @overload
    def execute(
        self, operation: str, parameters: Sequence[Any] | dict[Any, Any] | None = None
    ) -> psycopg.Cursor:
        ...

    def execute(
        self,
        operation: BuildProtcol | str,
        parameters: Sequence[Any] | dict[Any, Any] | None = None,
    ):
        if isinstance(operation, str):
            parameters = parameters or ()
        else:
            operation, parameters = operation.build({"style": "qmark"})

        logger.debug(f'query: "{operation}"')
        logger.debug(f"params: {parameters}")

        return self._cursor.execute(cast(LiteralString, operation), parameters)

    @overload
    def execute_many(
        self,
        operation: InsertQuery,
        parameters: None = None,
    ) -> None:
        ...

    @overload
    def execute_many(
        self,
        operation: str,
        parameters: Sequence[Sequence[Any]] | Sequence[dict[Any, Any]] | None = None,
    ) -> None:
        ...

    def execute_many(
        self,
        operation: InsertQuery | str,
        parameters: Sequence[Sequence[Any]] | Sequence[dict[Any, Any]] | None = None,
    ) -> None:
        if isinstance(operation, str):
            parameters = parameters or ()
        else:
            operation, parameters = operation.build_many({"style": "qmark"})

        logger.debug(f'query: "{operation}"')
        logger.debug(f"params: {parameters}")

        return self._cursor.executemany(cast(LiteralString, operation), parameters)
