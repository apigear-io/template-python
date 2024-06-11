import asyncio
from typing import Any
from olink.core import Name
from olink.client import IObjectSink, ClientNode
from utils.eventhook import EventHook
import utils.base_types
import tb_names.api
import logging

class NamEsSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._switch = False
        self.on_switch_changed = EventHook()
        self._some_property = 0
        self.on_some_property_changed = EventHook()
        self._some_poperty2 = 0
        self.on_some_poperty2_changed = EventHook()
        self.on_some_signal = EventHook()
        self.on_some_signal2 = EventHook()
        self._on_is_ready= EventHook()
        self.client = ClientNode.register_sink(self)

    def _set_switch(self, value):
        if self._switch == value:
            return
        self._switch = value
        self.on_switch_changed.fire(self._switch)

    def set_switch(self, value):
        if self._switch == value:
            return
        self.client.set_remote_property('tb.names.Nam_Es/Switch', utils.base_types.from_bool(value))

    def get_switch(self):
        return self._switch

    def _set_some_property(self, value):
        if self._some_property == value:
            return
        self._some_property = value
        self.on_some_property_changed.fire(self._some_property)

    def set_some_property(self, value):
        if self._some_property == value:
            return
        self.client.set_remote_property('tb.names.Nam_Es/SOME_PROPERTY', utils.base_types.from_int(value))

    def get_some_property(self):
        return self._some_property

    def _set_some_poperty2(self, value):
        if self._some_poperty2 == value:
            return
        self._some_poperty2 = value
        self.on_some_poperty2_changed.fire(self._some_poperty2)

    def set_some_poperty2(self, value):
        if self._some_poperty2 == value:
            return
        self.client.set_remote_property('tb.names.Nam_Es/Some_Poperty2', utils.base_types.from_int(value))

    def get_some_poperty2(self):
        return self._some_poperty2

    async def some_function(self, some_param: bool):
        _some_param = utils.base_types.from_bool(some_param)
        args = [_some_param]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(None)
        self.client.invoke_remote(f"tb.names.Nam_Es/SOME_FUNCTION", args, func)
        return await asyncio.wait_for(future, 500)

    async def some_function2(self, some_param: bool):
        _some_param = utils.base_types.from_bool(some_param)
        args = [_some_param]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(None)
        self.client.invoke_remote(f"tb.names.Nam_Es/Some_Function2", args, func)
        return await asyncio.wait_for(future, 500)

    def olink_object_name(self):
        return 'tb.names.Nam_Es'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "Switch":
                v =  utils.base_types.as_bool(props[k])
                self._set_switch(v)
            elif k == "SOME_PROPERTY":
                v =  utils.base_types.as_int(props[k])
                self._set_some_property(v)
            elif k == "Some_Poperty2":
                v =  utils.base_types.as_int(props[k])
                self._set_some_poperty2(v)
        self._on_is_ready.fire()

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "Switch":
            v =  utils.base_types.as_bool(value)
            self._set_switch(v)
            return
        elif path == "SOME_PROPERTY":
            v =  utils.base_types.as_int(value)
            self._set_some_property(v)
            return
        elif path == "Some_Poperty2":
            v =  utils.base_types.as_int(value)
            self._set_some_poperty2(v)
            return
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "SOME_SIGNAL":
            some_param =  utils.base_types.as_bool(args[0])
            self.on_some_signal.fire(some_param)
            return
        elif path == "Some_Signal2":
            some_param =  utils.base_types.as_bool(args[0])
            self.on_some_signal2.fire(some_param)
            return
        logging.error("unknown signal: %s", name)
