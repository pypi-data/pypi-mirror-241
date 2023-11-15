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
        self.__init__(emitter, capacity)
