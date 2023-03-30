from tb.simple.api import api
from typing import Iterable

class SimpleArrayInterface(api.ISimpleArrayInterface):
    def __init__(self):
        self.__propBool: list[bool] = []
        self.__propInt: list[int] = []
        self.__propFloat: list[float] = []
        self.__propString: list[str] = []

    @property
    def propBool(self):
        return self.__propBool

    @property
    def propInt(self):
        return self.__propInt

    @property
    def propFloat(self):
        return self.__propFloat

    @property
    def propString(self):
        return self.__propString

    def funcBool(self, paramBool: list[bool]) -> list[bool]:
        return []

    def funcInt(self, paramInt: list[int]) -> list[int]:
        return []

    def funcFloat(self, paramFloat: list[float]) -> list[float]:
        return []

    def funcString(self, paramString: list[str]) -> list[str]:
        return []