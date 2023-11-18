from __future__ import annotations

import asyncio
import json
import logging
from enum import Enum
from typing import ClassVar

from pygments import formatters, highlight, lexers
from typing_extensions import Self, override


class RecordKey(str, Enum):
    TIME = "asctime"
    LEVEL_NAME = "levelname"
    LEVEL_NO = "levelno"
    MSG = "msg"
    MESSAGE = "message"
    NAME = "name"
    PATH = "path"
    PATH_NAME = "pathname"
    FILE_NAME = "filename"
    LINE_NO = "lineno"
    FUNC_NAME = "funcName"
    THREAD_NAME = "threadName"
    PROCESS_NAME = "processName"
    TASK_NAME = "taskName"
    PROCESS = "process"
    THREAD = "thread"
    MODULE = "module"
    CREATED = "created"
    EXC_INFO = "exc_info"
    STACK_INFO = "stack_info"


record_key_items = [k.value for k in RecordKey]
ExtraKey = str


class JsonFormatter(logging.Formatter):
    DEFAULT_KEYS: ClassVar[list[RecordKey]] = [RecordKey.TIME, RecordKey.LEVEL_NAME, RecordKey.MESSAGE]

    def __init__(
        self: Self,
        *,
        keys: list[RecordKey | ExtraKey] | None = None,
        indent: int | None = None,
        datefmt: str | None = None,
        colorize: bool = False,
    ) -> None:
        super().__init__(datefmt=datefmt)
        self.keys = keys or self.DEFAULT_KEYS
        self.indent = indent
        self.colorize = colorize
        self.is_notebook = is_notebook()

    @override
    def format(self: Self, record: logging.LogRecord) -> str:
        dict_record: dict[RecordKey, str | int | float | bool | list[str] | None] = {
            RecordKey.TIME: self.formatTime(record, self.datefmt),
            RecordKey.LEVEL_NAME: record.levelname,
            RecordKey.LEVEL_NO: record.levelno,
            RecordKey.MSG: record.msg,
            RecordKey.MESSAGE: record.getMessage(),
            RecordKey.NAME: record.name,
            RecordKey.PATH: self.create_path(record),
            RecordKey.MODULE: record.module,
            RecordKey.PATH_NAME: record.pathname,
            RecordKey.FILE_NAME: record.filename,
            RecordKey.LINE_NO: record.lineno,
            RecordKey.FUNC_NAME: record.funcName,
            RecordKey.THREAD_NAME: record.threadName,
            RecordKey.THREAD: record.thread,
            RecordKey.PROCESS_NAME: record.processName,
            RecordKey.TASK_NAME: self.get_task_name(),
            RecordKey.PROCESS: record.process,
            RecordKey.CREATED: record.created,
            RecordKey.EXC_INFO: None,
            RecordKey.STACK_INFO: None,
        }

        if record.exc_info:
            dict_record[RecordKey.EXC_INFO] = self.formatException(record.exc_info).split("\n")

        if record.stack_info:
            dict_record[RecordKey.STACK_INFO] = self.formatStack(record.stack_info).split("\n")

        filtered_dict_record = self.filter_keys(dict_record=dict_record, record=record)
        json_record = json.dumps(filtered_dict_record, ensure_ascii=False, indent=self.indent)

        if self.colorize:
            return self.colorize_json(json_record)

        return json_record

    def create_path(self: Self, record: logging.LogRecord) -> str:
        path = f"{record.pathname}:{record.lineno}"
        if self.is_notebook:
            path = f" {path}"
        return path

    def get_task_name(self: Self) -> str | None:
        try:
            task = asyncio.current_task()
            if task is None:
                return None
        except RuntimeError:
            return None
        return task.get_name()

    def filter_keys(
        self: Self,
        dict_record: dict[RecordKey, str | int | float | bool | list[str] | None],
        record: logging.LogRecord,
    ) -> dict[str, str | int | float | bool | list[str] | None]:
        filtered_dict_record = {}
        for key in self.keys:
            if isinstance(key, RecordKey):
                filtered_dict_record[key.value] = dict_record[key]
                continue
            if key in record_key_items:
                filtered_dict_record[key] = dict_record[RecordKey(key)]
                continue
            # key is ExtraKey
            filtered_dict_record[key] = record.__dict__.get(key, None)
        return filtered_dict_record

    def colorize_json(self: Self, json_record: str) -> str:
        return highlight(
            json_record,
            lexers.JsonLexer(),
            formatters.TerminalFormatter(),
        ).strip("\n")


class JsonColorFormatter(JsonFormatter):
    def __init__(
        self: Self,
        *,
        keys: list[RecordKey | ExtraKey] | None = None,
        indent: int | None = None,
        datefmt: str | None = None,
    ) -> None:
        super().__init__(keys=keys, indent=indent, datefmt=datefmt, colorize=True)


def is_notebook() -> bool:
    try:
        from IPython import get_ipython

        return bool(get_ipython())
    except NameError:
        return False
