import logging
import logging.handlers
import time
import traceback


from loglib.base.emitter import LogEmitterBase
from loglib.base.thread import PeriodicFlush


class LogHandlerBase(logging.Handler):
    def handleError(self, record):
        """Handle error while logging"""
        super().handleError(record)
        self.emitter.disconnect()

    def emit(self, record):
        try:
            record_ts = int(record.created * 1000000000)
            record_data = self.format(record)
            #
            additional_labels = dict()
            if self.settings.get("include_level_name", True):
                additional_labels["level"] = record.levelname
            if self.settings.get("include_logger_name", True):
                additional_labels["logger"] = record.name
            #
            additional_labels["my_field"] = "custom"
            self.emitter.emit_line(record_ts, record_data, additional_labels)
        except:  # pylint: disable=W0702
            # In this case we should NOT use logging to log logging error. Only print()
            print("[FATAL] Exception during sending logs")
            traceback.print_exc()


class LogBufferingHandlerBase(logging.handlers.BufferingHandler):
    def __init__(self, emitter: LogEmitterBase, capacity):
        super().__init__(capacity)
        self.emitter = emitter
        self.last_flush = 0.0
        PeriodicFlush(self, self.settings.get("buffer_flush_deadline", 30)).start()

    def handleError(self, record):
        """Handle error while logging"""
        super().handleError(record)
        self.emitter.disconnect()

    def shouldFlush(self):
        """Check if we need to flush messages"""
        return (len(self.buffer) >= self.capacity) or (
            time.time() - self.last_flush
        ) >= self.settings.get("buffer_flush_interval", 10)
