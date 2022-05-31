from org_objectapi_testbed.api import api
from typing import Iterable


class Interface2(api.IInterface2):
    def __init__(self):        
        self.__prop200: int = 0        
        self.__prop201: int = 0        
        self.__prop202: int = 0        
        self.__prop203: float = 0.0        
        self.__prop204: float = 0.0        
        self.__prop205: str = str()

    @property
    def prop200(self):
        return self.__prop200

    @property
    def prop201(self):
        return self.__prop201

    @property
    def prop202(self):
        return self.__prop202

    @property
    def prop203(self):
        return self.__prop203

    @property
    def prop204(self):
        return self.__prop204

    @property
    def prop205(self):
        return self.__prop205