from tb_simple_api import api
from typing import Iterable

class NoOperationsInterface(api.INoOperationsInterface):
    def __init__(self, notifier=None):
        super().__init__()
        self._notifier = notifier
        self._prop_bool: bool = False
        self._prop_int: int = 0

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

    def sig_void(self):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.simple.NoOperationsInterface/sigVoid", [])

    def sig_bool(self, param_bool: bool):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.simple.NoOperationsInterface/sigBool", [param_bool])
