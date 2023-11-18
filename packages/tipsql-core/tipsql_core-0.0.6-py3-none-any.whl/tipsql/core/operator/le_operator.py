from typing import TYPE_CHECKING, Any, Self, overload

from tipsql.core.query.expression import Le
from tipsql.core.types.hint import (
    Expected,
    TypeMismatch,
)
from tipsql.core.value import SQLType

if TYPE_CHECKING:
    from tipsql.core.relation.column import ColumnType


class LeOperator[L, R](SQLType[L]):
    __slots__ = ()

    @overload
    def __le__(self, other: R) -> Le[Self, R]:
        ...

    @overload
    def __le__(self, other: "ColumnType[R]") -> Le[Self, "ColumnType[R]"]:
        ...

    @overload
    def __le__[U](self, other: U) -> TypeMismatch[L, Expected[U]]:
        ...

    def __le__(
        self, other
    ) -> Le[Self, R] | Le[Self, "ColumnType[R]"] | TypeMismatch[L, Any]:
        return Le(self, other)
