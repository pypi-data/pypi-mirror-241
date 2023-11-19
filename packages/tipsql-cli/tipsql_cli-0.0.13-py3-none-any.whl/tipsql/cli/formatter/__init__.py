from pathlib import Path
from typing import assert_never

from tipsql.cli.config.v1.formatter import ConfigV1Formatter

from .ruff_formatter import RuffFormatter

Formatter = RuffFormatter


def format_targets(target_paths: list[Path], config: ConfigV1Formatter):
    match config.formatter:
        case "ruff":
            RuffFormatter().format(
                target_paths,
                *config.tool_args,
            )

        case _:
            assert_never(config.formatter)
