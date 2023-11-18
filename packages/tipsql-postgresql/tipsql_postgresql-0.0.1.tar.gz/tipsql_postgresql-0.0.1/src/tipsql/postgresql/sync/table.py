from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True, slots=True)
class Table:
    table_catalog: str
    table_schema: str
    table_name: str
    table_type: Literal["BASE TABLE", "VIEW", "LOCAL TEMPORARY"]
