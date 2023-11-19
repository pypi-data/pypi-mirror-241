from typing import ClassVar, Self


class NoArg:
    __slots__ = ()
    __instance__: ClassVar[Self | None] = None

    # インスタンス生成時に既存のインスタンスがあればそれを返す
    def __new__(cls):
        if cls.__instance__ is None:
            cls.__instance__ = super().__new__(cls)
        return cls.__instance__

    # is演算子で比較できるように__eq__メソッドをオーバーライドする
    def __eq__(self, other):
        return isinstance(other, NoArg)


NO_ARG = NoArg()


class Unknown:
    __slots__ = ()


class Unguessable:
    """Alternative types used where types cannot be inferred.

    Unfortunately, it is not possible to guess this type at present,
    but it may become possible in the future.

    We cannot promise an improvement for the future, but we are using this type
    to show that there is a possibility of improvement.
    """

    __slots__ = ()


class NotSupport[Operator]:
    __slots__ = ()


class Expected[T]:
    __slots__ = ()


class TypeMismatch[T, U: Expected]:
    __slots__ = ("lvalue", "rvalue")

    def __init__(self, lvalue: T, rvalue: U) -> None:
        pass


class SelfTypeMismatch[T, U: Expected](TypeMismatch):
    __slots__ = ()


class ArgTypeMismatch[T, U: Expected](TypeMismatch):
    __slots__ = ()
