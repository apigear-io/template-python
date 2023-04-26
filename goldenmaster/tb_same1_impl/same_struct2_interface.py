from tb_same1_api import api
from typing import Iterable

class SameStruct2Interface(api.ISameStruct2Interface):
    def __init__(self, notifier=None):
        super().__init__()
        self._notifier = notifier
        self._prop1: api.Struct2 = {}
        self._prop2: api.Struct2 = {}

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        self._prop1 = value
    
    def get_prop1(self):
        return self._prop1        

    def push_prop1(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("tb.same1.SameStruct2Interface/prop1", value)

    def set_prop2(self, value):
        if self._prop2 == value:
            return
        self._prop2 = value
    
    def get_prop2(self):
        return self._prop2        

    def push_prop2(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("tb.same1.SameStruct2Interface/prop2", value)

    def func1(self, param1: api.Struct1) -> api.Struct1:
        return {}

    def func2(self, param1: api.Struct1, param2: api.Struct2) -> api.Struct1:
        return {}

    def sig1(self, param1: api.Struct1):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.same1.SameStruct2Interface/sig1", [param1])

    def sig2(self, param1: api.Struct1, param2: api.Struct2):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.same1.SameStruct2Interface/sig2", [param1, param2])
