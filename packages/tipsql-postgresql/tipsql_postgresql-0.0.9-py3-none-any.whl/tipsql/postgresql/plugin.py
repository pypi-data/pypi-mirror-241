from typing import Literal, override

from tipsql.core.dataclasses import extra_forbid_dataclass
from tipsql.core.plugins.database_plugin import TipsqlDatabasePlugin
from tipsql.postgresql.sync.table_generator import TableGenerator


@extra_forbid_dataclass
class PostgresqlDatabaseConfig:
    type: Literal["postgresql"]


class PostgresqlDatabasePlugin(TipsqlDatabasePlugin):
    @property
    def database_name(self) -> str:
        return "postgresql"

    @property
    def database_config(self) -> type[PostgresqlDatabaseConfig]:
        return PostgresqlDatabaseConfig

    @override
    def sync_database(self, config: PostgresqlDatabaseConfig) -> None:
        import tipsql.postgresql

        connection = tipsql.postgresql.Connection.from_env()

        with open("tables.py", "w") as f:
            f.write(TableGenerator(connection._connection).generate())

        print("syncing postgresql database")

        return None
