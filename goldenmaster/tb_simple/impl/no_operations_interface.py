from tb_simple.api import api
from utils.eventhook import EventHook
from typing import Iterable

class NoOperationsInterface(api.INoOperationsInterface):
    def __init__(self):
        super().__init__()
        self._prop_bool: bool = False
        self._prop_int: int = 0
        self.on_prop_bool_changed: bool = EventHook()
        self.on_prop_int_changed: int = EventHook()
        self.on_sig_void = EventHook()
        self.on_sig_bool = EventHook()

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

    def _sig_void(self):
        self.on_sig_void.fire()

    def _sig_bool(self, param_bool: bool):
        self.on_sig_bool.fire(param_bool)
