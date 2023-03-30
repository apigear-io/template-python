import requests
import os

from tb.simple.api import api
from . import shared


API_SERVER = os.getenv('API_SERVER', 'http://localhost:8000')




class SimpleInterface(api.ISimpleInterface):
    def __init__(self):
        super().__init__()        
        self._propBool = False        
        self._propInt = 0        
        self._propFloat = 0.0        
        self._propString = ""

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

    def funcBool(self, paramBool: bool):
        req = shared.SimpleInterfaceFuncBoolRequest(
            paramBool=paramBool
        )
        data = requests.post(
            f'{API_SERVER}/tb.simple/SimpleInterface/funcBool',
            req.json()
        )
        resp = shared.SimpleInterfaceFuncBoolResponse(**data.json())
        print(resp.json())

        self._propBool = resp.state.propBool
        self._propInt = resp.state.propInt
        self._propFloat = resp.state.propFloat
        self._propString = resp.state.propString


    def funcInt(self, paramInt: int):
        req = shared.SimpleInterfaceFuncIntRequest(
            paramInt=paramInt
        )
        data = requests.post(
            f'{API_SERVER}/tb.simple/SimpleInterface/funcInt',
            req.json()
        )
        resp = shared.SimpleInterfaceFuncIntResponse(**data.json())
        print(resp.json())

        self._propBool = resp.state.propBool
        self._propInt = resp.state.propInt
        self._propFloat = resp.state.propFloat
        self._propString = resp.state.propString


    def funcFloat(self, paramFloat: float):
        req = shared.SimpleInterfaceFuncFloatRequest(
            paramFloat=paramFloat
        )
        data = requests.post(
            f'{API_SERVER}/tb.simple/SimpleInterface/funcFloat',
            req.json()
        )
        resp = shared.SimpleInterfaceFuncFloatResponse(**data.json())
        print(resp.json())

        self._propBool = resp.state.propBool
        self._propInt = resp.state.propInt
        self._propFloat = resp.state.propFloat
        self._propString = resp.state.propString


    def funcString(self, paramString: str):
        req = shared.SimpleInterfaceFuncStringRequest(
            paramString=paramString
        )
        data = requests.post(
            f'{API_SERVER}/tb.simple/SimpleInterface/funcString',
            req.json()
        )
        resp = shared.SimpleInterfaceFuncStringResponse(**data.json())
        print(resp.json())

        self._propBool = resp.state.propBool
        self._propInt = resp.state.propInt
        self._propFloat = resp.state.propFloat
        self._propString = resp.state.propString




class SimpleArrayInterface(api.ISimpleArrayInterface):
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

    def funcBool(self, paramBool: list[bool]):
        req = shared.SimpleArrayInterfaceFuncBoolRequest(
            paramBool=paramBool
        )
        data = requests.post(
            f'{API_SERVER}/tb.simple/SimpleArrayInterface/funcBool',
            req.json()
        )
        resp = shared.SimpleArrayInterfaceFuncBoolResponse(**data.json())
        print(resp.json())

        self._propBool = resp.state.propBool
        self._propInt = resp.state.propInt
        self._propFloat = resp.state.propFloat
        self._propString = resp.state.propString


    def funcInt(self, paramInt: list[int]):
        req = shared.SimpleArrayInterfaceFuncIntRequest(
            paramInt=paramInt
        )
        data = requests.post(
            f'{API_SERVER}/tb.simple/SimpleArrayInterface/funcInt',
            req.json()
        )
        resp = shared.SimpleArrayInterfaceFuncIntResponse(**data.json())
        print(resp.json())

        self._propBool = resp.state.propBool
        self._propInt = resp.state.propInt
        self._propFloat = resp.state.propFloat
        self._propString = resp.state.propString


    def funcFloat(self, paramFloat: list[float]):
        req = shared.SimpleArrayInterfaceFuncFloatRequest(
            paramFloat=paramFloat
        )
        data = requests.post(
            f'{API_SERVER}/tb.simple/SimpleArrayInterface/funcFloat',
            req.json()
        )
        resp = shared.SimpleArrayInterfaceFuncFloatResponse(**data.json())
        print(resp.json())

        self._propBool = resp.state.propBool
        self._propInt = resp.state.propInt
        self._propFloat = resp.state.propFloat
        self._propString = resp.state.propString


    def funcString(self, paramString: list[str]):
        req = shared.SimpleArrayInterfaceFuncStringRequest(
            paramString=paramString
        )
        data = requests.post(
            f'{API_SERVER}/tb.simple/SimpleArrayInterface/funcString',
            req.json()
        )
        resp = shared.SimpleArrayInterfaceFuncStringResponse(**data.json())
        print(resp.json())

        self._propBool = resp.state.propBool
        self._propInt = resp.state.propInt
        self._propFloat = resp.state.propFloat
        self._propString = resp.state.propString



