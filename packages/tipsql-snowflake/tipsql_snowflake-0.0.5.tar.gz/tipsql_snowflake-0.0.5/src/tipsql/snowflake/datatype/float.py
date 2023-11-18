from tipsql.core.operator.eq_operator import EqOperator
from tipsql.core.operator.not_eq_operator import NotEqOperator
from tipsql.core.operator.order_operator import OrderOperator
from tipsql.core.relation.column import ColumnType


class Float(
    ColumnType[float],
    EqOperator[float, float | int],
    OrderOperator[float, float | int],
    NotEqOperator[float, float | int],
):
    __slots__ = ()


type Float4 = Float
type Float8 = Float
type Double = Float
type DoublePrecision = Float
type Real = Float
