from tb_simple_api import api
from tb_simple_api.shared import EventHook
from typing import Iterable

class NoPropertiesInterface(api.INoPropertiesInterface):
    def __init__(self):
        super().__init__()
        self.on_sig_void = EventHook()
        self.on_sig_bool = EventHook()

    def func_void(self) -> None:
        return None

    def func_bool(self, param_bool: bool) -> bool:
        return False

    def _sig_void(self):
        self.on_sig_void.fire()

    def _sig_bool(self, param_bool: bool):
        self.on_sig_bool.fire(param_bool)
