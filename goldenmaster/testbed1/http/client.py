import requests
import os

from testbed1.api import api
from . import shared



class StructInterface(api.IStructInterface):
    def __init__(self, url='http://localhost:8000'):
        super().__init__()
        self._url = url        
        self._prop_bool = api.StructBool()        
        self._prop_int = api.StructInt()        
        self._prop_float = api.StructFloat()        
        self._prop_string = api.StructString()
    
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

    def func_bool(self, param_bool: api.StructBool):
        req = shared.StructInterfaceFuncBoolRequest(
            param_bool=param_bool
        )
        data = requests.post(
            f'{self.url}/testbed1/struct_interface/func_bool',
            req.json()
        )
        resp = shared.StructInterfaceFuncBoolResponse(**data.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_float = resp.state.prop_float
        self._prop_string = resp.state.prop_string

    def func_int(self, param_int: api.StructInt):
        req = shared.StructInterfaceFuncIntRequest(
            param_int=param_int
        )
        data = requests.post(
            f'{self.url}/testbed1/struct_interface/func_int',
            req.json()
        )
        resp = shared.StructInterfaceFuncIntResponse(**data.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_float = resp.state.prop_float
        self._prop_string = resp.state.prop_string

    def func_float(self, param_float: api.StructFloat):
        req = shared.StructInterfaceFuncFloatRequest(
            param_float=param_float
        )
        data = requests.post(
            f'{self.url}/testbed1/struct_interface/func_float',
            req.json()
        )
        resp = shared.StructInterfaceFuncFloatResponse(**data.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_float = resp.state.prop_float
        self._prop_string = resp.state.prop_string

    def func_string(self, param_string: api.StructString):
        req = shared.StructInterfaceFuncStringRequest(
            param_string=param_string
        )
        data = requests.post(
            f'{self.url}/testbed1/struct_interface/func_string',
            req.json()
        )
        resp = shared.StructInterfaceFuncStringResponse(**data.json())
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

    def func_bool(self, param_bool: list[api.StructBool]):
        req = shared.StructArrayInterfaceFuncBoolRequest(
            param_bool=param_bool
        )
        data = requests.post(
            f'{self.url}/testbed1/struct_array_interface/func_bool',
            req.json()
        )
        resp = shared.StructArrayInterfaceFuncBoolResponse(**data.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_float = resp.state.prop_float
        self._prop_string = resp.state.prop_string

    def func_int(self, param_int: list[api.StructInt]):
        req = shared.StructArrayInterfaceFuncIntRequest(
            param_int=param_int
        )
        data = requests.post(
            f'{self.url}/testbed1/struct_array_interface/func_int',
            req.json()
        )
        resp = shared.StructArrayInterfaceFuncIntResponse(**data.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_float = resp.state.prop_float
        self._prop_string = resp.state.prop_string

    def func_float(self, param_float: list[api.StructFloat]):
        req = shared.StructArrayInterfaceFuncFloatRequest(
            param_float=param_float
        )
        data = requests.post(
            f'{self.url}/testbed1/struct_array_interface/func_float',
            req.json()
        )
        resp = shared.StructArrayInterfaceFuncFloatResponse(**data.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_float = resp.state.prop_float
        self._prop_string = resp.state.prop_string

    def func_string(self, param_string: list[api.StructString]):
        req = shared.StructArrayInterfaceFuncStringRequest(
            param_string=param_string
        )
        data = requests.post(
            f'{self.url}/testbed1/struct_array_interface/func_string',
            req.json()
        )
        resp = shared.StructArrayInterfaceFuncStringResponse(**data.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_float = resp.state.prop_float
        self._prop_string = resp.state.prop_string
