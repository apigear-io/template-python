import asyncio
from typing import Any
from olink.core import Name
from olink.client import IObjectSink, ClientNode
from testbed2_api.shared import EventHook
from testbed2_api import api

class ManyParamInterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._prop1 = 0
        self.on_prop1_changed = EventHook()
        self._prop2 = 0
        self.on_prop2_changed = EventHook()
        self._prop3 = 0
        self.on_prop3_changed = EventHook()
        self._prop4 = 0
        self.on_prop4_changed = EventHook()
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

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        self.client.set_remote_property('testbed2.ManyParamInterface/prop1', value)

    def get_prop1(self):
        return self._prop1

    def set_prop2(self, value):
        if self._prop2 == value:
            return
        self.client.set_remote_property('testbed2.ManyParamInterface/prop2', value)

    def get_prop2(self):
        return self._prop2

    def set_prop3(self, value):
        if self._prop3 == value:
            return
        self.client.set_remote_property('testbed2.ManyParamInterface/prop3', value)

    def get_prop3(self):
        return self._prop3

    def set_prop4(self, value):
        if self._prop4 == value:
            return
        self.client.set_remote_property('testbed2.ManyParamInterface/prop4', value)

    def get_prop4(self):
        return self._prop4

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
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "prop1":
                self._prop1 =  props[k]
            elif k == "prop2":
                self._prop2 =  props[k]
            elif k == "prop3":
                self._prop3 =  props[k]
            elif k == "prop4":
                self._prop4 =  props[k]

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
        elif path == "prop3":
            self._prop3 =  value
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop3)
        elif path == "prop4":
            self._prop4 =  value
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop4)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        hook = getattr(self, f'on_{path}')
        hook.fire(*args)

class NestedStruct1InterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._prop1 = api.NestedStruct1()
        self.on_prop1_changed = EventHook()
        self.on_sig1 = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote('testbed2.NestedStruct1Interface/NestedStruct1Interface', args, func)
        return await asyncio.wait_for(future, 500)

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        self.client.set_remote_property('testbed2.NestedStruct1Interface/prop1', value)

    def get_prop1(self):
        return self._prop1

    async def func1(self, param1: api.NestedStruct1):
        return await self._invoke("func1", [param1])

    def olink_object_name(self):
        return 'testbed2.NestedStruct1Interface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "prop1":
                self._prop1 =  props[k]

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "prop1":
            self._prop1 =  value
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop1)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        hook = getattr(self, f'on_{path}')
        hook.fire(*args)

class NestedStruct2InterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._prop1 = api.NestedStruct1()
        self.on_prop1_changed = EventHook()
        self._prop2 = api.NestedStruct2()
        self.on_prop2_changed = EventHook()
        self.on_sig1 = EventHook()
        self.on_sig2 = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote('testbed2.NestedStruct2Interface/NestedStruct2Interface', args, func)
        return await asyncio.wait_for(future, 500)

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        self.client.set_remote_property('testbed2.NestedStruct2Interface/prop1', value)

    def get_prop1(self):
        return self._prop1

    def set_prop2(self, value):
        if self._prop2 == value:
            return
        self.client.set_remote_property('testbed2.NestedStruct2Interface/prop2', value)

    def get_prop2(self):
        return self._prop2

    async def func1(self, param1: api.NestedStruct1):
        return await self._invoke("func1", [param1])

    async def func2(self, param1: api.NestedStruct1, param2: api.NestedStruct2):
        return await self._invoke("func2", [param1, param2])

    def olink_object_name(self):
        return 'testbed2.NestedStruct2Interface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "prop1":
                self._prop1 =  props[k]
            elif k == "prop2":
                self._prop2 =  props[k]

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
        hook = getattr(self, f'on_{path}')
        hook.fire(*args)

class NestedStruct3InterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._prop1 = api.NestedStruct1()
        self.on_prop1_changed = EventHook()
        self._prop2 = api.NestedStruct2()
        self.on_prop2_changed = EventHook()
        self._prop3 = api.NestedStruct3()
        self.on_prop3_changed = EventHook()
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

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        self.client.set_remote_property('testbed2.NestedStruct3Interface/prop1', value)

    def get_prop1(self):
        return self._prop1

    def set_prop2(self, value):
        if self._prop2 == value:
            return
        self.client.set_remote_property('testbed2.NestedStruct3Interface/prop2', value)

    def get_prop2(self):
        return self._prop2

    def set_prop3(self, value):
        if self._prop3 == value:
            return
        self.client.set_remote_property('testbed2.NestedStruct3Interface/prop3', value)

    def get_prop3(self):
        return self._prop3

    async def func1(self, param1: api.NestedStruct1):
        return await self._invoke("func1", [param1])

    async def func2(self, param1: api.NestedStruct1, param2: api.NestedStruct2):
        return await self._invoke("func2", [param1, param2])

    async def func3(self, param1: api.NestedStruct1, param2: api.NestedStruct2, param3: api.NestedStruct3):
        return await self._invoke("func3", [param1, param2, param3])

    def olink_object_name(self):
        return 'testbed2.NestedStruct3Interface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "prop1":
                self._prop1 =  props[k]
            elif k == "prop2":
                self._prop2 =  props[k]
            elif k == "prop3":
                self._prop3 =  props[k]

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
        elif path == "prop3":
            self._prop3 =  value
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop3)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        hook = getattr(self, f'on_{path}')
        hook.fire(*args)