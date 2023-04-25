from pydantic import BaseModel
from enum import IntEnum



class ICounter:
    def get_value(self):
        raise NotImplementedError

    def set_value(self, value):
        raise NotImplementedError
    def increment(self):
        raise NotImplementedError
    def decrement(self):
        raise NotImplementedError
