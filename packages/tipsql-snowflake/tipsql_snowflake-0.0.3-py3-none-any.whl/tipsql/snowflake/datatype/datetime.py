import datetime
from typing import LiteralString

from tipsql.core.operator.eq_operator import EqOperator
from tipsql.core.operator.not_eq_operator import NotEqOperator
from tipsql.core.operator.order_operator import OrderOperator
from tipsql.core.relation.column import ColumnType


class Date(
    ColumnType[datetime.date],
    EqOperator[datetime.date, datetime.date],
    OrderOperator[datetime.date, datetime.date],
    NotEqOperator[datetime.date, datetime.date],
):
    __slots__ = ()


class Time[Precision: int](
    ColumnType[datetime.time],
    EqOperator[datetime.time, datetime.time],
    OrderOperator[datetime.time, datetime.time],
    NotEqOperator[datetime.time, datetime.time],
):
    __slots__ = ()


class TimestampNTZ(
    ColumnType[datetime.datetime],
    EqOperator[datetime.datetime, datetime.datetime],
    OrderOperator[datetime.datetime, datetime.datetime],
    NotEqOperator[datetime.datetime, datetime.datetime],
):
    __slots__ = ()


type DateTime = TimestampNTZ
type TimestampLTZ[TimeZone: LiteralString] = TimestampNTZ
type TimestampTZ = TimestampNTZ
