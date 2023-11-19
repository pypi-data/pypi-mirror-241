from abc import ABCMeta, abstractmethod
from typing import Any, Callable, Literal, NotRequired, TypedDict, Unpack, assert_never


class QmarkParam(TypedDict):
    style: Literal["qmark"]
    params: NotRequired[list[Any]]


class NumericParam(TypedDict):
    style: Literal["numeric"]
    params: NotRequired[list[Any]]


class NamedParam(TypedDict):
    style: Literal["named"]
    params: NotRequired[dict[str, Any]]


class FormatParam(TypedDict):
    style: Literal["format"]
    params: NotRequired[list[Any]]


class PyformatParam(TypedDict):
    style: Literal["pyformat"]
    params: NotRequired[dict[str, Any]]
    stringify: NotRequired[bool]


type QueryParam = QmarkParam | NumericParam | NamedParam | FormatParam | PyformatParam


class ToQueryParams(TypedDict):
    separator: Literal[" ", "\n"]
    tabsize: int
    tmp_tables: set[str]
    param: NotRequired[QueryParam]


class ToQuery(metaclass=ABCMeta):
    @abstractmethod
    def _to_query(self, **kwargs: Unpack[ToQueryParams]) -> str:
        ...


class ToQueryFunc(ToQuery):
    def __init__(self, func: Callable[[ToQueryParams], str]) -> None:
        self._func = func

    def _to_query(self, **kwargs: Unpack[ToQueryParams]) -> str:
        return self._func(kwargs)


def querify(value, **kwargs: Unpack[ToQueryParams]) -> str:
    if to_query := getattr(value, "_to_query", None):
        return to_query(**kwargs)

    else:
        if (param := kwargs.get("param")) is not None:
            match param["style"]:
                case "qmark":
                    return _set_qmark_params(param.get("params", []), value)

                case "numeric":
                    return _set_numeric_params(param.get("params", []), value)

                case "named":
                    return _set_named_params(param.get("params", {}), value)

                case "format":
                    return _set_format_params(param.get("params", []), value)

                case "pyformat":
                    return _set_pyformat_params(
                        param.get("params", {}),
                        value,
                        stringify=param.get("stringify", False),
                    )

                case _:
                    assert_never(param["style"])

        else:
            if isinstance(value, bool):
                return "TRUE" if value else "FALSE"

            elif isinstance(value, str):
                return f"'{value}'"

            elif value is None:
                return "NULL"

            else:
                return str(value)


def _set_qmark_params(params: list[Any], value: Any) -> str:
    params.append(value)

    return "?"


def _set_numeric_params(params: list[Any], value: Any) -> str:
    params.append(value)

    return f":{len(params)}"


def _set_named_params(params: dict[str, Any], value: Any) -> str:
    key = f"p{len(params)+1}"
    params[key] = value

    return f":{key}"


def _set_format_params(params: list[Any], value: Any) -> str:
    if isinstance(value, str):
        params.append(value)

        return "%s"

    elif isinstance(value, int):
        params.append(value)

        return "%ld"

    elif isinstance(value, float):
        params.append(value)

        return "%lf"

    elif value is None:
        return "NULL"

    elif isinstance(value, bool):
        return "TRUE" if value else "FALSE"

    else:
        params.append(str(value))

        return "%s"


def _set_pyformat_params(
    params: dict[str, Any], value: Any, *, stringify: bool = False
) -> str:
    key = f"p{len(params)+1}"

    if stringify:
        params[key] = str(value)

        return f"%({key})s"

    if isinstance(value, str):
        params[key] = value

        return f"%({key})s"

    elif isinstance(value, int):
        params[key] = value

        return f"%({key})ld"

    elif isinstance(value, float):
        params[key] = value

        return f"%({key})lf"

    elif value is None:
        return "NULL"

    elif isinstance(value, bool):
        return "TRUE" if value else "FALSE"

    else:
        params[key] = value

        return f"%({key})s"


def build(builder, params: QueryParam) -> tuple[str, list[Any] | dict[str, Any]]:
    parameters: list[Any] | dict[str, Any]

    match params["style"]:
        case "qmark":
            parameters = []
            params["params"] = parameters

        case "numeric":
            parameters = []
            params["params"] = parameters

        case "named":
            parameters = {}
            params["params"] = parameters

        case "format":
            parameters = []
            params["params"] = parameters

        case "pyformat":
            parameters = {}
            params["params"] = parameters

    return (
        querify(
            builder,
            separator="\n",
            tabsize=4,
            tmp_tables=set(),
            param=params,
        )
        + ";",
        parameters,
    )
