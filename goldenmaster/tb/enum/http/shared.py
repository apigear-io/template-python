from pydantic import BaseModel
from typing import Iterable
from tb.enum.api import api

# interface EnumInterface
class EnumInterfaceState(BaseModel):
    prop0: api.Enum0
    prop1: api.Enum1
    prop2: api.Enum2
    prop3: api.Enum3

# method EnumInterface.func0
class EnumInterfaceFunc0Request(BaseModel):
    param0: api.Enum0 

class EnumInterfaceFunc0Response(BaseModel):
    result: api.Enum0
    state: EnumInterfaceState

# method EnumInterface.func1
class EnumInterfaceFunc1Request(BaseModel):
    param1: api.Enum1 

class EnumInterfaceFunc1Response(BaseModel):
    result: api.Enum1
    state: EnumInterfaceState

# method EnumInterface.func2
class EnumInterfaceFunc2Request(BaseModel):
    param2: api.Enum2 

class EnumInterfaceFunc2Response(BaseModel):
    result: api.Enum2
    state: EnumInterfaceState

# method EnumInterface.func3
class EnumInterfaceFunc3Request(BaseModel):
    param3: api.Enum3 

class EnumInterfaceFunc3Response(BaseModel):
    result: api.Enum3
    state: EnumInterfaceState  



