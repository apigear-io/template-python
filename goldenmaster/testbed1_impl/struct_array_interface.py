from testbed1_api import api
from typing import Iterable

class StructArrayInterface(api.IStructArrayInterface):
    def __init__(self, notifier=None):
        super().__init__()
        self._notifier = notifier
        self._prop_bool: list[api.StructBool] = []
        self._prop_int: list[api.StructInt] = []
        self._prop_float: list[api.StructFloat] = []
        self._prop_string: list[api.StructString] = []

    def set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        self._prop_bool = value
    
    def get_prop_bool(self):
        return self._prop_bool        

    def push_prop_bool(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("testbed1.StructArrayInterface/propBool", value)

    def set_prop_int(self, value):
        if self._prop_int == value:
            return
        self._prop_int = value
    
    def get_prop_int(self):
        return self._prop_int        

    def push_prop_int(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("testbed1.StructArrayInterface/propInt", value)

    def set_prop_float(self, value):
        if self._prop_float == value:
            return
        self._prop_float = value
    
    def get_prop_float(self):
        return self._prop_float        

    def push_prop_float(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("testbed1.StructArrayInterface/propFloat", value)

    def set_prop_string(self, value):
        if self._prop_string == value:
            return
        self._prop_string = value
    
    def get_prop_string(self):
        return self._prop_string        

    def push_prop_string(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("testbed1.StructArrayInterface/propString", value)

    def func_bool(self, param_bool: list[api.StructBool]) -> api.StructBool:
        raise NotImplementedError()

    def func_int(self, param_int: list[api.StructInt]) -> api.StructBool:
        raise NotImplementedError()

    def func_float(self, param_float: list[api.StructFloat]) -> api.StructBool:
        raise NotImplementedError()

    def func_string(self, param_string: list[api.StructString]) -> api.StructBool:
        raise NotImplementedError()

    def sig_bool(self, param_bool: list[api.StructBool]):
        if not self._notifier:
            return
        self._notifier.notify_signal("testbed1.StructArrayInterface/sigBool", [param_bool])

    def sig_int(self, param_int: list[api.StructInt]):
        if not self._notifier:
            return
        self._notifier.notify_signal("testbed1.StructArrayInterface/sigInt", [param_int])

    def sig_float(self, param_float: list[api.StructFloat]):
        if not self._notifier:
            return
        self._notifier.notify_signal("testbed1.StructArrayInterface/sigFloat", [param_float])

    def sig_string(self, param_string: list[api.StructString]):
        if not self._notifier:
            return
        self._notifier.notify_signal("testbed1.StructArrayInterface/sigString", [param_string])
