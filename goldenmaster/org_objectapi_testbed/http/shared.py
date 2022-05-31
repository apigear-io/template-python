from pydantic import BaseModel
from typing import Iterable
from org_objectapi_testbed.api import api


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


class Interface1Op1Request(BaseModel):
    pass


class Interface1Op1Response(BaseModel):
    pass
    state: Interface1State


class Interface1Op2Request(BaseModel):
    step: int


class Interface1Op2Response(BaseModel):
    pass
    state: Interface1State


class Interface1Op3Request(BaseModel):
    pass


class Interface1Op3Response(BaseModel):
    result: int
    state: Interface1State


class Interface2State(BaseModel):
    prop200: int
    prop201: int
    prop202: int
    prop203: float
    prop204: float
    prop205: str
