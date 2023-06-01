from pydantic import BaseModel, Field
from enum import IntEnum

class EnhancedModel(BaseModel):
    """This model is used to enforce the json encoding by alias"""
    class config:
        allow_population_by_field_name = True
    def dict(self, **kwargs):
        kwargs.setdefault('by_alias', True)
        return super().dict(**kwargs)

class ISimpleInterface:
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

    def func_bool(self, param_bool: bool):
        raise NotImplementedError

    def func_int(self, param_int: int):
        raise NotImplementedError

    def func_float(self, param_float: float):
        raise NotImplementedError

    def func_string(self, param_string: str):
        raise NotImplementedError

class ISimpleArrayInterface:
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

    def func_bool(self, param_bool: list[bool]):
        raise NotImplementedError

    def func_int(self, param_int: list[int]):
        raise NotImplementedError

    def func_float(self, param_float: list[float]):
        raise NotImplementedError

    def func_string(self, param_string: list[str]):
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

