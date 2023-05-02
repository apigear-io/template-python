import requests
import os

from tb_empty_api import api
from . import shared



class EmptyInterface(api.IEmptyInterface):
    def __init__(self, url='http://localhost:8000'):
        super().__init__()
        self._url = url
