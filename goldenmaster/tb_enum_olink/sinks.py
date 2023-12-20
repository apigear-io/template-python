import asyncio
from typing import Any
from olink.core import Name
from olink.client import IObjectSink, ClientNode
from tb_enum_api.shared import EventHook
from tb_enum_api import api

class EnumInterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._prop0 = api.Enum0.VALUE0
        self.on_prop0_changed = EventHook()
        self._prop1 = api.Enum1.VALUE1
        self.on_prop1_changed = EventHook()
        self._prop2 = api.Enum2.VALUE2
        self.on_prop2_changed = EventHook()
        self._prop3 = api.Enum3.VALUE3
        self.on_prop3_changed = EventHook()
        self.on_sig0 = EventHook()
        self.on_sig1 = EventHook()
        self.on_sig2 = EventHook()
        self.on_sig3 = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote('tb.enum.EnumInterface/EnumInterface', args, func)
        return await asyncio.wait_for(future, 500)

    def set_prop0(self, value):
        if self._prop0 == value:
            return
        self.client.set_remote_property('tb.enum.EnumInterface/prop0', value)

    def get_prop0(self):
        return self._prop0

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        self.client.set_remote_property('tb.enum.EnumInterface/prop1', value)

    def get_prop1(self):
        return self._prop1

    def set_prop2(self, value):
        if self._prop2 == value:
            return
        self.client.set_remote_property('tb.enum.EnumInterface/prop2', value)

    def get_prop2(self):
        return self._prop2

    def set_prop3(self, value):
        if self._prop3 == value:
            return
        self.client.set_remote_property('tb.enum.EnumInterface/prop3', value)

    def get_prop3(self):
        return self._prop3

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
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "prop0":
                self._prop0 =  props[k]
            elif k == "prop1":
                self._prop1 =  props[k]
            elif k == "prop2":
                self._prop2 =  props[k]
            elif k == "prop3":
                self._prop3 =  props[k]

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "prop0":
            self._prop0 =  value
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop0)
        elif path == "prop1":
            self._prop1 =  value
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop1)
        elif path == "prop2":
            self._prop2 =  value
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop2)
        elif path == "prop3":
            self._prop3 =  value
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop3)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        hook = getattr(self, f'on_{path}')
        hook.fire(*args)