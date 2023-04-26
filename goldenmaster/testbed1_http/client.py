import requests
import os

from testbed1_api import api
from . import shared



class StructInterface(api.IStructInterface):
    def __init__(self, url='http://localhost:8000'):
        super().__init__()
        self._url = url        
        self._prop_bool = {}        
        self._prop_int = {}        
        self._prop_float = {}        
        self._prop_string = {}
    
    def get_prop_bool(self):
        return self._prop_bool

    def set_prop_bool(self, value):
        self._prop_bool = value
    
    def get_prop_int(self):
        return self._prop_int

    def set_prop_int(self, value):
        self._prop_int = value
    
    def get_prop_float(self):
        return self._prop_float

    def set_prop_float(self, value):
        self._prop_float = value
    
    def get_prop_string(self):
        return self._prop_string

    def set_prop_string(self, value):
        self._prop_string = value
    def func_bool(self, param_bool: StructBool):
        req = shared.StructInterfaceFuncBoolRequest(
            paramBool=paramBool
        )
        data = requests.post(
            f'{self.url}/testbed1/StructInterface/funcBool',
            req.json()
        )
        resp = shared.StructInterfaceFuncBoolResponse(**data.json())
        print(resp.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_float = resp.state.prop_float
        self._prop_string = resp.state.prop_string
    def func_int(self, param_int: StructInt):
        req = shared.StructInterfaceFuncIntRequest(
            paramInt=paramInt
        )
        data = requests.post(
            f'{self.url}/testbed1/StructInterface/funcInt',
            req.json()
        )
        resp = shared.StructInterfaceFuncIntResponse(**data.json())
        print(resp.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_float = resp.state.prop_float
        self._prop_string = resp.state.prop_string
    def func_float(self, param_float: StructFloat):
        req = shared.StructInterfaceFuncFloatRequest(
            paramFloat=paramFloat
        )
        data = requests.post(
            f'{self.url}/testbed1/StructInterface/funcFloat',
            req.json()
        )
        resp = shared.StructInterfaceFuncFloatResponse(**data.json())
        print(resp.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_float = resp.state.prop_float
        self._prop_string = resp.state.prop_string
    def func_string(self, param_string: StructString):
        req = shared.StructInterfaceFuncStringRequest(
            paramString=paramString
        )
        data = requests.post(
            f'{self.url}/testbed1/StructInterface/funcString',
            req.json()
        )
        resp = shared.StructInterfaceFuncStringResponse(**data.json())
        print(resp.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_float = resp.state.prop_float
        self._prop_string = resp.state.prop_string

class StructArrayInterface(api.IStructArrayInterface):
    def __init__(self, url='http://localhost:8000'):
        super().__init__()
        self._url = url        
        self._prop_bool = []        
        self._prop_int = []        
        self._prop_float = []        
        self._prop_string = []
    
    def get_prop_bool(self):
        return self._prop_bool

    def set_prop_bool(self, value):
        self._prop_bool = value
    
    def get_prop_int(self):
        return self._prop_int

    def set_prop_int(self, value):
        self._prop_int = value
    
    def get_prop_float(self):
        return self._prop_float

    def set_prop_float(self, value):
        self._prop_float = value
    
    def get_prop_string(self):
        return self._prop_string

    def set_prop_string(self, value):
        self._prop_string = value
    def func_bool(self, param_bool: list[StructBool]):
        req = shared.StructArrayInterfaceFuncBoolRequest(
            paramBool=paramBool
        )
        data = requests.post(
            f'{self.url}/testbed1/StructArrayInterface/funcBool',
            req.json()
        )
        resp = shared.StructArrayInterfaceFuncBoolResponse(**data.json())
        print(resp.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_float = resp.state.prop_float
        self._prop_string = resp.state.prop_string
    def func_int(self, param_int: list[StructInt]):
        req = shared.StructArrayInterfaceFuncIntRequest(
            paramInt=paramInt
        )
        data = requests.post(
            f'{self.url}/testbed1/StructArrayInterface/funcInt',
            req.json()
        )
        resp = shared.StructArrayInterfaceFuncIntResponse(**data.json())
        print(resp.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_float = resp.state.prop_float
        self._prop_string = resp.state.prop_string
    def func_float(self, param_float: list[StructFloat]):
        req = shared.StructArrayInterfaceFuncFloatRequest(
            paramFloat=paramFloat
        )
        data = requests.post(
            f'{self.url}/testbed1/StructArrayInterface/funcFloat',
            req.json()
        )
        resp = shared.StructArrayInterfaceFuncFloatResponse(**data.json())
        print(resp.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_float = resp.state.prop_float
        self._prop_string = resp.state.prop_string
    def func_string(self, param_string: list[StructString]):
        req = shared.StructArrayInterfaceFuncStringRequest(
            paramString=paramString
        )
        data = requests.post(
            f'{self.url}/testbed1/StructArrayInterface/funcString',
            req.json()
        )
        resp = shared.StructArrayInterfaceFuncStringResponse(**data.json())
        print(resp.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_float = resp.state.prop_float
        self._prop_string = resp.state.prop_string
