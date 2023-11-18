from tipsql.core.operator.eq_operator import EqOperator
from tipsql.core.operator.not_eq_operator import NotEqOperator
from tipsql.core.relation.column import ColumnType


class Binary[N: int](
    ColumnType[bytes],
    EqOperator[bytes, bytes],
    NotEqOperator[bytes, bytes],
):
    __slots__ = ()


type VarBinary[N: int] = Binary[N]
