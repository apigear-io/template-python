import requests
import os

from tb.data.api import api
from . import shared


API_SERVER = os.getenv('API_SERVER', 'http://localhost:8000')




class StructInterface(api.IStructInterface):
    def __init__(self):
        super().__init__()        
        self._propBool = {}        
        self._propInt = {}        
        self._propFloat = {}        
        self._propString = {}

    @property
    def propBool(self):
        return self._propBool

    @property
    def propInt(self):
        return self._propInt

    @property
    def propFloat(self):
        return self._propFloat

    @property
    def propString(self):
        return self._propString

    def funcBool(self, paramBool: StructBool):
        req = shared.StructInterfaceFuncBoolRequest(
            paramBool=paramBool
        )
        data = requests.post(
            f'{API_SERVER}/tb.data/StructInterface/funcBool',
            req.json()
        )
        resp = shared.StructInterfaceFuncBoolResponse(**data.json())
        print(resp.json())

        self._propBool = resp.state.propBool
        self._propInt = resp.state.propInt
        self._propFloat = resp.state.propFloat
        self._propString = resp.state.propString


    def funcInt(self, paramInt: StructInt):
        req = shared.StructInterfaceFuncIntRequest(
            paramInt=paramInt
        )
        data = requests.post(
            f'{API_SERVER}/tb.data/StructInterface/funcInt',
            req.json()
        )
        resp = shared.StructInterfaceFuncIntResponse(**data.json())
        print(resp.json())

        self._propBool = resp.state.propBool
        self._propInt = resp.state.propInt
        self._propFloat = resp.state.propFloat
        self._propString = resp.state.propString


    def funcFloat(self, paramFloat: StructFloat):
        req = shared.StructInterfaceFuncFloatRequest(
            paramFloat=paramFloat
        )
        data = requests.post(
            f'{API_SERVER}/tb.data/StructInterface/funcFloat',
            req.json()
        )
        resp = shared.StructInterfaceFuncFloatResponse(**data.json())
        print(resp.json())

        self._propBool = resp.state.propBool
        self._propInt = resp.state.propInt
        self._propFloat = resp.state.propFloat
        self._propString = resp.state.propString


    def funcString(self, paramString: StructString):
        req = shared.StructInterfaceFuncStringRequest(
            paramString=paramString
        )
        data = requests.post(
            f'{API_SERVER}/tb.data/StructInterface/funcString',
            req.json()
        )
        resp = shared.StructInterfaceFuncStringResponse(**data.json())
        print(resp.json())

        self._propBool = resp.state.propBool
        self._propInt = resp.state.propInt
        self._propFloat = resp.state.propFloat
        self._propString = resp.state.propString




class StructArrayInterface(api.IStructArrayInterface):
    def __init__(self):
        super().__init__()        
        self._propBool = []        
        self._propInt = []        
        self._propFloat = []        
        self._propString = []

    @property
    def propBool(self):
        return self._propBool

    @property
    def propInt(self):
        return self._propInt

    @property
    def propFloat(self):
        return self._propFloat

    @property
    def propString(self):
        return self._propString

    def funcBool(self, paramBool: list[StructBool]):
        req = shared.StructArrayInterfaceFuncBoolRequest(
            paramBool=paramBool
        )
        data = requests.post(
            f'{API_SERVER}/tb.data/StructArrayInterface/funcBool',
            req.json()
        )
        resp = shared.StructArrayInterfaceFuncBoolResponse(**data.json())
        print(resp.json())

        self._propBool = resp.state.propBool
        self._propInt = resp.state.propInt
        self._propFloat = resp.state.propFloat
        self._propString = resp.state.propString


    def funcInt(self, paramInt: list[StructInt]):
        req = shared.StructArrayInterfaceFuncIntRequest(
            paramInt=paramInt
        )
        data = requests.post(
            f'{API_SERVER}/tb.data/StructArrayInterface/funcInt',
            req.json()
        )
        resp = shared.StructArrayInterfaceFuncIntResponse(**data.json())
        print(resp.json())

        self._propBool = resp.state.propBool
        self._propInt = resp.state.propInt
        self._propFloat = resp.state.propFloat
        self._propString = resp.state.propString


    def funcFloat(self, paramFloat: list[StructFloat]):
        req = shared.StructArrayInterfaceFuncFloatRequest(
            paramFloat=paramFloat
        )
        data = requests.post(
            f'{API_SERVER}/tb.data/StructArrayInterface/funcFloat',
            req.json()
        )
        resp = shared.StructArrayInterfaceFuncFloatResponse(**data.json())
        print(resp.json())

        self._propBool = resp.state.propBool
        self._propInt = resp.state.propInt
        self._propFloat = resp.state.propFloat
        self._propString = resp.state.propString


    def funcString(self, paramString: list[StructString]):
        req = shared.StructArrayInterfaceFuncStringRequest(
            paramString=paramString
        )
        data = requests.post(
            f'{API_SERVER}/tb.data/StructArrayInterface/funcString',
            req.json()
        )
        resp = shared.StructArrayInterfaceFuncStringResponse(**data.json())
        print(resp.json())

        self._propBool = resp.state.propBool
        self._propInt = resp.state.propInt
        self._propFloat = resp.state.propFloat
        self._propString = resp.state.propString



