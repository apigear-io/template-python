from pydantic import BaseModel
from typing import Iterable
from org_objectapi_testbed.api import api

### Interface1 ###

# Service Signal Listener

class Interface1EventListener(object):

    def sig1(self):
        pass

    def sig2(self, step: int):
        pass

    def sig3(self):
        pass

# Service State Model

class Interface1State(BaseModel):
    prop1: bool
    prop2: int
    prop3: float
    prop4: str
    prop5: Iterable[int]
    prop6: api.Struct1
    prop7: int
    prop10: Iterable[int]
    prop11: Iterable[api.Struct1]
    prop12: Iterable[api.Enum1]
    prop14: Iterable[api.Struct1]

### Interface2 ###

# Service Signal Listener

class Interface2EventListener(object):
    pass

# Service State Model

class Interface2State(BaseModel):
    prop200: int
    prop201: int
    prop202: int
    prop203: float
    prop204: float
    prop205: str
