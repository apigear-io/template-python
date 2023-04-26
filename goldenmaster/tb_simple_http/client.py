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
            paramBool=paramBool
        )
        data = requests.post(
            f'{self.url}/tb.simple/SimpleInterface/funcBool',
            req.json()
        )
        resp = shared.SimpleInterfaceFuncBoolResponse(**data.json())
        print(resp.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_float = resp.state.prop_float
        self._prop_string = resp.state.prop_string
    def func_int(self, param_int: int):
        req = shared.SimpleInterfaceFuncIntRequest(
            paramInt=paramInt
        )
        data = requests.post(
            f'{self.url}/tb.simple/SimpleInterface/funcInt',
            req.json()
        )
        resp = shared.SimpleInterfaceFuncIntResponse(**data.json())
        print(resp.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_float = resp.state.prop_float
        self._prop_string = resp.state.prop_string
    def func_float(self, param_float: float):
        req = shared.SimpleInterfaceFuncFloatRequest(
            paramFloat=paramFloat
        )
        data = requests.post(
            f'{self.url}/tb.simple/SimpleInterface/funcFloat',
            req.json()
        )
        resp = shared.SimpleInterfaceFuncFloatResponse(**data.json())
        print(resp.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_float = resp.state.prop_float
        self._prop_string = resp.state.prop_string
    def func_string(self, param_string: str):
        req = shared.SimpleInterfaceFuncStringRequest(
            paramString=paramString
        )
        data = requests.post(
            f'{self.url}/tb.simple/SimpleInterface/funcString',
            req.json()
        )
        resp = shared.SimpleInterfaceFuncStringResponse(**data.json())
        print(resp.json())
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
            paramBool=paramBool
        )
        data = requests.post(
            f'{self.url}/tb.simple/SimpleArrayInterface/funcBool',
            req.json()
        )
        resp = shared.SimpleArrayInterfaceFuncBoolResponse(**data.json())
        print(resp.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_float = resp.state.prop_float
        self._prop_string = resp.state.prop_string
    def func_int(self, param_int: list[int]):
        req = shared.SimpleArrayInterfaceFuncIntRequest(
            paramInt=paramInt
        )
        data = requests.post(
            f'{self.url}/tb.simple/SimpleArrayInterface/funcInt',
            req.json()
        )
        resp = shared.SimpleArrayInterfaceFuncIntResponse(**data.json())
        print(resp.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_float = resp.state.prop_float
        self._prop_string = resp.state.prop_string
    def func_float(self, param_float: list[float]):
        req = shared.SimpleArrayInterfaceFuncFloatRequest(
            paramFloat=paramFloat
        )
        data = requests.post(
            f'{self.url}/tb.simple/SimpleArrayInterface/funcFloat',
            req.json()
        )
        resp = shared.SimpleArrayInterfaceFuncFloatResponse(**data.json())
        print(resp.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_float = resp.state.prop_float
        self._prop_string = resp.state.prop_string
    def func_string(self, param_string: list[str]):
        req = shared.SimpleArrayInterfaceFuncStringRequest(
            paramString=paramString
        )
        data = requests.post(
            f'{self.url}/tb.simple/SimpleArrayInterface/funcString',
            req.json()
        )
        resp = shared.SimpleArrayInterfaceFuncStringResponse(**data.json())
        print(resp.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_float = resp.state.prop_float
        self._prop_string = resp.state.prop_string
