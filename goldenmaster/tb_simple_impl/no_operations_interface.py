from tb_simple_api import api
from tb_simple_api.shared import EventHook
from typing import Iterable

class NoOperationsInterface(api.INoOperationsInterface):
    def __init__(self, notifier=None):
        super().__init__()
        self._notifier = notifier
        self._prop_bool: bool = False
        self._prop_int: int = 0
        self.on_sig_void = EventHook()
        self.on_sig_bool = EventHook()

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
        self._notifier.notify_property("tb.simple.NoOperationsInterface/propBool", value)

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
        self._notifier.notify_property("tb.simple.NoOperationsInterface/propInt", value)

    def _sig_void(self):
        self.on_sig_void.fire()

    def _sig_bool(self, param_bool: bool):
        self.on_sig_bool.fire(param_bool)
