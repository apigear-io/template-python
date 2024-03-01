from tb_simple_api import api
from tb_simple_api.shared import EventHook
from typing import Iterable

class SimpleInterface(api.ISimpleInterface):
    def __init__(self):
        super().__init__()
        self._prop_bool: bool = False
        self._prop_int: int = 0
        self._prop_int32: int = 0
        self._prop_int64: int = 0
        self._prop_float: float = 0.0
        self._prop_float32: float = 0.0
        self._prop_float64: float = 0.0
        self._prop_string: str = ""
        self._prop_read_only_string: str = ""
        self.on_prop_bool_changed: bool = EventHook()
        self.on_prop_int_changed: int = EventHook()
        self.on_prop_int32_changed: int = EventHook()
        self.on_prop_int64_changed: int = EventHook()
        self.on_prop_float_changed: float = EventHook()
        self.on_prop_float32_changed: float = EventHook()
        self.on_prop_float64_changed: float = EventHook()
        self.on_prop_string_changed: str = EventHook()
        self.on_prop_read_only_string_changed: str = EventHook()
        self.on_sig_void = EventHook()
        self.on_sig_bool = EventHook()
        self.on_sig_int = EventHook()
        self.on_sig_int32 = EventHook()
        self.on_sig_int64 = EventHook()
        self.on_sig_float = EventHook()
        self.on_sig_float32 = EventHook()
        self.on_sig_float64 = EventHook()
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

    def set_prop_int32(self, value):
        if self._prop_int32 == value:
            return
        self._prop_int32 = value
        self._push_prop_int32(self._prop_int32)
    
    def get_prop_int32(self):
        return self._prop_int32        

    def _push_prop_int32(self, value):
        self.on_prop_int32_changed.fire(value)

    def set_prop_int64(self, value):
        if self._prop_int64 == value:
            return
        self._prop_int64 = value
        self._push_prop_int64(self._prop_int64)
    
    def get_prop_int64(self):
        return self._prop_int64        

    def _push_prop_int64(self, value):
        self.on_prop_int64_changed.fire(value)

    def set_prop_float(self, value):
        if self._prop_float == value:
            return
        self._prop_float = value
        self._push_prop_float(self._prop_float)
    
    def get_prop_float(self):
        return self._prop_float        

    def _push_prop_float(self, value):
        self.on_prop_float_changed.fire(value)

    def set_prop_float32(self, value):
        if self._prop_float32 == value:
            return
        self._prop_float32 = value
        self._push_prop_float32(self._prop_float32)
    
    def get_prop_float32(self):
        return self._prop_float32        

    def _push_prop_float32(self, value):
        self.on_prop_float32_changed.fire(value)

    def set_prop_float64(self, value):
        if self._prop_float64 == value:
            return
        self._prop_float64 = value
        self._push_prop_float64(self._prop_float64)
    
    def get_prop_float64(self):
        return self._prop_float64        

    def _push_prop_float64(self, value):
        self.on_prop_float64_changed.fire(value)

    def set_prop_string(self, value):
        if self._prop_string == value:
            return
        self._prop_string = value
        self._push_prop_string(self._prop_string)
    
    def get_prop_string(self):
        return self._prop_string        

    def _push_prop_string(self, value):
        self.on_prop_string_changed.fire(value)
    
    def get_prop_read_only_string(self):
        return self._prop_read_only_string        

    def _push_prop_read_only_string(self, value):
        self.on_prop_read_only_string_changed.fire(value)

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

    def _sig_void(self):
        self.on_sig_void.fire()

    def _sig_bool(self, param_bool: bool):
        self.on_sig_bool.fire(param_bool)

    def _sig_int(self, param_int: int):
        self.on_sig_int.fire(param_int)

    def _sig_int32(self, param_int32: int):
        self.on_sig_int32.fire(param_int32)

    def _sig_int64(self, param_int64: int):
        self.on_sig_int64.fire(param_int64)

    def _sig_float(self, param_float: float):
        self.on_sig_float.fire(param_float)

    def _sig_float32(self, param_float32: float):
        self.on_sig_float32.fire(param_float32)

    def _sig_float64(self, param_float64: float):
        self.on_sig_float64.fire(param_float64)

    def _sig_string(self, param_string: str):
        self.on_sig_string.fire(param_string)
