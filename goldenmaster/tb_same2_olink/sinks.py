import asyncio
from typing import Any
from olink.core import Name
from olink.client import IObjectSink, ClientNode
from utils.eventhook import EventHook
from tb_same2_api import api
import logging

class SameStruct1InterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._prop1 = api.Struct1()
        self.on_prop1_changed = EventHook()
        self.on_sig1 = EventHook()
        self._on_is_ready= EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args, no_wait=False):
        if no_wait:
            self.client.invoke_remote(f"tb.same2.SameStruct1Interface/{name}", args, func=None)
        else:
            future = asyncio.get_running_loop().create_future()
            def func(args):
                return future.set_result(args.value)
            self.client.invoke_remote(f"tb.same2.SameStruct1Interface/{name}", args, func)
            return await asyncio.wait_for(future, 500)

    def _set_prop1(self, value):
        if self._prop1 == value:
            return
        self._prop1 = value
        self.on_prop1_changed.fire(self._prop1)

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        self.client.set_remote_property('tb.same2.SameStruct1Interface/prop1', value)

    def get_prop1(self):
        return self._prop1

    async def func1(self, param1: api.Struct1):
        _param1 = api.from_struct1(param1)
        return await self._invoke("func1", [_param1])

    def olink_object_name(self):
        return 'tb.same2.SameStruct1Interface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "prop1":
                v =  api.as_struct1(props[k])
                self._set_prop1(v)
        self._on_is_ready.fire()

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "prop1":
            v =  api.as_struct1(value)
            self._set_prop1(v)
            return
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sig1":
            param1 =  api.as_struct1(args[0])
            self.on_sig1.fire(param1)
            return
        logging.error("unknown signal: %s", name)

class SameStruct2InterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._prop1 = api.Struct2()
        self.on_prop1_changed = EventHook()
        self._prop2 = api.Struct2()
        self.on_prop2_changed = EventHook()
        self.on_sig1 = EventHook()
        self.on_sig2 = EventHook()
        self._on_is_ready= EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args, no_wait=False):
        if no_wait:
            self.client.invoke_remote(f"tb.same2.SameStruct2Interface/{name}", args, func=None)
        else:
            future = asyncio.get_running_loop().create_future()
            def func(args):
                return future.set_result(args.value)
            self.client.invoke_remote(f"tb.same2.SameStruct2Interface/{name}", args, func)
            return await asyncio.wait_for(future, 500)

    def _set_prop1(self, value):
        if self._prop1 == value:
            return
        self._prop1 = value
        self.on_prop1_changed.fire(self._prop1)

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        self.client.set_remote_property('tb.same2.SameStruct2Interface/prop1', value)

    def get_prop1(self):
        return self._prop1

    def _set_prop2(self, value):
        if self._prop2 == value:
            return
        self._prop2 = value
        self.on_prop2_changed.fire(self._prop2)

    def set_prop2(self, value):
        if self._prop2 == value:
            return
        self.client.set_remote_property('tb.same2.SameStruct2Interface/prop2', value)

    def get_prop2(self):
        return self._prop2

    async def func1(self, param1: api.Struct1):
        _param1 = api.from_struct1(param1)
        return await self._invoke("func1", [_param1])

    async def func2(self, param1: api.Struct1, param2: api.Struct2):
        _param1 = api.from_struct1(param1)
        _param2 = api.from_struct2(param2)
        return await self._invoke("func2", [_param1, _param2])

    def olink_object_name(self):
        return 'tb.same2.SameStruct2Interface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "prop1":
                v =  api.as_struct2(props[k])
                self._set_prop1(v)
            elif k == "prop2":
                v =  api.as_struct2(props[k])
                self._set_prop2(v)
        self._on_is_ready.fire()

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "prop1":
            v =  api.as_struct2(value)
            self._set_prop1(v)
            return
        elif path == "prop2":
            v =  api.as_struct2(value)
            self._set_prop2(v)
            return
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sig1":
            param1 =  api.as_struct1(args[0])
            self.on_sig1.fire(param1)
            return
        elif path == "sig2":
            param1 =  api.as_struct1(args[0])
            param2 =  api.as_struct2(args[1])
            self.on_sig2.fire(param1, param2)
            return
        logging.error("unknown signal: %s", name)

class SameEnum1InterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._prop1 = api.Enum1.VALUE1
        self.on_prop1_changed = EventHook()
        self.on_sig1 = EventHook()
        self._on_is_ready= EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args, no_wait=False):
        if no_wait:
            self.client.invoke_remote(f"tb.same2.SameEnum1Interface/{name}", args, func=None)
        else:
            future = asyncio.get_running_loop().create_future()
            def func(args):
                return future.set_result(args.value)
            self.client.invoke_remote(f"tb.same2.SameEnum1Interface/{name}", args, func)
            return await asyncio.wait_for(future, 500)

    def _set_prop1(self, value):
        if self._prop1 == value:
            return
        self._prop1 = value
        self.on_prop1_changed.fire(self._prop1)

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        self.client.set_remote_property('tb.same2.SameEnum1Interface/prop1', value)

    def get_prop1(self):
        return self._prop1

    async def func1(self, param1: api.Enum1):
        _param1 = api.from_enum1(param1)
        return await self._invoke("func1", [_param1])

    def olink_object_name(self):
        return 'tb.same2.SameEnum1Interface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "prop1":
                v =  api.as_enum1(props[k])
                self._set_prop1(v)
        self._on_is_ready.fire()

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "prop1":
            v =  api.as_enum1(value)
            self._set_prop1(v)
            return
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sig1":
            param1 =  api.as_enum1(args[0])
            self.on_sig1.fire(param1)
            return
        logging.error("unknown signal: %s", name)

class SameEnum2InterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._prop1 = api.Enum1.VALUE1
        self.on_prop1_changed = EventHook()
        self._prop2 = api.Enum2.VALUE1
        self.on_prop2_changed = EventHook()
        self.on_sig1 = EventHook()
        self.on_sig2 = EventHook()
        self._on_is_ready= EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args, no_wait=False):
        if no_wait:
            self.client.invoke_remote(f"tb.same2.SameEnum2Interface/{name}", args, func=None)
        else:
            future = asyncio.get_running_loop().create_future()
            def func(args):
                return future.set_result(args.value)
            self.client.invoke_remote(f"tb.same2.SameEnum2Interface/{name}", args, func)
            return await asyncio.wait_for(future, 500)

    def _set_prop1(self, value):
        if self._prop1 == value:
            return
        self._prop1 = value
        self.on_prop1_changed.fire(self._prop1)

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        self.client.set_remote_property('tb.same2.SameEnum2Interface/prop1', value)

    def get_prop1(self):
        return self._prop1

    def _set_prop2(self, value):
        if self._prop2 == value:
            return
        self._prop2 = value
        self.on_prop2_changed.fire(self._prop2)

    def set_prop2(self, value):
        if self._prop2 == value:
            return
        self.client.set_remote_property('tb.same2.SameEnum2Interface/prop2', value)

    def get_prop2(self):
        return self._prop2

    async def func1(self, param1: api.Enum1):
        _param1 = api.from_enum1(param1)
        return await self._invoke("func1", [_param1])

    async def func2(self, param1: api.Enum1, param2: api.Enum2):
        _param1 = api.from_enum1(param1)
        _param2 = api.from_enum2(param2)
        return await self._invoke("func2", [_param1, _param2])

    def olink_object_name(self):
        return 'tb.same2.SameEnum2Interface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "prop1":
                v =  api.as_enum1(props[k])
                self._set_prop1(v)
            elif k == "prop2":
                v =  api.as_enum2(props[k])
                self._set_prop2(v)
        self._on_is_ready.fire()

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "prop1":
            v =  api.as_enum1(value)
            self._set_prop1(v)
            return
        elif path == "prop2":
            v =  api.as_enum2(value)
            self._set_prop2(v)
            return
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sig1":
            param1 =  api.as_enum1(args[0])
            self.on_sig1.fire(param1)
            return
        elif path == "sig2":
            param1 =  api.as_enum1(args[0])
            param2 =  api.as_enum2(args[1])
            self.on_sig2.fire(param1, param2)
            return
        logging.error("unknown signal: %s", name)
