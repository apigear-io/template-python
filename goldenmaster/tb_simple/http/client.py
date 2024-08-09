import requests
import os

from tb_simple.api import api
from . import shared



class VoidInterface(api.IVoidInterface):
    def __init__(self, url='http://localhost:8000'):
        super().__init__()
        self._url = url

    def func_void(self):
        req = shared.VoidInterfaceFuncVoidRequest(
        )
        data = requests.post(
            f'{self.url}/tb_simple/void_interface/func_void',
            req.json()
        )
        resp = shared.VoidInterfaceFuncVoidResponse(**data.json())

class SimpleInterface(api.ISimpleInterface):
    def __init__(self, url='http://localhost:8000'):
        super().__init__()
        self._url = url        
        self._prop_bool = False        
        self._prop_int = 0        
        self._prop_int32 = 0        
        self._prop_int64 = 0        
        self._prop_float = 0.0        
        self._prop_float32 = 0.0        
        self._prop_float64 = 0.0        
        self._prop_string = ""
    
    def get_prop_bool(self):
        return self._prop_bool

    def set_prop_bool(self, value):
        self._prop_bool = value
    
    def get_prop_int(self):
        return self._prop_int

    def set_prop_int(self, value):
        self._prop_int = value
    
    def get_prop_int32(self):
        return self._prop_int32

    def set_prop_int32(self, value):
        self._prop_int32 = value
    
    def get_prop_int64(self):
        return self._prop_int64

    def set_prop_int64(self, value):
        self._prop_int64 = value
    
    def get_prop_float(self):
        return self._prop_float

    def set_prop_float(self, value):
        self._prop_float = value
    
    def get_prop_float32(self):
        return self._prop_float32

    def set_prop_float32(self, value):
        self._prop_float32 = value
    
    def get_prop_float64(self):
        return self._prop_float64

    def set_prop_float64(self, value):
        self._prop_float64 = value
    
    def get_prop_string(self):
        return self._prop_string

    def set_prop_string(self, value):
        self._prop_string = value

    def func_no_return_value(self, param_bool: bool):
        req = shared.SimpleInterfaceFuncNoReturnValueRequest(
            param_bool=param_bool
        )
        data = requests.post(
            f'{self.url}/tb_simple/simple_interface/func_no_return_value',
            req.json()
        )
        resp = shared.SimpleInterfaceFuncNoReturnValueResponse(**data.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_int32 = resp.state.prop_int32
        self._prop_int64 = resp.state.prop_int64
        self._prop_float = resp.state.prop_float
        self._prop_float32 = resp.state.prop_float32
        self._prop_float64 = resp.state.prop_float64
        self._prop_string = resp.state.prop_string

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
        self._prop_int32 = resp.state.prop_int32
        self._prop_int64 = resp.state.prop_int64
        self._prop_float = resp.state.prop_float
        self._prop_float32 = resp.state.prop_float32
        self._prop_float64 = resp.state.prop_float64
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
        self._prop_int32 = resp.state.prop_int32
        self._prop_int64 = resp.state.prop_int64
        self._prop_float = resp.state.prop_float
        self._prop_float32 = resp.state.prop_float32
        self._prop_float64 = resp.state.prop_float64
        self._prop_string = resp.state.prop_string

    def func_int32(self, param_int32: int):
        req = shared.SimpleInterfaceFuncInt32Request(
            param_int32=param_int32
        )
        data = requests.post(
            f'{self.url}/tb_simple/simple_interface/func_int32',
            req.json()
        )
        resp = shared.SimpleInterfaceFuncInt32Response(**data.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_int32 = resp.state.prop_int32
        self._prop_int64 = resp.state.prop_int64
        self._prop_float = resp.state.prop_float
        self._prop_float32 = resp.state.prop_float32
        self._prop_float64 = resp.state.prop_float64
        self._prop_string = resp.state.prop_string

    def func_int64(self, param_int64: int):
        req = shared.SimpleInterfaceFuncInt64Request(
            param_int64=param_int64
        )
        data = requests.post(
            f'{self.url}/tb_simple/simple_interface/func_int64',
            req.json()
        )
        resp = shared.SimpleInterfaceFuncInt64Response(**data.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_int32 = resp.state.prop_int32
        self._prop_int64 = resp.state.prop_int64
        self._prop_float = resp.state.prop_float
        self._prop_float32 = resp.state.prop_float32
        self._prop_float64 = resp.state.prop_float64
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
        self._prop_int32 = resp.state.prop_int32
        self._prop_int64 = resp.state.prop_int64
        self._prop_float = resp.state.prop_float
        self._prop_float32 = resp.state.prop_float32
        self._prop_float64 = resp.state.prop_float64
        self._prop_string = resp.state.prop_string

    def func_float32(self, param_float32: float):
        req = shared.SimpleInterfaceFuncFloat32Request(
            param_float32=param_float32
        )
        data = requests.post(
            f'{self.url}/tb_simple/simple_interface/func_float32',
            req.json()
        )
        resp = shared.SimpleInterfaceFuncFloat32Response(**data.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_int32 = resp.state.prop_int32
        self._prop_int64 = resp.state.prop_int64
        self._prop_float = resp.state.prop_float
        self._prop_float32 = resp.state.prop_float32
        self._prop_float64 = resp.state.prop_float64
        self._prop_string = resp.state.prop_string

    def func_float64(self, param_float: float):
        req = shared.SimpleInterfaceFuncFloat64Request(
            param_float=param_float
        )
        data = requests.post(
            f'{self.url}/tb_simple/simple_interface/func_float64',
            req.json()
        )
        resp = shared.SimpleInterfaceFuncFloat64Response(**data.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_int32 = resp.state.prop_int32
        self._prop_int64 = resp.state.prop_int64
        self._prop_float = resp.state.prop_float
        self._prop_float32 = resp.state.prop_float32
        self._prop_float64 = resp.state.prop_float64
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
        self._prop_int32 = resp.state.prop_int32
        self._prop_int64 = resp.state.prop_int64
        self._prop_float = resp.state.prop_float
        self._prop_float32 = resp.state.prop_float32
        self._prop_float64 = resp.state.prop_float64
        self._prop_string = resp.state.prop_string

class SimpleArrayInterface(api.ISimpleArrayInterface):
    def __init__(self, url='http://localhost:8000'):
        super().__init__()
        self._url = url        
        self._prop_bool = []        
        self._prop_int = []        
        self._prop_int32 = []        
        self._prop_int64 = []        
        self._prop_float = []        
        self._prop_float32 = []        
        self._prop_float64 = []        
        self._prop_string = []        
        self._prop_read_only_string = ""
    
    def get_prop_bool(self):
        return self._prop_bool

    def set_prop_bool(self, value):
        self._prop_bool = value
    
    def get_prop_int(self):
        return self._prop_int

    def set_prop_int(self, value):
        self._prop_int = value
    
    def get_prop_int32(self):
        return self._prop_int32

    def set_prop_int32(self, value):
        self._prop_int32 = value
    
    def get_prop_int64(self):
        return self._prop_int64

    def set_prop_int64(self, value):
        self._prop_int64 = value
    
    def get_prop_float(self):
        return self._prop_float

    def set_prop_float(self, value):
        self._prop_float = value
    
    def get_prop_float32(self):
        return self._prop_float32

    def set_prop_float32(self, value):
        self._prop_float32 = value
    
    def get_prop_float64(self):
        return self._prop_float64

    def set_prop_float64(self, value):
        self._prop_float64 = value
    
    def get_prop_string(self):
        return self._prop_string

    def set_prop_string(self, value):
        self._prop_string = value
    
    def get_prop_read_only_string(self):
        return self._prop_read_only_string

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
        self._prop_int32 = resp.state.prop_int32
        self._prop_int64 = resp.state.prop_int64
        self._prop_float = resp.state.prop_float
        self._prop_float32 = resp.state.prop_float32
        self._prop_float64 = resp.state.prop_float64
        self._prop_string = resp.state.prop_string
        self._prop_read_only_string = resp.state.prop_read_only_string

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
        self._prop_int32 = resp.state.prop_int32
        self._prop_int64 = resp.state.prop_int64
        self._prop_float = resp.state.prop_float
        self._prop_float32 = resp.state.prop_float32
        self._prop_float64 = resp.state.prop_float64
        self._prop_string = resp.state.prop_string
        self._prop_read_only_string = resp.state.prop_read_only_string

    def func_int32(self, param_int32: list[int]):
        req = shared.SimpleArrayInterfaceFuncInt32Request(
            param_int32=param_int32
        )
        data = requests.post(
            f'{self.url}/tb_simple/simple_array_interface/func_int32',
            req.json()
        )
        resp = shared.SimpleArrayInterfaceFuncInt32Response(**data.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_int32 = resp.state.prop_int32
        self._prop_int64 = resp.state.prop_int64
        self._prop_float = resp.state.prop_float
        self._prop_float32 = resp.state.prop_float32
        self._prop_float64 = resp.state.prop_float64
        self._prop_string = resp.state.prop_string
        self._prop_read_only_string = resp.state.prop_read_only_string

    def func_int64(self, param_int64: list[int]):
        req = shared.SimpleArrayInterfaceFuncInt64Request(
            param_int64=param_int64
        )
        data = requests.post(
            f'{self.url}/tb_simple/simple_array_interface/func_int64',
            req.json()
        )
        resp = shared.SimpleArrayInterfaceFuncInt64Response(**data.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_int32 = resp.state.prop_int32
        self._prop_int64 = resp.state.prop_int64
        self._prop_float = resp.state.prop_float
        self._prop_float32 = resp.state.prop_float32
        self._prop_float64 = resp.state.prop_float64
        self._prop_string = resp.state.prop_string
        self._prop_read_only_string = resp.state.prop_read_only_string

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
        self._prop_int32 = resp.state.prop_int32
        self._prop_int64 = resp.state.prop_int64
        self._prop_float = resp.state.prop_float
        self._prop_float32 = resp.state.prop_float32
        self._prop_float64 = resp.state.prop_float64
        self._prop_string = resp.state.prop_string
        self._prop_read_only_string = resp.state.prop_read_only_string

    def func_float32(self, param_float32: list[float]):
        req = shared.SimpleArrayInterfaceFuncFloat32Request(
            param_float32=param_float32
        )
        data = requests.post(
            f'{self.url}/tb_simple/simple_array_interface/func_float32',
            req.json()
        )
        resp = shared.SimpleArrayInterfaceFuncFloat32Response(**data.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_int32 = resp.state.prop_int32
        self._prop_int64 = resp.state.prop_int64
        self._prop_float = resp.state.prop_float
        self._prop_float32 = resp.state.prop_float32
        self._prop_float64 = resp.state.prop_float64
        self._prop_string = resp.state.prop_string
        self._prop_read_only_string = resp.state.prop_read_only_string

    def func_float64(self, param_float: list[float]):
        req = shared.SimpleArrayInterfaceFuncFloat64Request(
            param_float=param_float
        )
        data = requests.post(
            f'{self.url}/tb_simple/simple_array_interface/func_float64',
            req.json()
        )
        resp = shared.SimpleArrayInterfaceFuncFloat64Response(**data.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
        self._prop_int32 = resp.state.prop_int32
        self._prop_int64 = resp.state.prop_int64
        self._prop_float = resp.state.prop_float
        self._prop_float32 = resp.state.prop_float32
        self._prop_float64 = resp.state.prop_float64
        self._prop_string = resp.state.prop_string
        self._prop_read_only_string = resp.state.prop_read_only_string

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
        self._prop_int32 = resp.state.prop_int32
        self._prop_int64 = resp.state.prop_int64
        self._prop_float = resp.state.prop_float
        self._prop_float32 = resp.state.prop_float32
        self._prop_float64 = resp.state.prop_float64
        self._prop_string = resp.state.prop_string
        self._prop_read_only_string = resp.state.prop_read_only_string

class NoPropertiesInterface(api.INoPropertiesInterface):
    def __init__(self, url='http://localhost:8000'):
        super().__init__()
        self._url = url

    def func_void(self):
        req = shared.NoPropertiesInterfaceFuncVoidRequest(
        )
        data = requests.post(
            f'{self.url}/tb_simple/no_properties_interface/func_void',
            req.json()
        )
        resp = shared.NoPropertiesInterfaceFuncVoidResponse(**data.json())

    def func_bool(self, param_bool: bool):
        req = shared.NoPropertiesInterfaceFuncBoolRequest(
            param_bool=param_bool
        )
        data = requests.post(
            f'{self.url}/tb_simple/no_properties_interface/func_bool',
            req.json()
        )
        resp = shared.NoPropertiesInterfaceFuncBoolResponse(**data.json())

class NoOperationsInterface(api.INoOperationsInterface):
    def __init__(self, url='http://localhost:8000'):
        super().__init__()
        self._url = url        
        self._prop_bool = False        
        self._prop_int = 0
    
    def get_prop_bool(self):
        return self._prop_bool

    def set_prop_bool(self, value):
        self._prop_bool = value
    
    def get_prop_int(self):
        return self._prop_int

    def set_prop_int(self, value):
        self._prop_int = value

class NoSignalsInterface(api.INoSignalsInterface):
    def __init__(self, url='http://localhost:8000'):
        super().__init__()
        self._url = url        
        self._prop_bool = False        
        self._prop_int = 0
    
    def get_prop_bool(self):
        return self._prop_bool

    def set_prop_bool(self, value):
        self._prop_bool = value
    
    def get_prop_int(self):
        return self._prop_int

    def set_prop_int(self, value):
        self._prop_int = value

    def func_void(self):
        req = shared.NoSignalsInterfaceFuncVoidRequest(
        )
        data = requests.post(
            f'{self.url}/tb_simple/no_signals_interface/func_void',
            req.json()
        )
        resp = shared.NoSignalsInterfaceFuncVoidResponse(**data.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int

    def func_bool(self, param_bool: bool):
        req = shared.NoSignalsInterfaceFuncBoolRequest(
            param_bool=param_bool
        )
        data = requests.post(
            f'{self.url}/tb_simple/no_signals_interface/func_bool',
            req.json()
        )
        resp = shared.NoSignalsInterfaceFuncBoolResponse(**data.json())
        self._prop_bool = resp.state.prop_bool
        self._prop_int = resp.state.prop_int
