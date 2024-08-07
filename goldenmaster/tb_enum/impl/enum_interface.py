from tb_enum.api import api
from utils.eventhook import EventHook
from typing import Iterable

class EnumInterface(api.IEnumInterface):
    def __init__(self):
        super().__init__()
        self._prop0: api.Enum0 = api.Enum0.VALUE0
        self._prop1: api.Enum1 = api.Enum1.VALUE1
        self._prop2: api.Enum2 = api.Enum2.VALUE2
        self._prop3: api.Enum3 = api.Enum3.VALUE3
        self.on_prop0_changed: api.Enum0 = EventHook()
        self.on_prop1_changed: api.Enum1 = EventHook()
        self.on_prop2_changed: api.Enum2 = EventHook()
        self.on_prop3_changed: api.Enum3 = EventHook()
        self.on_sig0 = EventHook()
        self.on_sig1 = EventHook()
        self.on_sig2 = EventHook()
        self.on_sig3 = EventHook()

    def set_prop0(self, value):
        if self._prop0 == value:
            return
        self._prop0 = value
        self._push_prop0(self._prop0)
    
    def get_prop0(self):
        return self._prop0        

    def _push_prop0(self, value):
        self.on_prop0_changed.fire(value)

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

    def func0(self, param0: api.Enum0) -> api.Enum0:
        return api.Enum0.VALUE0

    def func1(self, param1: api.Enum1) -> api.Enum1:
        return api.Enum1.VALUE1

    def func2(self, param2: api.Enum2) -> api.Enum2:
        return api.Enum2.VALUE2

    def func3(self, param3: api.Enum3) -> api.Enum3:
        return api.Enum3.VALUE3

    def _sig0(self, param0: api.Enum0):
        self.on_sig0.fire(param0)

    def _sig1(self, param1: api.Enum1):
        self.on_sig1.fire(param1)

    def _sig2(self, param2: api.Enum2):
        self.on_sig2.fire(param2)

    def _sig3(self, param3: api.Enum3):
        self.on_sig3.fire(param3)
