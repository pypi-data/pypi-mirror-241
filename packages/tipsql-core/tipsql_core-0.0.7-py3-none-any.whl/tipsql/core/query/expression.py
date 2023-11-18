from typing import TYPE_CHECKING, Unpack, override

from tipsql.core.query.querable import ToQuery, ToQueryParams, querify

if TYPE_CHECKING:
    from tipsql.core.relation.trait import SelectableRelation
    from tipsql.core.value import SQLType


class Expression[*Ts, T: "SelectableRelation"](ToQuery):
    __slots__ = ()


class Eq[L, R](Expression):
    __slots__ = ("_lvalue", "_rvalue")

    def __init__(self, lvalue: L, rvalue: R) -> None:
        self._lvalue = lvalue
        self._rvalue = rvalue

    @override
    def _to_query(self, **kwargs: Unpack[ToQueryParams]) -> str:
        return f"{self._lvalue} = {querify(self._rvalue, **kwargs)}"


class NotEq[L, R](Expression):
    __slots__ = ("_lvalue", "_rvalue")

    def __init__(self, lvalue: L, rvalue: R) -> None:
        self._lvalue = lvalue
        self._rvalue = rvalue

    @override
    def _to_query(self, **kwargs: Unpack[ToQueryParams]) -> str:
        return f"{self._lvalue} != {querify(self._rvalue, **kwargs)}"


class Le[L, R](Expression):
    __slots__ = ("_lvalue", "_rvalue")

    def __init__(self, lvalue: L, rvalue: R) -> None:
        self._lvalue = lvalue
        self._rvalue = rvalue

    @override
    def _to_query(self, **kwargs: Unpack[ToQueryParams]) -> str:
        return f"{self._lvalue} <= {querify(self._rvalue, **kwargs)}"


class Ge[L, R](Expression):
    __slots__ = ("_lvalue", "_rvalue")

    def __init__(self, lvalue: L, rvalue: R) -> None:
        self._lvalue = lvalue
        self._rvalue = rvalue

    @override
    def _to_query(self, **kwargs: Unpack[ToQueryParams]) -> str:
        return f"{self._lvalue} >= {querify(self._rvalue, **kwargs)}"


class Gt[L, R](Expression):
    __slots__ = ("_lvalue", "_rvalue")

    def __init__(self, lvalue: L, rvalue: R) -> None:
        self._lvalue = lvalue
        self._rvalue = rvalue

    @override
    def _to_query(self, **kwargs: Unpack[ToQueryParams]) -> str:
        return f"{self._lvalue} > {querify(self._rvalue, **kwargs)}"


class Lt[L, R](Expression):
    __slots__ = ("_lvalue", "_rvalue")

    def __init__(self, lvalue: L, rvalue: R) -> None:
        self._lvalue = lvalue
        self._rvalue = rvalue

    @override
    def _to_query(self, **kwargs: Unpack[ToQueryParams]) -> str:
        return f"{self._lvalue} < {querify(self._rvalue, **kwargs)}"


class IsTrue[T](Expression):
    __slots__ = ("_value",)

    def __init__(self, value: "SQLType[T]") -> None:
        self._value = value

    @override
    def _to_query(self, **kwargs: Unpack[ToQueryParams]) -> str:
        return f"{self._value} IS TRUE"


class IsNotTrue[T](Expression):
    __slots__ = ("_value",)

    def __init__(self, value: "SQLType[T]") -> None:
        self._value = value

    @override
    def _to_query(self, **kwargs: Unpack[ToQueryParams]) -> str:
        return f"{self._value} IS NOT TRUE"


class IsFalse[T](Expression):
    __slots__ = ("_value",)

    def __init__(self, value: "SQLType[T]") -> None:
        self._value = value

    @override
    def _to_query(self, **kwargs: Unpack[ToQueryParams]) -> str:
        return f"{self._value} IS FALSE"


class IsNotFalse[T](Expression):
    __slots__ = ("_value",)

    def __init__(self, value: "SQLType[T]") -> None:
        self._value = value

    @override
    def _to_query(self, **kwargs: Unpack[ToQueryParams]) -> str:
        return f"{self._value} IS NOT FALSE"


class IsNull[T](Expression):
    __slots__ = ("_value",)

    def __init__(self, value: "SQLType[T]") -> None:
        self._value = value

    @override
    def _to_query(self, **kwargs: Unpack[ToQueryParams]) -> str:
        return f"{self._value} IS NULL"


class IsNotNull[T](Expression):
    __slots__ = ("_value",)

    def __init__(self, value: "SQLType[T]") -> None:
        self._value = value

    @override
    def _to_query(self, **kwargs: Unpack[ToQueryParams]) -> str:
        return f"{self._value} IS NOT NULL"
