from tb_simple_api import api
from typing import Iterable

class NoPropertiesInterface(api.INoPropertiesInterface):
    def __init__(self, notifier=None):
        super().__init__()
        self._notifier = notifier

    def func_void(self) -> None:
        return None

    def func_bool(self, param_bool: bool) -> bool:
        return False

    def sig_void(self):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.simple.NoPropertiesInterface/sigVoid", [])

    def sig_bool(self, param_bool: bool):
        if not self._notifier:
            return
        self._notifier.notify_signal("tb.simple.NoPropertiesInterface/sigBool", [param_bool])
