from tb.same.api import api
from typing import Iterable

class SameEnum2Interface(api.ISameEnum2Interface):
    def __init__(self):
        self.__prop1: api.Enum1 = Enum1.value1
        self.__prop2: api.Enum2 = Enum2.value1

    @property
    def prop1(self):
        return self.__prop1

    @property
    def prop2(self):
        return self.__prop2