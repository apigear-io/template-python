from tb_same1_api import api
from typing import Iterable

class SameEnum1Interface(api.ISameEnum1Interface):
    def __init__(self, notifier=None):
        super().__init__()
        self._notifier = notifier
        self._prop1: api.Enum1 = api.Enum1.value1

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        self._prop1 = value
    
    def get_prop1(self):
        return self._prop1        

    def push_prop1(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("tb.same1.SameEnum1Interface/prop1", value)

    def func1(self, param1: api.Enum1) -> api.Enum1:
        raise NotImplementedError()

    def sig1(self, param1: api.Enum1):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.same1.SameEnum1Interface/sig1", [param1])
