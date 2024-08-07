import asyncio
from typing import Any
from olink.core import Name
from olink.client import IObjectSink, ClientNode
from utils.eventhook import EventHook
import utils.base_types
import tb_same1.api
import logging

class SameStruct1InterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._prop1 = tb_same1.api.Struct1()
        self.on_prop1_changed = EventHook()
        self.on_sig1 = EventHook()
        self._on_is_ready= EventHook()
        self.client = ClientNode.register_sink(self)

    def _set_prop1(self, value):
        if self._prop1 == value:
            return
        self._prop1 = value
        self.on_prop1_changed.fire(self._prop1)

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        self.client.set_remote_property('tb.same1.SameStruct1Interface/prop1', tb_same1.api.from_struct1(value))

    def get_prop1(self):
        return self._prop1

    async def func1(self, param1: tb_same1.api.Struct1):
        _param1 = tb_same1.api.from_struct1(param1)
        args = [_param1]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(tb_same1.api.as_struct1(result.value))
        self.client.invoke_remote(f"tb.same1.SameStruct1Interface/func1", args, func)
        return await asyncio.wait_for(future, 500)

    def olink_object_name(self):
        return 'tb.same1.SameStruct1Interface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "prop1":
                v =  tb_same1.api.as_struct1(props[k])
                self._set_prop1(v)
        self._on_is_ready.fire()

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "prop1":
            v =  tb_same1.api.as_struct1(value)
            self._set_prop1(v)
            return
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sig1":
            param1 =  tb_same1.api.as_struct1(args[0])
            self.on_sig1.fire(param1)
            return
        logging.error("unknown signal: %s", name)

class SameStruct2InterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._prop1 = tb_same1.api.Struct2()
        self.on_prop1_changed = EventHook()
        self._prop2 = tb_same1.api.Struct2()
        self.on_prop2_changed = EventHook()
        self.on_sig1 = EventHook()
        self.on_sig2 = EventHook()
        self._on_is_ready= EventHook()
        self.client = ClientNode.register_sink(self)

    def _set_prop1(self, value):
        if self._prop1 == value:
            return
        self._prop1 = value
        self.on_prop1_changed.fire(self._prop1)

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        self.client.set_remote_property('tb.same1.SameStruct2Interface/prop1', tb_same1.api.from_struct2(value))

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
        self.client.set_remote_property('tb.same1.SameStruct2Interface/prop2', tb_same1.api.from_struct2(value))

    def get_prop2(self):
        return self._prop2

    async def func1(self, param1: tb_same1.api.Struct1):
        _param1 = tb_same1.api.from_struct1(param1)
        args = [_param1]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(tb_same1.api.as_struct1(result.value))
        self.client.invoke_remote(f"tb.same1.SameStruct2Interface/func1", args, func)
        return await asyncio.wait_for(future, 500)

    async def func2(self, param1: tb_same1.api.Struct1, param2: tb_same1.api.Struct2):
        _param1 = tb_same1.api.from_struct1(param1)
        _param2 = tb_same1.api.from_struct2(param2)
        args = [_param1, _param2]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(tb_same1.api.as_struct1(result.value))
        self.client.invoke_remote(f"tb.same1.SameStruct2Interface/func2", args, func)
        return await asyncio.wait_for(future, 500)

    def olink_object_name(self):
        return 'tb.same1.SameStruct2Interface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "prop1":
                v =  tb_same1.api.as_struct2(props[k])
                self._set_prop1(v)
            elif k == "prop2":
                v =  tb_same1.api.as_struct2(props[k])
                self._set_prop2(v)
        self._on_is_ready.fire()

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "prop1":
            v =  tb_same1.api.as_struct2(value)
            self._set_prop1(v)
            return
        elif path == "prop2":
            v =  tb_same1.api.as_struct2(value)
            self._set_prop2(v)
            return
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sig1":
            param1 =  tb_same1.api.as_struct1(args[0])
            self.on_sig1.fire(param1)
            return
        elif path == "sig2":
            param1 =  tb_same1.api.as_struct1(args[0])
            param2 =  tb_same1.api.as_struct2(args[1])
            self.on_sig2.fire(param1, param2)
            return
        logging.error("unknown signal: %s", name)

class SameEnum1InterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._prop1 = tb_same1.api.Enum1.VALUE1
        self.on_prop1_changed = EventHook()
        self.on_sig1 = EventHook()
        self._on_is_ready= EventHook()
        self.client = ClientNode.register_sink(self)

    def _set_prop1(self, value):
        if self._prop1 == value:
            return
        self._prop1 = value
        self.on_prop1_changed.fire(self._prop1)

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        self.client.set_remote_property('tb.same1.SameEnum1Interface/prop1', tb_same1.api.from_enum1(value))

    def get_prop1(self):
        return self._prop1

    async def func1(self, param1: tb_same1.api.Enum1):
        _param1 = tb_same1.api.from_enum1(param1)
        args = [_param1]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(tb_same1.api.as_enum1(result.value))
        self.client.invoke_remote(f"tb.same1.SameEnum1Interface/func1", args, func)
        return await asyncio.wait_for(future, 500)

    def olink_object_name(self):
        return 'tb.same1.SameEnum1Interface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "prop1":
                v =  tb_same1.api.as_enum1(props[k])
                self._set_prop1(v)
        self._on_is_ready.fire()

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "prop1":
            v =  tb_same1.api.as_enum1(value)
            self._set_prop1(v)
            return
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sig1":
            param1 =  tb_same1.api.as_enum1(args[0])
            self.on_sig1.fire(param1)
            return
        logging.error("unknown signal: %s", name)

class SameEnum2InterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._prop1 = tb_same1.api.Enum1.VALUE1
        self.on_prop1_changed = EventHook()
        self._prop2 = tb_same1.api.Enum2.VALUE1
        self.on_prop2_changed = EventHook()
        self.on_sig1 = EventHook()
        self.on_sig2 = EventHook()
        self._on_is_ready= EventHook()
        self.client = ClientNode.register_sink(self)

    def _set_prop1(self, value):
        if self._prop1 == value:
            return
        self._prop1 = value
        self.on_prop1_changed.fire(self._prop1)

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        self.client.set_remote_property('tb.same1.SameEnum2Interface/prop1', tb_same1.api.from_enum1(value))

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
        self.client.set_remote_property('tb.same1.SameEnum2Interface/prop2', tb_same1.api.from_enum2(value))

    def get_prop2(self):
        return self._prop2

    async def func1(self, param1: tb_same1.api.Enum1):
        _param1 = tb_same1.api.from_enum1(param1)
        args = [_param1]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(tb_same1.api.as_enum1(result.value))
        self.client.invoke_remote(f"tb.same1.SameEnum2Interface/func1", args, func)
        return await asyncio.wait_for(future, 500)

    async def func2(self, param1: tb_same1.api.Enum1, param2: tb_same1.api.Enum2):
        _param1 = tb_same1.api.from_enum1(param1)
        _param2 = tb_same1.api.from_enum2(param2)
        args = [_param1, _param2]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(tb_same1.api.as_enum1(result.value))
        self.client.invoke_remote(f"tb.same1.SameEnum2Interface/func2", args, func)
        return await asyncio.wait_for(future, 500)

    def olink_object_name(self):
        return 'tb.same1.SameEnum2Interface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "prop1":
                v =  tb_same1.api.as_enum1(props[k])
                self._set_prop1(v)
            elif k == "prop2":
                v =  tb_same1.api.as_enum2(props[k])
                self._set_prop2(v)
        self._on_is_ready.fire()

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "prop1":
            v =  tb_same1.api.as_enum1(value)
            self._set_prop1(v)
            return
        elif path == "prop2":
            v =  tb_same1.api.as_enum2(value)
            self._set_prop2(v)
            return
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sig1":
            param1 =  tb_same1.api.as_enum1(args[0])
            self.on_sig1.fire(param1)
            return
        elif path == "sig2":
            param1 =  tb_same1.api.as_enum1(args[0])
            param2 =  tb_same1.api.as_enum2(args[1])
            self.on_sig2.fire(param1, param2)
            return
        logging.error("unknown signal: %s", name)
