import textwrap
from typing import (
    Iterable,
    Unpack,
    override,
)

from tipsql.core.query.querable import ToQuery, ToQueryParams
from tipsql.core.relation.column import HasColumnName
from tipsql.core.relation.trait import SelectableRelation


class SelectColumnsClause[*Ts, T: SelectableRelation](ToQuery):
    def __init__(self, columns: Iterable[HasColumnName]) -> None:
        self._columns = columns

    @override
    def _to_query(self, **kwargs: Unpack[ToQueryParams]) -> str:
        separator = kwargs["separator"]
        tabsize = kwargs["tabsize"]

        query = f"SELECT{separator}"
        query += textwrap.indent(
            separator.join(
                column._to_query(**kwargs) + "," for column in self._columns
            )[:-1],
            " " * tabsize,
        )

        return query


class SelectDistinctcolumnsClause[*Ts, T: SelectableRelation](
    SelectColumnsClause[*Ts, T]
):
    @override
    def _to_query(self, **kwargs: Unpack[ToQueryParams]) -> str:
        separator = kwargs["separator"]
        tabsize = kwargs["tabsize"]

        query = f"SELECT{separator}"
        query += textwrap.indent(f"DISTINCT{separator}", " " * tabsize)
        query += textwrap.indent(
            separator.join(
                column._to_query(**kwargs) + "," for column in self._columns
            )[:-1],
            " " * 2 * tabsize,
        )

        return query
