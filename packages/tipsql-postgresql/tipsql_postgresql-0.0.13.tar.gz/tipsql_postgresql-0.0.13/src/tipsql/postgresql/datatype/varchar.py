from tipsql.core.operator.eq_operator import EqOperator
from tipsql.core.operator.not_eq_operator import NotEqOperator
from tipsql.core.relation.column import ColumnType


class Varchar(
    ColumnType[str],
    EqOperator[str, str],
    NotEqOperator[str, str],
):
    __slots__ = ()


class OctetLength:
    def __init__(self, n: int, /):
        self.value = n
