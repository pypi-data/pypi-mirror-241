from pathlib import Path
from typing import Literal

from tipsql.cli.config.model import ExtraForbidModel


class RuffFormatter(ExtraForbidModel):
    formatter: Literal["ruff"]
    options: dict[str, str | int | bool | None] | None = None
    config_path: Path | None = None

    @property
    def tool_args(self) -> list[str]:
        args = []
        if self.options is not None:
            for key, value in self.options.items():
                if value is not None:
                    args.append(f"{key}={repr(value)}")
                else:
                    args.append(key)

        if self.config_path is not None and "--config" not in (self.options or {}):
            args.append(f"--config={self.config_path}")

        return args
