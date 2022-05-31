from pydantic import BaseModel
from typing import Iterable
from enum import IntEnum

class Enum1(IntEnum):  
    Member1 = 0  
    Member2 = 1  
    Member3 = 2  
    Member4 = 3

class Enum2(IntEnum):  
    Member1 = 0  
    Member2 = 1  
    Member3 = 2  
    Member4 = 3

class Struct1(BaseModel):
    field1 : bool = False
    field2 : int = 0
    field3 : float = 0.0
    field4 : str = str()

class IInterface1:
    @property
    def prop1(self):
        raise NotImplementedError
    @property
    def prop2(self):
        raise NotImplementedError
    @property
    def prop3(self):
        raise NotImplementedError
    @property
    def prop4(self):
        raise NotImplementedError
    @property
    def prop5(self):
        raise NotImplementedError
    @property
    def prop6(self):
        raise NotImplementedError
    @property
    def prop7(self):
        raise NotImplementedError
    @property
    def prop10(self):
        raise NotImplementedError
    @property
    def prop11(self):
        raise NotImplementedError
    @property
    def prop12(self):
        raise NotImplementedError
    @property
    def prop14(self):
        raise NotImplementedError
    def op1(self):
        raise NotImplementedError
    def op2(self, step: int):
        raise NotImplementedError
    def op3(self):
        raise NotImplementedError

class IInterface2:
    @property
    def prop200(self):
        raise NotImplementedError
    @property
    def prop201(self):
        raise NotImplementedError
    @property
    def prop202(self):
        raise NotImplementedError
    @property
    def prop203(self):
        raise NotImplementedError
    @property
    def prop204(self):
        raise NotImplementedError
    @property
    def prop205(self):
        raise NotImplementedError

class Factory:
    def __init__(self):
        self.formats = {}

    def register_interface1(self, format, cls):
      self.formats[format] = cls

    def get_interface1(self, format):
        if format in self.formats:
          cls = self.formats[format]
          return cls()
        return None

    def register_interface2(self, format, cls):
      self.formats[format] = cls

    def get_interface2(self, format):
        if format in self.formats:
          cls = self.formats[format]
          return cls()
        return None
