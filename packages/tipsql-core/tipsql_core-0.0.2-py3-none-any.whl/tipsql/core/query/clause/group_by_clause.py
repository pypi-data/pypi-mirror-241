import textwrap
from typing import (
    Any,
    Iterable,
    Unpack,
    override,
)

from tipsql.core.query.querable import ToQuery, ToQueryParams


class GroupByClause(ToQuery):
    def __init__(self, columns: Iterable[Any]) -> None:
        self._columns = columns

    @override
    def _to_query(self, **kwargs: Unpack[ToQueryParams]) -> str:
        separator = kwargs["separator"]
        tabsize = kwargs["tabsize"]

        query = f"GROUP BY{separator}"
        query += textwrap.indent(
            separator.join(f"{column}," for column in self._columns)[:-1],
            " " * tabsize,
        )

        return query
