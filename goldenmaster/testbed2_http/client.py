import requests
import os

from testbed2_api import api
from . import shared



class ManyParamInterface(api.IManyParamInterface):
    def __init__(self, url='http://localhost:8000'):
        super().__init__()
        self._url = url        
        self._prop1 = 0        
        self._prop2 = 0        
        self._prop3 = 0        
        self._prop4 = 0
    
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
    
    def get_prop4(self):
        return self._prop4

    def set_prop4(self, value):
        self._prop4 = value

    def func1(self, param1: int):
        req = shared.ManyParamInterfaceFunc1Request(
            param1=param1
        )
        data = requests.post(
            f'{self.url}/testbed2/many_param_interface/func1',
            req.json()
        )
        resp = shared.ManyParamInterfaceFunc1Response(**data.json())
        self._prop1 = resp.state.prop1
        self._prop2 = resp.state.prop2
        self._prop3 = resp.state.prop3
        self._prop4 = resp.state.prop4

    def func2(self, param1: int, param2: int):
        req = shared.ManyParamInterfaceFunc2Request(
            param1=param1
            , param2=param2
        )
        data = requests.post(
            f'{self.url}/testbed2/many_param_interface/func2',
            req.json()
        )
        resp = shared.ManyParamInterfaceFunc2Response(**data.json())
        self._prop1 = resp.state.prop1
        self._prop2 = resp.state.prop2
        self._prop3 = resp.state.prop3
        self._prop4 = resp.state.prop4

    def func3(self, param1: int, param2: int, param3: int):
        req = shared.ManyParamInterfaceFunc3Request(
            param1=param1
            , param2=param2
            , param3=param3
        )
        data = requests.post(
            f'{self.url}/testbed2/many_param_interface/func3',
            req.json()
        )
        resp = shared.ManyParamInterfaceFunc3Response(**data.json())
        self._prop1 = resp.state.prop1
        self._prop2 = resp.state.prop2
        self._prop3 = resp.state.prop3
        self._prop4 = resp.state.prop4

    def func4(self, param1: int, param2: int, param3: int, param4: int):
        req = shared.ManyParamInterfaceFunc4Request(
            param1=param1
            , param2=param2
            , param3=param3
            , param4=param4
        )
        data = requests.post(
            f'{self.url}/testbed2/many_param_interface/func4',
            req.json()
        )
        resp = shared.ManyParamInterfaceFunc4Response(**data.json())
        self._prop1 = resp.state.prop1
        self._prop2 = resp.state.prop2
        self._prop3 = resp.state.prop3
        self._prop4 = resp.state.prop4

class NestedStruct1Interface(api.INestedStruct1Interface):
    def __init__(self, url='http://localhost:8000'):
        super().__init__()
        self._url = url        
        self._prop1 = {}
    
    def get_prop1(self):
        return self._prop1

    def set_prop1(self, value):
        self._prop1 = value

    def func1(self, param1: api.NestedStruct1):
        req = shared.NestedStruct1InterfaceFunc1Request(
            param1=param1
        )
        data = requests.post(
            f'{self.url}/testbed2/nested_struct1_interface/func1',
            req.json()
        )
        resp = shared.NestedStruct1InterfaceFunc1Response(**data.json())
        self._prop1 = resp.state.prop1

class NestedStruct2Interface(api.INestedStruct2Interface):
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

    def func1(self, param1: api.NestedStruct1):
        req = shared.NestedStruct2InterfaceFunc1Request(
            param1=param1
        )
        data = requests.post(
            f'{self.url}/testbed2/nested_struct2_interface/func1',
            req.json()
        )
        resp = shared.NestedStruct2InterfaceFunc1Response(**data.json())
        self._prop1 = resp.state.prop1
        self._prop2 = resp.state.prop2

    def func2(self, param1: api.NestedStruct1, param2: api.NestedStruct2):
        req = shared.NestedStruct2InterfaceFunc2Request(
            param1=param1
            , param2=param2
        )
        data = requests.post(
            f'{self.url}/testbed2/nested_struct2_interface/func2',
            req.json()
        )
        resp = shared.NestedStruct2InterfaceFunc2Response(**data.json())
        self._prop1 = resp.state.prop1
        self._prop2 = resp.state.prop2

class NestedStruct3Interface(api.INestedStruct3Interface):
    def __init__(self, url='http://localhost:8000'):
        super().__init__()
        self._url = url        
        self._prop1 = {}        
        self._prop2 = {}        
        self._prop3 = {}
    
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

    def func1(self, param1: api.NestedStruct1):
        req = shared.NestedStruct3InterfaceFunc1Request(
            param1=param1
        )
        data = requests.post(
            f'{self.url}/testbed2/nested_struct3_interface/func1',
            req.json()
        )
        resp = shared.NestedStruct3InterfaceFunc1Response(**data.json())
        self._prop1 = resp.state.prop1
        self._prop2 = resp.state.prop2
        self._prop3 = resp.state.prop3

    def func2(self, param1: api.NestedStruct1, param2: api.NestedStruct2):
        req = shared.NestedStruct3InterfaceFunc2Request(
            param1=param1
            , param2=param2
        )
        data = requests.post(
            f'{self.url}/testbed2/nested_struct3_interface/func2',
            req.json()
        )
        resp = shared.NestedStruct3InterfaceFunc2Response(**data.json())
        self._prop1 = resp.state.prop1
        self._prop2 = resp.state.prop2
        self._prop3 = resp.state.prop3

    def func3(self, param1: api.NestedStruct1, param2: api.NestedStruct2, param3: api.NestedStruct3):
        req = shared.NestedStruct3InterfaceFunc3Request(
            param1=param1
            , param2=param2
            , param3=param3
        )
        data = requests.post(
            f'{self.url}/testbed2/nested_struct3_interface/func3',
            req.json()
        )
        resp = shared.NestedStruct3InterfaceFunc3Response(**data.json())
        self._prop1 = resp.state.prop1
        self._prop2 = resp.state.prop2
        self._prop3 = resp.state.prop3
