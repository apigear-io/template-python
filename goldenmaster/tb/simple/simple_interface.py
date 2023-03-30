from tb.simple.api import api
from typing import Iterable

class SimpleInterface(api.ISimpleInterface):
    def __init__(self):
        self.__propBool: bool = False
        self.__propInt: int = 0
        self.__propFloat: float = 0.0
        self.__propString: str = ""

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

    def funcBool(self, paramBool: bool) -> bool:
        return False

    def funcInt(self, paramInt: int) -> int:
        return 0

    def funcFloat(self, paramFloat: float) -> float:
        return 0.0

    def funcString(self, paramString: str) -> str:
        return ""