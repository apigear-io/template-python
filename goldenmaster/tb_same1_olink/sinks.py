import asyncio
from typing import Any
from olink.core import Name
from olink.client import IObjectSink, ClientNode
from tb_same1_api.shared import EventHook
from tb_same1_api import api

class SameStruct1InterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._prop1 = api.Struct1()
        self.on_prop1_changed = EventHook()
        self.on_sig1 = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote('tb.same1.SameStruct1Interface/SameStruct1Interface', args, func)
        return await asyncio.wait_for(future, 500)

    def _set_prop1(self, value):
        if self._prop1 == value:
            return
        path = Name.path_from_name("prop1")
        self._prop1 = value
        self.on_property_changed.fire(path, self._prop1)

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        self.client.set_remote_property('tb.same1.SameStruct1Interface/prop1', value)

    def get_prop1(self):
        return self._prop1

    async def func1(self, param1: api.Struct1):
        return await self._invoke("func1", [param1])

    def olink_object_name(self):
        return 'tb.same1.SameStruct1Interface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "prop1":
                self._set_prop1(props[k])

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "prop1":
            self._prop1 =  value
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop1)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sig1":
            _param1 =  args[0]
            self.on_sig1.fire(_param1)

class SameStruct2InterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._prop1 = api.Struct2()
        self.on_prop1_changed = EventHook()
        self._prop2 = api.Struct2()
        self.on_prop2_changed = EventHook()
        self.on_sig1 = EventHook()
        self.on_sig2 = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote('tb.same1.SameStruct2Interface/SameStruct2Interface', args, func)
        return await asyncio.wait_for(future, 500)

    def _set_prop1(self, value):
        if self._prop1 == value:
            return
        path = Name.path_from_name("prop1")
        self._prop1 = value
        self.on_property_changed.fire(path, self._prop1)

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        self.client.set_remote_property('tb.same1.SameStruct2Interface/prop1', value)

    def get_prop1(self):
        return self._prop1

    def _set_prop2(self, value):
        if self._prop2 == value:
            return
        path = Name.path_from_name("prop2")
        self._prop2 = value
        self.on_property_changed.fire(path, self._prop2)

    def set_prop2(self, value):
        if self._prop2 == value:
            return
        self.client.set_remote_property('tb.same1.SameStruct2Interface/prop2', value)

    def get_prop2(self):
        return self._prop2

    async def func1(self, param1: api.Struct1):
        return await self._invoke("func1", [param1])

    async def func2(self, param1: api.Struct1, param2: api.Struct2):
        return await self._invoke("func2", [param1, param2])

    def olink_object_name(self):
        return 'tb.same1.SameStruct2Interface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "prop1":
                self._set_prop1(props[k])
            elif k == "prop2":
                self._set_prop2(props[k])

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "prop1":
            self._prop1 =  value
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop1)
        elif path == "prop2":
            self._prop2 =  value
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop2)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sig1":
            _param1 =  args[0]
            self.on_sig1.fire(_param1)
        elif path == "sig2":
            _param1 =  args[0]
            _param2 =  args[1]
            self.on_sig2.fire(_param1, _param2)

class SameEnum1InterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._prop1 = api.Enum1.VALUE1
        self.on_prop1_changed = EventHook()
        self.on_sig1 = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote('tb.same1.SameEnum1Interface/SameEnum1Interface', args, func)
        return await asyncio.wait_for(future, 500)

    def _set_prop1(self, value):
        if self._prop1 == value:
            return
        path = Name.path_from_name("prop1")
        self._prop1 = value
        self.on_property_changed.fire(path, self._prop1)

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        self.client.set_remote_property('tb.same1.SameEnum1Interface/prop1', value)

    def get_prop1(self):
        return self._prop1

    async def func1(self, param1: api.Enum1):
        return await self._invoke("func1", [param1])

    def olink_object_name(self):
        return 'tb.same1.SameEnum1Interface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "prop1":
                self._set_prop1(props[k])

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "prop1":
            self._prop1 =  value
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop1)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sig1":
            _param1 =  args[0]
            self.on_sig1.fire(_param1)

class SameEnum2InterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._prop1 = api.Enum1.VALUE1
        self.on_prop1_changed = EventHook()
        self._prop2 = api.Enum2.VALUE1
        self.on_prop2_changed = EventHook()
        self.on_sig1 = EventHook()
        self.on_sig2 = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote('tb.same1.SameEnum2Interface/SameEnum2Interface', args, func)
        return await asyncio.wait_for(future, 500)

    def _set_prop1(self, value):
        if self._prop1 == value:
            return
        path = Name.path_from_name("prop1")
        self._prop1 = value
        self.on_property_changed.fire(path, self._prop1)

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        self.client.set_remote_property('tb.same1.SameEnum2Interface/prop1', value)

    def get_prop1(self):
        return self._prop1

    def _set_prop2(self, value):
        if self._prop2 == value:
            return
        path = Name.path_from_name("prop2")
        self._prop2 = value
        self.on_property_changed.fire(path, self._prop2)

    def set_prop2(self, value):
        if self._prop2 == value:
            return
        self.client.set_remote_property('tb.same1.SameEnum2Interface/prop2', value)

    def get_prop2(self):
        return self._prop2

    async def func1(self, param1: api.Enum1):
        return await self._invoke("func1", [param1])

    async def func2(self, param1: api.Enum1, param2: api.Enum2):
        return await self._invoke("func2", [param1, param2])

    def olink_object_name(self):
        return 'tb.same1.SameEnum2Interface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "prop1":
                self._set_prop1(props[k])
            elif k == "prop2":
                self._set_prop2(props[k])

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "prop1":
            self._prop1 =  value
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop1)
        elif path == "prop2":
            self._prop2 =  value
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop2)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sig1":
            _param1 =  args[0]
            self.on_sig1.fire(_param1)
        elif path == "sig2":
            _param1 =  args[0]
            _param2 =  args[1]
            self.on_sig2.fire(_param1, _param2)
