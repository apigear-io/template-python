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
    result: api.StructInt
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
    prop_enum: list[api.Enum0] = Field(default=[], alias="propEnum")

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

# method StructArrayInterface.funcEnum
class StructArrayInterfaceFuncEnumRequest(BaseModel):
    param_enum: list[api.Enum0] = Field(default=[], alias="paramEnum") 

class StructArrayInterfaceFuncEnumResponse(BaseModel):
    result: list[api.Enum0]
    state: StructArrayInterfaceState

class StructArray2InterfaceState(BaseModel):
    prop_bool: api.StructBoolWithArray = Field(default=api.StructBoolWithArray(), alias="propBool")
    prop_int: api.StructIntWithArray = Field(default=api.StructIntWithArray(), alias="propInt")
    prop_float: api.StructFloatWithArray = Field(default=api.StructFloatWithArray(), alias="propFloat")
    prop_string: api.StructStringWithArray = Field(default=api.StructStringWithArray(), alias="propString")
    prop_enum: api.StructEnumWithArray = Field(default=api.StructEnumWithArray(), alias="propEnum")

# method StructArray2Interface.funcBool
class StructArray2InterfaceFuncBoolRequest(BaseModel):
    param_bool: api.StructBoolWithArray = Field(default=api.StructBoolWithArray(), alias="paramBool") 

class StructArray2InterfaceFuncBoolResponse(BaseModel):
    result: list[api.StructBool]
    state: StructArray2InterfaceState

# method StructArray2Interface.funcInt
class StructArray2InterfaceFuncIntRequest(BaseModel):
    param_int: api.StructIntWithArray = Field(default=api.StructIntWithArray(), alias="paramInt") 

class StructArray2InterfaceFuncIntResponse(BaseModel):
    result: list[api.StructInt]
    state: StructArray2InterfaceState

# method StructArray2Interface.funcFloat
class StructArray2InterfaceFuncFloatRequest(BaseModel):
    param_float: api.StructFloatWithArray = Field(default=api.StructFloatWithArray(), alias="paramFloat") 

class StructArray2InterfaceFuncFloatResponse(BaseModel):
    result: list[api.StructFloat]
    state: StructArray2InterfaceState

# method StructArray2Interface.funcString
class StructArray2InterfaceFuncStringRequest(BaseModel):
    param_string: api.StructStringWithArray = Field(default=api.StructStringWithArray(), alias="paramString") 

class StructArray2InterfaceFuncStringResponse(BaseModel):
    result: list[api.StructString]
    state: StructArray2InterfaceState

# method StructArray2Interface.funcEnum
class StructArray2InterfaceFuncEnumRequest(BaseModel):
    param_enum: api.StructEnumWithArray = Field(default=api.StructEnumWithArray(), alias="paramEnum") 

class StructArray2InterfaceFuncEnumResponse(BaseModel):
    result: list[api.Enum0]
    state: StructArray2InterfaceState



