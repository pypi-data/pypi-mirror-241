import textwrap
from collections import namedtuple
from typing import (
    TYPE_CHECKING,
    Any,
    ClassVar,
    LiteralString,
    Unpack,
    override,
)

from tipsql.core.exception import TipsqlTemporaryTableColumnNameError
from tipsql.core.query.querable import ToQuery, ToQueryParams
from tipsql.core.types.data import AnyType

if TYPE_CHECKING:
    from tipsql.core.query.statement.select import SelectQuery
    from tipsql.core.relation.trait import SelectableRelation


class _NamedTemporaryTableMetaClass(ToQuery, type):
    __tipsql_table_name__: ClassVar[str]

    def __getattr__(self, key: str) -> "Any":
        return None

    @override
    def _to_query(cls, **kwargs: Unpack[ToQueryParams]) -> str:
        return ".".join(
            name for name in (cls.__tipsql_table_name__,) if name is not None
        )


class TemporaryTable:
    pass


class NamedTemporaryTableType[TableName: LiteralString, *Ts, T: SelectableRelation](
    ToQuery
):
    __slots__ = ("__tipsql_table_name__", "_select_query")

    def __init__(self, table_name: TableName, select_query: "SelectQuery"):
        self.__tipsql_table_name__ = table_name
        self._select_query = select_query
        self._columns = {
            column.column_name: AnyType(None, table_name, column.column_name, Any)
            for column in self._select_query._columns._columns
        }

    def __getattr__(self, key: str) -> Any:
        if key in self._columns:
            return self._columns[key]

        raise TipsqlTemporaryTableColumnNameError(self.__tipsql_table_name__, key)

    def _to_query(self, **kwargs: Unpack[ToQueryParams]) -> str:
        separator = kwargs["separator"]
        tabsize = kwargs["tabsize"]
        tmp_tables = kwargs.get("tmp_tables", set())

        if self.__tipsql_table_name__ in tmp_tables:
            return self.__tipsql_table_name__

        tmp_tables.add(self.__tipsql_table_name__)

        query = f"({separator}"

        query += textwrap.indent(
            self._select_query._to_query(**kwargs),
            " " * tabsize,
        )
        query += f"{separator}) AS {self.__tipsql_table_name__}"

        return query


class NamedTemporaryTable[TableName: LiteralString](
    metaclass=_NamedTemporaryTableMetaClass
):
    __slots__ = ("__tipsql_table_name__", "_named_tuple", "_select_query")

    def __init__(self, table_name: TableName, select_query: "SelectQuery") -> None:
        self.__tipsql_table_name__ = table_name
        self._select_query = select_query

        columns = {
            column.column_name: AnyType(None, table_name, column.column_name, Any)
            for column in self._select_query._columns._columns
        }
        self._named_tuple = namedtuple(table_name, columns.keys())(**columns)

    def __getattr__(self, key: str) -> Any:
        return getattr(self._named_tuple, key)


def make_named_temporary_table_type[TableName: LiteralString](
    table_name: TableName, select_query: "SelectQuery"
) -> type[NamedTemporaryTable[TableName]]:
    return NamedTemporaryTableType(table_name, select_query)  # type: ignore
