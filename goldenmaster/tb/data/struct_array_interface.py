from tb.data.api import api
from typing import Iterable

class StructArrayInterface(api.IStructArrayInterface):
    def __init__(self):
        self.__propBool: list[api.StructBool] = []
        self.__propInt: list[api.StructInt] = []
        self.__propFloat: list[api.StructFloat] = []
        self.__propString: list[api.StructString] = []

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

    def funcBool(self, paramBool: list[api.StructBool]) -> list[api.StructBool]:
        return []

    def funcInt(self, paramInt: list[api.StructInt]) -> list[api.StructInt]:
        return []

    def funcFloat(self, paramFloat: list[api.StructFloat]) -> list[api.StructFloat]:
        return []

    def funcString(self, paramString: list[api.StructString]) -> list[api.StructString]:
        return []