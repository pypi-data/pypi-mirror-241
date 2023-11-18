"""In order to prevent third party logs from being output before
setting the LogLevel for logging, the less dependent paths are separated in this file.
"""

from pathlib import Path

DEFAULT_CONFIG_FILE = Path("tipsql.yml")
