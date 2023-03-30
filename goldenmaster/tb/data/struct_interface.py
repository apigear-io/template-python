from tb.data.api import api
from typing import Iterable

class StructInterface(api.IStructInterface):
    def __init__(self):
        self.__propBool: api.StructBool = {}
        self.__propInt: api.StructInt = {}
        self.__propFloat: api.StructFloat = {}
        self.__propString: api.StructString = {}

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

    def funcBool(self, paramBool: api.StructBool) -> api.StructBool:
        return {}

    def funcInt(self, paramInt: api.StructInt) -> api.StructInt:
        return {}

    def funcFloat(self, paramFloat: api.StructFloat) -> api.StructFloat:
        return {}

    def funcString(self, paramString: api.StructString) -> api.StructString:
        return {}