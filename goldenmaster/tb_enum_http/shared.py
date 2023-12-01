from pydantic import BaseModel, Field
from typing import Iterable
from tb.enum_api import api

class EnumInterfaceState(BaseModel):
    prop0: api.Enum0 = Field(default=api.Enum0.VALUE0, alias="prop0")
    prop1: api.Enum1 = Field(default=api.Enum1.VALUE1, alias="prop1")
    prop2: api.Enum2 = Field(default=api.Enum2.VALUE2, alias="prop2")
    prop3: api.Enum3 = Field(default=api.Enum3.VALUE3, alias="prop3")

# method EnumInterface.func0
class EnumInterfaceFunc0Request(BaseModel):
    param0: api.Enum0 = Field(default=api.Enum0.VALUE0, alias="param0") 

class EnumInterfaceFunc0Response(BaseModel):
    result: api.Enum0
    state: EnumInterfaceState

# method EnumInterface.func1
class EnumInterfaceFunc1Request(BaseModel):
    param1: api.Enum1 = Field(default=api.Enum1.VALUE1, alias="param1") 

class EnumInterfaceFunc1Response(BaseModel):
    result: api.Enum1
    state: EnumInterfaceState

# method EnumInterface.func2
class EnumInterfaceFunc2Request(BaseModel):
    param2: api.Enum2 = Field(default=api.Enum2.VALUE2, alias="param2") 

class EnumInterfaceFunc2Response(BaseModel):
    result: api.Enum2
    state: EnumInterfaceState

# method EnumInterface.func3
class EnumInterfaceFunc3Request(BaseModel):
    param3: api.Enum3 = Field(default=api.Enum3.VALUE3, alias="param3") 

class EnumInterfaceFunc3Response(BaseModel):
    result: api.Enum3
    state: EnumInterfaceState



