from counter.api import api
from utils.eventhook import EventHook
from typing import Iterable
import custom_types.api
import extern_types.api
import vector3d.vector

class Counter(api.ICounter):
    def __init__(self):
        super().__init__()
        self._vector: custom_types.api.Vector3D = custom_types.api.Vector3D()
        self._extern_vector: vector3d.vector.Vector = vector3d.vector.Vector()
        self.on_vector_changed: custom_types.api.Vector3D = EventHook()
        self.on_extern_vector_changed: vector3d.vector.Vector = EventHook()

    def set_vector(self, value):
        if self._vector == value:
            return
        self._vector = value
        self._push_vector(self._vector)
    
    def get_vector(self):
        return self._vector        

    def _push_vector(self, value):
        self.on_vector_changed.fire(value)

    def set_extern_vector(self, value):
        if self._extern_vector == value:
            return
        self._extern_vector = value
        self._push_extern_vector(self._extern_vector)
    
    def get_extern_vector(self):
        return self._extern_vector        

    def _push_extern_vector(self, value):
        self.on_extern_vector_changed.fire(value)

    def increment(self, vec: vector3d.vector.Vector) -> vector3d.vector.Vector:
        return vector3d.vector.Vector()

    def decrement(self, vec: custom_types.api.Vector3D) -> custom_types.api.Vector3D:
        return custom_types.api.Vector3D()
