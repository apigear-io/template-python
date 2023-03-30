from tb.conflict.api import api
from typing import Iterable

class Conflict2(api.IConflict2):
    def __init__(self):
        self.__sameName: int = 0

    @property
    def sameName(self):
        return self.__sameName