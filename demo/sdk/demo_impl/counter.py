from demo_api import api
from typing import Iterable


class Counter(api.ICounter):
    def __init__(self, notifier=None):
        super().__init__()
        self._notifier = notifier
        self._value: int = 0

    def set_value(self, value):
        if self._value == value:
            return
        self._value = value

    def get_value(self):
        return self._value

    def push_value(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("demo.Counter/value", value)

    def increment(self) -> None:
        self._value += 1
        self.push_value(self._value)

    def decrement(self) -> None:
        self._value -= 1
        self.push_value(self._value)
