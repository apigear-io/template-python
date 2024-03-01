import asyncio
from typing import Any
from olink.core import Name
from olink.client import IObjectSink, ClientNode
from tb_enum_api.shared import EventHook
from tb_enum_api import api

class EnumInterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self.prop0 = api.Enum0.VALUE0
        self.prop1 = api.Enum1.VALUE1
        self.prop2 = api.Enum2.VALUE2
        self.prop3 = api.Enum3.VALUE3
        self.on_property_changed = EventHook()
        self.sig0 = EventHook()
        self.sig1 = EventHook()
        self.sig2 = EventHook()
        self.sig3 = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote('tb.enum.EnumInterface/EnumInterface', args, func)
        return await asyncio.wait_for(future, 500)

    async def func0(self, param0: api.Enum0):
        return await self._invoke("func0", [param0])

    async def func1(self, param1: api.Enum1):
        return await self._invoke("func1", [param1])

    async def func2(self, param2: api.Enum2):
        return await self._invoke("func2", [param2])

    async def func3(self, param3: api.Enum3):
        return await self._invoke("func3", [param3])

    def olink_object_name(self):
        return 'tb.enum.EnumInterface'

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