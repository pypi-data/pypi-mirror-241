from typing import Any
from pathlib import Path
import sys


if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib


def get_config() -> dict[str, Any]:
    cur_dir = Path(".")

    config = get_pyproject_config(cur_dir)

    return config


def get_pyproject_config(directory: Path) -> dict[str, Any]:
    pyproject_toml: dict[str, Any] = {}
    with Path(directory / "pyproject.toml").open("rb") as f:
        try:
            pyproject_toml = tomllib.load(f)
        except NameError:
            pyproject_toml = tomllib.loads(f.read().decode("UTF-8"))

    config: dict[str, Any] = pyproject_toml.get("tool", {}).get("pyallel", {})

    return config
