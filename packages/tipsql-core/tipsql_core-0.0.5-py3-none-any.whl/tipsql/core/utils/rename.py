from typing import Any, Unpack, override

from tipsql.core.query.querable import ToQuery, ToQueryParams, querify
from tipsql.core.relation.column import HasColumnName


class Rename(HasColumnName):
    def __init__(
        self, origin: ToQuery | str | int | float | bool | None, /, *, as_: str
    ) -> None:
        self._origin = origin
        self._as = as_

    @property
    def column_name(self) -> str:
        return self._as

    @override
    def _to_query(self, **kwargs: Unpack[ToQueryParams]) -> str:
        if to_query := getattr(self._origin, "_to_query", None):
            origin = to_query(**kwargs)
        else:
            origin = querify(self._origin, **kwargs)

        return f"{origin} AS {self.column_name}"

    def __getattr__(self, name: str) -> Any:
        return getattr(self._origin, name)


def rename(origin, /, *, as_: str) -> Rename:
    return Rename(origin, as_=as_)
