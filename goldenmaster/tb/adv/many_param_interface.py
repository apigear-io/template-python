from tb.adv.api import api
from typing import Iterable

class ManyParamInterface(api.IManyParamInterface):
    def __init__(self):
        self.__prop1: int = 0
        self.__prop2: int = 0
        self.__prop3: int = 0
        self.__prop4: int = 0

    @property
    def prop1(self):
        return self.__prop1

    @property
    def prop2(self):
        return self.__prop2

    @property
    def prop3(self):
        return self.__prop3

    @property
    def prop4(self):
        return self.__prop4