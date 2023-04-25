from pydantic import BaseModel
from typing import Iterable
from demo_api import api

class CounterState(BaseModel):
    value: int

# method Counter.increment
class CounterIncrementRequest(BaseModel):
    pass 

class CounterIncrementResponse(BaseModel):
    result: None
    state: CounterState

# method Counter.decrement
class CounterDecrementRequest(BaseModel):
    pass 

class CounterDecrementResponse(BaseModel):
    result: None
    state: CounterState



