from tb.adv.api import api
from typing import Iterable

class NestedStruct2Interface(api.INestedStruct2Interface):
    def __init__(self):
        self.__prop1: api.NestedStruct1 = {}
        self.__prop2: api.NestedStruct2 = {}

    @property
    def prop1(self):
        return self.__prop1

    @property
    def prop2(self):
        return self.__prop2