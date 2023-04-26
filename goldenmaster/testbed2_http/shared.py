from pydantic import BaseModel
from typing import Iterable
from testbed2_api import api

class ManyParamInterfaceState(BaseModel):
    prop1: int
    prop2: int
    prop3: int
    prop4: int

# method ManyParamInterface.func1
class ManyParamInterfaceFunc1Request(BaseModel):
    param1: int 

class ManyParamInterfaceFunc1Response(BaseModel):
    result: int
    state: ManyParamInterfaceState

# method ManyParamInterface.func2
class ManyParamInterfaceFunc2Request(BaseModel):
    param1: int
    param2: int 

class ManyParamInterfaceFunc2Response(BaseModel):
    result: int
    state: ManyParamInterfaceState

# method ManyParamInterface.func3
class ManyParamInterfaceFunc3Request(BaseModel):
    param1: int
    param2: int
    param3: int 

class ManyParamInterfaceFunc3Response(BaseModel):
    result: int
    state: ManyParamInterfaceState

# method ManyParamInterface.func4
class ManyParamInterfaceFunc4Request(BaseModel):
    param1: int
    param2: int
    param3: int
    param4: int 

class ManyParamInterfaceFunc4Response(BaseModel):
    result: int
    state: ManyParamInterfaceState

class NestedStruct1InterfaceState(BaseModel):
    prop1: api.NestedStruct1

# method NestedStruct1Interface.func1
class NestedStruct1InterfaceFunc1Request(BaseModel):
    param1: api.NestedStruct1 

class NestedStruct1InterfaceFunc1Response(BaseModel):
    result: api.NestedStruct1
    state: NestedStruct1InterfaceState

class NestedStruct2InterfaceState(BaseModel):
    prop1: api.NestedStruct1
    prop2: api.NestedStruct2

# method NestedStruct2Interface.func1
class NestedStruct2InterfaceFunc1Request(BaseModel):
    param1: api.NestedStruct1 

class NestedStruct2InterfaceFunc1Response(BaseModel):
    result: api.NestedStruct1
    state: NestedStruct2InterfaceState

# method NestedStruct2Interface.func2
class NestedStruct2InterfaceFunc2Request(BaseModel):
    param1: api.NestedStruct1
    param2: api.NestedStruct2 

class NestedStruct2InterfaceFunc2Response(BaseModel):
    result: api.NestedStruct1
    state: NestedStruct2InterfaceState

class NestedStruct3InterfaceState(BaseModel):
    prop1: api.NestedStruct1
    prop2: api.NestedStruct2
    prop3: api.NestedStruct3

# method NestedStruct3Interface.func1
class NestedStruct3InterfaceFunc1Request(BaseModel):
    param1: api.NestedStruct1 

class NestedStruct3InterfaceFunc1Response(BaseModel):
    result: api.NestedStruct1
    state: NestedStruct3InterfaceState

# method NestedStruct3Interface.func2
class NestedStruct3InterfaceFunc2Request(BaseModel):
    param1: api.NestedStruct1
    param2: api.NestedStruct2 

class NestedStruct3InterfaceFunc2Response(BaseModel):
    result: api.NestedStruct1
    state: NestedStruct3InterfaceState

# method NestedStruct3Interface.func3
class NestedStruct3InterfaceFunc3Request(BaseModel):
    param1: api.NestedStruct1
    param2: api.NestedStruct2
    param3: api.NestedStruct3 

class NestedStruct3InterfaceFunc3Response(BaseModel):
    result: api.NestedStruct1
    state: NestedStruct3InterfaceState


