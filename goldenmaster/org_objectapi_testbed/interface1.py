from org_objectapi_testbed.api import api
from typing import Iterable


class Interface1(api.IInterface1):
    def __init__(self):        
        self.__prop1: bool = False        
        self.__prop2: int = 0        
        self.__prop3: float = 0.0        
        self.__prop4: str = str()        
        self.__prop5: Iterable[int] = []        
        self.__prop6: api.Struct1 = {}        
        self.__prop7: int = 0        
        self.__prop10: Iterable[int] = []        
        self.__prop11: Iterable[api.Struct1] = []        
        self.__prop12: Iterable[api.Enum1] = []        
        self.__prop14: Iterable[api.Struct1] = []

    @property
    def prop1(self):
        return self.__prop1

    @property
    def prop2(self):
        return self.__prop2

    @property
    def prop3(self):
        return self.__prop3

    @property
    def prop4(self):
        return self.__prop4

    @property
    def prop5(self):
        return self.__prop5

    @property
    def prop6(self):
        return self.__prop6

    @property
    def prop7(self):
        return self.__prop7

    @property
    def prop10(self):
        return self.__prop10

    @property
    def prop11(self):
        return self.__prop11

    @property
    def prop12(self):
        return self.__prop12

    @property
    def prop14(self):
        return self.__prop14

    def op1(self) -> None:
        return None

    def op2(self, step: int) -> None:
        return None

    def op3(self) -> int:
        return 0