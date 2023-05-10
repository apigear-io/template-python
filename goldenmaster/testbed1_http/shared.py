from pydantic import BaseModel, Field
from typing import Iterable
from testbed1_api import api

class StructInterfaceState(BaseModel):
    prop_bool: api.StructBool = Field(None, alias="propBool")
    prop_int: api.StructInt = Field(None, alias="propInt")
    prop_float: api.StructFloat = Field(None, alias="propFloat")
    prop_string: api.StructString = Field(None, alias="propString")

# method StructInterface.funcBool
class StructInterfaceFuncBoolRequest(BaseModel):
    param_bool: api.StructBool = Field(None, alias="paramBool") 

class StructInterfaceFuncBoolResponse(BaseModel):
    result: api.StructBool
    state: StructInterfaceState

# method StructInterface.funcInt
class StructInterfaceFuncIntRequest(BaseModel):
    param_int: api.StructInt = Field(None, alias="paramInt") 

class StructInterfaceFuncIntResponse(BaseModel):
    result: api.StructBool
    state: StructInterfaceState

# method StructInterface.funcFloat
class StructInterfaceFuncFloatRequest(BaseModel):
    param_float: api.StructFloat = Field(None, alias="paramFloat") 

class StructInterfaceFuncFloatResponse(BaseModel):
    result: api.StructFloat
    state: StructInterfaceState

# method StructInterface.funcString
class StructInterfaceFuncStringRequest(BaseModel):
    param_string: api.StructString = Field(None, alias="paramString") 

class StructInterfaceFuncStringResponse(BaseModel):
    result: api.StructString
    state: StructInterfaceState

class StructArrayInterfaceState(BaseModel):
    prop_bool: list[api.StructBool] = Field(None, alias="propBool")
    prop_int: list[api.StructInt] = Field(None, alias="propInt")
    prop_float: list[api.StructFloat] = Field(None, alias="propFloat")
    prop_string: list[api.StructString] = Field(None, alias="propString")

# method StructArrayInterface.funcBool
class StructArrayInterfaceFuncBoolRequest(BaseModel):
    param_bool: list[api.StructBool] = Field(None, alias="paramBool") 

class StructArrayInterfaceFuncBoolResponse(BaseModel):
    result: api.StructBool
    state: StructArrayInterfaceState

# method StructArrayInterface.funcInt
class StructArrayInterfaceFuncIntRequest(BaseModel):
    param_int: list[api.StructInt] = Field(None, alias="paramInt") 

class StructArrayInterfaceFuncIntResponse(BaseModel):
    result: api.StructBool
    state: StructArrayInterfaceState

# method StructArrayInterface.funcFloat
class StructArrayInterfaceFuncFloatRequest(BaseModel):
    param_float: list[api.StructFloat] = Field(None, alias="paramFloat") 

class StructArrayInterfaceFuncFloatResponse(BaseModel):
    result: api.StructBool
    state: StructArrayInterfaceState

# method StructArrayInterface.funcString
class StructArrayInterfaceFuncStringRequest(BaseModel):
    param_string: list[api.StructString] = Field(None, alias="paramString") 

class StructArrayInterfaceFuncStringResponse(BaseModel):
    result: api.StructBool
    state: StructArrayInterfaceState



