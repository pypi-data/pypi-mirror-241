from __future__ import annotations

import logging
from abc import abstractmethod
from typing import Literal

from typing_extensions import Self, override


class WordFilter(logging.Filter):
    def __init__(
        self: Self,
        *,
        includes: list[str] | None = None,
        excludes: list[str] | None = None,
        include_type: Literal["any", "all"] = "any",
    ) -> None:
        self.includes = includes or []
        self.excludes = excludes or []
        self.include_type = include_type

    @abstractmethod
    def get_target(self: Self, record: logging.LogRecord) -> str | None:
        raise NotImplementedError  # pragma: no cover

    def filter(self: Self, record: logging.LogRecord) -> bool:
        target = self.get_target(record)
        if target is None:
            return True  # pragma: no cover

        check_select = any(w in target for w in self.includes) if self.include_type == "any" else all(w in target for w in self.includes)
        check_ignore = any(w in target for w in self.excludes)
        if self.includes != [] and self.excludes != []:
            return check_select and not check_ignore
        if self.includes == [] and self.excludes != []:
            return not check_ignore
        if self.includes != [] and self.excludes == []:
            return check_select
        return True


class MessageWordFilter(WordFilter):
    @override
    def get_target(self: Self, record: logging.LogRecord) -> str | None:
        return record.getMessage()


class ThreadNameFilter(WordFilter):
    @override
    def get_target(self: Self, record: logging.LogRecord) -> str | None:
        return record.threadName


class ProcessNameFilter(WordFilter):
    @override
    def get_target(self: Self, record: logging.LogRecord) -> str | None:
        return record.processName


class NameFilter(WordFilter):
    @override
    def get_target(self: Self, record: logging.LogRecord) -> str | None:
        return record.name
