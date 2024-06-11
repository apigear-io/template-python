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

class INamEs:
    def __init__(self):
        pass

    def get_switch(self):
        raise NotImplementedError("Method tb.names/nam_es:get_switch is not implemented.")

    def set_switch(self, value):
        raise NotImplementedError("Method tb.names/nam_es:set_switch is not implemented.")

    def get_some_property(self):
        raise NotImplementedError("Method tb.names/nam_es:get_some_property is not implemented.")

    def set_some_property(self, value):
        raise NotImplementedError("Method tb.names/nam_es:set_some_property is not implemented.")

    def get_some_poperty2(self):
        raise NotImplementedError("Method tb.names/nam_es:get_some_poperty2 is not implemented.")

    def set_some_poperty2(self, value):
        raise NotImplementedError("Method tb.names/nam_es:set_some_poperty2 is not implemented.")

    def some_function(self, some_param: bool):
        raise NotImplementedError("Method tb.names/nam_es:some_function is not implemented.")

    def some_function2(self, some_param: bool):
        raise NotImplementedError("Method tb.names/nam_es:some_function2 is not implemented.")

