from tb_simple_api import api
from tb_simple_api.shared import EventHook
from typing import Iterable

class NoSignalsInterface(api.INoSignalsInterface):
    def __init__(self):
        super().__init__()
        self._prop_bool: bool = False
        self._prop_int: int = 0
        self.on_prop_bool_changed: bool = EventHook()
        self.on_prop_int_changed: int = EventHook()

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

    def func_void(self) -> None:
        return None

    def func_bool(self, param_bool: bool) -> bool:
        return False
