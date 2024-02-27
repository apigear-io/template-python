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

    def get_prop_int32(self):
        raise NotImplementedError

    def set_prop_int32(self, value):
        raise NotImplementedError

    def get_prop_int64(self):
        raise NotImplementedError

    def set_prop_int64(self, value):
        raise NotImplementedError

    def get_prop_float(self):
        raise NotImplementedError

    def set_prop_float(self, value):
        raise NotImplementedError

    def get_prop_float32(self):
        raise NotImplementedError

    def set_prop_float32(self, value):
        raise NotImplementedError

    def get_prop_float64(self):
        raise NotImplementedError

    def set_prop_float64(self, value):
        raise NotImplementedError

    def get_prop_string(self):
        raise NotImplementedError

    def set_prop_string(self, value):
        raise NotImplementedError

    def get_prop_read_only_string(self):
        raise NotImplementedError

    def func_void(self):
        raise NotImplementedError

    def func_bool(self, param_bool: bool):
        raise NotImplementedError

    def func_int(self, param_int: int):
        raise NotImplementedError

    def func_int32(self, param_int32: int):
        raise NotImplementedError

    def func_int64(self, param_int64: int):
        raise NotImplementedError

    def func_float(self, param_float: float):
        raise NotImplementedError

    def func_float32(self, param_float32: float):
        raise NotImplementedError

    def func_float64(self, param_float: float):
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

    def get_prop_int32(self):
        raise NotImplementedError

    def set_prop_int32(self, value):
        raise NotImplementedError

    def get_prop_int64(self):
        raise NotImplementedError

    def set_prop_int64(self, value):
        raise NotImplementedError

    def get_prop_float(self):
        raise NotImplementedError

    def set_prop_float(self, value):
        raise NotImplementedError

    def get_prop_float32(self):
        raise NotImplementedError

    def set_prop_float32(self, value):
        raise NotImplementedError

    def get_prop_float64(self):
        raise NotImplementedError

    def set_prop_float64(self, value):
        raise NotImplementedError

    def get_prop_string(self):
        raise NotImplementedError

    def set_prop_string(self, value):
        raise NotImplementedError

    def func_bool(self, param_bool: list[bool]):
        raise NotImplementedError

    def func_int(self, param_int: list[int]):
        raise NotImplementedError

    def func_int32(self, param_int32: list[int]):
        raise NotImplementedError

    def func_int64(self, param_int64: list[int]):
        raise NotImplementedError

    def func_float(self, param_float: list[float]):
        raise NotImplementedError

    def func_float32(self, param_float32: list[float]):
        raise NotImplementedError

    def func_float64(self, param_float: list[float]):
        raise NotImplementedError

    def func_string(self, param_string: list[str]):
        raise NotImplementedError

class INoPropertiesInterface:
    def __init__(self):
        pass

    def func_void(self):
        raise NotImplementedError

    def func_bool(self, param_bool: bool):
        raise NotImplementedError

class INoOperationsInterface:
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

class INoSignalsInterface:
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

    def func_void(self):
        raise NotImplementedError

    def func_bool(self, param_bool: bool):
        raise NotImplementedError

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

