from abc import ABC, abstractmethod
import requests  # pylint: disable=E0401
import gzip
import json
import time


class LogEmitterBase(ABC):
    def __init__(
        self,
        url,
        user=None,
        password=None,
        token=None,
        default_labels=None,
        verify=True,
        retries=3,
        retry_delay=0.5,
        timeout=15,
    ):
        self.push_url = url
        self.user = user
        self.password = password
        self.token = token
        #
        self.default_labels = default_labels if default_labels is not None else dict()
        #
        self.verify = verify
        self.retries = retries
        self.retry_delay = retry_delay
        self.timeout = timeout
        #
        self._connection = None

    def connect(self):
        """Get connection object"""
        if self._connection is not None:
            return self._connection
        #
        self._connection = requests.Session()
        #
        if self.user is not None and self.password is not None:
            self._connection.auth = (self.user, self.password)
        if self.token is not None:
            self._connection.headers.update(
                {
                    "Authorization": f"Bearer {self.token}",
                }
            )
        #
        self._connection.headers.update(
            {
                "Content-Type": "application/json",
            }
        )
        #
        print(f"{self._connection.headers}")
        return self._connection

    def disconnect(self):
        """Destroy connection object"""
        if self._connection is not None:
            try:
                self._connection.close()
            except:  # pylint: disable=W0702
                pass
            self._connection = None

    def post_data(self, data):
        """Do a POST to Loki"""
        for _ in range(self.retries):
            try:
                connection = self.connect()
                payload = json.dumps(data).encode("utf-8")
                response = connection.post(
                    self.push_url,
                    data=payload,
                    verify=self.verify,
                    timeout=self.timeout,
                )
                response.raise_for_status()
                return response
            except Exception as e:  # pylint: disable=W0702
                self.disconnect()
                time.sleep(self.retry_delay)

    @abstractmethod
    def emit_line(self, timestamp, line, labels):
        pass

    @abstractmethod
    def emit_batch(self, batch_data, additional_labels=None):
        pass
