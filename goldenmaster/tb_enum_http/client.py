import requests
import os

from tb_enum_api import api
from . import shared



class EnumInterface(api.IEnumInterface):
    def __init__(self, url='http://localhost:8000'):
        super().__init__()
        self._url = url        
        self._prop0 = api.Enum0.VALUE0        
        self._prop1 = api.Enum1.VALUE1        
        self._prop2 = api.Enum2.VALUE2        
        self._prop3 = api.Enum3.VALUE3
    
    def get_prop0(self):
        return self._prop0

    def set_prop0(self, value):
        self._prop0 = value
    
    def get_prop1(self):
        return self._prop1

    def set_prop1(self, value):
        self._prop1 = value
    
    def get_prop2(self):
        return self._prop2

    def set_prop2(self, value):
        self._prop2 = value
    
    def get_prop3(self):
        return self._prop3

    def set_prop3(self, value):
        self._prop3 = value

    def func0(self, param0: api.Enum0):
        req = shared.EnumInterfaceFunc0Request(
            param0=param0
        )
        data = requests.post(
            f'{self.url}/tb_enum/enum_interface/func0',
            req.json()
        )
        resp = shared.EnumInterfaceFunc0Response(**data.json())
        self._prop0 = resp.state.prop0
        self._prop1 = resp.state.prop1
        self._prop2 = resp.state.prop2
        self._prop3 = resp.state.prop3

    def func1(self, param1: api.Enum1):
        req = shared.EnumInterfaceFunc1Request(
            param1=param1
        )
        data = requests.post(
            f'{self.url}/tb_enum/enum_interface/func1',
            req.json()
        )
        resp = shared.EnumInterfaceFunc1Response(**data.json())
        self._prop0 = resp.state.prop0
        self._prop1 = resp.state.prop1
        self._prop2 = resp.state.prop2
        self._prop3 = resp.state.prop3

    def func2(self, param2: api.Enum2):
        req = shared.EnumInterfaceFunc2Request(
            param2=param2
        )
        data = requests.post(
            f'{self.url}/tb_enum/enum_interface/func2',
            req.json()
        )
        resp = shared.EnumInterfaceFunc2Response(**data.json())
        self._prop0 = resp.state.prop0
        self._prop1 = resp.state.prop1
        self._prop2 = resp.state.prop2
        self._prop3 = resp.state.prop3

    def func3(self, param3: api.Enum3):
        req = shared.EnumInterfaceFunc3Request(
            param3=param3
        )
        data = requests.post(
            f'{self.url}/tb_enum/enum_interface/func3',
            req.json()
        )
        resp = shared.EnumInterfaceFunc3Response(**data.json())
        self._prop0 = resp.state.prop0
        self._prop1 = resp.state.prop1
        self._prop2 = resp.state.prop2
        self._prop3 = resp.state.prop3
