import importlib.metadata

from tipsql.core.relation.column import Column
from tipsql.core.relation.table import table

from .connection import Connection
from .cursor import Cursor
from .query.builder import PostgresQueryBuilder as QueryBuilder
from .relation import Table

__version__ = importlib.metadata.version("tipsql-postgresql")


__all__ = [
    "__version__",
    "Column",
    "Connection",
    "Cursor",
    "QueryBuilder",
    "table",
    "Table",
]
