from tb.same.api import api
from typing import Iterable

class SameStruct1Interface(api.ISameStruct1Interface):
    def __init__(self):
        self.__prop1: api.Struct1 = {}

    @property
    def prop1(self):
        return self.__prop1