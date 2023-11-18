try:
    from pydantic import ConfigDict  # type: ignore
    from pydantic.dataclasses import dataclass as pydantic_dataclass  # type: ignore

    dataclass = pydantic_dataclass(config=ConfigDict(extra="forbid"))
    extra_forbid_dataclass = pydantic_dataclass(config=ConfigDict(extra="forbid"))

except ImportError:
    from dataclasses import dataclass
    from logging import getLogger

    logger = getLogger(__name__)
    logger.warning(
        "pydantic is not installed, "
        'using "dataclasses" instead of "extra_forbid_dataclass".',
    )

    extra_forbid_dataclass = dataclass

__all__ = ["dataclass", "extra_forbid_dataclass"]
