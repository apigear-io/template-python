import requests
import os

from tb.same.api import api
from . import shared


API_SERVER = os.getenv('API_SERVER', 'http://localhost:8000')




class SameStruct1Interface(api.ISameStruct1Interface):
    def __init__(self):
        super().__init__()        
        self._prop1 = {}

    @property
    def prop1(self):
        return self._prop1



class SameStruct2Interface(api.ISameStruct2Interface):
    def __init__(self):
        super().__init__()        
        self._prop1 = {}        
        self._prop2 = {}

    @property
    def prop1(self):
        return self._prop1

    @property
    def prop2(self):
        return self._prop2



class SameEnum1Interface(api.ISameEnum1Interface):
    def __init__(self):
        super().__init__()        
        self._prop1 = Enum1.value1

    @property
    def prop1(self):
        return self._prop1



class SameEnum2Interface(api.ISameEnum2Interface):
    def __init__(self):
        super().__init__()        
        self._prop1 = Enum1.value1        
        self._prop2 = Enum2.value1

    @property
    def prop1(self):
        return self._prop1

    @property
    def prop2(self):
        return self._prop2


