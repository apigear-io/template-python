from pydantic import BaseModel, Field
from typing import Iterable
from tb.simple_api import api

class SimpleInterfaceState(BaseModel):
    prop_bool: bool = Field(None, alias="propBool")
    prop_int: int = Field(None, alias="propInt")
    prop_float: float = Field(None, alias="propFloat")
    prop_string: str = Field(None, alias="propString")

# method SimpleInterface.funcBool
class SimpleInterfaceFuncBoolRequest(BaseModel):
    param_bool: bool = Field(None, alias="paramBool") 

class SimpleInterfaceFuncBoolResponse(BaseModel):
    result: bool
    state: SimpleInterfaceState

# method SimpleInterface.funcInt
class SimpleInterfaceFuncIntRequest(BaseModel):
    param_int: int = Field(None, alias="paramInt") 

class SimpleInterfaceFuncIntResponse(BaseModel):
    result: int
    state: SimpleInterfaceState

# method SimpleInterface.funcFloat
class SimpleInterfaceFuncFloatRequest(BaseModel):
    param_float: float = Field(None, alias="paramFloat") 

class SimpleInterfaceFuncFloatResponse(BaseModel):
    result: float
    state: SimpleInterfaceState

# method SimpleInterface.funcString
class SimpleInterfaceFuncStringRequest(BaseModel):
    param_string: str = Field(None, alias="paramString") 

class SimpleInterfaceFuncStringResponse(BaseModel):
    result: str
    state: SimpleInterfaceState

class SimpleArrayInterfaceState(BaseModel):
    prop_bool: list[bool] = Field(None, alias="propBool")
    prop_int: list[int] = Field(None, alias="propInt")
    prop_float: list[float] = Field(None, alias="propFloat")
    prop_string: list[str] = Field(None, alias="propString")

# method SimpleArrayInterface.funcBool
class SimpleArrayInterfaceFuncBoolRequest(BaseModel):
    param_bool: list[bool] = Field(None, alias="paramBool") 

class SimpleArrayInterfaceFuncBoolResponse(BaseModel):
    result: list[bool]
    state: SimpleArrayInterfaceState

# method SimpleArrayInterface.funcInt
class SimpleArrayInterfaceFuncIntRequest(BaseModel):
    param_int: list[int] = Field(None, alias="paramInt") 

class SimpleArrayInterfaceFuncIntResponse(BaseModel):
    result: list[int]
    state: SimpleArrayInterfaceState

# method SimpleArrayInterface.funcFloat
class SimpleArrayInterfaceFuncFloatRequest(BaseModel):
    param_float: list[float] = Field(None, alias="paramFloat") 

class SimpleArrayInterfaceFuncFloatResponse(BaseModel):
    result: list[float]
    state: SimpleArrayInterfaceState

# method SimpleArrayInterface.funcString
class SimpleArrayInterfaceFuncStringRequest(BaseModel):
    param_string: list[str] = Field(None, alias="paramString") 

class SimpleArrayInterfaceFuncStringResponse(BaseModel):
    result: list[str]
    state: SimpleArrayInterfaceState



