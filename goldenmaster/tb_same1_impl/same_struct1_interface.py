from tb_same1_api import api
from tb_same1_api.shared import EventHook
from typing import Iterable

class SameStruct1Interface(api.ISameStruct1Interface):
    def __init__(self, notifier=None):
        super().__init__()
        self._notifier = notifier
        self._prop1: api.Struct1 = api.Struct1()
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
        self._notifier.notify_property("tb.same1.SameStruct1Interface/prop1", value)

    def func1(self, param1: api.Struct1) -> api.Struct1:
        return api.Struct1()

    def _sig1(self, param1: api.Struct1):
        self.on_sig1.fire(param1)
