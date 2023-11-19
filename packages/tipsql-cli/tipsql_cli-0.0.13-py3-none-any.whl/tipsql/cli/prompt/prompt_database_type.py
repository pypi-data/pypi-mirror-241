from typing import get_args

from tipsql.cli.plugins import DatabaseType
from tipsql.cli.prompt.prompt_choice import prompt_choice


def prompt_database_type(database_type: DatabaseType | None) -> DatabaseType:
    if database_type is not None:
        return database_type

    database_types = get_args(DatabaseType)
    match len(database_types):
        case 0:
            from tipsql.cli.exception import TipsqlDatabasePluginNotFoundError

            raise TipsqlDatabasePluginNotFoundError()

        case 1:
            return database_types[0]

        case _:
            return prompt_choice(database_types)
