from pydantic import BaseModel, Field
from typing import Iterable
from counter.api import api

class CounterState(BaseModel):
    vector: custom_types.api.Vector3D = Field(default=custom_types.api.Vector3D(), alias="vector")
    extern_vector: vector3d.vector.Vector = Field(default=vector3d.vector.Vector(), alias="extern_vector")
    vector_array: list[custom_types.api.Vector3D] = Field(default=[], alias="vectorArray")
    extern_vector_array: list[vector3d.vector.Vector] = Field(default=[], alias="extern_vectorArray")

# method Counter.increment
class CounterIncrementRequest(BaseModel):
    vec: vector3d.vector.Vector = Field(default=vector3d.vector.Vector(), alias="vec") 

class CounterIncrementResponse(BaseModel):
    result: vector3d.vector.Vector
    state: CounterState

# method Counter.incrementArray
class CounterIncrementArrayRequest(BaseModel):
    vec: list[vector3d.vector.Vector] = Field(default=[], alias="vec") 

class CounterIncrementArrayResponse(BaseModel):
    result: list[vector3d.vector.Vector]
    state: CounterState

# method Counter.decrement
class CounterDecrementRequest(BaseModel):
    vec: custom_types.api.Vector3D = Field(default=custom_types.api.Vector3D(), alias="vec") 

class CounterDecrementResponse(BaseModel):
    result: custom_types.api.Vector3D
    state: CounterState

# method Counter.decrementArray
class CounterDecrementArrayRequest(BaseModel):
    vec: list[custom_types.api.Vector3D] = Field(default=[], alias="vec") 

class CounterDecrementArrayResponse(BaseModel):
    result: list[custom_types.api.Vector3D]
    state: CounterState



