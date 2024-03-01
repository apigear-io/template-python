import asyncio
from typing import Any
from olink.core import Name
from olink.client import IObjectSink, ClientNode
from tb_simple_api.shared import EventHook
from tb_simple_api import api

class SimpleInterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self.prop_bool = False
        self.prop_int = 0
        self.prop_int32 = 0
        self.prop_int64 = 0
        self.prop_float = 0.0
        self.prop_float32 = 0.0
        self.prop_float64 = 0.0
        self.prop_string = ""
        self.prop_read_only_string = ""
        self.on_property_changed = EventHook()
        self.sig_void = EventHook()
        self.sig_bool = EventHook()
        self.sig_int = EventHook()
        self.sig_int32 = EventHook()
        self.sig_int64 = EventHook()
        self.sig_float = EventHook()
        self.sig_float32 = EventHook()
        self.sig_float64 = EventHook()
        self.sig_string = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote('tb.simple.SimpleInterface/SimpleInterface', args, func)
        return await asyncio.wait_for(future, 500)

    async def func_void(self):
        return await self._invoke("funcVoid", [])

    async def func_bool(self, param_bool: bool):
        return await self._invoke("funcBool", [param_bool])

    async def func_int(self, param_int: int):
        return await self._invoke("funcInt", [param_int])

    async def func_int32(self, param_int32: int):
        return await self._invoke("funcInt32", [param_int32])

    async def func_int64(self, param_int64: int):
        return await self._invoke("funcInt64", [param_int64])

    async def func_float(self, param_float: float):
        return await self._invoke("funcFloat", [param_float])

    async def func_float32(self, param_float32: float):
        return await self._invoke("funcFloat32", [param_float32])

    async def func_float64(self, param_float: float):
        return await self._invoke("funcFloat64", [param_float])

    async def func_string(self, param_string: str):
        return await self._invoke("funcString", [param_string])

    def olink_object_name(self):
        return 'tb.simple.SimpleInterface'

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

class SimpleArrayInterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self.prop_bool = []
        self.prop_int = []
        self.prop_int32 = []
        self.prop_int64 = []
        self.prop_float = []
        self.prop_float32 = []
        self.prop_float64 = []
        self.prop_string = []
        self.on_property_changed = EventHook()
        self.sig_bool = EventHook()
        self.sig_int = EventHook()
        self.sig_int32 = EventHook()
        self.sig_int64 = EventHook()
        self.sig_float = EventHook()
        self.sig_float32 = EventHook()
        self.sig_float64 = EventHook()
        self.sig_string = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote('tb.simple.SimpleArrayInterface/SimpleArrayInterface', args, func)
        return await asyncio.wait_for(future, 500)

    async def func_bool(self, param_bool: list[bool]):
        return await self._invoke("funcBool", [param_bool])

    async def func_int(self, param_int: list[int]):
        return await self._invoke("funcInt", [param_int])

    async def func_int32(self, param_int32: list[int]):
        return await self._invoke("funcInt32", [param_int32])

    async def func_int64(self, param_int64: list[int]):
        return await self._invoke("funcInt64", [param_int64])

    async def func_float(self, param_float: list[float]):
        return await self._invoke("funcFloat", [param_float])

    async def func_float32(self, param_float32: list[float]):
        return await self._invoke("funcFloat32", [param_float32])

    async def func_float64(self, param_float: list[float]):
        return await self._invoke("funcFloat64", [param_float])

    async def func_string(self, param_string: list[str]):
        return await self._invoke("funcString", [param_string])

    def olink_object_name(self):
        return 'tb.simple.SimpleArrayInterface'

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

class NoPropertiesInterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self.on_property_changed = EventHook()
        self.sig_void = EventHook()
        self.sig_bool = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote('tb.simple.NoPropertiesInterface/NoPropertiesInterface', args, func)
        return await asyncio.wait_for(future, 500)

    async def func_void(self):
        return await self._invoke("funcVoid", [])

    async def func_bool(self, param_bool: bool):
        return await self._invoke("funcBool", [param_bool])

    def olink_object_name(self):
        return 'tb.simple.NoPropertiesInterface'

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

class NoOperationsInterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self.prop_bool = False
        self.prop_int = 0
        self.on_property_changed = EventHook()
        self.sig_void = EventHook()
        self.sig_bool = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote('tb.simple.NoOperationsInterface/NoOperationsInterface', args, func)
        return await asyncio.wait_for(future, 500)

    def olink_object_name(self):
        return 'tb.simple.NoOperationsInterface'

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

class NoSignalsInterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self.prop_bool = False
        self.prop_int = 0
        self.on_property_changed = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote('tb.simple.NoSignalsInterface/NoSignalsInterface', args, func)
        return await asyncio.wait_for(future, 500)

    async def func_void(self):
        return await self._invoke("funcVoid", [])

    async def func_bool(self, param_bool: bool):
        return await self._invoke("funcBool", [param_bool])

    def olink_object_name(self):
        return 'tb.simple.NoSignalsInterface'

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

class EmptyInterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self.on_property_changed = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote('tb.simple.EmptyInterface/EmptyInterface', args, func)
        return await asyncio.wait_for(future, 500)

    def olink_object_name(self):
        return 'tb.simple.EmptyInterface'

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