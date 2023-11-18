from typing import TYPE_CHECKING, Any, Self, overload

from tipsql.core.query.expression import Gt
from tipsql.core.types.hint import (
    Expected,
    TypeMismatch,
)
from tipsql.core.value import SQLType

if TYPE_CHECKING:
    from tipsql.core.relation.column import ColumnType


class GtOperator[L, R](SQLType[L]):
    __slots__ = ()

    @overload
    def __gt__(self, other: R) -> Gt[Self, R]:
        ...

    @overload
    def __gt__(self, other: "ColumnType[R]") -> Gt[Self, "ColumnType[R]"]:
        ...

    @overload
    def __gt__[U](self, other: U) -> TypeMismatch[L, Expected[U]]:
        ...

    def __gt__(
        self, other
    ) -> Gt[Self, R] | Gt[Self, "ColumnType[R]"] | TypeMismatch[L, Any]:
        return Gt(self, other)
