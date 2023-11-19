import textwrap
from abc import abstractmethod
from typing import Unpack, override

from tipsql.core.query.condition import Condition
from tipsql.core.query.querable import ToQuery, ToQueryParams
from tipsql.core.relation.trait import SelectableRelation


class JoinClause[T: SelectableRelation](ToQuery):
    __slots__ = "left"

    def __init__(self, table: type[T]) -> None:
        self._table = table


class _OnJoinClause[T: SelectableRelation](JoinClause[T]):
    __slots__ = ("on",)

    def __init__(self, table: type[T], on: Condition) -> None:
        super().__init__(table)
        self.on = on

    @property
    @abstractmethod
    def _join_type(self) -> str:
        ...

    @override
    def _to_query(self, **kwargs: Unpack[ToQueryParams]) -> str:
        separator = kwargs["separator"]
        tabsize = kwargs["tabsize"]

        indent = " " * tabsize

        query = f"{self._join_type}{separator}"
        query += textwrap.indent(
            self._table._to_query(**kwargs),
            indent,
        )

        query += f"{separator}ON{separator}"
        query += textwrap.indent(
            self.on._to_query(**kwargs),
            indent,
        )

        return query


class InnerJoinClause[T: SelectableRelation](_OnJoinClause[T]):
    __slots__ = ()

    @property
    @override
    def _join_type(self) -> str:
        return "INNER JOIN"


class LeftOuterJoinClause[T: SelectableRelation](_OnJoinClause[T]):
    __slots__ = ()

    @property
    @override
    def _join_type(self) -> str:
        return "LEFT OUTER JOIN"


class FullOuterJoinClause[T: SelectableRelation](_OnJoinClause[T]):
    __slots__ = ()

    @property
    @override
    def _join_type(self) -> str:
        return "FULL OUTER JOIN"


class CrossJoinClause[T: SelectableRelation](_OnJoinClause[T]):
    __slots__ = ()

    @property
    @override
    def _join_type(self) -> str:
        return "CROSS JOIN"
