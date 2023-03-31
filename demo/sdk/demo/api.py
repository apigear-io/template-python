from pydantic import BaseModel
from enum import IntEnum



class Counter(BaseModel):
    count: int

    def increment(self):
        raise NotImplementedError

    def decrement(self):
        raise NotImplementedError
