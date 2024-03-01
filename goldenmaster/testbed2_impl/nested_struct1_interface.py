from testbed2_api import api
from testbed2_api.shared import EventHook
from typing import Iterable

class NestedStruct1Interface(api.INestedStruct1Interface):
    def __init__(self, notifier=None):
        super().__init__()
        self._notifier = notifier
        self._prop1: api.NestedStruct1 = api.NestedStruct1()
        self.on_sig1 = EventHook()

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        self._prop1 = value
        self.push_prop1(self._prop1)
    
    def get_prop1(self):
        return self._prop1        

    def push_prop1(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("testbed2.NestedStruct1Interface/prop1", value)

    def func1(self, param1: api.NestedStruct1) -> api.NestedStruct1:
        return api.NestedStruct1()

    def _sig1(self, param1: api.NestedStruct1):
        self.on_sig1.fire(param1)
