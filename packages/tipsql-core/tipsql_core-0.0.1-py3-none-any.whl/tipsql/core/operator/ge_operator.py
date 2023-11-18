from typing import TYPE_CHECKING, Any, Self, overload

from tipsql.core.query.expression import Ge
from tipsql.core.types.hint import (
    Expected,
    TypeMismatch,
)
from tipsql.core.value import SQLType

if TYPE_CHECKING:
    from tipsql.core.relation.column import ColumnType


class GeOperator[L, R](SQLType[L]):
    __slots__ = ()

    @overload
    def __ge__(self, other: R) -> Ge[Self, R]:
        ...

    @overload
    def __ge__(self, other: "ColumnType[R]") -> Ge[Self, "ColumnType[R]"]:
        ...

    @overload
    def __ge__[U](self, other: U) -> TypeMismatch[L, Expected[U]]:
        ...

    def __ge__(
        self, other
    ) -> Ge[Self, R] | Ge[Self, "ColumnType[R]"] | TypeMismatch[L, Any]:
        return Ge(self, other)
