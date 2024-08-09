from pydantic import ConfigDict, BaseModel, Field
from enum import IntEnum
import custom_types.api
import extern_types.api
import vector3d.vector

class EnhancedModel(BaseModel):
    """This model is used to enforce the json encoding by alias"""
    model_config = ConfigDict(populate_by_name=True)

    def model_dump(self, **kwargs):
        kwargs.setdefault('by_alias', True)
        return super().model_dump(**kwargs)

    def __init__(self, **kw):
        super().__init__(**kw)

class ICounter:
    def __init__(self):
        pass

    def get_vector(self):
        raise NotImplementedError("Method counter/counter:get_vector is not implemented.")

    def set_vector(self, value):
        raise NotImplementedError("Method counter/counter:set_vector is not implemented.")

    def get_extern_vector(self):
        raise NotImplementedError("Method counter/counter:get_extern_vector is not implemented.")

    def set_extern_vector(self, value):
        raise NotImplementedError("Method counter/counter:set_extern_vector is not implemented.")

    def increment(self, vec: vector3d.vector.Vector):
        raise NotImplementedError("Method counter/counter:increment is not implemented.")

    def decrement(self, vec: custom_types.api.Vector3D):
        raise NotImplementedError("Method counter/counter:decrement is not implemented.")

