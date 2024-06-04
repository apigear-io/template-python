from testbed2.api import api
from utils.eventhook import EventHook
from typing import Iterable

class ManyParamInterface(api.IManyParamInterface):
    def __init__(self):
        super().__init__()
        self._prop1: int = 0
        self._prop2: int = 0
        self._prop3: int = 0
        self._prop4: int = 0
        self.on_prop1_changed: int = EventHook()
        self.on_prop2_changed: int = EventHook()
        self.on_prop3_changed: int = EventHook()
        self.on_prop4_changed: int = EventHook()
        self.on_sig1 = EventHook()
        self.on_sig2 = EventHook()
        self.on_sig3 = EventHook()
        self.on_sig4 = EventHook()

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

    def set_prop4(self, value):
        if self._prop4 == value:
            return
        self._prop4 = value
        self._push_prop4(self._prop4)
    
    def get_prop4(self):
        return self._prop4        

    def _push_prop4(self, value):
        self.on_prop4_changed.fire(value)

    def func1(self, param1: int) -> int:
        return 0

    def func2(self, param1: int, param2: int) -> int:
        return 0

    def func3(self, param1: int, param2: int, param3: int) -> int:
        return 0

    def func4(self, param1: int, param2: int, param3: int, param4: int) -> int:
        return 0

    def _sig1(self, param1: int):
        self.on_sig1.fire(param1)

    def _sig2(self, param1: int, param2: int):
        self.on_sig2.fire(param1, param2)

    def _sig3(self, param1: int, param2: int, param3: int):
        self.on_sig3.fire(param1, param2, param3)

    def _sig4(self, param1: int, param2: int, param3: int, param4: int):
        self.on_sig4.fire(param1, param2, param3, param4)
