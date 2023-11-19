from typing import Literal

from tipsql.cli.config.model import ExtraForbidModel
from tipsql.cli.plugins import DatabaseConfig

from .formatter import ConfigV1Formatter, RuffFormatter


class ConfigV1(ExtraForbidModel):
    version: Literal[1]
    database: DatabaseConfig
    formatter: ConfigV1Formatter = RuffFormatter(formatter="ruff")
