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
    VALUE3 = 3
    VALUE4 = 4

class Enum2(IntEnum):
    VALUE1 = 1
    VALUE2 = 2
    VALUE3 = 3
    VALUE4 = 4

class Enum3(IntEnum):
    VALUE1 = 1
    VALUE2 = 2
    VALUE3 = 3
    VALUE4 = 4

class Struct1(EnhancedModel):
    field1: int = Field(default=0, alias="field1")

    def __init__(self, **kw):
        super().__init__(**kw)

class Struct2(EnhancedModel):
    field1: int = Field(default=0, alias="field1")
    field2: int = Field(default=0, alias="field2")

    def __init__(self, **kw):
        super().__init__(**kw)

class Struct3(EnhancedModel):
    field1: int = Field(default=0, alias="field1")
    field2: int = Field(default=0, alias="field2")
    field3: int = Field(default=0, alias="field3")

    def __init__(self, **kw):
        super().__init__(**kw)

class Struct4(EnhancedModel):
    field1: int = Field(default=0, alias="field1")
    field2: int = Field(default=0, alias="field2")
    field3: int = Field(default=0, alias="field3")
    field4: int = Field(default=0, alias="field4")

    def __init__(self, **kw):
        super().__init__(**kw)

class NestedStruct1(EnhancedModel):
    field1: Struct1 = Field(default_factory=lambda :Struct1(), alias="field1")

    def __init__(self, **kw):
        super().__init__(**kw)

class NestedStruct2(EnhancedModel):
    field1: Struct1 = Field(default_factory=lambda :Struct1(), alias="field1")
    field2: Struct2 = Field(default_factory=lambda :Struct2(), alias="field2")

    def __init__(self, **kw):
        super().__init__(**kw)

class NestedStruct3(EnhancedModel):
    field1: Struct1 = Field(default_factory=lambda :Struct1(), alias="field1")
    field2: Struct2 = Field(default_factory=lambda :Struct2(), alias="field2")
    field3: Struct3 = Field(default_factory=lambda :Struct3(), alias="field3")

    def __init__(self, **kw):
        super().__init__(**kw)

class IManyParamInterface:
    def __init__(self):
        pass

    def get_prop1(self):
        raise NotImplementedError("Method testbed2/many_param_interface:get_prop1 is not implemented.")

    def set_prop1(self, value):
        raise NotImplementedError("Method testbed2/many_param_interface:set_prop1 is not implemented.")

    def get_prop2(self):
        raise NotImplementedError("Method testbed2/many_param_interface:get_prop2 is not implemented.")

    def set_prop2(self, value):
        raise NotImplementedError("Method testbed2/many_param_interface:set_prop2 is not implemented.")

    def get_prop3(self):
        raise NotImplementedError("Method testbed2/many_param_interface:get_prop3 is not implemented.")

    def set_prop3(self, value):
        raise NotImplementedError("Method testbed2/many_param_interface:set_prop3 is not implemented.")

    def get_prop4(self):
        raise NotImplementedError("Method testbed2/many_param_interface:get_prop4 is not implemented.")

    def set_prop4(self, value):
        raise NotImplementedError("Method testbed2/many_param_interface:set_prop4 is not implemented.")

    def func1(self, param1: int):
        raise NotImplementedError("Method testbed2/many_param_interface:func1 is not implemented.")

    def func2(self, param1: int, param2: int):
        raise NotImplementedError("Method testbed2/many_param_interface:func2 is not implemented.")

    def func3(self, param1: int, param2: int, param3: int):
        raise NotImplementedError("Method testbed2/many_param_interface:func3 is not implemented.")

    def func4(self, param1: int, param2: int, param3: int, param4: int):
        raise NotImplementedError("Method testbed2/many_param_interface:func4 is not implemented.")

class INestedStruct1Interface:
    def __init__(self):
        pass

    def get_prop1(self):
        raise NotImplementedError("Method testbed2/nested_struct1_interface:get_prop1 is not implemented.")

    def set_prop1(self, value):
        raise NotImplementedError("Method testbed2/nested_struct1_interface:set_prop1 is not implemented.")

    def func1(self, param1: NestedStruct1):
        raise NotImplementedError("Method testbed2/nested_struct1_interface:func1 is not implemented.")

class INestedStruct2Interface:
    def __init__(self):
        pass

    def get_prop1(self):
        raise NotImplementedError("Method testbed2/nested_struct2_interface:get_prop1 is not implemented.")

    def set_prop1(self, value):
        raise NotImplementedError("Method testbed2/nested_struct2_interface:set_prop1 is not implemented.")

    def get_prop2(self):
        raise NotImplementedError("Method testbed2/nested_struct2_interface:get_prop2 is not implemented.")

    def set_prop2(self, value):
        raise NotImplementedError("Method testbed2/nested_struct2_interface:set_prop2 is not implemented.")

    def func1(self, param1: NestedStruct1):
        raise NotImplementedError("Method testbed2/nested_struct2_interface:func1 is not implemented.")

    def func2(self, param1: NestedStruct1, param2: NestedStruct2):
        raise NotImplementedError("Method testbed2/nested_struct2_interface:func2 is not implemented.")

class INestedStruct3Interface:
    def __init__(self):
        pass

    def get_prop1(self):
        raise NotImplementedError("Method testbed2/nested_struct3_interface:get_prop1 is not implemented.")

    def set_prop1(self, value):
        raise NotImplementedError("Method testbed2/nested_struct3_interface:set_prop1 is not implemented.")

    def get_prop2(self):
        raise NotImplementedError("Method testbed2/nested_struct3_interface:get_prop2 is not implemented.")

    def set_prop2(self, value):
        raise NotImplementedError("Method testbed2/nested_struct3_interface:set_prop2 is not implemented.")

    def get_prop3(self):
        raise NotImplementedError("Method testbed2/nested_struct3_interface:get_prop3 is not implemented.")

    def set_prop3(self, value):
        raise NotImplementedError("Method testbed2/nested_struct3_interface:set_prop3 is not implemented.")

    def func1(self, param1: NestedStruct1):
        raise NotImplementedError("Method testbed2/nested_struct3_interface:func1 is not implemented.")

    def func2(self, param1: NestedStruct1, param2: NestedStruct2):
        raise NotImplementedError("Method testbed2/nested_struct3_interface:func2 is not implemented.")

    def func3(self, param1: NestedStruct1, param2: NestedStruct2, param3: NestedStruct3):
        raise NotImplementedError("Method testbed2/nested_struct3_interface:func3 is not implemented.")

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
    return Struct1.model_validate(v)

def from_struct1(v):
    return v.model_dump()

def as_struct2(v):
    return Struct2.model_validate(v)

def from_struct2(v):
    return v.model_dump()

def as_struct3(v):
    return Struct3.model_validate(v)

def from_struct3(v):
    return v.model_dump()

def as_struct4(v):
    return Struct4.model_validate(v)

def from_struct4(v):
    return v.model_dump()

def as_nested_struct1(v):
    return NestedStruct1.model_validate(v)

def from_nested_struct1(v):
    return v.model_dump()

def as_nested_struct2(v):
    return NestedStruct2.model_validate(v)

def from_nested_struct2(v):
    return v.model_dump()

def as_nested_struct3(v):
    return NestedStruct3.model_validate(v)

def from_nested_struct3(v):
    return v.model_dump()

