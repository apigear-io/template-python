from tb_names.api import api
from utils.eventhook import EventHook
from typing import Iterable

class NamEs(api.INamEs):
    def __init__(self):
        super().__init__()
        self._switch: bool = False
        self._some_property: int = 0
        self._some_poperty2: int = 0
        self.on_switch_changed: bool = EventHook()
        self.on_some_property_changed: int = EventHook()
        self.on_some_poperty2_changed: int = EventHook()
        self.on_some_signal = EventHook()
        self.on_some_signal2 = EventHook()

    def set_switch(self, value):
        if self._switch == value:
            return
        self._switch = value
        self._push_switch(self._switch)
    
    def get_switch(self):
        return self._switch        

    def _push_switch(self, value):
        self.on_switch_changed.fire(value)

    def set_some_property(self, value):
        if self._some_property == value:
            return
        self._some_property = value
        self._push_some_property(self._some_property)
    
    def get_some_property(self):
        return self._some_property        

    def _push_some_property(self, value):
        self.on_some_property_changed.fire(value)

    def set_some_poperty2(self, value):
        if self._some_poperty2 == value:
            return
        self._some_poperty2 = value
        self._push_some_poperty2(self._some_poperty2)
    
    def get_some_poperty2(self):
        return self._some_poperty2        

    def _push_some_poperty2(self, value):
        self.on_some_poperty2_changed.fire(value)

    def some_function(self, some_param: bool) -> None:
        return None

    def some_function2(self, some_param: bool) -> None:
        return None

    def _some_signal(self, some_param: bool):
        self.on_some_signal.fire(some_param)

    def _some_signal2(self, some_param: bool):
        self.on_some_signal2.fire(some_param)
