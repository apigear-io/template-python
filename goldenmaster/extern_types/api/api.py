from pydantic import ConfigDict, BaseModel, Field
from enum import IntEnum
import vector3d.vector

class EnhancedModel(BaseModel):
    """This model is used to enforce the json encoding by alias"""
    model_config = ConfigDict(populate_by_name=True)

    def model_dump(self, **kwargs):
        kwargs.setdefault('by_alias', True)
        return super().model_dump(**kwargs)

    def __init__(self, **kw):
        super().__init__(**kw)
def as_vector3d_vector_vector(v):
    
    deserialized = vector3d.vector.Vector()
    # deserialize your vector3d.vector.Vector from json string
    return deserialized

def from_vector3d_vector_vector(v):
    serialized = ""
    #serialize your vector3d.vector.Vector here to json string
    return serialized

