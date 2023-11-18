import logging

import freezegun
from utils import temporary_env_var

import aglog.formatter.json_formatter as target


@freezegun.freeze_time("1970-01-01 00:00:00")
@temporary_env_var("TZ", "UTC")
def test_json_formatter():
    formatter = target.JsonFormatter()

    record = logging.LogRecord(
        name="test",
        level=logging.INFO,
        pathname="test.py",
        lineno=1,
        msg="test",
        args=(),
        exc_info=None,
        func="test_func",
    )

    assert formatter.format(record) == '{"asctime": "1970-01-01 00:00:00,000", "levelname": "INFO", "message": "test"}'
    formatter = target.JsonFormatter(keys=[target.RecordKey.CREATED])
    assert formatter.format(record) == '{"created": 0.0}'
    formatter = target.JsonFormatter(keys=[target.RecordKey.PATH])
    assert formatter.format(record) == '{"path": "test.py:1"}'
    formatter = target.JsonFormatter(keys=[target.RecordKey.PATH_NAME])
    assert formatter.format(record) == '{"pathname": "test.py"}'
    formatter = target.JsonFormatter(keys=[target.RecordKey.FILE_NAME])
    assert formatter.format(record) == '{"filename": "test.py"}'
    formatter = target.JsonFormatter(keys=[target.RecordKey.LINE_NO])
    assert formatter.format(record) == '{"lineno": 1}'
    formatter = target.JsonFormatter(keys=[target.RecordKey.FUNC_NAME])
    assert formatter.format(record) == '{"funcName": "test_func"}'
    formatter = target.JsonFormatter(keys=[target.RecordKey.THREAD_NAME])
    assert formatter.format(record) == '{"threadName": "MainThread"}'
    formatter = target.JsonFormatter(keys=[target.RecordKey.THREAD])
    assert '"thread":' in formatter.format(record)
    formatter = target.JsonFormatter(keys=[target.RecordKey.PROCESS_NAME])
    assert formatter.format(record) == '{"processName": "MainProcess"}'
    formatter = target.JsonFormatter(keys=[target.RecordKey.PROCESS])
    assert '"process"' in formatter.format(record)
    formatter = target.JsonFormatter(keys=[target.RecordKey.MODULE])
    assert formatter.format(record) == '{"module": "test"}'
    formatter = target.JsonFormatter(keys=[target.RecordKey.NAME])
    assert formatter.format(record) == '{"name": "test"}'
    formatter = target.JsonFormatter(keys=[target.RecordKey.MSG])
    assert formatter.format(record) == '{"msg": "test"}'
    formatter = target.JsonFormatter(keys=[target.RecordKey.MESSAGE])
    assert formatter.format(record) == '{"message": "test"}'
    formatter = target.JsonFormatter(keys=[target.RecordKey.TIME])
    assert formatter.format(record) == '{"asctime": "1970-01-01 00:00:00,000"}'

    keys = [k.value for k in target.RecordKey]
    formatter = target.JsonFormatter(keys=keys)
    for key in keys:
        assert key in formatter.format(record)

    # extra
    record.__dict__["extra_key"] = "extra_value"
    formatter = target.JsonFormatter(keys=["extra_key"])
    assert formatter.format(record) == '{"extra_key": "extra_value"}'

    # exc_info
    record.exc_info = (ValueError, ValueError("test"), None)
    formatter = target.JsonFormatter(keys=[target.RecordKey.EXC_INFO])
    assert formatter.format(record) == '{"exc_info": ["ValueError: test"]}'

    # stack_info
    record.stack_info = "test"
    formatter = target.JsonFormatter(keys=[target.RecordKey.STACK_INFO])
    assert formatter.format(record) == '{"stack_info": ["test"]}'
