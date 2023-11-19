from typing import Unpack, override

from tipsql.core.query.querable import ToQuery, ToQueryParams


class View(ToQuery):
    @override
    def _to_query(cls, **kwargs: Unpack[ToQueryParams]) -> str:
        return cls.__str__()

    def __str__(self) -> str:
        return "view"
