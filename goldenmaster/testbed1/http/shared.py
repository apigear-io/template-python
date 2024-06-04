from pydantic import BaseModel, Field
from typing import Iterable
from testbed1.api import api

class StructInterfaceState(BaseModel):
    prop_bool: api.StructBool = Field(default=api.StructBool(), alias="propBool")
    prop_int: api.StructInt = Field(default=api.StructInt(), alias="propInt")
    prop_float: api.StructFloat = Field(default=api.StructFloat(), alias="propFloat")
    prop_string: api.StructString = Field(default=api.StructString(), alias="propString")

# method StructInterface.funcBool
class StructInterfaceFuncBoolRequest(BaseModel):
    param_bool: api.StructBool = Field(default=api.StructBool(), alias="paramBool") 

class StructInterfaceFuncBoolResponse(BaseModel):
    result: api.StructBool
    state: StructInterfaceState

# method StructInterface.funcInt
class StructInterfaceFuncIntRequest(BaseModel):
    param_int: api.StructInt = Field(default=api.StructInt(), alias="paramInt") 

class StructInterfaceFuncIntResponse(BaseModel):
    result: api.StructBool
    state: StructInterfaceState

# method StructInterface.funcFloat
class StructInterfaceFuncFloatRequest(BaseModel):
    param_float: api.StructFloat = Field(default=api.StructFloat(), alias="paramFloat") 

class StructInterfaceFuncFloatResponse(BaseModel):
    result: api.StructFloat
    state: StructInterfaceState

# method StructInterface.funcString
class StructInterfaceFuncStringRequest(BaseModel):
    param_string: api.StructString = Field(default=api.StructString(), alias="paramString") 

class StructInterfaceFuncStringResponse(BaseModel):
    result: api.StructString
    state: StructInterfaceState

class StructArrayInterfaceState(BaseModel):
    prop_bool: list[api.StructBool] = Field(default=[], alias="propBool")
    prop_int: list[api.StructInt] = Field(default=[], alias="propInt")
    prop_float: list[api.StructFloat] = Field(default=[], alias="propFloat")
    prop_string: list[api.StructString] = Field(default=[], alias="propString")

# method StructArrayInterface.funcBool
class StructArrayInterfaceFuncBoolRequest(BaseModel):
    param_bool: list[api.StructBool] = Field(default=[], alias="paramBool") 

class StructArrayInterfaceFuncBoolResponse(BaseModel):
    result: list[api.StructBool]
    state: StructArrayInterfaceState

# method StructArrayInterface.funcInt
class StructArrayInterfaceFuncIntRequest(BaseModel):
    param_int: list[api.StructInt] = Field(default=[], alias="paramInt") 

class StructArrayInterfaceFuncIntResponse(BaseModel):
    result: list[api.StructInt]
    state: StructArrayInterfaceState

# method StructArrayInterface.funcFloat
class StructArrayInterfaceFuncFloatRequest(BaseModel):
    param_float: list[api.StructFloat] = Field(default=[], alias="paramFloat") 

class StructArrayInterfaceFuncFloatResponse(BaseModel):
    result: list[api.StructFloat]
    state: StructArrayInterfaceState

# method StructArrayInterface.funcString
class StructArrayInterfaceFuncStringRequest(BaseModel):
    param_string: list[api.StructString] = Field(default=[], alias="paramString") 

class StructArrayInterfaceFuncStringResponse(BaseModel):
    result: list[api.StructString]
    state: StructArrayInterfaceState



