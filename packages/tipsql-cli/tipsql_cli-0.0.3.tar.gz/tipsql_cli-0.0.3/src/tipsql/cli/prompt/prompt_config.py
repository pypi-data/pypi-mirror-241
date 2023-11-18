from tipsql.cli.config.v1.config import ConfigV1
from tipsql.cli.plugins import DatabaseType
from tipsql.cli.prompt.prompt_database_type import prompt_database_type


def prompt_config(
    database_type: DatabaseType | None,  # type: ignore
) -> ConfigV1:
    database_type = prompt_database_type(database_type)

    return ConfigV1.model_validate(
        {
            "version": 1,
            "database": {
                "type": database_type,
            },
        }
    )
