from tb_same2.api import api
from utils.eventhook import EventHook
from typing import Iterable

class SameStruct1Interface(api.ISameStruct1Interface):
    def __init__(self):
        super().__init__()
        self._prop1: api.Struct1 = api.Struct1()
        self.on_prop1_changed: api.Struct1 = EventHook()
        self.on_sig1 = EventHook()

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        self._prop1 = value
        self._push_prop1(self._prop1)
    
    def get_prop1(self):
        return self._prop1        

    def _push_prop1(self, value):
        self.on_prop1_changed.fire(value)

    def func1(self, param1: api.Struct1) -> api.Struct1:
        return api.Struct1()

    def _sig1(self, param1: api.Struct1):
        self.on_sig1.fire(param1)
