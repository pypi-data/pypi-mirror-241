from types import NoneType, UnionType
from typing import TYPE_CHECKING, Literal, Self, overload

from tipsql.core.query.expression import (
    IsFalse,
    IsNotFalse,
    IsNotNull,
    IsNotTrue,
    IsNull,
    IsTrue,
)
from tipsql.core.types.hint import (
    ArgTypeMismatch,
    Expected,
    NotSupport,
    SelfTypeMismatch,
    TypeMismatch,
)

if TYPE_CHECKING:
    from tipsql.core.operator.eq_operator import EqOperator
    from tipsql.core.operator.not_eq_operator import NotEqOperator


class SQLType[PyType]:
    __slots__ = ("py_type",)

    def __init__(
        self,
        py_type: type[PyType],
    ) -> None:
        self.py_type = py_type

    @overload
    def __eq__[U](self, __value: U) -> "NotSupport[EqOperator[Self, U]]":
        ...

    @overload
    def __eq__[U](self, __value: U) -> "NotSupport[NotEqOperator[Self, U]]":
        ...

    def __eq__(self, __value):
        raise NotImplementedError(
            f'"{self.__class__}" does not support equality comparison.'
        )

    @overload
    def is_(
        self: "SQLType[bool]",
        value: Literal[True],
    ) -> IsTrue[PyType]:
        ...

    @overload
    def is_(
        self: "SQLType[bool]",
        value: Literal[False],
    ) -> IsFalse[PyType]:
        ...

    @overload
    def is_[U](
        self: "SQLType[bool]",
        value: U,
    ) -> ArgTypeMismatch[U, Expected[bool]]:
        ...

    @overload
    def is_(
        self: "SQLType[PyType | None]",
        value: NoneType,
    ) -> IsNull[PyType]:
        ...

    @overload
    def is_(
        self: "SQLType[PyType]",
        value: bool,
    ) -> "SelfTypeMismatch[SQLType[PyType], Expected[SQLType[bool]]]":
        ...

    @overload
    def is_(
        self: "SQLType[PyType]",
        value: None,
    ) -> "SelfTypeMismatch[SQLType[PyType], Expected[SQLType[PyType | None]]]":
        ...

    @overload
    def is_[U](
        self: "SQLType[PyType]",
        value: U,
    ) -> "ArgTypeMismatch[U, Expected[bool | None]]":
        ...

    def is_(self, value):
        if isinstance(self.py_type, UnionType):
            if bool in self.py_type.__args__:
                if value is True:
                    return IsTrue(self)

                elif value is False:
                    return IsFalse(self)

            if NoneType in self.py_type.__args__:
                if value is None:
                    return IsNull(self)

        elif issubclass(self.py_type, bool):
            if value is True:
                return IsTrue(self)

            elif value is False:
                return IsFalse(self)

        return TypeMismatch(self, value)

    @overload
    def is_not(
        self: "SQLType[bool]",
        value: Literal[True],
    ) -> IsNotTrue[PyType]:
        ...

    @overload
    def is_not(
        self: "SQLType[bool]",
        value: Literal[False],
    ) -> IsNotFalse[PyType]:
        ...

    @overload
    def is_not[U](
        self: "SQLType[bool]",
        value: U,
    ) -> ArgTypeMismatch[U, Expected[bool]]:
        ...

    @overload
    def is_not(
        self: "SQLType[PyType | None]",
        value: NoneType,
    ) -> IsNotNull[PyType]:
        ...

    @overload
    def is_not(
        self: "SQLType[PyType]",
        value: bool,
    ) -> "SelfTypeMismatch[SQLType[PyType], Expected[SQLType[bool]]]":
        ...

    @overload
    def is_not(
        self: "SQLType[PyType]",
        value: None,
    ) -> "SelfTypeMismatch[SQLType[PyType], Expected[SQLType[PyType | None]]]":
        ...

    @overload
    def is_not[U](
        self: "SQLType[PyType]",
        value: U,
    ) -> "ArgTypeMismatch[U, Expected[bool | None]]":
        ...

    def is_not(self, value):
        if isinstance(self.py_type, UnionType):
            if bool in self.py_type.__args__:
                if value is True:
                    return IsNotTrue(self)

                elif value is False:
                    return IsNotFalse(self)

            if NoneType in self.py_type.__args__:
                if value is None:
                    return IsNotNull(self)

        elif issubclass(self.py_type, bool):
            if value is True:
                return IsNotTrue(self)

            elif value is False:
                return IsNotFalse(self)

        return TypeMismatch(self, value)
