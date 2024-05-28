from testbed2_api import api
from utils.eventhook import EventHook
from typing import Iterable

class NestedStruct3Interface(api.INestedStruct3Interface):
    def __init__(self):
        super().__init__()
        self._prop1: api.NestedStruct1 = api.NestedStruct1()
        self._prop2: api.NestedStruct2 = api.NestedStruct2()
        self._prop3: api.NestedStruct3 = api.NestedStruct3()
        self.on_prop1_changed: api.NestedStruct1 = EventHook()
        self.on_prop2_changed: api.NestedStruct2 = EventHook()
        self.on_prop3_changed: api.NestedStruct3 = EventHook()
        self.on_sig1 = EventHook()
        self.on_sig2 = EventHook()
        self.on_sig3 = EventHook()

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        self._prop1 = value
        self._push_prop1(self._prop1)
    
    def get_prop1(self):
        return self._prop1        

    def _push_prop1(self, value):
        self.on_prop1_changed.fire(value)

    def set_prop2(self, value):
        if self._prop2 == value:
            return
        self._prop2 = value
        self._push_prop2(self._prop2)
    
    def get_prop2(self):
        return self._prop2        

    def _push_prop2(self, value):
        self.on_prop2_changed.fire(value)

    def set_prop3(self, value):
        if self._prop3 == value:
            return
        self._prop3 = value
        self._push_prop3(self._prop3)
    
    def get_prop3(self):
        return self._prop3        

    def _push_prop3(self, value):
        self.on_prop3_changed.fire(value)

    def func1(self, param1: api.NestedStruct1) -> api.NestedStruct1:
        return api.NestedStruct1()

    def func2(self, param1: api.NestedStruct1, param2: api.NestedStruct2) -> api.NestedStruct1:
        return api.NestedStruct1()

    def func3(self, param1: api.NestedStruct1, param2: api.NestedStruct2, param3: api.NestedStruct3) -> api.NestedStruct1:
        return api.NestedStruct1()

    def _sig1(self, param1: api.NestedStruct1):
        self.on_sig1.fire(param1)

    def _sig2(self, param1: api.NestedStruct1, param2: api.NestedStruct2):
        self.on_sig2.fire(param1, param2)

    def _sig3(self, param1: api.NestedStruct1, param2: api.NestedStruct2, param3: api.NestedStruct3):
        self.on_sig3.fire(param1, param2, param3)
