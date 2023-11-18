from inspect import isclass
from typing import (
    Annotated,
    Any,
    Callable,
    Literal,
    TypeAliasType,
    Unpack,
    get_origin,
    overload,
    override,
)

from tipsql.core.query.querable import ToQuery, ToQueryParams
from tipsql.core.types.hint import NO_ARG, NoArg
from tipsql.core.value import SQLType


class HasColumnName(ToQuery):
    @property
    def column_name(self) -> str:
        ...


class ColumnType[PyType](HasColumnName, SQLType[PyType]):
    __slots__ = ("schema_name", "table_name", "_column_name")

    def __init__(
        self,
        schema_name: str | None,
        table_name: str,
        column_name: str,
        py_type: type[PyType],
    ) -> None:
        self.schema_name = schema_name
        self.table_name = table_name
        self._column_name = column_name
        super().__init__(py_type)

    @property
    @override
    def column_name(self) -> str:
        return self._column_name

    @override
    def _to_query(self, **kwargs: Unpack[ToQueryParams]) -> str:
        if self.schema_name is None:
            return f"{self.table_name}.{self.column_name}"

        else:
            return f"{self.schema_name}.{self.table_name}.{self.column_name}"

    def __hash__(self) -> int:
        return hash((self.schema_name, self.table_name, self.column_name))

    def __str__(self) -> str:
        return self._to_query(
            separator=" ",
            tabsize=0,
            tmp_tables=set(),
        )


class Column[SqlType: ColumnType, PyType]:
    __slots__ = ("schema_name", "table_name", "column_name", "sql_type", "py_type")

    def __init__(
        self,
        schema_name: str | None,
        table_name: str,
        column_name: str,
        sql_type: type[SqlType],
        py_type: type[PyType],
    ) -> None:
        self.schema_name = schema_name
        self.table_name = table_name
        self.column_name = column_name
        self.sql_type = sql_type
        self.py_type = py_type

    @overload
    def __get__(self, instance: None, objtype: type[Any]) -> SqlType:
        ...

    @overload
    def __get__(self, instance: object, objtype: type[Any]) -> PyType:
        ...

    def __get__(
        self, instance: object | None, objtype: type[Any]
    ) -> PyType | "SqlType":
        if instance is None:
            return self.sql_type(
                self.schema_name, self.table_name, self.column_name, self.py_type
            )

        else:
            return self.py_type()

    def __hash__(self) -> int:
        return hash((self.schema_name, self.table_name, self.column_name))

    def __str__(self) -> str:
        if self.schema_name is None:
            return f"{self.table_name}.{self.column_name}"

        else:
            return f"{self.schema_name}.{self.table_name}.{self.column_name}"


def column[T](
    primary_key: Literal[True] | NoArg = NO_ARG,
    init: bool | NoArg = NO_ARG,
    default: T | NoArg = NO_ARG,
    default_factory: Callable[[], T] | NoArg = NO_ARG,
) -> Column[Any, T]:
    """Column type annotation."""
    ...


def find_column_type(cls, key: str) -> tuple[type[ColumnType], type] | None:
    if key in cls.__annotations__:
        annotation = cls.__annotations__[key]

        if hasattr(annotation, "__origin__"):
            origin = annotation.__origin__

            # case: Annotated Column type
            if get_origin(annotation) is Annotated and hasattr(origin, "__origin__"):
                annotation = origin
                origin = origin.__origin__

            # When field type is Column, return SQLType instance
            if isclass(origin) and issubclass(origin, Column):
                sql_type = annotation.__args__[0]
                py_type = annotation.__args__[1]

                while isinstance(sql_type, TypeAliasType):
                    sql_type = sql_type.__value__

                return (sql_type, py_type)

    return None
