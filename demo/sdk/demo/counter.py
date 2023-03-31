from demo import api
from typing import Iterable

class Counter(api.Counter):
    count: int = 0

    def increment(self) -> None:
        return None

    def decrement(self) -> None:
        return None