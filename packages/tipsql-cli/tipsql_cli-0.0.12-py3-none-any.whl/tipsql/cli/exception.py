from pathlib import Path

from tipsql.core.exception import TipsqlError


class TipsqlFileNotFoundError(TipsqlError, FileNotFoundError):
    def __init__(self, path: Path) -> None:
        self.path = path

    @property
    def message(self) -> str:
        return f'file not found: "{self.path}"'


class TipsqlFileExistsError(TipsqlError, FileExistsError):
    def __init__(self, path: Path) -> None:
        self.path = path

    @property
    def message(self) -> str:
        return f'file already exists: "{self.path}"'


class TipsqlDatabasePluginTypeError(TipsqlError, TypeError):
    def __init__(self, database_plugin_type: type) -> None:
        self._database_plugin_type = database_plugin_type

    @property
    def message(self) -> str:
        return (
            "Expected subclass of TipsqlDatabasePlugin, "
            f"got {self._database_plugin_type!r}"
        )


class TipsqlDatabasePluginNotFoundError(TipsqlError, ImportError):
    @property
    def message(self) -> str:
        return (
            "tipsql database plugin not found. "
            "please install your database plugin "
            'like "tipsql-sqlite3", "tipsql-postgresql".'
        )
