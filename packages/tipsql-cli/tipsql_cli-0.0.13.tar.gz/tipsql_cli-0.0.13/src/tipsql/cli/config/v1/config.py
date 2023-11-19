from typing import Annotated, Literal

from pydantic import Field
from tipsql.cli.config.model import ExtraForbidModel
from tipsql.cli.plugins import DatabaseConfig

from .formatter import ConfigV1Formatter, RuffFormatter


class ConfigV1(ExtraForbidModel):
    version: Annotated[
        Literal[1],
        Field(
            title="tipsql CLI config version",
        ),
    ]

    database: Annotated[
        DatabaseConfig,
        Field(
            title="tipsql CLI database config",
        ),
    ]

    formatter: Annotated[
        ConfigV1Formatter | None,
        Field(
            title="generated code formatter",
        ),
    ] = RuffFormatter(formatter="ruff")
