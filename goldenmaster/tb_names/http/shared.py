from pydantic import BaseModel, Field
from typing import Iterable
from tb.names.api import api

class NamEsState(BaseModel):
    switch: bool = Field(default=False, alias="Switch")
    some_property: int = Field(default=0, alias="SOME_PROPERTY")
    some_poperty2: int = Field(default=0, alias="Some_Poperty2")

# method Nam_Es.SOME_FUNCTION
class Nam_EsSomeFunctionRequest(BaseModel):
    some_param: bool = Field(default=False, alias="SOME_PARAM") 

class Nam_EsSomeFunctionResponse(BaseModel):
    result: None
    state: Nam_EsState

# method Nam_Es.Some_Function2
class Nam_EsSomeFunction2Request(BaseModel):
    some_param: bool = Field(default=False, alias="Some_Param") 

class Nam_EsSomeFunction2Response(BaseModel):
    result: None
    state: Nam_EsState



