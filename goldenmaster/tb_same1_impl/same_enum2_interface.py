from tb_same1_api import api
from tb_same1_api.shared import EventHook
from typing import Iterable

class SameEnum2Interface(api.ISameEnum2Interface):
    def __init__(self):
        super().__init__()
        self._prop1: api.Enum1 = api.Enum1.VALUE1
        self._prop2: api.Enum2 = api.Enum2.VALUE1
        self.on_prop1_changed: api.Enum1 = EventHook()
        self.on_prop2_changed: api.Enum2 = EventHook()
        self.on_sig1 = EventHook()
        self.on_sig2 = EventHook()

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

    def func1(self, param1: api.Enum1) -> api.Enum1:
        return api.Enum1.VALUE1

    def func2(self, param1: api.Enum1, param2: api.Enum2) -> api.Enum1:
        return api.Enum1.VALUE1

    def _sig1(self, param1: api.Enum1):
        self.on_sig1.fire(param1)

    def _sig2(self, param1: api.Enum1, param2: api.Enum2):
        self.on_sig2.fire(param1, param2)
