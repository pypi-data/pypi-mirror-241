import logging
import sys
from argparse import ArgumentParser, BooleanOptionalAction
from logging import getLogger
from pathlib import Path

import tipsql.cli
from rich.console import Console as RichConsole
from rich.logging import RichHandler
from rich_argparse import RichHelpFormatter
from tipsql.cli.utils.path import DEFAULT_CONFIG_FILE

logger = getLogger(__name__)


class TipsqlArgumentParser(ArgumentParser):
    def error(self, message: str):
        self.print_usage(sys.stderr)
        raise RuntimeError(message)


def run(args: list[str] | None = None) -> None:
    verbose = "--verbose" in (args or sys.argv[1:])

    try:
        logging.basicConfig(
            format="%(message)s",
            level=logging.INFO,
            handlers=[
                RichHandler(
                    level=logging.DEBUG,
                    console=RichConsole(stderr=True),
                    show_time=False,
                    show_path=False,
                    rich_tracebacks=True,
                )
            ],
        )
        logging.root.setLevel(logging.DEBUG if verbose else logging.INFO)
        logging.getLogger("snowflake").setLevel(logging.ERROR)

        from tipsql.cli.commands import config_jsonschema, new, sync

        RichHelpFormatter.styles["tipsql"] = "italic bold green"
        RichHelpFormatter.styles["literal"] = RichHelpFormatter.styles[
            "argparse.metavar"
        ]

        parser = TipsqlArgumentParser(
            prog="tipsql",
            description="[tipsql]tipsql[/] is a tool to operate [tipsql]tipsql[/].",
            formatter_class=RichHelpFormatter,
        )

        parser.add_argument(
            "--config",
            type=Path,
            help=f'config filepath. default is [literal]"{DEFAULT_CONFIG_FILE}"[/]',
        )

        parser.add_argument(
            "--version",
            action="version",
            version=f"[argparse.prog]%(prog)s[/] {tipsql.cli.__version__}",
        )

        parser.add_argument(
            "--verbose",
            action=BooleanOptionalAction,
            help="output verbose log",
        )

        subparser = parser.add_subparsers(
            title="commands",
            metavar="COMMAND",
        )

        for add_subparser in [
            new.add_subparser,
            sync.add_subparser,
            config_jsonschema.add_subparser,
        ]:
            add_subparser(
                subparser,
                formatter_class=parser.formatter_class,
            )

        parser.set_defaults(handler=lambda _: parser.print_help())

        space = parser.parse_args(args)

        if hasattr(space, "handler"):
            space.handler(space)

        else:
            parser.print_help()

    except KeyboardInterrupt:
        print()
        logger.info("Cancelled by user 👋")

        sys.exit(1)

    except Exception as e:
        if verbose:
            logger.exception(e)

        else:
            logger.error(e)

        raise e
