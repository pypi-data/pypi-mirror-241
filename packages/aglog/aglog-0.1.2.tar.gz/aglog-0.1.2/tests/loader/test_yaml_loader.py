import logging
from pathlib import Path

import pytest
from utils import temporary_env_var

import aglog.loader.yaml_loader as target

test_config = """
version: 1
disable_existing_loggers: False
formatters:
  simple:
    format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
handlers:
  console:
    class: logging.StreamHandler
    formatter: simple
    stream: ext://sys.stdout
root:
  level: ${LOG_LEVEL:-WARNING}
  handlers: [console]
"""

no_env_var_config = """
version: 1
"""


def test_load_yaml(tmp_path: Path) -> None:
    yaml_path = tmp_path / "test.yaml"

    with yaml_path.open("w") as f:
        f.write(test_config)

    with temporary_env_var("LOG_LEVEL", "DEBUG"):
        res = target.load_yaml(yaml_path)
    assert res["root"]["level"] == "DEBUG"

    res = target.load_yaml(yaml_path)
    assert res["root"]["level"] == "WARNING"

    # config file not found
    with pytest.raises(FileNotFoundError):
        target.load_yaml(tmp_path / "not_found.yaml")

    # no env var
    no_env_yaml_path = tmp_path / "no_env_var.yaml"
    with no_env_yaml_path.open("w") as f:
        f.write(no_env_var_config)
    res = target.load_yaml(no_env_yaml_path)
    assert res == {"version": 1}


def test_dict_config_from_yaml(tmp_path: Path) -> None:
    yaml_path = tmp_path / "test.yaml"

    with yaml_path.open("w") as f:
        f.write(test_config)

    with temporary_env_var("LOG_LEVEL", "DEBUG"):
        target.dict_config_from_yaml(yaml_path)
    assert logging.getLogger().level == logging.DEBUG

    target.dict_config_from_yaml(yaml_path)
    assert logging.getLogger().level == logging.WARNING
