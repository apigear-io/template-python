from tb_simple_api import api
from typing import Iterable

class SimpleArrayInterface(api.ISimpleArrayInterface):
    def __init__(self, notifier=None):
        super().__init__()
        self._notifier = notifier
        self._prop_bool: list[bool] = []
        self._prop_int: list[int] = []
        self._prop_int32: list[int] = []
        self._prop_int64: list[int] = []
        self._prop_float: list[float] = []
        self._prop_float32: list[float] = []
        self._prop_float64: list[float] = []
        self._prop_string: list[str] = []

    def set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        self._prop_bool = value
        self.push_prop_bool(self._prop_bool)
    
    def get_prop_bool(self):
        return self._prop_bool        

    def push_prop_bool(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("tb.simple.SimpleArrayInterface/propBool", value)

    def set_prop_int(self, value):
        if self._prop_int == value:
            return
        self._prop_int = value
        self.push_prop_int(self._prop_int)
    
    def get_prop_int(self):
        return self._prop_int        

    def push_prop_int(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("tb.simple.SimpleArrayInterface/propInt", value)

    def set_prop_int32(self, value):
        if self._prop_int32 == value:
            return
        self._prop_int32 = value
        self.push_prop_int32(self._prop_int32)
    
    def get_prop_int32(self):
        return self._prop_int32        

    def push_prop_int32(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("tb.simple.SimpleArrayInterface/propInt32", value)

    def set_prop_int64(self, value):
        if self._prop_int64 == value:
            return
        self._prop_int64 = value
        self.push_prop_int64(self._prop_int64)
    
    def get_prop_int64(self):
        return self._prop_int64        

    def push_prop_int64(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("tb.simple.SimpleArrayInterface/propInt64", value)

    def set_prop_float(self, value):
        if self._prop_float == value:
            return
        self._prop_float = value
        self.push_prop_float(self._prop_float)
    
    def get_prop_float(self):
        return self._prop_float        

    def push_prop_float(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("tb.simple.SimpleArrayInterface/propFloat", value)

    def set_prop_float32(self, value):
        if self._prop_float32 == value:
            return
        self._prop_float32 = value
        self.push_prop_float32(self._prop_float32)
    
    def get_prop_float32(self):
        return self._prop_float32        

    def push_prop_float32(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("tb.simple.SimpleArrayInterface/propFloat32", value)

    def set_prop_float64(self, value):
        if self._prop_float64 == value:
            return
        self._prop_float64 = value
        self.push_prop_float64(self._prop_float64)
    
    def get_prop_float64(self):
        return self._prop_float64        

    def push_prop_float64(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("tb.simple.SimpleArrayInterface/propFloat64", value)

    def set_prop_string(self, value):
        if self._prop_string == value:
            return
        self._prop_string = value
        self.push_prop_string(self._prop_string)
    
    def get_prop_string(self):
        return self._prop_string        

    def push_prop_string(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("tb.simple.SimpleArrayInterface/propString", value)

    def func_bool(self, param_bool: list[bool]) -> list[bool]:
        return []

    def func_int(self, param_int: list[int]) -> list[int]:
        return []

    def func_int32(self, param_int32: list[int]) -> list[int]:
        return []

    def func_int64(self, param_int64: list[int]) -> list[int]:
        return []

    def func_float(self, param_float: list[float]) -> list[float]:
        return []

    def func_float32(self, param_float32: list[float]) -> list[float]:
        return []

    def func_float64(self, param_float: list[float]) -> list[float]:
        return []

    def func_string(self, param_string: list[str]) -> list[str]:
        return []

    def sig_bool(self, param_bool: list[bool]):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.simple.SimpleArrayInterface/sigBool", [param_bool])

    def sig_int(self, param_int: list[int]):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.simple.SimpleArrayInterface/sigInt", [param_int])

    def sig_int32(self, param_int32: list[int]):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.simple.SimpleArrayInterface/sigInt32", [param_int32])

    def sig_int64(self, param_int64: list[int]):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.simple.SimpleArrayInterface/sigInt64", [param_int64])

    def sig_float(self, param_float: list[float]):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.simple.SimpleArrayInterface/sigFloat", [param_float])

    def sig_float32(self, param_float32: list[float]):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.simple.SimpleArrayInterface/sigFloat32", [param_float32])

    def sig_float64(self, param_float64: list[float]):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.simple.SimpleArrayInterface/sigFloat64", [param_float64])

    def sig_string(self, param_string: list[str]):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.simple.SimpleArrayInterface/sigString", [param_string])
