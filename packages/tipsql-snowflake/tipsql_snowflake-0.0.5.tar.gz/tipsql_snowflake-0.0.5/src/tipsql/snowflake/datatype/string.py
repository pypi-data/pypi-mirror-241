from tipsql.core.operator.eq_operator import EqOperator
from tipsql.core.operator.not_eq_operator import NotEqOperator
from tipsql.core.relation.column import ColumnType


class Varchar[N: int](
    ColumnType[str],
    EqOperator[str, str],
    NotEqOperator[str, str],
):
    __slots__ = ()


type Char[N: int] = Varchar[N]
type Character[N: int] = Varchar[N]
type NChar[N: int] = Varchar[N]
type String[N: int] = Varchar[N]
type Text[N: int] = Varchar[N]
type NVarchar[N: int] = Varchar[N]
type NVarchar2[N: int] = Varchar[N]
type CharVarying[N: int] = Varchar[N]
type NCharVarying[N: int] = Varchar[N]
