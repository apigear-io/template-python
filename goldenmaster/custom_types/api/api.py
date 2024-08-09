from pydantic import ConfigDict, BaseModel, Field
from enum import IntEnum

class EnhancedModel(BaseModel):
    """This model is used to enforce the json encoding by alias"""
    model_config = ConfigDict(populate_by_name=True)

    def model_dump(self, **kwargs):
        kwargs.setdefault('by_alias', True)
        return super().model_dump(**kwargs)

    def __init__(self, **kw):
        super().__init__(**kw)

class Vector3D(EnhancedModel):
    x: float = Field(default=0.0, alias="x")
    y: float = Field(default=0.0, alias="y")
    z: float = Field(default=0.0, alias="z")

    def __init__(self, **kw):
        super().__init__(**kw)

def as_vector3_d(v):
    return Vector3D.model_validate(v)

def from_vector3_d(v):
    return v.model_dump()

