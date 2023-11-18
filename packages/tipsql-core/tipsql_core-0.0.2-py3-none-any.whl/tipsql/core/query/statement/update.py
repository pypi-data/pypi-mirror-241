import textwrap
from typing import Any, Callable, Sequence, TypedDict, Unpack

from tipsql.core.context.condition_context import ConditionContext
from tipsql.core.query.clause.where_clause import WhereClause
from tipsql.core.query.condition import Condition, convert_to_condition
from tipsql.core.query.expression import Expression
from tipsql.core.query.querable import (
    QueryParam,
    ToQueryFunc,
    ToQueryParams,
    build,
    querify,
)
from tipsql.core.relation.table import Table

type UpdatableRelation[UpdateColumns: TypedDict] = Table[Any, UpdateColumns]


class UpdateStmt[Columns: TypedDict]:
    def __init__(self, table: type[UpdatableRelation[Columns]]) -> None:
        self._table = table

    def set(
        self,
        columns: Columns,
    ) -> "WherableUpdateQuery[Columns]":
        return WherableUpdateQuery(self, columns)


class UpdateQuery[Columns: TypedDict]:
    def __init__(
        self,
        stmt: UpdateStmt[Columns],
        columns: Columns,
        where: Condition | None = None,
    ) -> None:
        self._stmt = stmt
        self._columns = columns
        self._where = where

    def _to_query(
        self,
        **kwargs: Unpack[ToQueryParams],
    ) -> str:
        separator = kwargs["separator"]
        tabsize = kwargs["tabsize"]

        query = f"UPDATE{separator}"
        query += textwrap.indent(self._stmt._table._to_query(**kwargs), " " * tabsize)
        query += f"{separator}SET{separator}"
        query += textwrap.indent(
            f",{separator}".join(
                [f"{k} = {querify(v, **kwargs)}" for k, v in self._columns.items()]
            ),
            " " * tabsize,
        )

        if self._where is not None:
            query += separator
            query += WhereClause(self._where)._to_query(**kwargs)

        return query

    def build(
        self,
        params: QueryParam,
    ) -> tuple[str, Sequence[Any] | dict[str, Any]]:
        return build(
            ToQueryFunc(lambda kwargs: self._to_query(**kwargs)),
            params,
        )


class WherableUpdateQuery[Columns: TypedDict](UpdateQuery[Columns]):
    def where(
        self,
        condition: Expression
        | Callable[["ConditionContext[UpdatableRelation[Columns]]"], Condition],
    ) -> UpdateQuery:
        return UpdateQuery(
            stmt=self._stmt,
            columns=self._columns,
            where=convert_to_condition(condition),
        )
