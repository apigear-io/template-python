from tb_simple_api import api
from typing import Iterable

class EmptyInterface(api.IEmptyInterface):
    def __init__(self, notifier=None):
        super().__init__()
        self._notifier = notifier