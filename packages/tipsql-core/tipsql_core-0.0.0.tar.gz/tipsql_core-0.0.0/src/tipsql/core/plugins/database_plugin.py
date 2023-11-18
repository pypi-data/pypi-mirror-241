from abc import ABC, abstractmethod


class TipsqlDatabasePlugin(ABC):
    """
    Base class for database plugins.
    """

    @property
    @abstractmethod
    def database_name(self) -> str:
        ...

    @property
    @abstractmethod
    def database_config(self) -> type:
        ...

    @abstractmethod
    def sync_database(self, config) -> None:
        ...
