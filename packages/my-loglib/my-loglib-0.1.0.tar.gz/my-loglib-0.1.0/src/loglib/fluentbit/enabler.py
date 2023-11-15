#!/usr/bin/python3
# coding=utf-8

#   Copyright 2023 getcarrier.io
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""
    Logging tool: Fluentbit support
"""
import socket
import logging
import logging.handlers
from fluent import handler as fluent_handler


def enable_fluentbit_logging_with_syslog(context):
    """Enable logging to SysLog"""
    if "fluentbit" not in context.settings.get("logging", {}):
        return
    #
    settings = context.settings.get("logging").get("fluentbit")
    #
    address = (settings.get("address", "localhost"), settings.get("port", 514))
    facility = settings.get("facility", "user")
    socktype = (
        socket.SOCK_DGRAM
        if settings.get("socktype", "udp").lower() == "udp"
        else socket.SOCK_STREAM
    )
    #
    service = settings.get("service", "")
    #
    handler = logging.handlers.SysLogHandler(
        address=address,
        facility=facility,
        socktype=socktype,
    )
    #
    formatter = logging.Formatter(
        fmt=f"%(asctime)s - %(levelname)s - {service} - %(name)s - %(message)s",
        datefmt="%Y.%m.%d %H:%M:%S UTC",
    )
    handler.setFormatter(formatter)
    logging.getLogger("").addHandler(handler)


def enable_fluentbit_logging(context):
    settings = context.settings.get("logging").get("fluentbit")
    host = settings.get("address", "localhost")
    port = settings.get("port", 24224)
    service = settings.get("service", "")
    tag = settings.get("tag", service)
    labels = settings.get("labels", {})

    format = {
        "host": "%(hostname)s",
        "time": "%(asctime)s",
        "level": "%(levelname)s",
        "service": service,
        "path_file": "%(name)s",
        "stack_trace": "%(exc_text)s",
        "msg": "%(message)s",
    }

    for key, value in labels.items():
        if not key in format:
            format[key] = value

    handler = fluent_handler.FluentHandler(tag, host=host, port=port)
    formatter = fluent_handler.FluentRecordFormatter(format)
    handler.setFormatter(formatter)
    logging.getLogger("").addHandler(handler)
