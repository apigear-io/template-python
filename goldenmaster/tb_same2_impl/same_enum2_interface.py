from tb_same2_api import api
from typing import Iterable

class SameEnum2Interface(api.ISameEnum2Interface):
    def __init__(self, notifier=None):
        super().__init__()
        self._notifier = notifier
        self._prop1: api.Enum1 = api.Enum1.VALUE1
        self._prop2: api.Enum2 = api.Enum2.VALUE1

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        self._prop1 = value
    
    def get_prop1(self):
        return self._prop1        

    def push_prop1(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("tb.same2.SameEnum2Interface/prop1", value)

    def set_prop2(self, value):
        if self._prop2 == value:
            return
        self._prop2 = value
    
    def get_prop2(self):
        return self._prop2        

    def push_prop2(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("tb.same2.SameEnum2Interface/prop2", value)

    def func1(self, param1: api.Enum1) -> api.Enum1:
        return api.Enum1.VALUE1

    def func2(self, param1: api.Enum1, param2: api.Enum2) -> api.Enum1:
        return api.Enum1.VALUE1

    def sig1(self, param1: api.Enum1):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.same2.SameEnum2Interface/sig1", [param1])

    def sig2(self, param1: api.Enum1, param2: api.Enum2):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.same2.SameEnum2Interface/sig2", [param1, param2])
