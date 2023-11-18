import importlib.metadata
from typing import Literal, Union

from tipsql.core.plugins.database_plugin import TipsqlDatabasePlugin

database_plugin_types: list[type[TipsqlDatabasePlugin]] = [
    database_plugin.load()
    for database_plugin in importlib.metadata.entry_points(
        group="tipsql.database.plugin"
    )
]
for database_plugin_type in database_plugin_types:
    if not issubclass(database_plugin_type, TipsqlDatabasePlugin):
        from tipsql.cli.exception import TipsqlDatabasePluginTypeError

        raise TipsqlDatabasePluginTypeError(database_plugin_type)

_database_plugins = [
    database_plugin_type() for database_plugin_type in database_plugin_types
]
_database_names = [plugin.database_name for plugin in _database_plugins]
_database_configs = [plugin.database_config for plugin in _database_plugins]

if len(_database_configs) == 0:
    # NOTE: for lazy error handling, this timing set None type.
    #       `tipsql new` command occured TipsqlDatabasePluginNotFoundError.
    #
    # from tipsql.cli.exception import TipsqlDatabasePluginNotFoundError
    # raise TipsqlDatabasePluginNotFoundError()

    type DatabaseType = None
    type DatabaseConfig = None

else:
    DatabaseType = Literal[*_database_names]  # type: ignore
    DatabaseConfig = Union[*_database_configs]  # type: ignore

DATABASE_PLUGIN_MAP = {plugin.database_name: plugin for plugin in _database_plugins}


def get_database_plugin(data: DatabaseConfig) -> TipsqlDatabasePlugin:
    return DATABASE_PLUGIN_MAP[data.type]  # type: ignore
