import os
from collections.abc import Generator
from contextlib import contextmanager


@contextmanager
def temporary_env_var(key: str, value: str) -> Generator:
    original_value = os.environ.get(key)
    os.environ[key] = value
    try:
        yield
    finally:
        if original_value is None:
            del os.environ[key]
        else:
            os.environ[key] = original_value
