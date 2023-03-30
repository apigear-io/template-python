from pydantic import BaseModel
from typing import Iterable
from tb.conflict.api import api

# interface Conflict1
class Conflict1State(BaseModel):
    sameName: int 

# interface Conflict2
class Conflict2State(BaseModel):
    sameName: int 

# interface Conflict3
class Conflict3State(BaseModel):
    pass 

# interface Conflict4
class Conflict4State(BaseModel):
    pass  



