from pydantic import BaseModel, Field
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
    field1: int = Field(None, alias="field1")

class Struct2(BaseModel):
    field1: int = Field(None, alias="field1")
    field2: int = Field(None, alias="field2")

class Struct3(BaseModel):
    field1: int = Field(None, alias="field1")
    field2: int = Field(None, alias="field2")
    field3: int = Field(None, alias="field3")

class Struct4(BaseModel):
    field1: int = Field(None, alias="field1")
    field2: int = Field(None, alias="field2")
    field3: int = Field(None, alias="field3")
    field4: int = Field(None, alias="field4")

class NestedStruct1(BaseModel):
    field1: Struct1 = Field(None, alias="field1")

class NestedStruct2(BaseModel):
    field1: Struct1 = Field(None, alias="field1")
    field2: Struct2 = Field(None, alias="field2")

class NestedStruct3(BaseModel):
    field1: Struct1 = Field(None, alias="field1")
    field2: Struct2 = Field(None, alias="field2")
    field3: Struct3 = Field(None, alias="field3")

class IManyParamInterface:

    def get_prop1(self):
        raise NotImplementedError

    def set_prop1(self, value):
        raise NotImplementedError

    def get_prop2(self):
        raise NotImplementedError

    def set_prop2(self, value):
        raise NotImplementedError

    def get_prop3(self):
        raise NotImplementedError

    def set_prop3(self, value):
        raise NotImplementedError

    def get_prop4(self):
        raise NotImplementedError

    def set_prop4(self, value):
        raise NotImplementedError

    def func1(self, param1: int):
        raise NotImplementedError

    def func2(self, param1: int, param2: int):
        raise NotImplementedError

    def func3(self, param1: int, param2: int, param3: int):
        raise NotImplementedError

    def func4(self, param1: int, param2: int, param3: int, param4: int):
        raise NotImplementedError

class INestedStruct1Interface:

    def get_prop1(self):
        raise NotImplementedError

    def set_prop1(self, value):
        raise NotImplementedError

    def func1(self, param1: NestedStruct1):
        raise NotImplementedError

class INestedStruct2Interface:

    def get_prop1(self):
        raise NotImplementedError

    def set_prop1(self, value):
        raise NotImplementedError

    def get_prop2(self):
        raise NotImplementedError

    def set_prop2(self, value):
        raise NotImplementedError

    def func1(self, param1: NestedStruct1):
        raise NotImplementedError

    def func2(self, param1: NestedStruct1, param2: NestedStruct2):
        raise NotImplementedError

class INestedStruct3Interface:

    def get_prop1(self):
        raise NotImplementedError

    def set_prop1(self, value):
        raise NotImplementedError

    def get_prop2(self):
        raise NotImplementedError

    def set_prop2(self, value):
        raise NotImplementedError

    def get_prop3(self):
        raise NotImplementedError

    def set_prop3(self, value):
        raise NotImplementedError

    def func1(self, param1: NestedStruct1):
        raise NotImplementedError

    def func2(self, param1: NestedStruct1, param2: NestedStruct2):
        raise NotImplementedError

    def func3(self, param1: NestedStruct1, param2: NestedStruct2, param3: NestedStruct3):
        raise NotImplementedError


def as_int(v):
    return int(v)

def from_int(v):
    return v

def as_string(v):
    return str(v)

def from_string(v):
    return v


def as_bool(v):
    return str(v).lower() in ['true', '1', 't', 'y', 'yes']

def from_bool(v):
    return v

def as_float(v):
    return float(v)

def from_float(v):
    return v

def as_enum1(v):
    return Enum1(int(v))

def from_enum1(v):
    return v

def as_enum2(v):
    return Enum2(int(v))

def from_enum2(v):
    return v

def as_enum3(v):
    return Enum3(int(v))

def from_enum3(v):
    return v

def as_struct1(v):
    return Struct1.parse_obj(v)

def from_struct1(v):
    return v.dict()

def as_struct2(v):
    return Struct2.parse_obj(v)

def from_struct2(v):
    return v.dict()

def as_struct3(v):
    return Struct3.parse_obj(v)

def from_struct3(v):
    return v.dict()

def as_struct4(v):
    return Struct4.parse_obj(v)

def from_struct4(v):
    return v.dict()

def as_nested_struct1(v):
    return NestedStruct1.parse_obj(v)

def from_nested_struct1(v):
    return v.dict()

def as_nested_struct2(v):
    return NestedStruct2.parse_obj(v)

def from_nested_struct2(v):
    return v.dict()

def as_nested_struct3(v):
    return NestedStruct3.parse_obj(v)

def from_nested_struct3(v):
    return v.dict()
