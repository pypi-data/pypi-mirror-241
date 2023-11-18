import logging

import aglog.handler.queue_handler_listener as target


class DummyHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.call_count = 0

    def emit(self: "DummyHandler", record: logging.LogRecord) -> None:
        self.call_count += 1


def test_queue_handler_listener():
    logger = logging.getLogger("test")
    dummy_handler = DummyHandler()
    lister = target.QueueHandlerListener(handlers=[dummy_handler], stop_timeout=0.1)
    lister.start()

    logger.addHandler(lister)
    logger.error("test")
    logger.error("test")
    lister.stop()

    assert dummy_handler.call_count == 2
