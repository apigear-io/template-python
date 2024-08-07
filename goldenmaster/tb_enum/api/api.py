from pydantic import ConfigDict, BaseModel, Field
from enum import IntEnum

class EnhancedModel(BaseModel):
    """This model is used to enforce the json encoding by alias"""
    model_config = ConfigDict(populate_by_name=True)

    def model_dump(self, **kwargs):
        kwargs.setdefault('by_alias', True)
        return super().model_dump(**kwargs)

    def __init__(self, **kw):
        super().__init__(**kw)

class Enum0(IntEnum):
    VALUE0 = 0
    VALUE1 = 1
    VALUE2 = 2

class Enum1(IntEnum):
    VALUE1 = 1
    VALUE2 = 2
    VALUE3 = 3

class Enum2(IntEnum):
    VALUE2 = 2
    VALUE1 = 1
    VALUE0 = 0

class Enum3(IntEnum):
    VALUE3 = 3
    VALUE2 = 2
    VALUE1 = 1

class IEnumInterface:
    def __init__(self):
        pass

    def get_prop0(self):
        raise NotImplementedError("Method tb.enum/enum_interface:get_prop0 is not implemented.")

    def set_prop0(self, value):
        raise NotImplementedError("Method tb.enum/enum_interface:set_prop0 is not implemented.")

    def get_prop1(self):
        raise NotImplementedError("Method tb.enum/enum_interface:get_prop1 is not implemented.")

    def set_prop1(self, value):
        raise NotImplementedError("Method tb.enum/enum_interface:set_prop1 is not implemented.")

    def get_prop2(self):
        raise NotImplementedError("Method tb.enum/enum_interface:get_prop2 is not implemented.")

    def set_prop2(self, value):
        raise NotImplementedError("Method tb.enum/enum_interface:set_prop2 is not implemented.")

    def get_prop3(self):
        raise NotImplementedError("Method tb.enum/enum_interface:get_prop3 is not implemented.")

    def set_prop3(self, value):
        raise NotImplementedError("Method tb.enum/enum_interface:set_prop3 is not implemented.")

    def func0(self, param0: Enum0):
        raise NotImplementedError("Method tb.enum/enum_interface:func0 is not implemented.")

    def func1(self, param1: Enum1):
        raise NotImplementedError("Method tb.enum/enum_interface:func1 is not implemented.")

    def func2(self, param2: Enum2):
        raise NotImplementedError("Method tb.enum/enum_interface:func2 is not implemented.")

    def func3(self, param3: Enum3):
        raise NotImplementedError("Method tb.enum/enum_interface:func3 is not implemented.")

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

