import requests
import os

from org_objectapi_testbed.api import api
from . import shared


API_SERVER = os.getenv('API_SERVER', 'http://localhost:8000')


class Interface1(api.IInterface1):
    def __init__(self):
        super().__init__()
        self._prop1 = False
        self._prop2 = 0
        self._prop3 = 0.0
        self._prop4 = str()
        self._prop5 = []
        self._prop6 = {}
        self._prop7 = 0
        self._prop10 = []
        self._prop11 = []
        self._prop12 = []
        self._prop14 = []

    @property
    def prop1(self):
        return self._prop1

    @property
    def prop2(self):
        return self._prop2

    @property
    def prop3(self):
        return self._prop3

    @property
    def prop4(self):
        return self._prop4

    @property
    def prop5(self):
        return self._prop5

    @property
    def prop6(self):
        return self._prop6

    @property
    def prop7(self):
        return self._prop7

    @property
    def prop10(self):
        return self._prop10

    @property
    def prop11(self):
        return self._prop11

    @property
    def prop12(self):
        return self._prop12

    @property
    def prop14(self):
        return self._prop14

    def op1(self):
        req = shared.Interface1Op1Request(          
        )
        data = requests.post(
            f'{API_SERVER}/org.objectapi.testbed/Interface1/op1',
            req.json()
        )
        resp = shared.Interface1Op1Response(**data.json())
        print(resp.json())
        self._prop1 = resp.state.prop1
        self._prop2 = resp.state.prop2
        self._prop3 = resp.state.prop3
        self._prop4 = resp.state.prop4
        self._prop5 = resp.state.prop5
        self._prop6 = resp.state.prop6
        self._prop7 = resp.state.prop7
        self._prop10 = resp.state.prop10
        self._prop11 = resp.state.prop11
        self._prop12 = resp.state.prop12
        self._prop14 = resp.state.prop14

    def op2(self, step: int):
        req = shared.Interface1Op2Request(
            step=step          
        )
        data = requests.post(
            f'{API_SERVER}/org.objectapi.testbed/Interface1/op2',
            req.json()
        )
        resp = shared.Interface1Op2Response(**data.json())
        print(resp.json())
        self._prop1 = resp.state.prop1
        self._prop2 = resp.state.prop2
        self._prop3 = resp.state.prop3
        self._prop4 = resp.state.prop4
        self._prop5 = resp.state.prop5
        self._prop6 = resp.state.prop6
        self._prop7 = resp.state.prop7
        self._prop10 = resp.state.prop10
        self._prop11 = resp.state.prop11
        self._prop12 = resp.state.prop12
        self._prop14 = resp.state.prop14

    def op3(self):
        req = shared.Interface1Op3Request(          
        )
        data = requests.post(
            f'{API_SERVER}/org.objectapi.testbed/Interface1/op3',
            req.json()
        )
        resp = shared.Interface1Op3Response(**data.json())
        print(resp.json())
        self._prop1 = resp.state.prop1
        self._prop2 = resp.state.prop2
        self._prop3 = resp.state.prop3
        self._prop4 = resp.state.prop4
        self._prop5 = resp.state.prop5
        self._prop6 = resp.state.prop6
        self._prop7 = resp.state.prop7
        self._prop10 = resp.state.prop10
        self._prop11 = resp.state.prop11
        self._prop12 = resp.state.prop12
        self._prop14 = resp.state.prop14


class Interface2(api.IInterface2):
    def __init__(self):
        super().__init__()
        self._prop200 = 0
        self._prop201 = 0
        self._prop202 = 0
        self._prop203 = 0.0
        self._prop204 = 0.0
        self._prop205 = str()

    @property
    def prop200(self):
        return self._prop200

    @property
    def prop201(self):
        return self._prop201

    @property
    def prop202(self):
        return self._prop202

    @property
    def prop203(self):
        return self._prop203

    @property
    def prop204(self):
        return self._prop204

    @property
    def prop205(self):
        return self._prop205
