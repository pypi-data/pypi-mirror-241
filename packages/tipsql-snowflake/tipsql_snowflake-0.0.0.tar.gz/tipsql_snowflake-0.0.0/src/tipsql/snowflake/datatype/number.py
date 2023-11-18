from typing import Literal

from tipsql.core.operator.eq_operator import EqOperator
from tipsql.core.operator.not_eq_operator import NotEqOperator
from tipsql.core.operator.order_operator import OrderOperator
from tipsql.core.relation.column import ColumnType


class Number[Precision: int, Scale: int](
    ColumnType[int],
    EqOperator[int, int],
    OrderOperator[int, int],
    NotEqOperator[int, int],
):
    __slots__ = ()


type Decimal[Precision: int, Scale: int] = Number[Precision, Scale]
type Numeric[Precision: int, Scale: int] = Number[Precision, Scale]


type Int = Number[Literal[38], Literal[0]]
type Integer = Int
type BigInt = Int
type SmallInt = Int
type TinyInt = Int
type ByteInt = Int
