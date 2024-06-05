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

class StructBool(EnhancedModel):
    field_bool: bool = Field(default=False, alias="fieldBool")

    def __init__(self, **kw):
        super().__init__(**kw)

class StructInt(EnhancedModel):
    field_int: int = Field(default=0, alias="fieldInt")

    def __init__(self, **kw):
        super().__init__(**kw)

class StructFloat(EnhancedModel):
    field_float: float = Field(default=0.0, alias="fieldFloat")

    def __init__(self, **kw):
        super().__init__(**kw)

class StructString(EnhancedModel):
    field_string: str = Field(default="", alias="fieldString")

    def __init__(self, **kw):
        super().__init__(**kw)

class IStructInterface:
    def __init__(self):
        pass

    def get_prop_bool(self):
        raise NotImplementedError("Method testbed1/struct_interface:get_prop_bool is not implemented.")

    def set_prop_bool(self, value):
        raise NotImplementedError("Method testbed1/struct_interface:set_prop_bool is not implemented.")

    def get_prop_int(self):
        raise NotImplementedError("Method testbed1/struct_interface:get_prop_int is not implemented.")

    def set_prop_int(self, value):
        raise NotImplementedError("Method testbed1/struct_interface:set_prop_int is not implemented.")

    def get_prop_float(self):
        raise NotImplementedError("Method testbed1/struct_interface:get_prop_float is not implemented.")

    def set_prop_float(self, value):
        raise NotImplementedError("Method testbed1/struct_interface:set_prop_float is not implemented.")

    def get_prop_string(self):
        raise NotImplementedError("Method testbed1/struct_interface:get_prop_string is not implemented.")

    def set_prop_string(self, value):
        raise NotImplementedError("Method testbed1/struct_interface:set_prop_string is not implemented.")

    def func_bool(self, param_bool: StructBool):
        raise NotImplementedError("Method testbed1/struct_interface:func_bool is not implemented.")

    def func_int(self, param_int: StructInt):
        raise NotImplementedError("Method testbed1/struct_interface:func_int is not implemented.")

    def func_float(self, param_float: StructFloat):
        raise NotImplementedError("Method testbed1/struct_interface:func_float is not implemented.")

    def func_string(self, param_string: StructString):
        raise NotImplementedError("Method testbed1/struct_interface:func_string is not implemented.")

class IStructArrayInterface:
    def __init__(self):
        pass

    def get_prop_bool(self):
        raise NotImplementedError("Method testbed1/struct_array_interface:get_prop_bool is not implemented.")

    def set_prop_bool(self, value):
        raise NotImplementedError("Method testbed1/struct_array_interface:set_prop_bool is not implemented.")

    def get_prop_int(self):
        raise NotImplementedError("Method testbed1/struct_array_interface:get_prop_int is not implemented.")

    def set_prop_int(self, value):
        raise NotImplementedError("Method testbed1/struct_array_interface:set_prop_int is not implemented.")

    def get_prop_float(self):
        raise NotImplementedError("Method testbed1/struct_array_interface:get_prop_float is not implemented.")

    def set_prop_float(self, value):
        raise NotImplementedError("Method testbed1/struct_array_interface:set_prop_float is not implemented.")

    def get_prop_string(self):
        raise NotImplementedError("Method testbed1/struct_array_interface:get_prop_string is not implemented.")

    def set_prop_string(self, value):
        raise NotImplementedError("Method testbed1/struct_array_interface:set_prop_string is not implemented.")

    def func_bool(self, param_bool: list[StructBool]):
        raise NotImplementedError("Method testbed1/struct_array_interface:func_bool is not implemented.")

    def func_int(self, param_int: list[StructInt]):
        raise NotImplementedError("Method testbed1/struct_array_interface:func_int is not implemented.")

    def func_float(self, param_float: list[StructFloat]):
        raise NotImplementedError("Method testbed1/struct_array_interface:func_float is not implemented.")

    def func_string(self, param_string: list[StructString]):
        raise NotImplementedError("Method testbed1/struct_array_interface:func_string is not implemented.")

def as_struct_bool(v):
    return StructBool.model_validate(v)

def from_struct_bool(v):
    return v.model_dump()

def as_struct_int(v):
    return StructInt.model_validate(v)

def from_struct_int(v):
    return v.model_dump()

def as_struct_float(v):
    return StructFloat.model_validate(v)

def from_struct_float(v):
    return v.model_dump()

def as_struct_string(v):
    return StructString.model_validate(v)

def from_struct_string(v):
    return v.model_dump()

