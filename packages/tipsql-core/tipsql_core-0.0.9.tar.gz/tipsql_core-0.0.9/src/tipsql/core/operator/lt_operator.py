from typing import TYPE_CHECKING, Any, Self, overload

from tipsql.core.query.expression import Lt
from tipsql.core.types.hint import (
    Expected,
    TypeMismatch,
)
from tipsql.core.value import SQLType

if TYPE_CHECKING:
    from tipsql.core.relation.column import ColumnType


class LtOperator[L, R](SQLType[L]):
    __slots__ = ()

    @overload
    def __lt__(self, other: R) -> Lt[Self, R]:
        ...

    @overload
    def __lt__(self, other: "ColumnType[R]") -> Lt[Self, "ColumnType[R]"]:
        ...

    @overload
    def __lt__[U](self, other: U) -> TypeMismatch[L, Expected[U]]:
        ...

    def __lt__(
        self, other
    ) -> Lt[Self, R] | Lt[Self, "ColumnType[R]"] | TypeMismatch[L, Any]:
        return Lt(self, other)
