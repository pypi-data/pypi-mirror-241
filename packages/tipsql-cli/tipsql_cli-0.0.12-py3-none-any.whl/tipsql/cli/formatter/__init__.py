from pathlib import Path
from typing import assert_never

from tipsql.cli.config import Config

from .ruff_formatter import RuffFormatter

Formatter = RuffFormatter


def format_targets(target_paths: list[Path], config: Config):
    match config.root.formatter.formatter:
        case "ruff":
            RuffFormatter().format(
                target_paths,
                *config.root.formatter.tool_args,
            )

        case _:
            assert_never(config.root.formatter.formatter)
