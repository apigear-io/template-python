import requests
import os

from counter.api import api
from . import shared
import custom_types.api
import extern_types.api
import vector3d.vector



class Counter(api.ICounter):
    def __init__(self, url='http://localhost:8000'):
        super().__init__()
        self._url = url        
        self._vector = custom_types.api.Vector3D()        
        self._extern_vector = vector3d.vector.Vector()
    
    def get_vector(self):
        return self._vector

    def set_vector(self, value):
        self._vector = value
    
    def get_extern_vector(self):
        return self._extern_vector

    def set_extern_vector(self, value):
        self._extern_vector = value

    def increment(self, vec: vector3d.vector.Vector):
        req = shared.CounterIncrementRequest(
            vec=vec
        )
        data = requests.post(
            f'{self.url}/counter/counter/increment',
            req.json()
        )
        resp = shared.CounterIncrementResponse(**data.json())
        self._vector = resp.state.vector
        self._extern_vector = resp.state.extern_vector

    def decrement(self, vec: custom_types.api.Vector3D):
        req = shared.CounterDecrementRequest(
            vec=vec
        )
        data = requests.post(
            f'{self.url}/counter/counter/decrement',
            req.json()
        )
        resp = shared.CounterDecrementResponse(**data.json())
        self._vector = resp.state.vector
        self._extern_vector = resp.state.extern_vector
