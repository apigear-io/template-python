import requests
import os

from tb.conflict.api import api
from . import shared


API_SERVER = os.getenv('API_SERVER', 'http://localhost:8000')




class Conflict1(api.IConflict1):
    def __init__(self):
        super().__init__()        
        self._sameName = 0

    @property
    def sameName(self):
        return self._sameName



class Conflict2(api.IConflict2):
    def __init__(self):
        super().__init__()        
        self._sameName = 0

    @property
    def sameName(self):
        return self._sameName



class Conflict3(api.IConflict3):
    def __init__(self):
        super().__init__()



class Conflict4(api.IConflict4):
    def __init__(self):
        super().__init__()


