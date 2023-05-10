import asyncio
from typing import Any
from olink.core import Name
from olink.client import IObjectSink, ClientNode
from .shared import EventHook
from tb_same2_api import api

class SameStruct1InterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self.prop1 = {}
        self.on_property_changed = EventHook()
        self.sig1 = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote('tb.same2.SameStruct1Interface/SameStruct1Interface', args, func)
        return await asyncio.wait_for(future, 500)

    async def func1(self, param1: api.Struct1):
        return await self._invoke("func1", [param1])

    def olink_object_name(self):
        return 'tb.same2.SameStruct1Interface'

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

class SameStruct2InterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self.prop1 = {}
        self.prop2 = {}
        self.on_property_changed = EventHook()
        self.sig1 = EventHook()
        self.sig2 = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote('tb.same2.SameStruct2Interface/SameStruct2Interface', args, func)
        return await asyncio.wait_for(future, 500)

    async def func1(self, param1: api.Struct1):
        return await self._invoke("func1", [param1])

    async def func2(self, param1: api.Struct1, param2: api.Struct2):
        return await self._invoke("func2", [param1, param2])

    def olink_object_name(self):
        return 'tb.same2.SameStruct2Interface'

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

class SameEnum1InterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self.prop1 = api.Enum1.VALUE1
        self.on_property_changed = EventHook()
        self.sig1 = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote('tb.same2.SameEnum1Interface/SameEnum1Interface', args, func)
        return await asyncio.wait_for(future, 500)

    async def func1(self, param1: api.Enum1):
        return await self._invoke("func1", [param1])

    def olink_object_name(self):
        return 'tb.same2.SameEnum1Interface'

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

class SameEnum2InterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self.prop1 = api.Enum1.VALUE1
        self.prop2 = api.Enum2.VALUE1
        self.on_property_changed = EventHook()
        self.sig1 = EventHook()
        self.sig2 = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote('tb.same2.SameEnum2Interface/SameEnum2Interface', args, func)
        return await asyncio.wait_for(future, 500)

    async def func1(self, param1: api.Enum1):
        return await self._invoke("func1", [param1])

    async def func2(self, param1: api.Enum1, param2: api.Enum2):
        return await self._invoke("func2", [param1, param2])

    def olink_object_name(self):
        return 'tb.same2.SameEnum2Interface'

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