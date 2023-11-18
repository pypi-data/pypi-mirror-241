from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Iterable,
    LiteralString,
    Never,
    Sequence,
    Union,
    Unpack,
    overload,
)

from tipsql.core.context.select_context import SelectColumnsContext
from tipsql.core.query.clause.from_clause import FromClause
from tipsql.core.query.clause.group_by_clause import GroupByClause
from tipsql.core.query.clause.having_clause import HavingClause
from tipsql.core.query.clause.join_clause import (
    CrossJoinClause,
    FullOuterJoinClause,
    InnerJoinClause,
    JoinClause,
    LeftOuterJoinClause,
)
from tipsql.core.query.clause.order_by_clause import OrderByClause
from tipsql.core.query.clause.select_columns_clause import (
    SelectColumnsClause,
)
from tipsql.core.query.clause.where_clause import WhereClause
from tipsql.core.query.clause.with_clause import WithClause
from tipsql.core.query.condition import (
    Condition,
    convert_to_condition,
)
from tipsql.core.query.expression import Expression
from tipsql.core.query.querable import QueryParam, ToQuery, ToQueryParams, build
from tipsql.core.relation.temporary_table import (
    NamedTemporaryTable,
    make_named_temporary_table_type,
)
from tipsql.core.relation.trait import SelectableRelation
from tipsql.core.utils.rename import rename
from typing_extensions import deprecated

type SelectableRelations[*Ts, T: SelectableRelation] = tuple[
    *Ts,
    Union[
        FromClause[T],
        JoinClause[T],
        WithClause[T],  # type: ignore
    ],
]


if TYPE_CHECKING:
    from tipsql.core.context.condition_context import ConditionContext
    from tipsql.core.relation.column import ColumnType, HasColumnName


class Selectable[*Ts, T: SelectableRelation]:
    def __init__(
        self,
        tables: SelectableRelations[*Ts, T],
        where: Condition | None = None,
        group_by: Iterable[Any] | None = None,
        having: Condition | None = None,
    ) -> None:
        self._tables = tables
        self._where = where
        self._group_by = group_by
        self._having = having

    @overload
    def select(
        self,
        column: dict[str, "HasColumnName | int | float | str | bool | None"],
    ) -> "OrderableSelectQuery[*Ts, T]":
        ...

    @overload
    def select(
        self,
        column: Callable[[SelectColumnsContext[*Ts, T]], SelectColumnsClause[*Ts, T]],
    ) -> "OrderableSelectQuery[*Ts, T]":
        ...

    @overload
    def select(
        self,
        column: "HasColumnName",
        *columns: "HasColumnName",
    ) -> "OrderableSelectQuery[*Ts, T]":
        ...

    def select(
        self,
        column,
        *columns,
    ) -> "OrderableSelectQuery[*Ts, T]":
        if callable(column):
            columns = column(SelectColumnsContext())

        elif isinstance(column, dict):
            columns = SelectColumnsClause(
                rename(column, as_=name) for name, column in column.items()
            )

        else:
            columns = SelectColumnsClause((column,) + columns)

        return OrderableSelectQuery(
            columns=columns,
            tables=self._tables,
            where=self._where,
            group_by=self._group_by,
            having=self._having,
        )


class SelectStmt[*Ts, T: SelectableRelation](Selectable[*Ts, T]):
    def __init__(
        self,
        tables: SelectableRelations[*Ts, T],
        where: Callable[["ConditionContext"], Condition] | None = None,
    ) -> None:
        super().__init__(tables=tables, where=convert_to_condition(where))

    @deprecated(
        "For accuracy, use `inner_join()` instead.",
        category=SyntaxWarning,
    )
    def join[U: SelectableRelation](self, table: type[U]) -> Never:
        raise NotImplementedError("For accuracy, use `inner_join()` instead.")

    def inner_join[U: SelectableRelation](
        self, table: type[U]
    ) -> "SelectFromJoin[*Ts, T, U]":
        return SelectFromJoin(
            lambda condition: self._tables + (InnerJoinClause(table, on=condition),),
        )  # type: ignore

    def left_outer_join[U: SelectableRelation](
        self, table: type[U]
    ) -> "SelectFromJoin[*Ts, T, U]":
        return SelectFromJoin(
            lambda condition: self._tables + (LeftOuterJoinClause(table, on=condition),)
        )  # type: ignore

    @deprecated(
        "For readability, use left_outer_join()` instead.",
        category=SyntaxWarning,
    )
    def right_outer_join[U: SelectableRelation](self, table: type[U]) -> Never:
        raise NotImplementedError("For readability, use left_outer_join()` instead.")

    def full_outer_join[U: SelectableRelation](
        self, table: type[U]
    ) -> "SelectFromJoin[*Ts, T, U]":
        return SelectFromJoin(
            lambda condition: self._tables + (FullOuterJoinClause(table, on=condition),)
        )  # type: ignore

    def cross_join[U: SelectableRelation](
        self, table: type[U]
    ) -> "SelectFromJoin[*Ts, T, U]":
        return SelectFromJoin(
            lambda condition: self._tables + (CrossJoinClause(table, on=condition),)
        )  # type: ignore

    def where(
        self,
        condition: Expression[*Ts, T]
        | Callable[["ConditionContext[*Ts, T]"], Condition[*Ts, T]],
    ) -> "SelectFromWhere[*Ts, T]":
        return SelectFromWhere(
            tables=self._tables, where=convert_to_condition(condition)
        )

    def group_by(
        self,
        *columns: "int | HasColumnName",
    ) -> "SelectFromWhereGroupBy[*Ts, T]":
        return SelectFromWhereGroupBy(
            tables=self._tables, where=self._where, group_by=columns
        )


class SelectFromJoin[*Ts, T: SelectableRelation]:
    def __init__(
        self,
        join_table_fn: Callable[[Condition], SelectableRelations[*Ts, T]],
    ) -> None:
        self._join_fn = join_table_fn

    def on(
        self,
        condition: Expression[*Ts, T]
        | Callable[["ConditionContext[*Ts, T]"], Condition[*Ts, T]],
    ) -> SelectStmt[*Ts, T]:
        return SelectStmt(tables=self._join_fn(convert_to_condition(condition)))


class SelectFromWhere[*Ts, T: SelectableRelation](Selectable[*Ts, T]):
    def __init__(
        self,
        tables: SelectableRelations[*Ts, T],
        where: Condition | None = None,
    ) -> None:
        super().__init__(tables=tables, where=where)

    def group_by(
        self,
        *columns: "int | ColumnType",
    ) -> "SelectFromWhereGroupBy[*Ts, T]":
        return SelectFromWhereGroupBy(
            tables=self._tables,
            where=self._where,
            group_by=columns,
        )


class SelectFromWhereGroupBy[*Ts, T: SelectableRelation](Selectable[*Ts, T]):
    def __init__(
        self,
        tables: SelectableRelations[*Ts, T],
        where: Condition | None = None,
        group_by: Iterable[Any] | None = None,
    ) -> None:
        super().__init__(tables=tables, where=where, group_by=group_by)

    def having(
        self,
        condition: Expression[*Ts, T]
        | Callable[["ConditionContext[*Ts, T]"], Condition[*Ts, T]],
    ) -> "SelectFromWhereGroupByHaving[*Ts, T]":
        return SelectFromWhereGroupByHaving(
            tables=self._tables,
            where=self._where,
            group_by=self._group_by,
            having=convert_to_condition(condition),
        )


class SelectFromWhereGroupByHaving[*Ts, T: SelectableRelation](Selectable[*Ts, T]):
    def __init__(
        self,
        tables: SelectableRelations[*Ts, T],
        where: Condition | None = None,
        group_by: Iterable[Any] | None = None,
        having: Condition | None = None,
    ) -> None:
        super().__init__(
            tables=tables,
            where=where,
            group_by=group_by,
            having=having,
        )


class SelectQuery[*Ts, T: SelectableRelation](ToQuery):
    def __init__(
        self,
        *,
        columns: SelectColumnsClause,
        tables: SelectableRelations[*Ts, T],
        where: Condition[*Ts, T] | None = None,
        group_by: Iterable[Any] | None = None,
        having: Condition[*Ts, T] | None = None,
        order_by: Iterable[Any] | None = None,
    ) -> None:
        self._columns = columns
        self._tables = tables
        self._where = where
        self._group_by = group_by
        self._having = having
        self._order_by = order_by

    def _to_query(self, **kwargs: Unpack[ToQueryParams]) -> str:
        query = ""
        separator = kwargs["separator"]

        with_tables = []
        from_tables = []
        for table in self._tables:
            if isinstance(table, WithClause):
                with_tables.append(table)
            else:
                from_tables.append(table)

        for table in with_tables:
            query += table._to_query(**kwargs)

        if len(with_tables) > 0:
            query += separator

        query += self._columns._to_query(**kwargs)

        if self._tables == 0:
            return query

        for table in from_tables:
            query += separator
            query += table._to_query(**kwargs)  # type: ignore

        if self._where is not None:
            query += separator
            query += WhereClause(self._where)._to_query(**kwargs)

        if self._group_by is not None:
            query += separator
            query += GroupByClause(self._group_by)._to_query(**kwargs)

        if self._having is not None:
            query += separator
            query += HavingClause(self._having)._to_query(**kwargs)

        if self._order_by is not None:
            query += separator
            query += OrderByClause(self._order_by)._to_query(**kwargs)

        return query

    def as_[TableName: LiteralString](
        self, table_name: TableName, /
    ) -> type[NamedTemporaryTable[TableName]]:
        self.__tipsql_table_name__ = table_name
        return make_named_temporary_table_type(table_name, self)

    def build(self, params: QueryParam) -> tuple[str, Sequence[Any] | dict[str, Any]]:
        return build(self, params)


class OrderableSelectQuery[*Ts, T: SelectableRelation](SelectQuery[*Ts, T]):
    def __init__(
        self,
        *,
        columns: SelectColumnsClause,
        tables: SelectableRelations[*Ts, T],
        where: Condition | None = None,
        group_by: Iterable[Any] | None = None,
        having: Condition | None = None,
    ) -> None:
        super().__init__(
            columns=columns,
            tables=tables,
            where=where,
            group_by=group_by,
            having=having,
        )

    def order_by(
        self,
        *columns: "int | HasColumnName",
    ) -> SelectQuery[*Ts, T]:
        return SelectQuery(
            columns=self._columns,
            tables=self._tables,
            where=self._where,
            group_by=self._group_by,
            having=self._having,
            order_by=columns,
        )  # type: ignore
