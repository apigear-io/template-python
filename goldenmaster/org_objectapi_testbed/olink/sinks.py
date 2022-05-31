import asyncio
from typing import Any
from olink.core.types import Name
from olink.clientnode import IObjectSink, ClientNode
from .shared import EventHook
from org_objectapi_testbed.api import api


class Interface1Sink(IObjectSink):
    prop1=False
    prop2=0
    prop3=0.0
    prop4=str()
    prop5=[]
    prop6={}
    prop7=0
    prop10=[]
    prop11=[]
    prop12=[]
    prop14=[]
    on_property_changed = EventHook()
    on_sig1 = EventHook()
    on_sig2 = EventHook()
    on_sig3 = EventHook()

    client = None

    def __init__(self):
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote(f'org.objectapi.testbed.Interface1/{name}', args, func)
        return await asyncio.wait_for(future, 500)

    async def op1(self):
        return await self._invoke('op1', [])

    async def op2(self, step: int):
        return await self._invoke('op2', [step])

    async def op3(self):
        return await self._invoke('op3', [])

    def olink_object_name(self):
        return 'org.objectapi.testbed.Interface1'

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


class Interface2Sink(IObjectSink):
    prop200=0
    prop201=0
    prop202=0
    prop203=0.0
    prop204=0.0
    prop205=str()
    on_property_changed = EventHook()

    client = None

    def __init__(self):
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote(f'org.objectapi.testbed.Interface2/{name}', args, func)
        return await asyncio.wait_for(future, 500)

    def olink_object_name(self):
        return 'org.objectapi.testbed.Interface2'

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
