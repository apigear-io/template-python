from tb_simple_api import api
from typing import Iterable

class SimpleArrayInterface(api.ISimpleArrayInterface):
    def __init__(self, notifier=None):
        super().__init__()
        self._notifier = notifier
        self._prop_bool: list[bool] = []
        self._prop_int: list[int] = []
        self._prop_float: list[float] = []
        self._prop_string: list[str] = []

    def set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        self._prop_bool = value
    
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
    
    def get_prop_int(self):
        return self._prop_int        

    def push_prop_int(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("tb.simple.SimpleArrayInterface/propInt", value)

    def set_prop_float(self, value):
        if self._prop_float == value:
            return
        self._prop_float = value
    
    def get_prop_float(self):
        return self._prop_float        

    def push_prop_float(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("tb.simple.SimpleArrayInterface/propFloat", value)

    def set_prop_string(self, value):
        if self._prop_string == value:
            return
        self._prop_string = value
    
    def get_prop_string(self):
        return self._prop_string        

    def push_prop_string(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("tb.simple.SimpleArrayInterface/propString", value)

    def func_bool(self, param_bool: list[bool]) -> list[bool]:
        raise NotImplementedError()

    def func_int(self, param_int: list[int]) -> list[int]:
        raise NotImplementedError()

    def func_float(self, param_float: list[float]) -> list[float]:
        raise NotImplementedError()

    def func_string(self, param_string: list[str]) -> list[str]:
        raise NotImplementedError()

    def sig_bool(self, param_bool: list[bool]):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.simple.SimpleArrayInterface/sigBool", [param_bool])

    def sig_int(self, param_int: list[int]):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.simple.SimpleArrayInterface/sigInt", [param_int])

    def sig_float(self, param_float: list[float]):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.simple.SimpleArrayInterface/sigFloat", [param_float])

    def sig_string(self, param_string: list[str]):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.simple.SimpleArrayInterface/sigString", [param_string])
