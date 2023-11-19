from typing import (
    TYPE_CHECKING,
    Any,
    LiteralString,
    Protocol,
    Sequence,
    TypedDict,
    overload,
)

from tipsql.core.query.clause.from_clause import FromClause
from tipsql.core.query.clause.with_clause import WithHeadClause
from tipsql.core.query.statement.delete import DeletableRelation, WherableDeleteQuery
from tipsql.core.query.statement.insert import InsertableRelation, InsertStmt
from tipsql.core.query.statement.select import (
    SelectFromWhereGroupByHaving,
    SelectStmt,
)
from tipsql.core.query.statement.update import UpdatableRelation, UpdateStmt
from tipsql.core.query.statement.with_ import With_
from tipsql.core.relation.temporary_table import NamedTemporaryTable
from tipsql.core.relation.trait import SelectableRelation

if TYPE_CHECKING:
    from tipsql.core.query.querable import QueryParam
    from tipsql.core.relation.table import NoTable


class BuildProtcol(Protocol):
    def build(self, params: "QueryParam") -> tuple[str, Sequence[Any] | dict[str, Any]]:
        ...


class _QueryBuilder:
    def with_[TableName: LiteralString](
        self, table: type[NamedTemporaryTable[TableName]]
    ) -> With_[NamedTemporaryTable[TableName]]:
        return With_((WithHeadClause(table),))

    @overload
    def from_(self, table: None) -> "SelectFromWhereGroupByHaving[NoTable]":
        ...

    @overload
    def from_[T: SelectableRelation](self, table: type[T]) -> SelectStmt[T]:
        ...

    def from_(self, table):
        """Assemble a `select ...` statement."""
        if table is None:
            return SelectFromWhereGroupByHaving(tables=())  # type: ignore
        else:
            return SelectStmt((FromClause(table),))

    def insert_into[Columns: TypedDict](
        self, table: type[InsertableRelation[Columns]]
    ) -> InsertStmt[Columns]:
        """Assemble a `insert into ...` statement."""

        return InsertStmt(table)

    def update[Columns: TypedDict](
        self, table: type[UpdatableRelation[Columns]]
    ) -> UpdateStmt[Columns]:
        """Assemble a `update ...` statement."""

        return UpdateStmt(table)

    def delete_from[T: DeletableRelation](
        self, table: type[T]
    ) -> WherableDeleteQuery[T]:
        """Assemble a `delete from ...` statement."""

        return WherableDeleteQuery(table)


class QueryBuilder(_QueryBuilder):
    def chain(self) -> _QueryBuilder:
        """Support functions to make chain methods look pretty in `black` formatter.

        Does not affect the query building logic.

        >>> from tipsql.core.query.builder import QueryBuilder
        >>> from tests.data.relation import User
        >>> query = (
        ...     QueryBuilder().chain()
        ...     .from_(User)
        ...     .where(User.id == 1)
        ...     .select(
        ...         User.id,
        ...         User.name,
        ...     )
        ... )
        """

        return self
