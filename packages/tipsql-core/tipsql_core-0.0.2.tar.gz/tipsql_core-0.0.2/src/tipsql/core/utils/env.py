from typing import Any, Literal


def get_env(
    env_key: str, default: Any | None = None, *, raise_error: Literal[True, None] = None
) -> Any:
    import os

    try:
        return os.environ[env_key]
    except KeyError:
        if raise_error:
            from tipsql.core.exception import TipsqlEnvironmentKeyError

            raise TipsqlEnvironmentKeyError(env_key)

        return default
