import textwrap
from typing import (
    Unpack,
    override,
)

from tipsql.core.query.condition import Condition
from tipsql.core.query.querable import ToQuery, ToQueryParams


class WhereClause(ToQuery):
    def __init__(self, condition: Condition) -> None:
        self._condition = condition

    @override
    def _to_query(self, **kwargs: Unpack[ToQueryParams]) -> str:
        separator = kwargs["separator"]
        tabsize = kwargs["tabsize"]

        query = f"WHERE{separator}"
        query += textwrap.indent(self._condition._to_query(**kwargs), " " * tabsize)

        return query
