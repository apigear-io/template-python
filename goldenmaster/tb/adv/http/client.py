import requests
import os

from tb.adv.api import api
from . import shared


API_SERVER = os.getenv('API_SERVER', 'http://localhost:8000')




class ManyParamInterface(api.IManyParamInterface):
    def __init__(self):
        super().__init__()        
        self._prop1 = 0        
        self._prop2 = 0        
        self._prop3 = 0        
        self._prop4 = 0

    @property
    def prop1(self):
        return self._prop1

    @property
    def prop2(self):
        return self._prop2

    @property
    def prop3(self):
        return self._prop3

    @property
    def prop4(self):
        return self._prop4



class NestedStruct1Interface(api.INestedStruct1Interface):
    def __init__(self):
        super().__init__()        
        self._prop1 = {}

    @property
    def prop1(self):
        return self._prop1



class NestedStruct2Interface(api.INestedStruct2Interface):
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



class NestedStruct3Interface(api.INestedStruct3Interface):
    def __init__(self):
        super().__init__()        
        self._prop1 = {}        
        self._prop2 = {}        
        self._prop3 = {}

    @property
    def prop1(self):
        return self._prop1

    @property
    def prop2(self):
        return self._prop2

    @property
    def prop3(self):
        return self._prop3


