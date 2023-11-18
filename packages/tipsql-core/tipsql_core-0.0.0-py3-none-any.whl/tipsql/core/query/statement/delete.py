import textwrap
from typing import Any, Callable, Sequence, Unpack

from tipsql.core.context.condition_context import ConditionContext
from tipsql.core.query.clause.where_clause import WhereClause
from tipsql.core.query.condition import Condition, convert_to_condition
from tipsql.core.query.expression import Expression
from tipsql.core.query.querable import (
    QueryParam,
    ToQuery,
    ToQueryParams,
    build,
)
from tipsql.core.relation.table import Table

type DeletableRelation = Table[Any, Any]


class DeleteQuery[T: DeletableRelation](ToQuery):
    def __init__(
        self,
        table: type[T],
        where: Condition | None = None,
    ) -> None:
        self._table = table
        self._where = where

    def _to_query(
        self,
        **kwargs: Unpack[ToQueryParams],
    ) -> str:
        separator = kwargs["separator"]
        tabsize = kwargs["tabsize"]

        query = f"DELETE FROM{separator}"
        query += textwrap.indent(self._table._to_query(**kwargs), " " * tabsize)

        if self._where is not None:
            query += separator
            query += WhereClause(self._where)._to_query(**kwargs)

        return query

    def build(
        self,
        params: QueryParam,
    ) -> tuple[str, Sequence[Any] | dict[str, Any]]:
        return build(
            self,
            params,
        )


class WherableDeleteQuery[T: DeletableRelation](DeleteQuery[T]):
    def where(
        self,
        condition: Expression | Callable[["ConditionContext[T]"], Condition],
    ) -> DeleteQuery:
        return DeleteQuery(
            table=self._table,
            where=convert_to_condition(condition),
        )
