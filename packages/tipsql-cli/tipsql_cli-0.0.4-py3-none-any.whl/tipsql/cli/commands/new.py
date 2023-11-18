from argparse import ArgumentParser, Namespace, _SubParsersAction
from logging import getLogger
from typing import get_args

from tipsql.cli.exception import TipsqlFileExistsError
from tipsql.cli.plugins import DatabaseType

logger = getLogger(__name__)


def add_subparser(subparsers: "_SubParsersAction[ArgumentParser]", **kwargs) -> None:
    description = "create new [tipsql]tipsql[/] config"

    parser = subparsers.add_parser(
        "new",
        description=description,
        help=description,
        **kwargs,
    )

    parser.add_argument(
        "--database-type",
        type=str,
        choices=get_args(DatabaseType),
        required=False,
        help="database type.",
    )

    parser.add_argument(
        "--overwrite",
        action="store_true",
        default=False,
        help="overwrite existing config.",
    )

    parser.set_defaults(handler=new_command)


def new_command(space: Namespace) -> None:
    from tipsql.cli.prompt.prompt_config import prompt_config
    from tipsql.cli.utils import yaml
    from tipsql.cli.utils.path import DEFAULT_CONFIG_FILE

    config = prompt_config(space.database_type)

    config_path = DEFAULT_CONFIG_FILE
    if config_path.exists() and not space.overwrite:
        raise TipsqlFileExistsError(config_path)

    with open(config_path, "w") as file:
        file.write(yaml.dump(config))

    logger.info(f'Create a new config: "{config_path.name}" 🚀')
