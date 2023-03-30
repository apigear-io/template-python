from pydantic import BaseModel
from typing import Iterable
from tb.same.api import api

# interface SameStruct1Interface
class SameStruct1InterfaceState(BaseModel):
    prop1: api.Struct1 

# interface SameStruct2Interface
class SameStruct2InterfaceState(BaseModel):
    prop1: api.Struct2
    prop2: api.Struct2 

# interface SameEnum1Interface
class SameEnum1InterfaceState(BaseModel):
    prop1: api.Enum1 

# interface SameEnum2Interface
class SameEnum2InterfaceState(BaseModel):
    prop1: api.Enum1
    prop2: api.Enum2  



