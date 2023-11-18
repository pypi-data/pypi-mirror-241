from typing import (
    overload,
)

from tipsql.core.query.clause.select_columns_clause import (
    SelectColumnsClause,
    SelectDistinctcolumnsClause,
)
from tipsql.core.relation.column import HasColumnName
from tipsql.core.relation.trait import SelectableRelation
from tipsql.core.utils.rename import rename


class SelectColumnsContext[*Ts, T: SelectableRelation]:
    __slots__ = ()

    @overload
    def __call__(
        self, column: dict[str, HasColumnName | int | float | str | bool | None]
    ) -> SelectColumnsClause[*Ts, T]:
        ...

    @overload
    def __call__(
        self, column: HasColumnName, *columns: HasColumnName
    ) -> SelectColumnsClause[*Ts, T]:
        ...

    def __call__(self, column, *columns) -> SelectColumnsClause[*Ts, T]:
        if isinstance(column, dict):
            return SelectColumnsClause(
                rename(column, as_=name) for name, column in column.items()
            )

        else:
            return SelectColumnsClause((column,) + columns)

    def distinct(
        self, column: HasColumnName, *columns: HasColumnName
    ) -> SelectDistinctcolumnsClause[*Ts, T]:
        return SelectDistinctcolumnsClause((column,) + columns)
