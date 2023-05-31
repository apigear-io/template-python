from testbed1_api import api
from typing import Iterable

class StructInterface(api.IStructInterface):
    def __init__(self, notifier=None):
        super().__init__()
        self._notifier = notifier
        self._prop_bool: api.StructBool = {}
        self._prop_int: api.StructInt = {}
        self._prop_float: api.StructFloat = {}
        self._prop_string: api.StructString = {}

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
        self._notifier.notify_property("testbed1.StructInterface/propBool", value)

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
        self._notifier.notify_property("testbed1.StructInterface/propInt", value)

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
        self._notifier.notify_property("testbed1.StructInterface/propFloat", value)

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
        self._notifier.notify_property("testbed1.StructInterface/propString", value)

    def func_bool(self, param_bool: api.StructBool) -> api.StructBool:
        return {}

    def func_int(self, param_int: api.StructInt) -> api.StructBool:
        return {}

    def func_float(self, param_float: api.StructFloat) -> api.StructFloat:
        return {}

    def func_string(self, param_string: api.StructString) -> api.StructString:
        return {}

    def sig_bool(self, param_bool: api.StructBool):
        if not self._notifier:
            return
        self._notifier.notify_signal("testbed1.StructInterface/sigBool", [param_bool])

    def sig_int(self, param_int: api.StructInt):
        if not self._notifier:
            return
        self._notifier.notify_signal("testbed1.StructInterface/sigInt", [param_int])

    def sig_float(self, param_float: api.StructFloat):
        if not self._notifier:
            return
        self._notifier.notify_signal("testbed1.StructInterface/sigFloat", [param_float])

    def sig_string(self, param_string: api.StructString):
        if not self._notifier:
            return
        self._notifier.notify_signal("testbed1.StructInterface/sigString", [param_string])
