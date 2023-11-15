import logging
from loglib.loki.handler import CarrierLokiBufferedLogHandler, CarrierLokiLogHandler


def enable_loki_logging(context):
    """Enable logging to Loki"""
    if "logging" not in context.settings and "loki" not in context.settings["logging"]:
        return
    #
    settings = context.settings.get("logging").get("loki")
    if settings.get("buffering", True):
        LokiLogHandler = CarrierLokiBufferedLogHandler
    else:
        LokiLogHandler = CarrierLokiLogHandler
    #
    if settings.get("include_node_name", True):
        settings.get("labels", {})["node"] = context.node_name

    handler = LokiLogHandler(settings)
    handler.setFormatter(logging.getLogger("").handlers[0].formatter)
    logging.getLogger("").addHandler(handler)
