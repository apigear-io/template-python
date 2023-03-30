from pydantic import BaseModel
from enum import IntEnum



class Enum1(IntEnum):
    value1 = 1
    value2 = 2
    value3 = 3
    value4 = 4

class Enum2(IntEnum):
    value1 = 1
    value2 = 2
    value3 = 3
    value4 = 4

class Enum3(IntEnum):
    value1 = 1
    value2 = 2
    value3 = 3
    value4 = 4

class Struct1(BaseModel):
    field1: int

class Struct2(BaseModel):
    field1: int
    field2: int

class Struct3(BaseModel):
    field1: int
    field2: int
    field3: int

class Struct4(BaseModel):
    field1: int
    field2: int
    field3: int
    field4: int

class NestedStruct1(BaseModel):
    field1: Struct1

class NestedStruct2(BaseModel):
    field1: Struct1
    field2: Struct2

class NestedStruct3(BaseModel):
    field1: Struct1
    field2: Struct2
    field3: Struct3

class ManyParamInterface(BaseModel):
    prop1: int
    prop2: int
    prop3: int
    prop4: int

class NestedStruct1Interface(BaseModel):
    prop1: NestedStruct1

class NestedStruct2Interface(BaseModel):
    prop1: NestedStruct1
    prop2: NestedStruct2

class NestedStruct3Interface(BaseModel):
    prop1: NestedStruct1
    prop2: NestedStruct2
    prop3: NestedStruct3
