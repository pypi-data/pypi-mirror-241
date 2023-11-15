from enum import StrEnum
from typing import List, Optional

from datadog import initialize, statsd  # type: ignore


class FreeplayMetric(StrEnum):
    pass


class DatadogClient:
    def __init__(self, host: str = '127.0.0.1', port: int = 8125) -> None:
        self.host = host
        self.port = port
        self.initialize_client()

    def initialize_client(self) -> None:
        options = {
            'statsd_host': self.host,
            'statsd_port': self.port
        }
        initialize(**options)  # type: ignore

    def increment(self, metric: FreeplayMetric, tags: Optional[List[str]] = None) -> None:
        statsd.increment(metric.value, tags=tags)

    def decrement(self, metric: FreeplayMetric, tags: Optional[List[str]] = None) -> None:
        statsd.decrement(metric.value, tags=tags)

    def timing(self, metric: FreeplayMetric, value: float, tags: Optional[List[str]] = None) -> None:
        statsd.timing(metric.value, value, tags=tags)
