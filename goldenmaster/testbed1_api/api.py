from pydantic import BaseModel, Field
from enum import IntEnum

class EnhancedModel(BaseModel):
    """This model is used to enforce the json encoding by alias"""
    class config:
        allow_population_by_field_name = True
    def dict(self, **kwargs):
        kwargs.setdefault('by_alias', True)
        return super().dict(**kwargs)

class StructBool(EnhancedModel):
    field_bool: bool = Field(None, alias="fieldBool")

    def __init__(self, **kw):
        super().__init__(**kw)

class StructInt(EnhancedModel):
    field_int: int = Field(None, alias="fieldInt")

    def __init__(self, **kw):
        super().__init__(**kw)

class StructFloat(EnhancedModel):
    field_float: float = Field(None, alias="fieldFloat")

    def __init__(self, **kw):
        super().__init__(**kw)

class StructString(EnhancedModel):
    field_string: str = Field(None, alias="fieldString")

    def __init__(self, **kw):
        super().__init__(**kw)

class IStructInterface:
    def __init__(self):
        pass

    def get_prop_bool(self):
        raise NotImplementedError

    def set_prop_bool(self, value):
        raise NotImplementedError

    def get_prop_int(self):
        raise NotImplementedError

    def set_prop_int(self, value):
        raise NotImplementedError

    def get_prop_float(self):
        raise NotImplementedError

    def set_prop_float(self, value):
        raise NotImplementedError

    def get_prop_string(self):
        raise NotImplementedError

    def set_prop_string(self, value):
        raise NotImplementedError

    def func_bool(self, param_bool: StructBool):
        raise NotImplementedError

    def func_int(self, param_int: StructInt):
        raise NotImplementedError

    def func_float(self, param_float: StructFloat):
        raise NotImplementedError

    def func_string(self, param_string: StructString):
        raise NotImplementedError

class IStructArrayInterface:
    def __init__(self):
        pass

    def get_prop_bool(self):
        raise NotImplementedError

    def set_prop_bool(self, value):
        raise NotImplementedError

    def get_prop_int(self):
        raise NotImplementedError

    def set_prop_int(self, value):
        raise NotImplementedError

    def get_prop_float(self):
        raise NotImplementedError

    def set_prop_float(self, value):
        raise NotImplementedError

    def get_prop_string(self):
        raise NotImplementedError

    def set_prop_string(self, value):
        raise NotImplementedError

    def func_bool(self, param_bool: list[StructBool]):
        raise NotImplementedError

    def func_int(self, param_int: list[StructInt]):
        raise NotImplementedError

    def func_float(self, param_float: list[StructFloat]):
        raise NotImplementedError

    def func_string(self, param_string: list[StructString]):
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

def as_struct_bool(v):
    return StructBool.parse_obj(v)

def from_struct_bool(v):
    return v.dict()

def as_struct_int(v):
    return StructInt.parse_obj(v)

def from_struct_int(v):
    return v.dict()

def as_struct_float(v):
    return StructFloat.parse_obj(v)

def from_struct_float(v):
    return v.dict()

def as_struct_string(v):
    return StructString.parse_obj(v)

def from_struct_string(v):
    return v.dict()

