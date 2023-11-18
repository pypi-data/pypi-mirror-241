from __future__ import annotations

import logging
import logging.config
import os
import re
from pathlib import Path
from typing import Any

_env_pattern = re.compile(r"\$\{(.*)\}")

logger = logging.getLogger(__name__)


def load_yaml(file_path: str | Path) -> dict[str, Any]:
    import yaml

    file_path = Path(file_path)

    if not file_path.exists():
        msg = "Logging config file not found: %s"
        raise FileNotFoundError(msg, file_path)

    def env_var_constructor(loader, node):  # noqa: ANN001 ANN202
        value = loader.construct_scalar(node)
        m = _env_pattern.match(value)
        if not m:
            return value  # pragma: no cover
        key, default = m.group(1).split(":-") if len(m.group(1).split(":-")) > 1 else (m.group(1), None)
        return os.environ.get(key, default)

    yaml.add_implicit_resolver("!env_var", _env_pattern, None, yaml.SafeLoader)
    yaml.add_constructor("!env_var", env_var_constructor, yaml.SafeLoader)

    with file_path.open() as f:
        logging_config = f.read()

    return yaml.load(logging_config, Loader=yaml.SafeLoader)


def dict_config_from_yaml(file_path: str | Path) -> None:
    conf = load_yaml(file_path)
    logging.config.dictConfig(conf)
    logger.debug("Logging configured")
