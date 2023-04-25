import requests
import os

from demo_api import api
from . import shared



class Counter(api.ICounter):
    def __init__(self, url='http://localhost:8000'):
        super().__init__()
        self._url = url        
        self._value = 0
    
    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value
    def increment(self):
        req = shared.CounterIncrementRequest(
        )
        data = requests.post(
            f'{self.url}/demo/Counter/increment',
            req.json()
        )
        resp = shared.CounterIncrementResponse(**data.json())
        print(resp.json())
        self._value = resp.state.value
    def decrement(self):
        req = shared.CounterDecrementRequest(
        )
        data = requests.post(
            f'{self.url}/demo/Counter/decrement',
            req.json()
        )
        resp = shared.CounterDecrementResponse(**data.json())
        print(resp.json())
        self._value = resp.state.value
