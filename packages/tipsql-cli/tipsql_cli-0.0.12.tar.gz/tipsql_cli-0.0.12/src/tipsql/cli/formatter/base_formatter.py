from abc import ABC, abstractmethod
from pathlib import Path


class BaseFormatter(ABC):
    @abstractmethod
    def format(self, target_path: Path, *tool_args: str) -> str:
        ...
