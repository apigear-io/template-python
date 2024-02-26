from pydantic import BaseModel, Field
from typing import Iterable
from tb.simple_api import api

class SimpleInterfaceState(BaseModel):
    prop_bool: bool = Field(default=False, alias="propBool")
    prop_int: int = Field(default=0, alias="propInt")
    prop_int32: int = Field(default=0, alias="propInt32")
    prop_int64: int = Field(default=0, alias="propInt64")
    prop_float: float = Field(default=0.0, alias="propFloat")
    prop_float32: float = Field(default=0.0, alias="propFloat32")
    prop_float64: float = Field(default=0.0, alias="propFloat64")
    prop_string: str = Field(default="", alias="propString")
    prop_read_only_string: str = Field(default="", alias="propReadOnlyString")

# method SimpleInterface.funcVoid
class SimpleInterfaceFuncVoidRequest(BaseModel):
    pass 

class SimpleInterfaceFuncVoidResponse(BaseModel):
    result: None
    state: SimpleInterfaceState

# method SimpleInterface.funcBool
class SimpleInterfaceFuncBoolRequest(BaseModel):
    param_bool: bool = Field(default=False, alias="paramBool") 

class SimpleInterfaceFuncBoolResponse(BaseModel):
    result: bool
    state: SimpleInterfaceState

# method SimpleInterface.funcInt
class SimpleInterfaceFuncIntRequest(BaseModel):
    param_int: int = Field(default=0, alias="paramInt") 

class SimpleInterfaceFuncIntResponse(BaseModel):
    result: int
    state: SimpleInterfaceState

# method SimpleInterface.funcInt32
class SimpleInterfaceFuncInt32Request(BaseModel):
    param_int32: int = Field(default=0, alias="paramInt32") 

class SimpleInterfaceFuncInt32Response(BaseModel):
    result: int
    state: SimpleInterfaceState

# method SimpleInterface.funcInt64
class SimpleInterfaceFuncInt64Request(BaseModel):
    param_int64: int = Field(default=0, alias="paramInt64") 

class SimpleInterfaceFuncInt64Response(BaseModel):
    result: int
    state: SimpleInterfaceState

# method SimpleInterface.funcFloat
class SimpleInterfaceFuncFloatRequest(BaseModel):
    param_float: float = Field(default=0.0, alias="paramFloat") 

class SimpleInterfaceFuncFloatResponse(BaseModel):
    result: float
    state: SimpleInterfaceState

# method SimpleInterface.funcFloat32
class SimpleInterfaceFuncFloat32Request(BaseModel):
    param_float32: float = Field(default=0.0, alias="paramFloat32") 

class SimpleInterfaceFuncFloat32Response(BaseModel):
    result: float
    state: SimpleInterfaceState

# method SimpleInterface.funcFloat64
class SimpleInterfaceFuncFloat64Request(BaseModel):
    param_float: float = Field(default=0.0, alias="paramFloat") 

class SimpleInterfaceFuncFloat64Response(BaseModel):
    result: float
    state: SimpleInterfaceState

# method SimpleInterface.funcString
class SimpleInterfaceFuncStringRequest(BaseModel):
    param_string: str = Field(default="", alias="paramString") 

class SimpleInterfaceFuncStringResponse(BaseModel):
    result: str
    state: SimpleInterfaceState

class SimpleArrayInterfaceState(BaseModel):
    prop_bool: list[bool] = Field(default=[], alias="propBool")
    prop_int: list[int] = Field(default=[], alias="propInt")
    prop_int32: list[int] = Field(default=[], alias="propInt32")
    prop_int64: list[int] = Field(default=[], alias="propInt64")
    prop_float: list[float] = Field(default=[], alias="propFloat")
    prop_float32: list[float] = Field(default=[], alias="propFloat32")
    prop_float64: list[float] = Field(default=[], alias="propFloat64")
    prop_string: list[str] = Field(default=[], alias="propString")

# method SimpleArrayInterface.funcBool
class SimpleArrayInterfaceFuncBoolRequest(BaseModel):
    param_bool: list[bool] = Field(default=[], alias="paramBool") 

class SimpleArrayInterfaceFuncBoolResponse(BaseModel):
    result: list[bool]
    state: SimpleArrayInterfaceState

# method SimpleArrayInterface.funcInt
class SimpleArrayInterfaceFuncIntRequest(BaseModel):
    param_int: list[int] = Field(default=[], alias="paramInt") 

class SimpleArrayInterfaceFuncIntResponse(BaseModel):
    result: list[int]
    state: SimpleArrayInterfaceState

# method SimpleArrayInterface.funcInt32
class SimpleArrayInterfaceFuncInt32Request(BaseModel):
    param_int32: list[int] = Field(default=[], alias="paramInt32") 

class SimpleArrayInterfaceFuncInt32Response(BaseModel):
    result: list[int]
    state: SimpleArrayInterfaceState

# method SimpleArrayInterface.funcInt64
class SimpleArrayInterfaceFuncInt64Request(BaseModel):
    param_int64: list[int] = Field(default=[], alias="paramInt64") 

class SimpleArrayInterfaceFuncInt64Response(BaseModel):
    result: list[int]
    state: SimpleArrayInterfaceState

# method SimpleArrayInterface.funcFloat
class SimpleArrayInterfaceFuncFloatRequest(BaseModel):
    param_float: list[float] = Field(default=[], alias="paramFloat") 

class SimpleArrayInterfaceFuncFloatResponse(BaseModel):
    result: list[float]
    state: SimpleArrayInterfaceState

# method SimpleArrayInterface.funcFloat32
class SimpleArrayInterfaceFuncFloat32Request(BaseModel):
    param_float32: list[float] = Field(default=[], alias="paramFloat32") 

class SimpleArrayInterfaceFuncFloat32Response(BaseModel):
    result: list[float]
    state: SimpleArrayInterfaceState

# method SimpleArrayInterface.funcFloat64
class SimpleArrayInterfaceFuncFloat64Request(BaseModel):
    param_float: list[float] = Field(default=[], alias="paramFloat") 

class SimpleArrayInterfaceFuncFloat64Response(BaseModel):
    result: list[float]
    state: SimpleArrayInterfaceState

# method SimpleArrayInterface.funcString
class SimpleArrayInterfaceFuncStringRequest(BaseModel):
    param_string: list[str] = Field(default=[], alias="paramString") 

class SimpleArrayInterfaceFuncStringResponse(BaseModel):
    result: list[str]
    state: SimpleArrayInterfaceState

class NoPropertiesInterfaceState(BaseModel):
    pass

# method NoPropertiesInterface.funcVoid
class NoPropertiesInterfaceFuncVoidRequest(BaseModel):
    pass 

class NoPropertiesInterfaceFuncVoidResponse(BaseModel):
    result: None
    state: NoPropertiesInterfaceState

# method NoPropertiesInterface.funcBool
class NoPropertiesInterfaceFuncBoolRequest(BaseModel):
    param_bool: bool = Field(default=False, alias="paramBool") 

class NoPropertiesInterfaceFuncBoolResponse(BaseModel):
    result: bool
    state: NoPropertiesInterfaceState

class NoOperationsInterfaceState(BaseModel):
    prop_bool: bool = Field(default=False, alias="propBool")
    prop_int: int = Field(default=0, alias="propInt")

class NoSignalsInterfaceState(BaseModel):
    prop_bool: bool = Field(default=False, alias="propBool")
    prop_int: int = Field(default=0, alias="propInt")

# method NoSignalsInterface.funcVoid
class NoSignalsInterfaceFuncVoidRequest(BaseModel):
    pass 

class NoSignalsInterfaceFuncVoidResponse(BaseModel):
    result: None
    state: NoSignalsInterfaceState

# method NoSignalsInterface.funcBool
class NoSignalsInterfaceFuncBoolRequest(BaseModel):
    param_bool: bool = Field(default=False, alias="paramBool") 

class NoSignalsInterfaceFuncBoolResponse(BaseModel):
    result: bool
    state: NoSignalsInterfaceState

class EmptyInterfaceState(BaseModel):
    pass



