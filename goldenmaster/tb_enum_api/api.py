from pydantic import BaseModel, Field
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

class IEnumInterface:

    def get_prop0(self):
        raise NotImplementedError

    def set_prop0(self, value):
        raise NotImplementedError

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

    def func0(self, param0: Enum0):
        raise NotImplementedError

    def func1(self, param1: Enum1):
        raise NotImplementedError

    def func2(self, param2: Enum2):
        raise NotImplementedError

    def func3(self, param3: Enum3):
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

def as_enum0(v):
    return Enum0(int(v))

def from_enum0(v):
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

