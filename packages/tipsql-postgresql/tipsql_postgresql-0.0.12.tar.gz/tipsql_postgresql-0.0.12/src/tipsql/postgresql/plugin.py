from pathlib import Path
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
    def sync_database(self, config: PostgresqlDatabaseConfig) -> list[Path]:
        import tipsql.postgresql

        paths = []

        connection = tipsql.postgresql.Connection.from_env()

        tables_path = Path("tables.py")
        paths.append(tables_path)
        with open(tables_path, "w") as f:
            f.write(TableGenerator(connection._connection).generate())

        return paths
