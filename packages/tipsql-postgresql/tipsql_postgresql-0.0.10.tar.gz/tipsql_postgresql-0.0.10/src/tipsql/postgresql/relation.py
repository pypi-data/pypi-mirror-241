from typing import TypedDict

from tipsql.core.relation.table import Table as CoreTable


class Table[InsertColumns: TypedDict, UpdateColumns: TypedDict](
    CoreTable[InsertColumns, UpdateColumns]
):
    pass
