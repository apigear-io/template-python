from testbed1_api import api
from testbed1_api.shared import EventHook
from typing import Iterable

class StructArrayInterface(api.IStructArrayInterface):
    def __init__(self):
        super().__init__()
        self._prop_bool: list[api.StructBool] = []
        self._prop_int: list[api.StructInt] = []
        self._prop_float: list[api.StructFloat] = []
        self._prop_string: list[api.StructString] = []
        self.on_prop_bool_changed: list[api.StructBool] = EventHook()
        self.on_prop_int_changed: list[api.StructInt] = EventHook()
        self.on_prop_float_changed: list[api.StructFloat] = EventHook()
        self.on_prop_string_changed: list[api.StructString] = EventHook()
        self.on_sig_bool = EventHook()
        self.on_sig_int = EventHook()
        self.on_sig_float = EventHook()
        self.on_sig_string = EventHook()

    def set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        self._prop_bool = value
        self._push_prop_bool(self._prop_bool)
    
    def get_prop_bool(self):
        return self._prop_bool        

    def _push_prop_bool(self, value):
        self.on_prop_bool_changed.fire(value)

    def set_prop_int(self, value):
        if self._prop_int == value:
            return
        self._prop_int = value
        self._push_prop_int(self._prop_int)
    
    def get_prop_int(self):
        return self._prop_int        

    def _push_prop_int(self, value):
        self.on_prop_int_changed.fire(value)

    def set_prop_float(self, value):
        if self._prop_float == value:
            return
        self._prop_float = value
        self._push_prop_float(self._prop_float)
    
    def get_prop_float(self):
        return self._prop_float        

    def _push_prop_float(self, value):
        self.on_prop_float_changed.fire(value)

    def set_prop_string(self, value):
        if self._prop_string == value:
            return
        self._prop_string = value
        self._push_prop_string(self._prop_string)
    
    def get_prop_string(self):
        return self._prop_string        

    def _push_prop_string(self, value):
        self.on_prop_string_changed.fire(value)

    def func_bool(self, param_bool: list[api.StructBool]) -> api.StructBool:
        return api.StructBool()

    def func_int(self, param_int: list[api.StructInt]) -> api.StructBool:
        return api.StructBool()

    def func_float(self, param_float: list[api.StructFloat]) -> api.StructBool:
        return api.StructBool()

    def func_string(self, param_string: list[api.StructString]) -> api.StructBool:
        return api.StructBool()

    def _sig_bool(self, param_bool: list[api.StructBool]):
        self.on_sig_bool.fire(param_bool)

    def _sig_int(self, param_int: list[api.StructInt]):
        self.on_sig_int.fire(param_int)

    def _sig_float(self, param_float: list[api.StructFloat]):
        self.on_sig_float.fire(param_float)

    def _sig_string(self, param_string: list[api.StructString]):
        self.on_sig_string.fire(param_string)
