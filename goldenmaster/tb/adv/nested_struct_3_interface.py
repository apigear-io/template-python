from tb.adv.api import api
from typing import Iterable

class NestedStruct3Interface(api.INestedStruct3Interface):
    def __init__(self):
        self.__prop1: api.NestedStruct1 = {}
        self.__prop2: api.NestedStruct2 = {}
        self.__prop3: api.NestedStruct3 = {}

    @property
    def prop1(self):
        return self.__prop1

    @property
    def prop2(self):
        return self.__prop2

    @property
    def prop3(self):
        return self.__prop3