import asyncio
from typing import Any
from olink.core import Name
from olink.client import IObjectSink, ClientNode
from .shared import EventHook
from testbed1_api import api

class StructInterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self.prop_bool = api.StructBool()
        self.prop_int = api.StructInt()
        self.prop_float = api.StructFloat()
        self.prop_string = api.StructString()
        self.on_property_changed = EventHook()
        self.sig_bool = EventHook()
        self.sig_int = EventHook()
        self.sig_float = EventHook()
        self.sig_string = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote('testbed1.StructInterface/StructInterface', args, func)
        return await asyncio.wait_for(future, 500)

    async def func_bool(self, param_bool: api.StructBool):
        return await self._invoke("funcBool", [param_bool])

    async def func_int(self, param_int: api.StructInt):
        return await self._invoke("funcInt", [param_int])

    async def func_float(self, param_float: api.StructFloat):
        return await self._invoke("funcFloat", [param_float])

    async def func_string(self, param_string: api.StructString):
        return await self._invoke("funcString", [param_string])

    def olink_object_name(self):
        return 'testbed1.StructInterface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        for k in props:
            setattr(self, k, props[k])

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        setattr(self, path, value)
        self.on_property_changed.fire(path, value)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        hook = getattr(self, f'on_{path}')        
        hook.fire(*args)

class StructArrayInterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self.prop_bool = []
        self.prop_int = []
        self.prop_float = []
        self.prop_string = []
        self.on_property_changed = EventHook()
        self.sig_bool = EventHook()
        self.sig_int = EventHook()
        self.sig_float = EventHook()
        self.sig_string = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote('testbed1.StructArrayInterface/StructArrayInterface', args, func)
        return await asyncio.wait_for(future, 500)

    async def func_bool(self, param_bool: list[api.StructBool]):
        return await self._invoke("funcBool", [param_bool])

    async def func_int(self, param_int: list[api.StructInt]):
        return await self._invoke("funcInt", [param_int])

    async def func_float(self, param_float: list[api.StructFloat]):
        return await self._invoke("funcFloat", [param_float])

    async def func_string(self, param_string: list[api.StructString]):
        return await self._invoke("funcString", [param_string])

    def olink_object_name(self):
        return 'testbed1.StructArrayInterface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        for k in props:
            setattr(self, k, props[k])

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        setattr(self, path, value)
        self.on_property_changed.fire(path, value)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        hook = getattr(self, f'on_{path}')        
        hook.fire(*args)