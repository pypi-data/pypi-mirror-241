from typing import Literal

from tipsql.cli.config.model import ExtraForbidModel
from tipsql.cli.plugins import DatabaseConfig


class ConfigV1(ExtraForbidModel):
    version: Literal[1]
    database: DatabaseConfig
