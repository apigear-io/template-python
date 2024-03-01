import asyncio
from typing import Any
from olink.core import Name
from olink.client import IObjectSink, ClientNode
from testbed2_api.shared import EventHook
from testbed2_api import api

class ManyParamInterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self.prop1 = 0
        self.prop2 = 0
        self.prop3 = 0
        self.prop4 = 0
        self.on_property_changed = EventHook()
        self.on_sig1 = EventHook()
        self.on_sig2 = EventHook()
        self.on_sig3 = EventHook()
        self.on_sig4 = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote('testbed2.ManyParamInterface/ManyParamInterface', args, func)
        return await asyncio.wait_for(future, 500)

    async def func1(self, param1: int):
        return await self._invoke("func1", [param1])

    async def func2(self, param1: int, param2: int):
        return await self._invoke("func2", [param1, param2])

    async def func3(self, param1: int, param2: int, param3: int):
        return await self._invoke("func3", [param1, param2, param3])

    async def func4(self, param1: int, param2: int, param3: int, param4: int):
        return await self._invoke("func4", [param1, param2, param3, param4])

    def olink_object_name(self):
        return 'testbed2.ManyParamInterface'

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

class NestedStruct1InterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self.prop1 = api.NestedStruct1()
        self.on_property_changed = EventHook()
        self.on_sig1 = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote('testbed2.NestedStruct1Interface/NestedStruct1Interface', args, func)
        return await asyncio.wait_for(future, 500)

    async def func1(self, param1: api.NestedStruct1):
        return await self._invoke("func1", [param1])

    def olink_object_name(self):
        return 'testbed2.NestedStruct1Interface'

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

class NestedStruct2InterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self.prop1 = api.NestedStruct1()
        self.prop2 = api.NestedStruct2()
        self.on_property_changed = EventHook()
        self.on_sig1 = EventHook()
        self.on_sig2 = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote('testbed2.NestedStruct2Interface/NestedStruct2Interface', args, func)
        return await asyncio.wait_for(future, 500)

    async def func1(self, param1: api.NestedStruct1):
        return await self._invoke("func1", [param1])

    async def func2(self, param1: api.NestedStruct1, param2: api.NestedStruct2):
        return await self._invoke("func2", [param1, param2])

    def olink_object_name(self):
        return 'testbed2.NestedStruct2Interface'

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

class NestedStruct3InterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self.prop1 = api.NestedStruct1()
        self.prop2 = api.NestedStruct2()
        self.prop3 = api.NestedStruct3()
        self.on_property_changed = EventHook()
        self.on_sig1 = EventHook()
        self.on_sig2 = EventHook()
        self.on_sig3 = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote('testbed2.NestedStruct3Interface/NestedStruct3Interface', args, func)
        return await asyncio.wait_for(future, 500)

    async def func1(self, param1: api.NestedStruct1):
        return await self._invoke("func1", [param1])

    async def func2(self, param1: api.NestedStruct1, param2: api.NestedStruct2):
        return await self._invoke("func2", [param1, param2])

    async def func3(self, param1: api.NestedStruct1, param2: api.NestedStruct2, param3: api.NestedStruct3):
        return await self._invoke("func3", [param1, param2, param3])

    def olink_object_name(self):
        return 'testbed2.NestedStruct3Interface'

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