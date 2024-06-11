from tb_simple.api import api
from utils.eventhook import EventHook
from typing import Iterable

class VoidInterface(api.IVoidInterface):
    def __init__(self):
        super().__init__()
        self.on_sig_void = EventHook()

    def func_void(self) -> None:
        return None

    def _sig_void(self):
        self.on_sig_void.fire()
