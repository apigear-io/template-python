from tb_empty_api import api
from tb_empty_api.shared import EventHook
from typing import Iterable

class EmptyInterface(api.IEmptyInterface):
    def __init__(self):
        super().__init__()
