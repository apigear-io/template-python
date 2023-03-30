from pydantic import BaseModel
from enum import IntEnum



class Enum0(IntEnum):
    value0 = 0
    value1 = 1
    value2 = 2

class Enum1(IntEnum):
    value1 = 1
    value2 = 2
    value3 = 3

class Enum2(IntEnum):
    value2 = 2
    value1 = 1
    value0 = 0

class Enum3(IntEnum):
    value3 = 3
    value2 = 2
    value1 = 1

class EnumInterface(BaseModel):
    prop0: Enum0
    prop1: Enum1
    prop2: Enum2
    prop3: Enum3

    def func0(self, param0: Enum0):
        raise NotImplementedError

    def func1(self, param1: Enum1):
        raise NotImplementedError

    def func2(self, param2: Enum2):
        raise NotImplementedError

    def func3(self, param3: Enum3):
        raise NotImplementedError
