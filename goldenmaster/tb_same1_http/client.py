import requests
import os

from tb_same1_api import api
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
    def func1(self, param1: Struct1):
        req = shared.SameStruct1InterfaceFunc1Request(
            param1=param1
        )
        data = requests.post(
            f'{self.url}/tb.same1/SameStruct1Interface/func1',
            req.json()
        )
        resp = shared.SameStruct1InterfaceFunc1Response(**data.json())
        print(resp.json())
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
    def func1(self, param1: Struct1):
        req = shared.SameStruct2InterfaceFunc1Request(
            param1=param1
        )
        data = requests.post(
            f'{self.url}/tb.same1/SameStruct2Interface/func1',
            req.json()
        )
        resp = shared.SameStruct2InterfaceFunc1Response(**data.json())
        print(resp.json())
        self._prop1 = resp.state.prop1
        self._prop2 = resp.state.prop2
    def func2(self, param1: Struct1, param2: Struct2):
        req = shared.SameStruct2InterfaceFunc2Request(
            param1=param1
            , param2=param2
        )
        data = requests.post(
            f'{self.url}/tb.same1/SameStruct2Interface/func2',
            req.json()
        )
        resp = shared.SameStruct2InterfaceFunc2Response(**data.json())
        print(resp.json())
        self._prop1 = resp.state.prop1
        self._prop2 = resp.state.prop2

class SameEnum1Interface(api.ISameEnum1Interface):
    def __init__(self, url='http://localhost:8000'):
        super().__init__()
        self._url = url        
        self._prop1 = Enum1.value1
    
    def get_prop1(self):
        return self._prop1

    def set_prop1(self, value):
        self._prop1 = value
    def func1(self, param1: Enum1):
        req = shared.SameEnum1InterfaceFunc1Request(
            param1=param1
        )
        data = requests.post(
            f'{self.url}/tb.same1/SameEnum1Interface/func1',
            req.json()
        )
        resp = shared.SameEnum1InterfaceFunc1Response(**data.json())
        print(resp.json())
        self._prop1 = resp.state.prop1

class SameEnum2Interface(api.ISameEnum2Interface):
    def __init__(self, url='http://localhost:8000'):
        super().__init__()
        self._url = url        
        self._prop1 = Enum1.value1        
        self._prop2 = Enum2.value1
    
    def get_prop1(self):
        return self._prop1

    def set_prop1(self, value):
        self._prop1 = value
    
    def get_prop2(self):
        return self._prop2

    def set_prop2(self, value):
        self._prop2 = value
    def func1(self, param1: Enum1):
        req = shared.SameEnum2InterfaceFunc1Request(
            param1=param1
        )
        data = requests.post(
            f'{self.url}/tb.same1/SameEnum2Interface/func1',
            req.json()
        )
        resp = shared.SameEnum2InterfaceFunc1Response(**data.json())
        print(resp.json())
        self._prop1 = resp.state.prop1
        self._prop2 = resp.state.prop2
    def func2(self, param1: Enum1, param2: Enum2):
        req = shared.SameEnum2InterfaceFunc2Request(
            param1=param1
            , param2=param2
        )
        data = requests.post(
            f'{self.url}/tb.same1/SameEnum2Interface/func2',
            req.json()
        )
        resp = shared.SameEnum2InterfaceFunc2Response(**data.json())
        print(resp.json())
        self._prop1 = resp.state.prop1
        self._prop2 = resp.state.prop2
