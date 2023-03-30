from pydantic import BaseModel
from enum import IntEnum



class Enum1(IntEnum):
    value1 = 1
    value2 = 2

class Enum2(IntEnum):
    value1 = 1
    value2 = 2

class Struct1(BaseModel):
    field1: int
    field2: int
    field3: int

class Struct2(BaseModel):
    field1: int
    field2: int
    field3: int

class SameStruct1Interface(BaseModel):
    prop1: Struct1

class SameStruct2Interface(BaseModel):
    prop1: Struct2
    prop2: Struct2

class SameEnum1Interface(BaseModel):
    prop1: Enum1

class SameEnum2Interface(BaseModel):
    prop1: Enum1
    prop2: Enum2
