import textwrap
from typing import TYPE_CHECKING, Unpack

from tipsql.core.query.querable import ToQuery, ToQueryParams
from tipsql.core.relation.temporary_table import NamedTemporaryTable
from tipsql.core.relation.trait import SelectableRelation

if TYPE_CHECKING:
    pass


class WithClause[T: NamedTemporaryTable](ToQuery):
    def __init__(self, named_temp_table: type[T]) -> None:
        self._table_name = named_temp_table.__tipsql_table_name__
        self._as = named_temp_table._select_query


class WithHeadClause[T: SelectableRelation](WithClause):
    def _to_query(self, **kwargs: Unpack[ToQueryParams]) -> str:
        separator = kwargs["separator"]
        tabsize = kwargs["tabsize"]
        kwargs.get("tmp_tables", set()).add(self._table_name)

        query = f"WITH {self._table_name} AS ({separator}"
        query += textwrap.indent(self._as._to_query(**kwargs), " " * tabsize)

        return query + f"{separator})"


class WithTailClause[T: SelectableRelation](WithClause):
    def _to_query(self, **kwargs: Unpack[ToQueryParams]) -> str:
        separator = kwargs["separator"]
        tabsize = kwargs["tabsize"]
        kwargs.get("tmp_tables", set()).add(self._table_name)

        query = f",{separator}{self._table_name} AS ({separator}"
        query += textwrap.indent(self._as._to_query(**kwargs), " " * tabsize)

        return query + f"{separator})"
