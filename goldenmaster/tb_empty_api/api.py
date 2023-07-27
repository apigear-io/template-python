from pydantic import BaseModel, Field
from enum import IntEnum

class EnhancedModel(BaseModel):
    """This model is used to enforce the json encoding by alias"""
    class config:
        allow_population_by_field_name = True
    def dict(self, **kwargs):
        kwargs.setdefault('by_alias', True)
        return super().dict(**kwargs)

class EmptyEnum(IntEnum):
    pass

class EmptyStruct(EnhancedModel):
    pass

class IEmptyInterface:
    def __init__(self):
        pass


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

def as_empty_enum(v):
    return EmptyEnum(int(v))

def from_empty_enum(v):
    return v

def as_empty_struct(v):
    return EmptyStruct.parse_obj(v)

def from_empty_struct(v):
    return v.dict()
