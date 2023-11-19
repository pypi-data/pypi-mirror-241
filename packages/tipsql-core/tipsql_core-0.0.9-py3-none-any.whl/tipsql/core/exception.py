from abc import ABCMeta, abstractmethod
from pathlib import Path

import jinja2


class TipsqlException(Exception, metaclass=ABCMeta):
    @property
    @abstractmethod
    def message(self) -> str:
        ...

    def __str__(self) -> str:
        return self.message


class TipsqlError(TipsqlException):
    pass


class TipsqlTemporaryTableColumnNameError(TipsqlError):
    def __init__(self, table_name: str, column_name) -> None:
        self.table_name = table_name
        self.column_name = column_name

    @property
    def message(self) -> str:
        return f'TemporaryTable("{self.table_name}") has no column "{self.column_name}"'


class TipsqlJinjaTemplateSyntaxError(jinja2.TemplateSyntaxError, TipsqlError):
    def __init__(self, template_path: Path, error: jinja2.TemplateSyntaxError) -> None:
        self.template_path = template_path
        self.error = error
        self.__traceback__ = error.__traceback__

    @property
    def message(self) -> str:
        return f'"{self.template_path}" template syntax error: {self.error}'


class TipsqlJinjaTemplateRuntimeError(jinja2.TemplateRuntimeError, TipsqlError):
    def __init__(self, template_path: Path, error: jinja2.TemplateRuntimeError) -> None:
        self.template_path = template_path
        self.error = error
        self.__traceback__ = error.__traceback__

    @property
    def message(self) -> str:
        return f'"{self.template_path}" jinja runtime error: {self.error}'


class TipsqlJinjaRenderError(TipsqlError):
    def __init__(self, template_path: Path, error: Exception) -> None:
        self.template_path = template_path
        self.error = error
        self.__traceback__ = error.__traceback__

    @property
    def message(self) -> str:
        return f'"{self.template_path}" jinja render error: {self.error}'


class TipsqlEnvironmentKeyError(TipsqlError, KeyError):
    def __init__(self, env_key: str) -> None:
        self.env_key = env_key

    @property
    def message(self) -> str:
        return f'environment variable not found: "{self.env_key}"'
