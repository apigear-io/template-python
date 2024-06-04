from pydantic import BaseModel, Field
from typing import Iterable
from tb.same2.api import api

class SameStruct1InterfaceState(BaseModel):
    prop1: api.Struct1 = Field(default=api.Struct1(), alias="prop1")

# method SameStruct1Interface.func1
class SameStruct1InterfaceFunc1Request(BaseModel):
    param1: api.Struct1 = Field(default=api.Struct1(), alias="param1") 

class SameStruct1InterfaceFunc1Response(BaseModel):
    result: api.Struct1
    state: SameStruct1InterfaceState

class SameStruct2InterfaceState(BaseModel):
    prop1: api.Struct2 = Field(default=api.Struct2(), alias="prop1")
    prop2: api.Struct2 = Field(default=api.Struct2(), alias="prop2")

# method SameStruct2Interface.func1
class SameStruct2InterfaceFunc1Request(BaseModel):
    param1: api.Struct1 = Field(default=api.Struct1(), alias="param1") 

class SameStruct2InterfaceFunc1Response(BaseModel):
    result: api.Struct1
    state: SameStruct2InterfaceState

# method SameStruct2Interface.func2
class SameStruct2InterfaceFunc2Request(BaseModel):
    param1: api.Struct1 = Field(default=api.Struct1(), alias="param1")
    param2: api.Struct2 = Field(default=api.Struct2(), alias="param2") 

class SameStruct2InterfaceFunc2Response(BaseModel):
    result: api.Struct1
    state: SameStruct2InterfaceState

class SameEnum1InterfaceState(BaseModel):
    prop1: api.Enum1 = Field(default=api.Enum1.VALUE1, alias="prop1")

# method SameEnum1Interface.func1
class SameEnum1InterfaceFunc1Request(BaseModel):
    param1: api.Enum1 = Field(default=api.Enum1.VALUE1, alias="param1") 

class SameEnum1InterfaceFunc1Response(BaseModel):
    result: api.Enum1
    state: SameEnum1InterfaceState

class SameEnum2InterfaceState(BaseModel):
    prop1: api.Enum1 = Field(default=api.Enum1.VALUE1, alias="prop1")
    prop2: api.Enum2 = Field(default=api.Enum2.VALUE1, alias="prop2")

# method SameEnum2Interface.func1
class SameEnum2InterfaceFunc1Request(BaseModel):
    param1: api.Enum1 = Field(default=api.Enum1.VALUE1, alias="param1") 

class SameEnum2InterfaceFunc1Response(BaseModel):
    result: api.Enum1
    state: SameEnum2InterfaceState

# method SameEnum2Interface.func2
class SameEnum2InterfaceFunc2Request(BaseModel):
    param1: api.Enum1 = Field(default=api.Enum1.VALUE1, alias="param1")
    param2: api.Enum2 = Field(default=api.Enum2.VALUE1, alias="param2") 

class SameEnum2InterfaceFunc2Response(BaseModel):
    result: api.Enum1
    state: SameEnum2InterfaceState



