import textwrap
from typing import TYPE_CHECKING, Callable, Unpack, overload, override

from tipsql.core.query.expression import Expression
from tipsql.core.query.querable import ToQuery, ToQueryParams
from tipsql.core.relation.trait import SelectableRelation

if TYPE_CHECKING:
    from tipsql.core.context.condition_context import ConditionContext


class Condition[*Ts, T: SelectableRelation](ToQuery):
    def and_(
        self,
        condition: Expression[*Ts, T]
        | Callable[["ConditionContext[*Ts, T]"], "Condition[*Ts, T]"],
    ) -> "And[*Ts, T]":
        return And(self, convert_to_condition(condition, grouping=True))

    def or_(
        self,
        condition: Expression[*Ts, T]
        | Callable[["ConditionContext[*Ts, T]"], "Condition[*Ts, T]"],
    ) -> "Or[*Ts, T]":
        return Or(self, convert_to_condition(condition, grouping=True))


class ExprCondition[*Ts, T: SelectableRelation](Condition[*Ts, T]):
    __slots__ = ("_expr",)

    def __init__(self, expr: Expression) -> None:
        self._expr = expr

    @override
    def _to_query(self, **kwargs: Unpack[ToQueryParams]) -> str:
        return self._expr._to_query(**kwargs)


@overload
def convert_to_condition(
    condition: Expression | Callable[["ConditionContext"], Condition],
    /,
    *,
    grouping: bool = False,
) -> Condition:
    ...


@overload
def convert_to_condition(
    condition: Expression | Callable[["ConditionContext"], Condition] | None,
    /,
    *,
    grouping: bool = False,
) -> Condition:
    ...


def convert_to_condition(condition, /, *, grouping=False):
    if condition is None:
        return None

    if isinstance(condition, Expression):
        return ExprCondition(condition)

    else:
        cond = condition(ExprCondition)

        if grouping:
            return Group(cond)

        else:
            return cond


class And[*Ts, T: SelectableRelation](Condition[*Ts, T]):
    __slots__ = ("_lvalue", "_rvalue")

    def __init__(self, lvalue: Condition[*Ts, T], rvalue: Condition[*Ts, T]) -> None:
        self._lvalue = lvalue
        self._rvalue = rvalue

    @override
    def _to_query(self, **kwargs: Unpack[ToQueryParams]) -> str:
        separator = kwargs["separator"]

        lvalue = self._lvalue._to_query(**kwargs)
        rvalue = self._rvalue._to_query(**kwargs)

        return f"{lvalue}{separator}AND {rvalue}"


class Or[*Ts, T: SelectableRelation](Condition[*Ts, T]):
    __slots__ = ("_lvalue", "_rvalue")

    def __init__(self, lvalue: Condition[*Ts, T], rvalue: Condition[*Ts, T]) -> None:
        self._rvalue = rvalue
        self._lvalue = lvalue

    @override
    def _to_query(self, **kwargs: Unpack[ToQueryParams]) -> str:
        separator = kwargs["separator"]

        lvalue = self._lvalue._to_query(**kwargs)
        rvalue = self._rvalue._to_query(**kwargs)

        return f"{lvalue}{separator}OR {rvalue}"


class Group[*Ts, T: SelectableRelation](Condition[*Ts, T]):
    __slots__ = ("_condition",)

    def __init__(self, condition: Condition[*Ts, T]) -> None:
        self._condition = condition

    @override
    def _to_query(self, **kwargs: Unpack[ToQueryParams]) -> str:
        separator = kwargs["separator"]
        tabsize = kwargs["tabsize"]

        query = textwrap.indent(
            self._condition._to_query(**kwargs),
            " " * tabsize,
        )

        return f"({separator}{query}{separator})"
