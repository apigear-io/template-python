from tb_same2_api import api
from tb_same2_api.shared import EventHook
from typing import Iterable

class SameStruct2Interface(api.ISameStruct2Interface):
    def __init__(self, notifier=None):
        super().__init__()
        self._notifier = notifier
        self._prop1: api.Struct2 = api.Struct2()
        self._prop2: api.Struct2 = api.Struct2()
        self.on_sig1 = EventHook()
        self.on_sig2 = EventHook()

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
        self._notifier.notify_property("tb.same2.SameStruct2Interface/prop1", value)

    def set_prop2(self, value):
        if self._prop2 == value:
            return
        self._prop2 = value
        self.push_prop2(self._prop2)
    
    def get_prop2(self):
        return self._prop2        

    def push_prop2(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("tb.same2.SameStruct2Interface/prop2", value)

    def func1(self, param1: api.Struct1) -> api.Struct1:
        return api.Struct1()

    def func2(self, param1: api.Struct1, param2: api.Struct2) -> api.Struct1:
        return api.Struct1()

    def _sig1(self, param1: api.Struct1):
        self.on_sig1.fire(param1)

    def _sig2(self, param1: api.Struct1, param2: api.Struct2):
        self.on_sig2.fire(param1, param2)
