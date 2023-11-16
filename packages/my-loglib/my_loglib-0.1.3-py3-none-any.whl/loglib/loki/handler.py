import time
import traceback
from loglib.base.handler import LogHandlerBase, LogBufferingHandlerBase
from loglib.loki.emitter import CarrierLokiLogEmitter


class CarrierLokiLogHandler(LogHandlerBase):
    """Log handler - send logs to storage"""

    def __init__(self, settings):
        super().__init__()
        self.settings = settings
        #
        default_loki_labels = self.settings.get("labels", dict())
        #
        self.emitter = CarrierLokiLogEmitter(
            url=self.settings.get("url"),
            user=self.settings.get("user", None),
            password=self.settings.get("password", None),
            token=self.settings.get("token", None),
            default_labels=default_loki_labels,
            verify=self.settings.get("verify", True),
        )


class CarrierLokiBufferedLogHandler(LogBufferingHandlerBase):
    """Log handler - buffer and send logs to storage"""

    def __init__(self, settings):
        capacity = settings.get("buffer_capacity", 100)
        self.settings = settings
        #
        default_loki_labels = self.settings.get("labels", dict())
        #
        emitter = CarrierLokiLogEmitter(
            url=self.settings.get("url"),
            user=self.settings.get("user", None),
            password=self.settings.get("password", None),
            token=self.settings.get("token", None),
            default_labels=default_loki_labels,
            verify=self.settings.get("verify", True),
        )
        #
        super().__init__(emitter, capacity)

    def flush(self):
        self.acquire()
        log_records = list()
        #
        try:
            while self.buffer:
                record = self.buffer.pop(0)
                record_ts = int(record.created * 1000000000)
                record_data = self.format(record)
                # TODO: batches with different stream labels (a.k.a. multiple streams support)
                log_records.append([f"{record_ts}", record_data])
        except:  # pylint: disable=W0702
            # In this case we should NOT use logging to log logging error. Only print()
            print("[FATAL] Exception during formatting logs")
            traceback.print_exc()
        finally:
            self.last_flush = time.time()
            self.release()
        #
        try:
            if log_records:
                self.emitter.emit_batch(log_records)
        except:  # pylint: disable=W0702
            # In this case we should NOT use logging to log logging error. Only print()
            print("[FATAL] Exception during sending logs to storage")
            traceback.print_exc()
