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
        raise NotImplementedError("Method tb.simple/simple_interface:get_prop_bool is not implemented.")

    def set_prop_bool(self, value):
        raise NotImplementedError("Method tb.simple/simple_interface:set_prop_bool is not implemented.")

    def get_prop_int(self):
        raise NotImplementedError("Method tb.simple/simple_interface:get_prop_int is not implemented.")

    def set_prop_int(self, value):
        raise NotImplementedError("Method tb.simple/simple_interface:set_prop_int is not implemented.")

    def get_prop_int32(self):
        raise NotImplementedError("Method tb.simple/simple_interface:get_prop_int32 is not implemented.")

    def set_prop_int32(self, value):
        raise NotImplementedError("Method tb.simple/simple_interface:set_prop_int32 is not implemented.")

    def get_prop_int64(self):
        raise NotImplementedError("Method tb.simple/simple_interface:get_prop_int64 is not implemented.")

    def set_prop_int64(self, value):
        raise NotImplementedError("Method tb.simple/simple_interface:set_prop_int64 is not implemented.")

    def get_prop_float(self):
        raise NotImplementedError("Method tb.simple/simple_interface:get_prop_float is not implemented.")

    def set_prop_float(self, value):
        raise NotImplementedError("Method tb.simple/simple_interface:set_prop_float is not implemented.")

    def get_prop_float32(self):
        raise NotImplementedError("Method tb.simple/simple_interface:get_prop_float32 is not implemented.")

    def set_prop_float32(self, value):
        raise NotImplementedError("Method tb.simple/simple_interface:set_prop_float32 is not implemented.")

    def get_prop_float64(self):
        raise NotImplementedError("Method tb.simple/simple_interface:get_prop_float64 is not implemented.")

    def set_prop_float64(self, value):
        raise NotImplementedError("Method tb.simple/simple_interface:set_prop_float64 is not implemented.")

    def get_prop_string(self):
        raise NotImplementedError("Method tb.simple/simple_interface:get_prop_string is not implemented.")

    def set_prop_string(self, value):
        raise NotImplementedError("Method tb.simple/simple_interface:set_prop_string is not implemented.")

    def get_prop_read_only_string(self):
        raise NotImplementedError("Method tb.simple/simple_interface:get_prop_read_only_string is not implemented.")

    def func_void(self):
        raise NotImplementedError("Method tb.simple/simple_interface:func_void is not implemented.")

    def func_bool(self, param_bool: bool):
        raise NotImplementedError("Method tb.simple/simple_interface:func_bool is not implemented.")

    def func_int(self, param_int: int):
        raise NotImplementedError("Method tb.simple/simple_interface:func_int is not implemented.")

    def func_int32(self, param_int32: int):
        raise NotImplementedError("Method tb.simple/simple_interface:func_int32 is not implemented.")

    def func_int64(self, param_int64: int):
        raise NotImplementedError("Method tb.simple/simple_interface:func_int64 is not implemented.")

    def func_float(self, param_float: float):
        raise NotImplementedError("Method tb.simple/simple_interface:func_float is not implemented.")

    def func_float32(self, param_float32: float):
        raise NotImplementedError("Method tb.simple/simple_interface:func_float32 is not implemented.")

    def func_float64(self, param_float: float):
        raise NotImplementedError("Method tb.simple/simple_interface:func_float64 is not implemented.")

    def func_string(self, param_string: str):
        raise NotImplementedError("Method tb.simple/simple_interface:func_string is not implemented.")

class ISimpleArrayInterface:
    def __init__(self):
        pass

    def get_prop_bool(self):
        raise NotImplementedError("Method tb.simple/simple_array_interface:get_prop_bool is not implemented.")

    def set_prop_bool(self, value):
        raise NotImplementedError("Method tb.simple/simple_array_interface:set_prop_bool is not implemented.")

    def get_prop_int(self):
        raise NotImplementedError("Method tb.simple/simple_array_interface:get_prop_int is not implemented.")

    def set_prop_int(self, value):
        raise NotImplementedError("Method tb.simple/simple_array_interface:set_prop_int is not implemented.")

    def get_prop_int32(self):
        raise NotImplementedError("Method tb.simple/simple_array_interface:get_prop_int32 is not implemented.")

    def set_prop_int32(self, value):
        raise NotImplementedError("Method tb.simple/simple_array_interface:set_prop_int32 is not implemented.")

    def get_prop_int64(self):
        raise NotImplementedError("Method tb.simple/simple_array_interface:get_prop_int64 is not implemented.")

    def set_prop_int64(self, value):
        raise NotImplementedError("Method tb.simple/simple_array_interface:set_prop_int64 is not implemented.")

    def get_prop_float(self):
        raise NotImplementedError("Method tb.simple/simple_array_interface:get_prop_float is not implemented.")

    def set_prop_float(self, value):
        raise NotImplementedError("Method tb.simple/simple_array_interface:set_prop_float is not implemented.")

    def get_prop_float32(self):
        raise NotImplementedError("Method tb.simple/simple_array_interface:get_prop_float32 is not implemented.")

    def set_prop_float32(self, value):
        raise NotImplementedError("Method tb.simple/simple_array_interface:set_prop_float32 is not implemented.")

    def get_prop_float64(self):
        raise NotImplementedError("Method tb.simple/simple_array_interface:get_prop_float64 is not implemented.")

    def set_prop_float64(self, value):
        raise NotImplementedError("Method tb.simple/simple_array_interface:set_prop_float64 is not implemented.")

    def get_prop_string(self):
        raise NotImplementedError("Method tb.simple/simple_array_interface:get_prop_string is not implemented.")

    def set_prop_string(self, value):
        raise NotImplementedError("Method tb.simple/simple_array_interface:set_prop_string is not implemented.")

    def func_bool(self, param_bool: list[bool]):
        raise NotImplementedError("Method tb.simple/simple_array_interface:func_bool is not implemented.")

    def func_int(self, param_int: list[int]):
        raise NotImplementedError("Method tb.simple/simple_array_interface:func_int is not implemented.")

    def func_int32(self, param_int32: list[int]):
        raise NotImplementedError("Method tb.simple/simple_array_interface:func_int32 is not implemented.")

    def func_int64(self, param_int64: list[int]):
        raise NotImplementedError("Method tb.simple/simple_array_interface:func_int64 is not implemented.")

    def func_float(self, param_float: list[float]):
        raise NotImplementedError("Method tb.simple/simple_array_interface:func_float is not implemented.")

    def func_float32(self, param_float32: list[float]):
        raise NotImplementedError("Method tb.simple/simple_array_interface:func_float32 is not implemented.")

    def func_float64(self, param_float: list[float]):
        raise NotImplementedError("Method tb.simple/simple_array_interface:func_float64 is not implemented.")

    def func_string(self, param_string: list[str]):
        raise NotImplementedError("Method tb.simple/simple_array_interface:func_string is not implemented.")

class INoPropertiesInterface:
    def __init__(self):
        pass

    def func_void(self):
        raise NotImplementedError("Method tb.simple/no_properties_interface:func_void is not implemented.")

    def func_bool(self, param_bool: bool):
        raise NotImplementedError("Method tb.simple/no_properties_interface:func_bool is not implemented.")

class INoOperationsInterface:
    def __init__(self):
        pass

    def get_prop_bool(self):
        raise NotImplementedError("Method tb.simple/no_operations_interface:get_prop_bool is not implemented.")

    def set_prop_bool(self, value):
        raise NotImplementedError("Method tb.simple/no_operations_interface:set_prop_bool is not implemented.")

    def get_prop_int(self):
        raise NotImplementedError("Method tb.simple/no_operations_interface:get_prop_int is not implemented.")

    def set_prop_int(self, value):
        raise NotImplementedError("Method tb.simple/no_operations_interface:set_prop_int is not implemented.")

class INoSignalsInterface:
    def __init__(self):
        pass

    def get_prop_bool(self):
        raise NotImplementedError("Method tb.simple/no_signals_interface:get_prop_bool is not implemented.")

    def set_prop_bool(self, value):
        raise NotImplementedError("Method tb.simple/no_signals_interface:set_prop_bool is not implemented.")

    def get_prop_int(self):
        raise NotImplementedError("Method tb.simple/no_signals_interface:get_prop_int is not implemented.")

    def set_prop_int(self, value):
        raise NotImplementedError("Method tb.simple/no_signals_interface:set_prop_int is not implemented.")

    def func_void(self):
        raise NotImplementedError("Method tb.simple/no_signals_interface:func_void is not implemented.")

    def func_bool(self, param_bool: bool):
        raise NotImplementedError("Method tb.simple/no_signals_interface:func_bool is not implemented.")

class IEmptyInterface:
    def __init__(self):
        pass

