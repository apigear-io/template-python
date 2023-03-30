import requests
import os

from tb.enum.api import api
from . import shared


API_SERVER = os.getenv('API_SERVER', 'http://localhost:8000')




class EnumInterface(api.IEnumInterface):
    def __init__(self):
        super().__init__()        
        self._prop0 = Enum0.value0        
        self._prop1 = Enum1.value1        
        self._prop2 = Enum2.value2        
        self._prop3 = Enum3.value3

    @property
    def prop0(self):
        return self._prop0

    @property
    def prop1(self):
        return self._prop1

    @property
    def prop2(self):
        return self._prop2

    @property
    def prop3(self):
        return self._prop3

    def func0(self, param0: Enum0):
        req = shared.EnumInterfaceFunc0Request(
            param0=param0
        )
        data = requests.post(
            f'{API_SERVER}/tb.enum/EnumInterface/func0',
            req.json()
        )
        resp = shared.EnumInterfaceFunc0Response(**data.json())
        print(resp.json())

        self._prop0 = resp.state.prop0
        self._prop1 = resp.state.prop1
        self._prop2 = resp.state.prop2
        self._prop3 = resp.state.prop3


    def func1(self, param1: Enum1):
        req = shared.EnumInterfaceFunc1Request(
            param1=param1
        )
        data = requests.post(
            f'{API_SERVER}/tb.enum/EnumInterface/func1',
            req.json()
        )
        resp = shared.EnumInterfaceFunc1Response(**data.json())
        print(resp.json())

        self._prop0 = resp.state.prop0
        self._prop1 = resp.state.prop1
        self._prop2 = resp.state.prop2
        self._prop3 = resp.state.prop3


    def func2(self, param2: Enum2):
        req = shared.EnumInterfaceFunc2Request(
            param2=param2
        )
        data = requests.post(
            f'{API_SERVER}/tb.enum/EnumInterface/func2',
            req.json()
        )
        resp = shared.EnumInterfaceFunc2Response(**data.json())
        print(resp.json())

        self._prop0 = resp.state.prop0
        self._prop1 = resp.state.prop1
        self._prop2 = resp.state.prop2
        self._prop3 = resp.state.prop3


    def func3(self, param3: Enum3):
        req = shared.EnumInterfaceFunc3Request(
            param3=param3
        )
        data = requests.post(
            f'{API_SERVER}/tb.enum/EnumInterface/func3',
            req.json()
        )
        resp = shared.EnumInterfaceFunc3Response(**data.json())
        print(resp.json())

        self._prop0 = resp.state.prop0
        self._prop1 = resp.state.prop1
        self._prop2 = resp.state.prop2
        self._prop3 = resp.state.prop3



