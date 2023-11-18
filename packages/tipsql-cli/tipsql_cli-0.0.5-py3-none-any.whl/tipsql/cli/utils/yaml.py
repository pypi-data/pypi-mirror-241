from pathlib import PosixPath, WindowsPath
from typing import OrderedDict

import yaml
from pydantic_core import Url
from tipsql.cli.config.model import Model
from yaml.nodes import ScalarNode as ScalarNode


class YamlDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow=flow, indentless=indentless)


def dump(data: Model) -> str:
    yaml.add_representer(
        str, lambda dumper, data: dumper.represent_scalar("tag:yaml.org,2002:str", data)
    )

    yaml.add_representer(
        OrderedDict,
        lambda dumper, data: dumper.represent_mapping(
            "tag:yaml.org,2002:map", data.items()
        ),
    )

    yaml.add_representer(
        PosixPath,
        lambda dumper, data: dumper.represent_str(str(data)),
    )

    yaml.add_representer(
        WindowsPath,
        lambda dumper, data: dumper.represent_str(str(data)),
    )

    yaml.add_representer(
        Url,
        lambda dumper, data: dumper.represent_str(str(data)),
    )

    return yaml.dump(
        data.model_dump(
            exclude_none=True,
            exclude_unset=True,
        ),
        sort_keys=False,
        allow_unicode=True,
        Dumper=YamlDumper,
    )
