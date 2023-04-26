from pydantic import BaseModel
from typing import Iterable
from tb.same1_api import api

class SameStruct1InterfaceState(BaseModel):
    prop1: api.Struct1

# method SameStruct1Interface.func1
class SameStruct1InterfaceFunc1Request(BaseModel):
    param1: api.Struct1 

class SameStruct1InterfaceFunc1Response(BaseModel):
    result: api.Struct1
    state: SameStruct1InterfaceState

class SameStruct2InterfaceState(BaseModel):
    prop1: api.Struct2
    prop2: api.Struct2

# method SameStruct2Interface.func1
class SameStruct2InterfaceFunc1Request(BaseModel):
    param1: api.Struct1 

class SameStruct2InterfaceFunc1Response(BaseModel):
    result: api.Struct1
    state: SameStruct2InterfaceState

# method SameStruct2Interface.func2
class SameStruct2InterfaceFunc2Request(BaseModel):
    param1: api.Struct1
    param2: api.Struct2 

class SameStruct2InterfaceFunc2Response(BaseModel):
    result: api.Struct1
    state: SameStruct2InterfaceState

class SameEnum1InterfaceState(BaseModel):
    prop1: api.Enum1

# method SameEnum1Interface.func1
class SameEnum1InterfaceFunc1Request(BaseModel):
    param1: api.Enum1 

class SameEnum1InterfaceFunc1Response(BaseModel):
    result: api.Enum1
    state: SameEnum1InterfaceState

class SameEnum2InterfaceState(BaseModel):
    prop1: api.Enum1
    prop2: api.Enum2

# method SameEnum2Interface.func1
class SameEnum2InterfaceFunc1Request(BaseModel):
    param1: api.Enum1 

class SameEnum2InterfaceFunc1Response(BaseModel):
    result: api.Enum1
    state: SameEnum2InterfaceState

# method SameEnum2Interface.func2
class SameEnum2InterfaceFunc2Request(BaseModel):
    param1: api.Enum1
    param2: api.Enum2 

class SameEnum2InterfaceFunc2Response(BaseModel):
    result: api.Enum1
    state: SameEnum2InterfaceState



