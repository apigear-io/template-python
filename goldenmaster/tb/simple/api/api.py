from pydantic import BaseModel
from enum import IntEnum



class SimpleInterface(BaseModel):
    propBool: bool
    propInt: int
    propFloat: float
    propString: str

    def funcBool(self, paramBool: bool):
        raise NotImplementedError

    def funcInt(self, paramInt: int):
        raise NotImplementedError

    def funcFloat(self, paramFloat: float):
        raise NotImplementedError

    def funcString(self, paramString: str):
        raise NotImplementedError

class SimpleArrayInterface(BaseModel):
    propBool: list[bool]
    propInt: list[int]
    propFloat: list[float]
    propString: list[str]

    def funcBool(self, paramBool: list[bool]):
        raise NotImplementedError

    def funcInt(self, paramInt: list[int]):
        raise NotImplementedError

    def funcFloat(self, paramFloat: list[float]):
        raise NotImplementedError

    def funcString(self, paramString: list[str]):
        raise NotImplementedError
