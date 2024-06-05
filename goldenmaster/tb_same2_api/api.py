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

class Enum1(IntEnum):
    VALUE1 = 1
    VALUE2 = 2

class Enum2(IntEnum):
    VALUE1 = 1
    VALUE2 = 2

class Struct1(EnhancedModel):
    field1: int = Field(default=0, alias="field1")
    field2: int = Field(default=0, alias="field2")
    field3: int = Field(default=0, alias="field3")

    def __init__(self, **kw):
        super().__init__(**kw)

class Struct2(EnhancedModel):
    field1: int = Field(default=0, alias="field1")
    field2: int = Field(default=0, alias="field2")
    field3: int = Field(default=0, alias="field3")

    def __init__(self, **kw):
        super().__init__(**kw)

class ISameStruct1Interface:
    def __init__(self):
        pass

    def get_prop1(self):
        raise NotImplementedError("Method tb.same2/same_struct1_interface:get_prop1 is not implemented.")

    def set_prop1(self, value):
        raise NotImplementedError("Method tb.same2/same_struct1_interface:set_prop1 is not implemented.")

    def func1(self, param1: Struct1):
        raise NotImplementedError("Method tb.same2/same_struct1_interface:func1 is not implemented.")

class ISameStruct2Interface:
    def __init__(self):
        pass

    def get_prop1(self):
        raise NotImplementedError("Method tb.same2/same_struct2_interface:get_prop1 is not implemented.")

    def set_prop1(self, value):
        raise NotImplementedError("Method tb.same2/same_struct2_interface:set_prop1 is not implemented.")

    def get_prop2(self):
        raise NotImplementedError("Method tb.same2/same_struct2_interface:get_prop2 is not implemented.")

    def set_prop2(self, value):
        raise NotImplementedError("Method tb.same2/same_struct2_interface:set_prop2 is not implemented.")

    def func1(self, param1: Struct1):
        raise NotImplementedError("Method tb.same2/same_struct2_interface:func1 is not implemented.")

    def func2(self, param1: Struct1, param2: Struct2):
        raise NotImplementedError("Method tb.same2/same_struct2_interface:func2 is not implemented.")

class ISameEnum1Interface:
    def __init__(self):
        pass

    def get_prop1(self):
        raise NotImplementedError("Method tb.same2/same_enum1_interface:get_prop1 is not implemented.")

    def set_prop1(self, value):
        raise NotImplementedError("Method tb.same2/same_enum1_interface:set_prop1 is not implemented.")

    def func1(self, param1: Enum1):
        raise NotImplementedError("Method tb.same2/same_enum1_interface:func1 is not implemented.")

class ISameEnum2Interface:
    def __init__(self):
        pass

    def get_prop1(self):
        raise NotImplementedError("Method tb.same2/same_enum2_interface:get_prop1 is not implemented.")

    def set_prop1(self, value):
        raise NotImplementedError("Method tb.same2/same_enum2_interface:set_prop1 is not implemented.")

    def get_prop2(self):
        raise NotImplementedError("Method tb.same2/same_enum2_interface:get_prop2 is not implemented.")

    def set_prop2(self, value):
        raise NotImplementedError("Method tb.same2/same_enum2_interface:set_prop2 is not implemented.")

    def func1(self, param1: Enum1):
        raise NotImplementedError("Method tb.same2/same_enum2_interface:func1 is not implemented.")

    def func2(self, param1: Enum1, param2: Enum2):
        raise NotImplementedError("Method tb.same2/same_enum2_interface:func2 is not implemented.")

def as_enum1(v):
    return Enum1(int(v))

def from_enum1(v):
    return v

def as_enum2(v):
    return Enum2(int(v))

def from_enum2(v):
    return v

def as_struct1(v):
    return Struct1.model_validate(v)

def from_struct1(v):
    return v.model_dump()

def as_struct2(v):
    return Struct2.model_validate(v)

def from_struct2(v):
    return v.model_dump()

