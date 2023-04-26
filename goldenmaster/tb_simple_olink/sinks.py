import asyncio
from typing import Any
from olink.core.types import Name
from olink.clientnode import IObjectSink, ClientNode
from .shared import EventHook
from tb_simple_api import api
class SimpleInterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self.prop_bool = False
        self.prop_int = 0
        self.prop_float = 0.0
        self.prop_string = ""
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
        self.client.invoke_remote('tb.simple.SimpleInterface/SimpleInterface', args, func)
        return await asyncio.wait_for(future, 500)
    async def func_bool(self, param_bool: bool):
        return await self._invoke("funcBool", [param_bool])
    async def func_int(self, param_int: int):
        return await self._invoke("funcInt", [param_int])
    async def func_float(self, param_float: float):
        return await self._invoke("funcFloat", [param_float])
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
        self.client.invoke_remote('tb.simple.SimpleArrayInterface/SimpleArrayInterface', args, func)
        return await asyncio.wait_for(future, 500)
    async def func_bool(self, param_bool: list[bool]):
        return await self._invoke("funcBool", [param_bool])
    async def func_int(self, param_int: list[int]):
        return await self._invoke("funcInt", [param_int])
    async def func_float(self, param_float: list[float]):
        return await self._invoke("funcFloat", [param_float])
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