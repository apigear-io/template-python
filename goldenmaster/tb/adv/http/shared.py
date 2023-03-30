from pydantic import BaseModel
from typing import Iterable
from tb.adv.api import api

# interface ManyParamInterface
class ManyParamInterfaceState(BaseModel):
    prop1: int
    prop2: int
    prop3: int
    prop4: int 

# interface NestedStruct1Interface
class NestedStruct1InterfaceState(BaseModel):
    prop1: api.NestedStruct1 

# interface NestedStruct2Interface
class NestedStruct2InterfaceState(BaseModel):
    prop1: api.NestedStruct1
    prop2: api.NestedStruct2 

# interface NestedStruct3Interface
class NestedStruct3InterfaceState(BaseModel):
    prop1: api.NestedStruct1
    prop2: api.NestedStruct2
    prop3: api.NestedStruct3  



