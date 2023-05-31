from tb_simple_api import api
from typing import Iterable

class SimpleInterface(api.ISimpleInterface):
    def __init__(self, notifier=None):
        super().__init__()
        self._notifier = notifier
        self._prop_bool: bool = False
        self._prop_int: int = 0
        self._prop_float: float = 0.0
        self._prop_string: str = ""

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

    def func_bool(self, param_bool: bool) -> bool:
        return False

    def func_int(self, param_int: int) -> int:
        return 0

    def func_float(self, param_float: float) -> float:
        return 0.0

    def func_string(self, param_string: str) -> str:
        return ""

    def sig_bool(self, param_bool: bool):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.simple.SimpleInterface/sigBool", [param_bool])

    def sig_int(self, param_int: int):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.simple.SimpleInterface/sigInt", [param_int])

    def sig_float(self, param_float: float):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.simple.SimpleInterface/sigFloat", [param_float])

    def sig_string(self, param_string: str):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.simple.SimpleInterface/sigString", [param_string])
