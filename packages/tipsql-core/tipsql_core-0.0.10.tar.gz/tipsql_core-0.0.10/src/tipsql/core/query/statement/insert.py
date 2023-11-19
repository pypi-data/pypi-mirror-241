import textwrap
from typing import Any, Sequence, TypedDict, Unpack

from tipsql.core.query.querable import (
    QueryParam,
    ToQueryFunc,
    ToQueryParams,
    build,
    querify,
)
from tipsql.core.relation.table import Table

type InsertableRelation[InsertColumns: TypedDict] = Table[InsertColumns, Any]


class InsertStmt[Columns: TypedDict]:
    def __init__(self, table: type[InsertableRelation[Columns]]) -> None:
        self._table = table

    def values(
        self,
        value: Columns,
        *values: Columns,
    ) -> "InsertQuery[Columns]":
        return InsertQuery(self, value, *values)


class InsertQuery[Columns: TypedDict]:
    def __init__(
        self,
        stmt: InsertStmt[Columns],
        value: Columns,
        *values: Columns,
    ) -> None:
        self._stmt = stmt
        self._value = value
        self._values = values

    def _to_query_base(
        self,
        values: Sequence[Columns],
        **kwargs: Unpack[ToQueryParams],
    ) -> str:
        separator = kwargs["separator"]
        tabsize = kwargs["tabsize"]

        query = f"INSERT INTO{separator}"
        query += textwrap.indent(self._stmt._table._to_query(**kwargs), " " * tabsize)
        query += separator
        query += textwrap.indent(
            "(" + ", ".join([key for key in self._value.keys()]) + ")",
            " " * tabsize,
        )
        query += f"{separator}VALUES{separator}"
        query += textwrap.indent(
            f",{separator}".join(
                [
                    "("
                    + ", ".join([querify(value[key], **kwargs) for key in value.keys()])
                    + ")"
                    for value in values
                ]
            ),
            " " * tabsize,
        )

        return query

    def build(
        self,
        params: QueryParam,
    ) -> tuple[str, Sequence[Any] | dict[str, Any]]:
        return build(
            ToQueryFunc(
                lambda kwargs: self._to_query_base(
                    (self._value,) + self._values, **kwargs
                )
            ),
            params,
        )

    def build_many(
        self,
        params: QueryParam,
    ) -> tuple[str, Sequence[Sequence[Any]] | Sequence[dict[str, Any]]]:
        query, _ = build(
            ToQueryFunc(lambda kwargs: self._to_query_base((self._value,), **kwargs)),
            params,
        )

        return query, [
            [value[key] for key in self._value.keys()]
            for value in (self._value,) + self._values
        ]
