from tb.same.api import api
from typing import Iterable

class SameStruct2Interface(api.ISameStruct2Interface):
    def __init__(self):
        self.__prop1: api.Struct2 = {}
        self.__prop2: api.Struct2 = {}

    @property
    def prop1(self):
        return self.__prop1

    @property
    def prop2(self):
        return self.__prop2