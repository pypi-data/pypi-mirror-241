from tipsql.core.operator.eq_operator import EqOperator
from tipsql.core.operator.not_eq_operator import NotEqOperator
from tipsql.core.relation.column import ColumnType


class Varchar[N: int](
    ColumnType[str],
    EqOperator[str, str],
    NotEqOperator[str, str],
):
    __slots__ = ()
