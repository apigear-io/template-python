from pydantic import BaseModel, Field
from enum import IntEnum



class Enum1(IntEnum):
    value1 = 1
    value2 = 2

class Enum2(IntEnum):
    value1 = 1
    value2 = 2

class Struct1(BaseModel):
    field1: int = Field(None, alias="field1")
    field2: int = Field(None, alias="field2")
    field3: int = Field(None, alias="field3")

class Struct2(BaseModel):
    field1: int = Field(None, alias="field1")
    field2: int = Field(None, alias="field2")
    field3: int = Field(None, alias="field3")

class ISameStruct1Interface:

    def get_prop1(self):
        raise NotImplementedError

    def set_prop1(self, value):
        raise NotImplementedError

    def func1(self, param1: Struct1):
        raise NotImplementedError

class ISameStruct2Interface:

    def get_prop1(self):
        raise NotImplementedError

    def set_prop1(self, value):
        raise NotImplementedError

    def get_prop2(self):
        raise NotImplementedError

    def set_prop2(self, value):
        raise NotImplementedError

    def func1(self, param1: Struct1):
        raise NotImplementedError

    def func2(self, param1: Struct1, param2: Struct2):
        raise NotImplementedError

class ISameEnum1Interface:

    def get_prop1(self):
        raise NotImplementedError

    def set_prop1(self, value):
        raise NotImplementedError

    def func1(self, param1: Enum1):
        raise NotImplementedError

class ISameEnum2Interface:

    def get_prop1(self):
        raise NotImplementedError

    def set_prop1(self, value):
        raise NotImplementedError

    def get_prop2(self):
        raise NotImplementedError

    def set_prop2(self, value):
        raise NotImplementedError

    def func1(self, param1: Enum1):
        raise NotImplementedError

    def func2(self, param1: Enum1, param2: Enum2):
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

def as_struct1(v):
    return Struct1.parse_obj(v)

def from_struct1(v):
    return v.dict()

def as_struct2(v):
    return Struct2.parse_obj(v)

def from_struct2(v):
    return v.dict()

