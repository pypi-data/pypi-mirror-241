from typing import TYPE_CHECKING, Any, Self, overload

from tipsql.core.query.expression import (
    Eq,
)
from tipsql.core.types.hint import (
    Expected,
    TypeMismatch,
)
from tipsql.core.value import SQLType

if TYPE_CHECKING:
    from tipsql.core.relation.column import ColumnType


class EqOperator[L, R](SQLType[L]):
    __slots__ = ()

    @overload
    def __eq__(self, other: R) -> Eq[Self, R]:
        ...

    @overload
    def __eq__(self, other: "ColumnType[R]") -> Eq[Self, "ColumnType[R]"]:
        ...

    @overload
    def __eq__[U](self, other: U) -> TypeMismatch[L, Expected[U]]:
        ...

    def __eq__(
        self, other
    ) -> Eq[Self, R] | Eq[Self, "ColumnType[R]"] | TypeMismatch[L, Any]:
        return Eq(self, other)
