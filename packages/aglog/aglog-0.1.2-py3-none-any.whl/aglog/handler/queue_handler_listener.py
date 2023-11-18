import logging
from logging.config import ConvertingList
from logging.handlers import QueueHandler, QueueListener
from queue import Queue

from typing_extensions import Self


class QueueHandlerListener(QueueHandler):
    def __init__(  # noqa: PLR0913
        self: Self,
        handlers: list[logging.Handler] | ConvertingList,
        *,
        auto_run: bool = True,
        max_queue_size: int = -1,
        stop_timeout: float = 60,
        respect_handler_level: bool = False,
    ) -> None:
        self.stop_timeout = stop_timeout
        self.queue = Queue(maxsize=max_queue_size)
        handlers = [handlers[i] for i in range(len(handlers))]
        super().__init__(self.queue)
        self.listener = QueueListener(self.queue, *handlers, respect_handler_level=respect_handler_level)

        if auto_run:
            self.start()

    def start(self: Self) -> None:
        self.listener.start()

    def stop(self: Self) -> None:
        self.listener.enqueue_sentinel()
        thread = self.listener._thread  # noqa: SLF001
        if thread is not None:
            thread.join(timeout=self.stop_timeout)
            self.listener._thread = None  # noqa: SLF001
