from tb_enum_api import api
from typing import Iterable

class EnumInterface(api.IEnumInterface):
    def __init__(self, notifier=None):
        super().__init__()
        self._notifier = notifier
        self._prop0: api.Enum0 = api.Enum0.VALUE0
        self._prop1: api.Enum1 = api.Enum1.VALUE1
        self._prop2: api.Enum2 = api.Enum2.VALUE2
        self._prop3: api.Enum3 = api.Enum3.VALUE3

    def set_prop0(self, value):
        if self._prop0 == value:
            return
        self._prop0 = value
        self.push_prop0(self._prop0)
    
    def get_prop0(self):
        return self._prop0        

    def push_prop0(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("tb.enum.EnumInterface/prop0", value)

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
        self._notifier.notify_property("tb.enum.EnumInterface/prop1", value)

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
        self._notifier.notify_property("tb.enum.EnumInterface/prop2", value)

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
        self._notifier.notify_property("tb.enum.EnumInterface/prop3", value)

    def func0(self, param0: api.Enum0) -> api.Enum0:
        return api.Enum0.VALUE0

    def func1(self, param1: api.Enum1) -> api.Enum1:
        return api.Enum1.VALUE1

    def func2(self, param2: api.Enum2) -> api.Enum2:
        return api.Enum2.VALUE2

    def func3(self, param3: api.Enum3) -> api.Enum3:
        return api.Enum3.VALUE3

    def sig0(self, param0: api.Enum0):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.enum.EnumInterface/sig0", [param0])

    def sig1(self, param1: api.Enum1):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.enum.EnumInterface/sig1", [param1])

    def sig2(self, param2: api.Enum2):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.enum.EnumInterface/sig2", [param2])

    def sig3(self, param3: api.Enum3):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.enum.EnumInterface/sig3", [param3])
