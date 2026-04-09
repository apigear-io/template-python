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
        self._vector_array: list[custom_types.api.Vector3D] = []
        self._extern_vector_array: list[vector3d.vector.Vector] = []
        self.on_vector_changed: custom_types.api.Vector3D = EventHook()
        self.on_extern_vector_changed: vector3d.vector.Vector = EventHook()
        self.on_vector_array_changed: list[custom_types.api.Vector3D] = EventHook()
        self.on_extern_vector_array_changed: list[vector3d.vector.Vector] = EventHook()
        self.on_value_changed = EventHook()

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

    def set_vector_array(self, value):
        if self._vector_array == value:
            return
        self._vector_array = value
        self._push_vector_array(self._vector_array)
    
    def get_vector_array(self):
        return self._vector_array        

    def _push_vector_array(self, value):
        self.on_vector_array_changed.fire(value)

    def set_extern_vector_array(self, value):
        if self._extern_vector_array == value:
            return
        self._extern_vector_array = value
        self._push_extern_vector_array(self._extern_vector_array)
    
    def get_extern_vector_array(self):
        return self._extern_vector_array        

    def _push_extern_vector_array(self, value):
        self.on_extern_vector_array_changed.fire(value)

    def increment(self, vec: vector3d.vector.Vector) -> vector3d.vector.Vector:
        return vector3d.vector.Vector()

    def increment_array(self, vec: list[vector3d.vector.Vector]) -> list[vector3d.vector.Vector]:
        return []

    def decrement(self, vec: custom_types.api.Vector3D) -> custom_types.api.Vector3D:
        return custom_types.api.Vector3D()

    def decrement_array(self, vec: list[custom_types.api.Vector3D]) -> list[custom_types.api.Vector3D]:
        return []

    def _value_changed(self, vector: custom_types.api.Vector3D, extern_vector: vector3d.vector.Vector, vector_array: list[custom_types.api.Vector3D], extern_vector_array: list[vector3d.vector.Vector]):
        self.on_value_changed.fire(vector, extern_vector, vector_array, extern_vector_array)
