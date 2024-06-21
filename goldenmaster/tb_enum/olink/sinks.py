import asyncio
from typing import Any
from olink.core import Name
from olink.client import IObjectSink, ClientNode
from utils.eventhook import EventHook
import utils.base_types
import tb_enum.api
import logging

class EnumInterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._prop0 = tb_enum.api.Enum0.VALUE0
        self.on_prop0_changed = EventHook()
        self._prop1 = tb_enum.api.Enum1.VALUE1
        self.on_prop1_changed = EventHook()
        self._prop2 = tb_enum.api.Enum2.VALUE2
        self.on_prop2_changed = EventHook()
        self._prop3 = tb_enum.api.Enum3.VALUE3
        self.on_prop3_changed = EventHook()
        self.on_sig0 = EventHook()
        self.on_sig1 = EventHook()
        self.on_sig2 = EventHook()
        self.on_sig3 = EventHook()
        self._on_is_ready= EventHook()
        self.client = ClientNode.register_sink(self)

    def _set_prop0(self, value):
        if self._prop0 == value:
            return
        self._prop0 = value
        self.on_prop0_changed.fire(self._prop0)

    def set_prop0(self, value):
        if self._prop0 == value:
            return
        self.client.set_remote_property('tb.enum.EnumInterface/prop0', tb_enum.api.from_enum0(value))

    def get_prop0(self):
        return self._prop0

    def _set_prop1(self, value):
        if self._prop1 == value:
            return
        self._prop1 = value
        self.on_prop1_changed.fire(self._prop1)

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        self.client.set_remote_property('tb.enum.EnumInterface/prop1', tb_enum.api.from_enum1(value))

    def get_prop1(self):
        return self._prop1

    def _set_prop2(self, value):
        if self._prop2 == value:
            return
        self._prop2 = value
        self.on_prop2_changed.fire(self._prop2)

    def set_prop2(self, value):
        if self._prop2 == value:
            return
        self.client.set_remote_property('tb.enum.EnumInterface/prop2', tb_enum.api.from_enum2(value))

    def get_prop2(self):
        return self._prop2

    def _set_prop3(self, value):
        if self._prop3 == value:
            return
        self._prop3 = value
        self.on_prop3_changed.fire(self._prop3)

    def set_prop3(self, value):
        if self._prop3 == value:
            return
        self.client.set_remote_property('tb.enum.EnumInterface/prop3', tb_enum.api.from_enum3(value))

    def get_prop3(self):
        return self._prop3

    async def func0(self, param0: tb_enum.api.Enum0):
        _param0 = tb_enum.api.from_enum0(param0)
        args = [_param0]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(tb_enum.api.as_enum0(result.value))
        self.client.invoke_remote(f"tb.enum.EnumInterface/func0", args, func)
        return await asyncio.wait_for(future, 500)

    async def func1(self, param1: tb_enum.api.Enum1):
        _param1 = tb_enum.api.from_enum1(param1)
        args = [_param1]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(tb_enum.api.as_enum1(result.value))
        self.client.invoke_remote(f"tb.enum.EnumInterface/func1", args, func)
        return await asyncio.wait_for(future, 500)

    async def func2(self, param2: tb_enum.api.Enum2):
        _param2 = tb_enum.api.from_enum2(param2)
        args = [_param2]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(tb_enum.api.as_enum2(result.value))
        self.client.invoke_remote(f"tb.enum.EnumInterface/func2", args, func)
        return await asyncio.wait_for(future, 500)

    async def func3(self, param3: tb_enum.api.Enum3):
        _param3 = tb_enum.api.from_enum3(param3)
        args = [_param3]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(tb_enum.api.as_enum3(result.value))
        self.client.invoke_remote(f"tb.enum.EnumInterface/func3", args, func)
        return await asyncio.wait_for(future, 500)

    def olink_object_name(self):
        return 'tb.enum.EnumInterface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "prop0":
                v =  tb_enum.api.as_enum0(props[k])
                self._set_prop0(v)
            elif k == "prop1":
                v =  tb_enum.api.as_enum1(props[k])
                self._set_prop1(v)
            elif k == "prop2":
                v =  tb_enum.api.as_enum2(props[k])
                self._set_prop2(v)
            elif k == "prop3":
                v =  tb_enum.api.as_enum3(props[k])
                self._set_prop3(v)
        self._on_is_ready.fire()

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "prop0":
            v =  tb_enum.api.as_enum0(value)
            self._set_prop0(v)
            return
        elif path == "prop1":
            v =  tb_enum.api.as_enum1(value)
            self._set_prop1(v)
            return
        elif path == "prop2":
            v =  tb_enum.api.as_enum2(value)
            self._set_prop2(v)
            return
        elif path == "prop3":
            v =  tb_enum.api.as_enum3(value)
            self._set_prop3(v)
            return
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sig0":
            param0 =  tb_enum.api.as_enum0(args[0])
            self.on_sig0.fire(param0)
            return
        elif path == "sig1":
            param1 =  tb_enum.api.as_enum1(args[0])
            self.on_sig1.fire(param1)
            return
        elif path == "sig2":
            param2 =  tb_enum.api.as_enum2(args[0])
            self.on_sig2.fire(param2)
            return
        elif path == "sig3":
            param3 =  tb_enum.api.as_enum3(args[0])
            self.on_sig3.fire(param3)
            return
        logging.error("unknown signal: %s", name)
