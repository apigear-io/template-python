import requests
import os

from tb_names.api import api
from . import shared



class NamEs(api.INamEs):
    def __init__(self, url='http://localhost:8000'):
        super().__init__()
        self._url = url        
        self._switch = False        
        self._some_property = 0        
        self._some_poperty2 = 0
    
    def get_switch(self):
        return self._switch

    def set_switch(self, value):
        self._switch = value
    
    def get_some_property(self):
        return self._some_property

    def set_some_property(self, value):
        self._some_property = value
    
    def get_some_poperty2(self):
        return self._some_poperty2

    def set_some_poperty2(self, value):
        self._some_poperty2 = value

    def some_function(self, some_param: bool):
        req = shared.Nam_EsSomeFunctionRequest(
            some_param=some_param
        )
        data = requests.post(
            f'{self.url}/tb_names/nam_es/some_function',
            req.json()
        )
        resp = shared.NamEsSomeFunctionResponse(**data.json())
        self._switch = resp.state.switch
        self._some_property = resp.state.some_property
        self._some_poperty2 = resp.state.some_poperty2

    def some_function2(self, some_param: bool):
        req = shared.Nam_EsSomeFunction2Request(
            some_param=some_param
        )
        data = requests.post(
            f'{self.url}/tb_names/nam_es/some_function2',
            req.json()
        )
        resp = shared.NamEsSomeFunction2Response(**data.json())
        self._switch = resp.state.switch
        self._some_property = resp.state.some_property
        self._some_poperty2 = resp.state.some_poperty2
