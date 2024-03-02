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

def as_int32(v):
    return as_int(v)

def from_int32(v):
    return from_int(v)

def as_int64(v):
    return as_int(v)

def from_int64(v):
    return from_int(v)

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

def as_float32(v):
    return as_float(v)

def from_float32(v):
    return from_float(v)

def as_float64(v):
    return as_float(v)

def from_float64(v):
    return from_float(v)

def as_empty_enum(v):
    return EmptyEnum(int(v))

def from_empty_enum(v):
    return v

def as_empty_struct(v):
    return EmptyStruct.model_validate(v)

def from_empty_struct(v):
    return v.model_dump()

