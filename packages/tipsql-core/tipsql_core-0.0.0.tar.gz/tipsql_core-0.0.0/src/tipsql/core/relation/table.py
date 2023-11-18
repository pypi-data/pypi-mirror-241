from functools import cache, lru_cache
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    ClassVar,
    LiteralString,
    TypedDict,
    Unpack,
    dataclass_transform,
    override,
)

from tipsql.core.query.querable import ToQuery, ToQueryParams
from tipsql.core.relation.column import column, find_column_type
from tipsql.core.types.hint import NO_ARG, NoArg


class _TableMetaclass(ToQuery, type):
    __tipsql_database_name__: ClassVar[str | None]
    __tipsql_schema_name__: ClassVar[str | None]
    __tipsql_table_name__: ClassVar[str]

    @cache
    def __getattr__(cls, key: str) -> Any:
        """
        Implementation to return an SQLType instance
        when the field type is accessed as a class property
        rather than an instance property.
        """

        column_type = find_column_type(cls, key)
        if column_type is not None:
            sql_type, py_type = column_type

            return sql_type(
                schema_name=cls.__tipsql_schema_name__,
                table_name=cls.__tipsql_table_name__,
                column_name=key,
                py_type=py_type,
            )

        if key in ("__tipsql_table_name__") and key not in cls.__dict__:
            return calc_table_name(cls)

        elif (
            key in ("__tipsql_database_name__", "__tipsql_schema_name__")
            and key not in cls.__dict__
        ):
            return None

        else:
            return getattr(super(), key)

    def __setattr__(cls, key: str, value: Any) -> None:
        super().__setattr__(key, value)

    def __delattr__(cls, key: str) -> None:
        super().__delattr__(key)

    @override
    def _to_query(cls, **kwargs: Unpack[ToQueryParams]) -> str:
        return ".".join(
            name
            for name in (
                cls.__tipsql_database_name__,
                cls.__tipsql_schema_name__,
                cls.__tipsql_table_name__,
            )
            if name is not None
        )


class Table[InsertColumns: TypedDict, UpdateColumns: TypedDict](
    metaclass=_TableMetaclass
):
    def __init__(
        self,
        **columns: Unpack[InsertColumns],  # type: ignore
    ) -> None:
        for column_name, column_type in columns.items():
            setattr(self, column_name, column_type)

    def __init_subclass__(cls) -> None:
        super().__init_subclass__()


@lru_cache
def calc_table_name(cls: type) -> str:
    import re

    return re.sub(r"(?<!^)(?=[A-Z])", "_", cls.__name__).lower()


@dataclass_transform(field_specifiers=(column,))
def table[InsertColumns: TypedDict, UpdateColumns: TypedDict](
    database_name_or_schema_name_or_table_name: LiteralString,
    schema_name_or_table_name: LiteralString | NoArg = NO_ARG,
    table_name: LiteralString | NoArg = NO_ARG,
    /,
) -> Callable[[type[Table]], type[Table]]:
    def decorate(cls: type[Table]) -> type[Table]:
        match (
            database_name_or_schema_name_or_table_name,
            schema_name_or_table_name,
            table_name,
        ):
            case str() as _table_name, NoArg(), NoArg():
                cls.__tipsql_table_name__ = _table_name

            case str() as _schema_name, str() as _table_name, NoArg():
                cls.__tipsql_schema_name__ = _schema_name
                cls.__tipsql_table_name__ = _table_name

            case str() as _database_name, str() as _schema_name, str() as _table_name:
                cls.__tipsql_database_name__ = _database_name
                cls.__tipsql_schema_name__ = _schema_name
                cls.__tipsql_table_name__ = _table_name

        return cls

    return decorate


if TYPE_CHECKING:

    class NoTable(Table):
        """Type Hint for `select` query has no table.

        >>> from tipsql.core.query.builder import QueryBuilder
        >>> from tipsql.core.query.statement.select import SelectQuery
        >>> from tests.data.relation import User
        >>>
        >>> query: SelectQuery[*tuple[()], "NoTable"] = (
        ...     QueryBuilder().chain()
        ...     .from_(None)
        ...     .select(
        ...         1,
        ...         True,
        ...         "name",
        ...     )
        ... )
        """

        __slots__ = ()
