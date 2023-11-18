from pathlib import Path

from pydantic import RootModel

from .v1.config import ConfigV1


class Config(RootModel):
    root: ConfigV1


def load(config_filepath: str | Path | None) -> Config:
    import yaml
    from tipsql.cli.exception import TipsqlFileNotFoundError
    from tipsql.cli.utils.path import DEFAULT_CONFIG_FILE

    if config_filepath is None:
        config_filepath = DEFAULT_CONFIG_FILE

    elif isinstance(config_filepath, str):
        config_filepath = Path(config_filepath)

    if not config_filepath.exists():
        raise TipsqlFileNotFoundError(config_filepath)

    with open(config_filepath, "r") as file:
        config = Config(**yaml.full_load(file))

    return config
