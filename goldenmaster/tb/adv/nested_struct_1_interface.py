from tb.adv.api import api
from typing import Iterable

class NestedStruct1Interface(api.INestedStruct1Interface):
    def __init__(self):
        self.__prop1: api.NestedStruct1 = {}

    @property
    def prop1(self):
        return self.__prop1