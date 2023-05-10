import requests
import os

from tb_same2_api import api
from . import shared



class SameStruct1Interface(api.ISameStruct1Interface):
    def __init__(self, url='http://localhost:8000'):
        super().__init__()
        self._url = url        
        self._prop1 = {}
    
    def get_prop1(self):
        return self._prop1

    def set_prop1(self, value):
        self._prop1 = value

    def func1(self, param1: api.Struct1):
        req = shared.SameStruct1InterfaceFunc1Request(
            param1=param1
        )
        data = requests.post(
            f'{self.url}/tb_same2/same_struct1_interface/func1',
            req.json()
        )
        resp = shared.SameStruct1InterfaceFunc1Response(**data.json())
        self._prop1 = resp.state.prop1

class SameStruct2Interface(api.ISameStruct2Interface):
    def __init__(self, url='http://localhost:8000'):
        super().__init__()
        self._url = url        
        self._prop1 = {}        
        self._prop2 = {}
    
    def get_prop1(self):
        return self._prop1

    def set_prop1(self, value):
        self._prop1 = value
    
    def get_prop2(self):
        return self._prop2

    def set_prop2(self, value):
        self._prop2 = value

    def func1(self, param1: api.Struct1):
        req = shared.SameStruct2InterfaceFunc1Request(
            param1=param1
        )
        data = requests.post(
            f'{self.url}/tb_same2/same_struct2_interface/func1',
            req.json()
        )
        resp = shared.SameStruct2InterfaceFunc1Response(**data.json())
        self._prop1 = resp.state.prop1
        self._prop2 = resp.state.prop2

    def func2(self, param1: api.Struct1, param2: api.Struct2):
        req = shared.SameStruct2InterfaceFunc2Request(
            param1=param1
            , param2=param2
        )
        data = requests.post(
            f'{self.url}/tb_same2/same_struct2_interface/func2',
            req.json()
        )
        resp = shared.SameStruct2InterfaceFunc2Response(**data.json())
        self._prop1 = resp.state.prop1
        self._prop2 = resp.state.prop2

class SameEnum1Interface(api.ISameEnum1Interface):
    def __init__(self, url='http://localhost:8000'):
        super().__init__()
        self._url = url        
        self._prop1 = api.Enum1.VALUE1
    
    def get_prop1(self):
        return self._prop1

    def set_prop1(self, value):
        self._prop1 = value

    def func1(self, param1: api.Enum1):
        req = shared.SameEnum1InterfaceFunc1Request(
            param1=param1
        )
        data = requests.post(
            f'{self.url}/tb_same2/same_enum1_interface/func1',
            req.json()
        )
        resp = shared.SameEnum1InterfaceFunc1Response(**data.json())
        self._prop1 = resp.state.prop1

class SameEnum2Interface(api.ISameEnum2Interface):
    def __init__(self, url='http://localhost:8000'):
        super().__init__()
        self._url = url        
        self._prop1 = api.Enum1.VALUE1        
        self._prop2 = api.Enum2.VALUE1
    
    def get_prop1(self):
        return self._prop1

    def set_prop1(self, value):
        self._prop1 = value
    
    def get_prop2(self):
        return self._prop2

    def set_prop2(self, value):
        self._prop2 = value

    def func1(self, param1: api.Enum1):
        req = shared.SameEnum2InterfaceFunc1Request(
            param1=param1
        )
        data = requests.post(
            f'{self.url}/tb_same2/same_enum2_interface/func1',
            req.json()
        )
        resp = shared.SameEnum2InterfaceFunc1Response(**data.json())
        self._prop1 = resp.state.prop1
        self._prop2 = resp.state.prop2

    def func2(self, param1: api.Enum1, param2: api.Enum2):
        req = shared.SameEnum2InterfaceFunc2Request(
            param1=param1
            , param2=param2
        )
        data = requests.post(
            f'{self.url}/tb_same2/same_enum2_interface/func2',
            req.json()
        )
        resp = shared.SameEnum2InterfaceFunc2Response(**data.json())
        self._prop1 = resp.state.prop1
        self._prop2 = resp.state.prop2
