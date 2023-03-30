from tb.again.api import api
from typing import Iterable

class SameEnum1Interface(api.ISameEnum1Interface):
    def __init__(self):
        self.__prop1: api.Enum1 = Enum1.value1

    @property
    def prop1(self):
        return self.__prop1