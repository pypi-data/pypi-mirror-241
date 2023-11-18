from typing import Optional, Self

import psycopg
from psycopg import connect
from psycopg.abc import AdaptContext
from tipsql.core.utils.env import get_env
from tipsql.postgresql.cursor import Cursor


class Connection:
    def __init__(self, connection: psycopg.Connection) -> None:
        self._connection = connection

    @classmethod
    def from_env(
        cls,
        autocommit: bool = False,
        prepare_threshold: Optional[int] = 5,
        context: Optional[AdaptContext] = None,
    ) -> Self:
        POSTGRES_USER = get_env("POSTGRES_USER")
        POSTGRES_PASSWORD = get_env("POSTGRES_PASSWORD")
        POSTGRES_HOST = get_env("POSTGRES_HOST")
        POSTGRES_DATABASE = get_env("POSTGRES_DATABASE")
        POSTGRES_PORT = get_env("POSTGRES_PORT")

        if POSTGRES_DATABASE is None:
            POSTGRES_DATABASE = get_env("POSTGRES_DB")

        conninfo = ""
        if POSTGRES_USER:
            conninfo += f"user={POSTGRES_USER} "
        if POSTGRES_PASSWORD:
            conninfo += f"password={POSTGRES_PASSWORD} "
        if POSTGRES_HOST:
            conninfo += f"host={POSTGRES_HOST} "
        if POSTGRES_DATABASE:
            conninfo += f"dbname={POSTGRES_DATABASE} "
        if POSTGRES_PORT:
            conninfo += f"port={POSTGRES_PORT} "

        return cls(
            connect(
                conninfo,
                autocommit=autocommit,
                prepare_threshold=prepare_threshold,
                context=context,
            )
        )

    def close(self) -> None:
        self._connection.close()

    def commit(self) -> None:
        self._connection.commit()

    def rollback(self) -> None:
        self._connection.rollback()

    def cursor(self) -> Cursor:
        return Cursor(self._connection.cursor())
