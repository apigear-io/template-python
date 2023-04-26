from pydantic import BaseModel
from typing import Iterable
from tb.simple_api import api

class SimpleInterfaceState(BaseModel):
    propBool: bool
    propInt: int
    propFloat: float
    propString: str

# method SimpleInterface.funcBool
class SimpleInterfaceFuncBoolRequest(BaseModel):
    paramBool: bool 

class SimpleInterfaceFuncBoolResponse(BaseModel):
    result: bool
    state: SimpleInterfaceState

# method SimpleInterface.funcInt
class SimpleInterfaceFuncIntRequest(BaseModel):
    paramInt: int 

class SimpleInterfaceFuncIntResponse(BaseModel):
    result: int
    state: SimpleInterfaceState

# method SimpleInterface.funcFloat
class SimpleInterfaceFuncFloatRequest(BaseModel):
    paramFloat: float 

class SimpleInterfaceFuncFloatResponse(BaseModel):
    result: float
    state: SimpleInterfaceState

# method SimpleInterface.funcString
class SimpleInterfaceFuncStringRequest(BaseModel):
    paramString: str 

class SimpleInterfaceFuncStringResponse(BaseModel):
    result: str
    state: SimpleInterfaceState

class SimpleArrayInterfaceState(BaseModel):
    propBool: list[bool]
    propInt: list[int]
    propFloat: list[float]
    propString: list[str]

# method SimpleArrayInterface.funcBool
class SimpleArrayInterfaceFuncBoolRequest(BaseModel):
    paramBool: list[bool] 

class SimpleArrayInterfaceFuncBoolResponse(BaseModel):
    result: list[bool]
    state: SimpleArrayInterfaceState

# method SimpleArrayInterface.funcInt
class SimpleArrayInterfaceFuncIntRequest(BaseModel):
    paramInt: list[int] 

class SimpleArrayInterfaceFuncIntResponse(BaseModel):
    result: list[int]
    state: SimpleArrayInterfaceState

# method SimpleArrayInterface.funcFloat
class SimpleArrayInterfaceFuncFloatRequest(BaseModel):
    paramFloat: list[float] 

class SimpleArrayInterfaceFuncFloatResponse(BaseModel):
    result: list[float]
    state: SimpleArrayInterfaceState

# method SimpleArrayInterface.funcString
class SimpleArrayInterfaceFuncStringRequest(BaseModel):
    paramString: list[str] 

class SimpleArrayInterfaceFuncStringResponse(BaseModel):
    result: list[str]
    state: SimpleArrayInterfaceState



