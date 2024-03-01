from tb_simple_api import api
from tb_simple_api.shared import EventHook
from typing import Iterable

class EmptyInterface(api.IEmptyInterface):
    def __init__(self):
        super().__init__()
