from tb_simple_api import api
from typing import Iterable

class SimpleInterface(api.ISimpleInterface):
    def __init__(self, notifier=None):
        super().__init__()
        self._notifier = notifier
        self._prop_bool: bool = False
        self._prop_int: int = 0
        self._prop_int32: int = 0
        self._prop_int64: int = 0
        self._prop_float: float = 0.0
        self._prop_float32: float = 0.0
        self._prop_float64: float = 0.0
        self._prop_string: str = ""
        self._prop_read_only_string: str = ""

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
        self._notifier.notify_property("tb.simple.SimpleInterface/propBool", value)

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
        self._notifier.notify_property("tb.simple.SimpleInterface/propInt", value)

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
        self._notifier.notify_property("tb.simple.SimpleInterface/propInt32", value)

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
        self._notifier.notify_property("tb.simple.SimpleInterface/propInt64", value)

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
        self._notifier.notify_property("tb.simple.SimpleInterface/propFloat", value)

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
        self._notifier.notify_property("tb.simple.SimpleInterface/propFloat32", value)

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
        self._notifier.notify_property("tb.simple.SimpleInterface/propFloat64", value)

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
        self._notifier.notify_property("tb.simple.SimpleInterface/propString", value)
    
    def get_prop_read_only_string(self):
        return self._prop_read_only_string        

    def push_prop_read_only_string(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("tb.simple.SimpleInterface/propReadOnlyString", value)

    def func_void(self) -> None:
        return None

    def func_bool(self, param_bool: bool) -> bool:
        return False

    def func_int(self, param_int: int) -> int:
        return 0

    def func_int32(self, param_int32: int) -> int:
        return 0

    def func_int64(self, param_int64: int) -> int:
        return 0

    def func_float(self, param_float: float) -> float:
        return 0.0

    def func_float32(self, param_float32: float) -> float:
        return 0.0

    def func_float64(self, param_float: float) -> float:
        return 0.0

    def func_string(self, param_string: str) -> str:
        return ""

    def sig_void(self):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.simple.SimpleInterface/sigVoid", [])

    def sig_bool(self, param_bool: bool):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.simple.SimpleInterface/sigBool", [param_bool])

    def sig_int(self, param_int: int):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.simple.SimpleInterface/sigInt", [param_int])

    def sig_int32(self, param_int32: int):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.simple.SimpleInterface/sigInt32", [param_int32])

    def sig_int64(self, param_int64: int):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.simple.SimpleInterface/sigInt64", [param_int64])

    def sig_float(self, param_float: float):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.simple.SimpleInterface/sigFloat", [param_float])

    def sig_float32(self, param_float32: float):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.simple.SimpleInterface/sigFloat32", [param_float32])

    def sig_float64(self, param_float64: float):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.simple.SimpleInterface/sigFloat64", [param_float64])

    def sig_string(self, param_string: str):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.simple.SimpleInterface/sigString", [param_string])
