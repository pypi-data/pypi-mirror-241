import logging

import aglog.filter.word_filter as target


def make_record(msg: str = "") -> logging.LogRecord:
    return logging.LogRecord(
        name="test",
        level=logging.INFO,
        pathname="test.py",
        lineno=1,
        msg=msg,
        args=(),
        exc_info=None,
        func="test",
        sinfo=None,
    )


def test_message_word_filter():
    filter = target.MessageWordFilter(includes=["foo", "bar"], excludes=["baz"])
    assert filter.filter(make_record("foo")) is True
    assert filter.filter(make_record("bar")) is True
    assert filter.filter(make_record("baz")) is False
    assert filter.filter(make_record("foobar")) is True
    assert filter.filter(make_record("bazbaz")) is False
    assert filter.filter(make_record("foobarbaz")) is False

    filter = target.MessageWordFilter(includes=["foo", "bar"], excludes=["baz"], include_type="all")
    assert filter.filter(make_record("foo")) is False
    assert filter.filter(make_record("bar")) is False
    assert filter.filter(make_record("baz")) is False
    assert filter.filter(make_record("foobar")) is True
    assert filter.filter(make_record("bazbaz")) is False
    assert filter.filter(make_record("foobarbaz")) is False

    filter = target.MessageWordFilter(includes=["foo", "bar"], excludes=[])
    assert filter.filter(make_record("foo")) is True
    assert filter.filter(make_record("bar")) is True
    assert filter.filter(make_record("baz")) is False
    assert filter.filter(make_record("foobar")) is True
    assert filter.filter(make_record("bazbaz")) is False
    assert filter.filter(make_record("foobarbaz")) is True

    filter = target.MessageWordFilter(excludes=["baz"])
    assert filter.filter(make_record("foo")) is True
    assert filter.filter(make_record("bar")) is True
    assert filter.filter(make_record("baz")) is False
    assert filter.filter(make_record("foobar")) is True
    assert filter.filter(make_record("bazbaz")) is False
    assert filter.filter(make_record("foobarbaz")) is False

    filter = target.MessageWordFilter()
    assert filter.filter(make_record("foo")) is True
    assert filter.filter(make_record("bar")) is True
    assert filter.filter(make_record("baz")) is True
    assert filter.filter(make_record("foobar")) is True
    assert filter.filter(make_record("bazbaz")) is True
    assert filter.filter(make_record("foobarbaz")) is True


def test_thread_name_filter():
    filter = target.ThreadNameFilter(includes=["MainThread"])
    assert filter.filter(make_record("foo")) is True

    filter = target.ThreadNameFilter(includes=["DummyThread"])
    assert filter.filter(make_record("foo")) is False


def test_process_name_filter():
    filter = target.ProcessNameFilter(includes=["MainProcess"])
    assert filter.filter(make_record("foo")) is True

    filter = target.ProcessNameFilter(includes=["DummyProcess"])
    assert filter.filter(make_record("foo")) is False
