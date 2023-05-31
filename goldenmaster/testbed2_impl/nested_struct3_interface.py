from testbed2_api import api
from typing import Iterable

class NestedStruct3Interface(api.INestedStruct3Interface):
    def __init__(self, notifier=None):
        super().__init__()
        self._notifier = notifier
        self._prop1: api.NestedStruct1 = {}
        self._prop2: api.NestedStruct2 = {}
        self._prop3: api.NestedStruct3 = {}

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
        self._notifier.notify_property("testbed2.NestedStruct3Interface/prop1", value)

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
        self._notifier.notify_property("testbed2.NestedStruct3Interface/prop2", value)

    def set_prop3(self, value):
        if self._prop3 == value:
            return
        self._prop3 = value
        self.push_prop3(self._prop3)
    
    def get_prop3(self):
        return self._prop3        

    def push_prop3(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("testbed2.NestedStruct3Interface/prop3", value)

    def func1(self, param1: api.NestedStruct1) -> api.NestedStruct1:
        return {}

    def func2(self, param1: api.NestedStruct1, param2: api.NestedStruct2) -> api.NestedStruct1:
        return {}

    def func3(self, param1: api.NestedStruct1, param2: api.NestedStruct2, param3: api.NestedStruct3) -> api.NestedStruct1:
        return {}

    def sig1(self, param1: api.NestedStruct1):
        if not self._notifier:
            return
        self._notifier.notify_signal("testbed2.NestedStruct3Interface/sig1", [param1])

    def sig2(self, param1: api.NestedStruct1, param2: api.NestedStruct2):
        if not self._notifier:
            return
        self._notifier.notify_signal("testbed2.NestedStruct3Interface/sig2", [param1, param2])

    def sig3(self, param1: api.NestedStruct1, param2: api.NestedStruct2, param3: api.NestedStruct3):
        if not self._notifier:
            return
        self._notifier.notify_signal("testbed2.NestedStruct3Interface/sig3", [param1, param2, param3])
