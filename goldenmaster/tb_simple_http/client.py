import requests
import os

from tb_simple_api import api
from . import shared



class SimpleInterface(api.ISimpleInterface):
    def __init__(self, url='http://localhost:8000'):
        super().__init__()
        self._url = url        
        self._prop_bool = False        
        self._prop_int = 0        
        self._prop_float = 0.0        
        self._prop_string = ""
    
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

    def func_bool(self, param_bool: bool):
        req = shared.SimpleInterfaceFuncBoolRequest(
            param_bool=param_bool
        )
        data = requests.post(
            f'{self.url}/tb_simple/simple_interface/func_bool',
            req.json()
        )
        resp = shared.SimpleInterfaceFuncBoolResponse(**data.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_float = resp.state.prop_float
        self._prop_string = resp.state.prop_string

    def func_int(self, param_int: int):
        req = shared.SimpleInterfaceFuncIntRequest(
            param_int=param_int
        )
        data = requests.post(
            f'{self.url}/tb_simple/simple_interface/func_int',
            req.json()
        )
        resp = shared.SimpleInterfaceFuncIntResponse(**data.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_float = resp.state.prop_float
        self._prop_string = resp.state.prop_string

    def func_float(self, param_float: float):
        req = shared.SimpleInterfaceFuncFloatRequest(
            param_float=param_float
        )
        data = requests.post(
            f'{self.url}/tb_simple/simple_interface/func_float',
            req.json()
        )
        resp = shared.SimpleInterfaceFuncFloatResponse(**data.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_float = resp.state.prop_float
        self._prop_string = resp.state.prop_string

    def func_string(self, param_string: str):
        req = shared.SimpleInterfaceFuncStringRequest(
            param_string=param_string
        )
        data = requests.post(
            f'{self.url}/tb_simple/simple_interface/func_string',
            req.json()
        )
        resp = shared.SimpleInterfaceFuncStringResponse(**data.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_float = resp.state.prop_float
        self._prop_string = resp.state.prop_string

class SimpleArrayInterface(api.ISimpleArrayInterface):
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

    def func_bool(self, param_bool: list[bool]):
        req = shared.SimpleArrayInterfaceFuncBoolRequest(
            param_bool=param_bool
        )
        data = requests.post(
            f'{self.url}/tb_simple/simple_array_interface/func_bool',
            req.json()
        )
        resp = shared.SimpleArrayInterfaceFuncBoolResponse(**data.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_float = resp.state.prop_float
        self._prop_string = resp.state.prop_string

    def func_int(self, param_int: list[int]):
        req = shared.SimpleArrayInterfaceFuncIntRequest(
            param_int=param_int
        )
        data = requests.post(
            f'{self.url}/tb_simple/simple_array_interface/func_int',
            req.json()
        )
        resp = shared.SimpleArrayInterfaceFuncIntResponse(**data.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_float = resp.state.prop_float
        self._prop_string = resp.state.prop_string

    def func_float(self, param_float: list[float]):
        req = shared.SimpleArrayInterfaceFuncFloatRequest(
            param_float=param_float
        )
        data = requests.post(
            f'{self.url}/tb_simple/simple_array_interface/func_float',
            req.json()
        )
        resp = shared.SimpleArrayInterfaceFuncFloatResponse(**data.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_float = resp.state.prop_float
        self._prop_string = resp.state.prop_string

    def func_string(self, param_string: list[str]):
        req = shared.SimpleArrayInterfaceFuncStringRequest(
            param_string=param_string
        )
        data = requests.post(
            f'{self.url}/tb_simple/simple_array_interface/func_string',
            req.json()
        )
        resp = shared.SimpleArrayInterfaceFuncStringResponse(**data.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_float = resp.state.prop_float
        self._prop_string = resp.state.prop_string
