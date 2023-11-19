from argparse import ArgumentParser, Namespace, _SubParsersAction
from logging import getLogger
from typing import Any

logger = getLogger(__name__)


def add_subparser(
    subparsers: "_SubParsersAction[ArgumentParser]", **kwargs: Any
) -> None:
    help = "sync database."

    parser = subparsers.add_parser(
        "sync",
        description=help,
        help=help,
        **kwargs,
    )

    parser.set_defaults(handler=sync_command)


def sync_command(space: Namespace) -> None:
    import tipsql.cli.config
    from tipsql.cli.plugins import get_database_plugin

    config = tipsql.cli.config.load(space.config)
    database_config = config.root.database

    database_plugin = get_database_plugin(database_config)
    database_plugin.sync_database(database_config)
