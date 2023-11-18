import textwrap
from typing import Unpack, override

from tipsql.core.query.querable import ToQuery, ToQueryParams
from tipsql.core.relation.trait import SelectableRelation


class FromClause[T: SelectableRelation](ToQuery):
    def __init__(self, table: type[T]):
        self._table = table

    @override
    def _to_query(self, **kwargs: Unpack[ToQueryParams]) -> str:
        separator = kwargs["separator"]
        tabsize = kwargs["tabsize"]

        query = f"FROM{separator}"
        query += textwrap.indent(self._table._to_query(**kwargs), " " * tabsize)

        return query
