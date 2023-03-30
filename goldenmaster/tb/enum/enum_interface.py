from tb.enum.api import api
from typing import Iterable

class EnumInterface(api.IEnumInterface):
    def __init__(self):
        self.__prop0: api.Enum0 = Enum0.value0
        self.__prop1: api.Enum1 = Enum1.value1
        self.__prop2: api.Enum2 = Enum2.value2
        self.__prop3: api.Enum3 = Enum3.value3

    @property
    def prop0(self):
        return self.__prop0

    @property
    def prop1(self):
        return self.__prop1

    @property
    def prop2(self):
        return self.__prop2

    @property
    def prop3(self):
        return self.__prop3

    def func0(self, param0: api.Enum0) -> api.Enum0:
        return Enum0.value0

    def func1(self, param1: api.Enum1) -> api.Enum1:
        return Enum1.value1

    def func2(self, param2: api.Enum2) -> api.Enum2:
        return Enum2.value2

    def func3(self, param3: api.Enum3) -> api.Enum3:
        return Enum3.value3