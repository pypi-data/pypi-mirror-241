import threading
import time


class PeriodicFlush(threading.Thread):  # pylint: disable=R0903
    """Flush logger time to time"""

    def __init__(self, handler, interval=30):
        super().__init__(daemon=True)
        self.handler = handler
        self.interval = interval

    def run(self):
        """Run handler thread"""
        while True:
            time.sleep(self.interval)
            self.handler.flush()
