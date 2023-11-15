from loglib.base.emitter import LogEmitterBase


class CarrierLokiLogEmitter(LogEmitterBase):
    """Emit logs to Loki"""

    def emit_line(self, unix_epoch_in_nanoseconds, log_line, additional_labels=None):
        """Emit log line"""
        labels = self.default_labels
        if additional_labels is not None:
            labels.update(additional_labels)
        #
        data = {
            "streams": [
                {
                    "stream": labels,
                    "values": [
                        [f"{unix_epoch_in_nanoseconds}", log_line],
                    ],
                }
            ]
        }
        #
        self.post_data(data)

    def emit_batch(self, batch_data, additional_labels=None):
        """Emit log line"""
        labels = self.default_labels
        if additional_labels is not None:
            labels.update(additional_labels)
        #
        data = {
            "streams": [
                {
                    "stream": labels,
                    "values": batch_data,
                }
            ]
        }
        #
        self.post_data(data)
        #
        # TODO: batches with different stream labels (a.k.a. multiple streams support)
