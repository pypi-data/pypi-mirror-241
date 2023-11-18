from argparse import ArgumentParser, FileType, Namespace, _SubParsersAction
from logging import getLogger

logger = getLogger(__name__)


def add_subparser(subparsers: _SubParsersAction, **kwargs) -> None:
    description = "generate config JSON Schema"

    parser: ArgumentParser = subparsers.add_parser(
        "config-jsonschema",
        description=description,
        help=description,
        **kwargs,
    )

    parser.add_argument(
        "--output",
        type=FileType("w"),
        required=False,
        default=None,
        help="output filepath. default is stdout.",
    )

    parser.set_defaults(handler=generate_config_schema_command)


def generate_config_schema_command(space: Namespace) -> None:
    import json

    from tipsql.cli.config import Config

    print(
        json.dumps(
            Config.model_json_schema(),
            indent=4,
            ensure_ascii=False,
        ),
        file=space.output,
    )
