from typing import TYPE_CHECKING, Any, Self, overload

from tipsql.core.query.expression import NotEq
from tipsql.core.types.hint import (
    Expected,
    TypeMismatch,
)
from tipsql.core.value import SQLType

if TYPE_CHECKING:
    from tipsql.core.relation.column import ColumnType


class NotEqOperator[L, R](SQLType[L]):
    __slots__ = ()

    @overload
    def __ne__(self, other: R) -> NotEq[Self, R]:
        ...

    @overload
    def __ne__(self, other: "ColumnType[R]") -> NotEq[Self, "ColumnType[R]"]:
        ...

    @overload
    def __ne__[U](self, other: U) -> TypeMismatch[L, Expected[U]]:
        ...

    def __ne__(
        self, other
    ) -> NotEq[Self, R] | NotEq[Self, "ColumnType[R]"] | TypeMismatch[L, Any]:
        return NotEq(self, other)
