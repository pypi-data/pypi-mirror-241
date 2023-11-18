from tipsql.core.operator.eq_operator import EqOperator
from tipsql.core.operator.not_eq_operator import NotEqOperator
from tipsql.core.relation.column import ColumnType

Json = int | float | str | bool | None | list["Json"] | dict[str, "Json"]


class Valiant(
    ColumnType[Json],
    EqOperator[Json, Json],
    NotEqOperator[Json, Json],
):
    __slots__ = ()


class Object(
    ColumnType[dict[str, Json]],
    EqOperator[dict[str, Json], dict[str, Json]],
    NotEqOperator[dict[str, Json], dict[str, Json]],
):
    __slots__ = ()


class Array(
    ColumnType[list[Json]],
    EqOperator[list[Json], list[Json]],
    NotEqOperator[list[Json], list[Json]],
):
    __slots__ = ()
