from pydantic import BaseModel
from typing import Iterable
from testbed1_api import api

class StructInterfaceState(BaseModel):
    propBool: api.StructBool
    propInt: api.StructInt
    propFloat: api.StructFloat
    propString: api.StructString

# method StructInterface.funcBool
class StructInterfaceFuncBoolRequest(BaseModel):
    paramBool: api.StructBool 

class StructInterfaceFuncBoolResponse(BaseModel):
    result: api.StructBool
    state: StructInterfaceState

# method StructInterface.funcInt
class StructInterfaceFuncIntRequest(BaseModel):
    paramInt: api.StructInt 

class StructInterfaceFuncIntResponse(BaseModel):
    result: api.StructBool
    state: StructInterfaceState

# method StructInterface.funcFloat
class StructInterfaceFuncFloatRequest(BaseModel):
    paramFloat: api.StructFloat 

class StructInterfaceFuncFloatResponse(BaseModel):
    result: api.StructFloat
    state: StructInterfaceState

# method StructInterface.funcString
class StructInterfaceFuncStringRequest(BaseModel):
    paramString: api.StructString 

class StructInterfaceFuncStringResponse(BaseModel):
    result: api.StructString
    state: StructInterfaceState

class StructArrayInterfaceState(BaseModel):
    propBool: list[api.StructBool]
    propInt: list[api.StructInt]
    propFloat: list[api.StructFloat]
    propString: list[api.StructString]

# method StructArrayInterface.funcBool
class StructArrayInterfaceFuncBoolRequest(BaseModel):
    paramBool: list[api.StructBool] 

class StructArrayInterfaceFuncBoolResponse(BaseModel):
    result: api.StructBool
    state: StructArrayInterfaceState

# method StructArrayInterface.funcInt
class StructArrayInterfaceFuncIntRequest(BaseModel):
    paramInt: list[api.StructInt] 

class StructArrayInterfaceFuncIntResponse(BaseModel):
    result: api.StructBool
    state: StructArrayInterfaceState

# method StructArrayInterface.funcFloat
class StructArrayInterfaceFuncFloatRequest(BaseModel):
    paramFloat: list[api.StructFloat] 

class StructArrayInterfaceFuncFloatResponse(BaseModel):
    result: api.StructBool
    state: StructArrayInterfaceState

# method StructArrayInterface.funcString
class StructArrayInterfaceFuncStringRequest(BaseModel):
    paramString: list[api.StructString] 

class StructArrayInterfaceFuncStringResponse(BaseModel):
    result: api.StructBool
    state: StructArrayInterfaceState



