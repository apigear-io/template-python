from testbed2_api import api
from typing import Iterable

class ManyParamInterface(api.IManyParamInterface):
    def __init__(self, notifier=None):
        super().__init__()
        self._notifier = notifier
        self._prop1: int = 0
        self._prop2: int = 0
        self._prop3: int = 0
        self._prop4: int = 0

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        self._prop1 = value
    
    def get_prop1(self):
        return self._prop1        

    def push_prop1(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("testbed2.ManyParamInterface/prop1", value)

    def set_prop2(self, value):
        if self._prop2 == value:
            return
        self._prop2 = value
    
    def get_prop2(self):
        return self._prop2        

    def push_prop2(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("testbed2.ManyParamInterface/prop2", value)

    def set_prop3(self, value):
        if self._prop3 == value:
            return
        self._prop3 = value
    
    def get_prop3(self):
        return self._prop3        

    def push_prop3(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("testbed2.ManyParamInterface/prop3", value)

    def set_prop4(self, value):
        if self._prop4 == value:
            return
        self._prop4 = value
    
    def get_prop4(self):
        return self._prop4        

    def push_prop4(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("testbed2.ManyParamInterface/prop4", value)

    def func1(self, param1: int) -> int:
        return 0

    def func2(self, param1: int, param2: int) -> int:
        return 0

    def func3(self, param1: int, param2: int, param3: int) -> int:
        return 0

    def func4(self, param1: int, param2: int, param3: int, param4: int) -> int:
        return 0

    def sig1(self, param1: int):
        if not self._notifier:
            return
        self._notifier.notify_signal("testbed2.ManyParamInterface/sig1", [param1])

    def sig2(self, param1: int, param2: int):
        if not self._notifier:
            return
        self._notifier.notify_signal("testbed2.ManyParamInterface/sig2", [param1, param2])

    def sig3(self, param1: int, param2: int, param3: int):
        if not self._notifier:
            return
        self._notifier.notify_signal("testbed2.ManyParamInterface/sig3", [param1, param2, param3])

    def sig4(self, param1: int, param2: int, param3: int, param4: int):
        if not self._notifier:
            return
        self._notifier.notify_signal("testbed2.ManyParamInterface/sig4", [param1, param2, param3, param4])
