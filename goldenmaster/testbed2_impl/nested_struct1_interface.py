from testbed2_api import api
from utils.eventhook import EventHook
from typing import Iterable

class NestedStruct1Interface(api.INestedStruct1Interface):
    def __init__(self):
        super().__init__()
        self._prop1: api.NestedStruct1 = api.NestedStruct1()
        self.on_prop1_changed: api.NestedStruct1 = EventHook()
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

    def func1(self, param1: api.NestedStruct1) -> api.NestedStruct1:
        return api.NestedStruct1()

    def _sig1(self, param1: api.NestedStruct1):
        self.on_sig1.fire(param1)
