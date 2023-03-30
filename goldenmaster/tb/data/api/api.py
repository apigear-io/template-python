from pydantic import BaseModel
from enum import IntEnum



class StructBool(BaseModel):
    fieldBool: bool

class StructInt(BaseModel):
    fieldInt: int

class StructFloat(BaseModel):
    fieldFloat: float

class StructString(BaseModel):
    fieldString: str

class StructInterface(BaseModel):
    propBool: StructBool
    propInt: StructInt
    propFloat: StructFloat
    propString: StructString

    def funcBool(self, paramBool: StructBool):
        raise NotImplementedError

    def funcInt(self, paramInt: StructInt):
        raise NotImplementedError

    def funcFloat(self, paramFloat: StructFloat):
        raise NotImplementedError

    def funcString(self, paramString: StructString):
        raise NotImplementedError

class StructArrayInterface(BaseModel):
    propBool: list[StructBool]
    propInt: list[StructInt]
    propFloat: list[StructFloat]
    propString: list[StructString]

    def funcBool(self, paramBool: list[StructBool]):
        raise NotImplementedError

    def funcInt(self, paramInt: list[StructInt]):
        raise NotImplementedError

    def funcFloat(self, paramFloat: list[StructFloat]):
        raise NotImplementedError

    def funcString(self, paramString: list[StructString]):
        raise NotImplementedError
