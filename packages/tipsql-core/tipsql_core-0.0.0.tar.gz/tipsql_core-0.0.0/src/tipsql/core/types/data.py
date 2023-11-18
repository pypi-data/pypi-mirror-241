from typing import Any, LiteralString

from tipsql.core.operator.eq_operator import EqOperator
from tipsql.core.operator.not_eq_operator import NotEqOperator
from tipsql.core.relation.column import ColumnType


class LiteralValue[ColumnName: LiteralString]:
    def __init__(self, value: int | float | str | bool, /, as_: ColumnName) -> None:
        self._value = value
        self.column_name = as_


class AnyType(
    ColumnType[Any],
    EqOperator[Any, Any],
    NotEqOperator[Any, Any],
):
    __slots__ = ()
