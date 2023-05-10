from pydantic import BaseModel, Field
from enum import IntEnum



class EmptyEnum(IntEnum):
    pass

class EmptyStruct(BaseModel):
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

