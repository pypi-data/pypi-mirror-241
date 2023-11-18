from typing import (
    LiteralString,
)

from tipsql.core.query.clause.from_clause import FromClause
from tipsql.core.query.clause.with_clause import WithTailClause
from tipsql.core.query.statement.select import (
    SelectableRelations,
    SelectStmt,
)
from tipsql.core.relation.temporary_table import NamedTemporaryTable
from tipsql.core.relation.trait import SelectableRelation


class With_[*Ts, T: SelectableRelation]:
    """A class that expresses the behavior of the with clause.

    NOTE: Several writing styles were considered during the review phase.

    1. call args a temporary table in the with method.

        ```python
        builder.with(Admin, Master, Professor).from_(User)
        ```

        This seemed to be the most beautiful way to write this case,
        but it could not be adopted because `TypeVarTuple` is not currently allowed
        to have bound constraints.

    2. using `__call__` method, similar to SQL syntax.

        ```python
        builder.with(Admin)(Master)(Professor).from_(User)
        ```

        I did not adopt it for readability in Python.

    3. The way to use a combination of `LiteralString` and `SelectQuery`,
        instead of `NamedTemporaryTable`.

        ```python
        builder.with(
            "admin",
            as_=builder.from_(...).select(...)
        ).with(
            "master",
            as_=builder.from_(...).select(...)
        ).with(
            "professor",
            as_=builder.from_(...).select(...)
        ).from_(User)
        ```

        From the standpoint of reusability and readability/simplicity,
        I choice `NamedTemporaryTable` usage only.
    """

    def __init__(self, tables: SelectableRelations[*Ts, T]) -> None:
        self._tables = tables

    def with_[TableName: LiteralString](
        self, table: type[NamedTemporaryTable[TableName]]
    ) -> "With_[*Ts, T, NamedTemporaryTable[TableName]]":
        return With_(self._tables + (WithTailClause(table),))  # type: ignore

    def from_[U: SelectableRelation](self, table: type[U]) -> SelectStmt[*Ts, T, U]:
        """Assemble a `select ...` statement."""

        return SelectStmt(self._tables + (FromClause(table),))  # type: ignore
