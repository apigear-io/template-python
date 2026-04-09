from testbed1.api import api
from utils.eventhook import EventHook
from typing import Iterable

class StructArray2Interface(api.IStructArray2Interface):
    def __init__(self):
        super().__init__()
        self._prop_bool: api.StructBoolWithArray = api.StructBoolWithArray()
        self._prop_int: api.StructIntWithArray = api.StructIntWithArray()
        self._prop_float: api.StructFloatWithArray = api.StructFloatWithArray()
        self._prop_string: api.StructStringWithArray = api.StructStringWithArray()
        self._prop_enum: api.StructEnumWithArray = api.StructEnumWithArray()
        self.on_prop_bool_changed: api.StructBoolWithArray = EventHook()
        self.on_prop_int_changed: api.StructIntWithArray = EventHook()
        self.on_prop_float_changed: api.StructFloatWithArray = EventHook()
        self.on_prop_string_changed: api.StructStringWithArray = EventHook()
        self.on_prop_enum_changed: api.StructEnumWithArray = EventHook()
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

    def set_prop_enum(self, value):
        if self._prop_enum == value:
            return
        self._prop_enum = value
        self._push_prop_enum(self._prop_enum)
    
    def get_prop_enum(self):
        return self._prop_enum        

    def _push_prop_enum(self, value):
        self.on_prop_enum_changed.fire(value)

    def func_bool(self, param_bool: api.StructBoolWithArray) -> list[api.StructBool]:
        return []

    def func_int(self, param_int: api.StructIntWithArray) -> list[api.StructInt]:
        return []

    def func_float(self, param_float: api.StructFloatWithArray) -> list[api.StructFloat]:
        return []

    def func_string(self, param_string: api.StructStringWithArray) -> list[api.StructString]:
        return []

    def func_enum(self, param_enum: api.StructEnumWithArray) -> list[api.Enum0]:
        return []

    def _sig_bool(self, param_bool: api.StructBoolWithArray):
        self.on_sig_bool.fire(param_bool)

    def _sig_int(self, param_int: api.StructIntWithArray):
        self.on_sig_int.fire(param_int)

    def _sig_float(self, param_float: api.StructFloatWithArray):
        self.on_sig_float.fire(param_float)

    def _sig_string(self, param_string: api.StructStringWithArray):
        self.on_sig_string.fire(param_string)
