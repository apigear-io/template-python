import asyncio
from typing import Any
from olink.core import Name
from olink.client import IObjectSink, ClientNode
from utils.eventhook import EventHook
import utils.base_types
import testbed1.api
import logging

class StructInterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._prop_bool = testbed1.api.StructBool()
        self.on_prop_bool_changed = EventHook()
        self._prop_int = testbed1.api.StructInt()
        self.on_prop_int_changed = EventHook()
        self._prop_float = testbed1.api.StructFloat()
        self.on_prop_float_changed = EventHook()
        self._prop_string = testbed1.api.StructString()
        self.on_prop_string_changed = EventHook()
        self.on_sig_bool = EventHook()
        self.on_sig_int = EventHook()
        self.on_sig_float = EventHook()
        self.on_sig_string = EventHook()
        self._on_is_ready= EventHook()
        self.client = ClientNode.register_sink(self)

    def _set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        self._prop_bool = value
        self.on_prop_bool_changed.fire(self._prop_bool)

    def set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        self.client.set_remote_property('testbed1.StructInterface/propBool', testbed1.api.from_struct_bool(value))

    def get_prop_bool(self):
        return self._prop_bool

    def _set_prop_int(self, value):
        if self._prop_int == value:
            return
        self._prop_int = value
        self.on_prop_int_changed.fire(self._prop_int)

    def set_prop_int(self, value):
        if self._prop_int == value:
            return
        self.client.set_remote_property('testbed1.StructInterface/propInt', testbed1.api.from_struct_int(value))

    def get_prop_int(self):
        return self._prop_int

    def _set_prop_float(self, value):
        if self._prop_float == value:
            return
        self._prop_float = value
        self.on_prop_float_changed.fire(self._prop_float)

    def set_prop_float(self, value):
        if self._prop_float == value:
            return
        self.client.set_remote_property('testbed1.StructInterface/propFloat', testbed1.api.from_struct_float(value))

    def get_prop_float(self):
        return self._prop_float

    def _set_prop_string(self, value):
        if self._prop_string == value:
            return
        self._prop_string = value
        self.on_prop_string_changed.fire(self._prop_string)

    def set_prop_string(self, value):
        if self._prop_string == value:
            return
        self.client.set_remote_property('testbed1.StructInterface/propString', testbed1.api.from_struct_string(value))

    def get_prop_string(self):
        return self._prop_string

    async def func_bool(self, param_bool: testbed1.api.StructBool):
        _param_bool = testbed1.api.from_struct_bool(param_bool)
        args = [_param_bool]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(testbed1.api.as_struct_bool(result.value))
        self.client.invoke_remote(f"testbed1.StructInterface/funcBool", args, func)
        return await asyncio.wait_for(future, 500)

    async def func_int(self, param_int: testbed1.api.StructInt):
        _param_int = testbed1.api.from_struct_int(param_int)
        args = [_param_int]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(testbed1.api.as_struct_bool(result.value))
        self.client.invoke_remote(f"testbed1.StructInterface/funcInt", args, func)
        return await asyncio.wait_for(future, 500)

    async def func_float(self, param_float: testbed1.api.StructFloat):
        _param_float = testbed1.api.from_struct_float(param_float)
        args = [_param_float]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(testbed1.api.as_struct_float(result.value))
        self.client.invoke_remote(f"testbed1.StructInterface/funcFloat", args, func)
        return await asyncio.wait_for(future, 500)

    async def func_string(self, param_string: testbed1.api.StructString):
        _param_string = testbed1.api.from_struct_string(param_string)
        args = [_param_string]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(testbed1.api.as_struct_string(result.value))
        self.client.invoke_remote(f"testbed1.StructInterface/funcString", args, func)
        return await asyncio.wait_for(future, 500)

    def olink_object_name(self):
        return 'testbed1.StructInterface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "propBool":
                v =  testbed1.api.as_struct_bool(props[k])
                self._set_prop_bool(v)
            elif k == "propInt":
                v =  testbed1.api.as_struct_int(props[k])
                self._set_prop_int(v)
            elif k == "propFloat":
                v =  testbed1.api.as_struct_float(props[k])
                self._set_prop_float(v)
            elif k == "propString":
                v =  testbed1.api.as_struct_string(props[k])
                self._set_prop_string(v)
        self._on_is_ready.fire()

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "propBool":
            v =  testbed1.api.as_struct_bool(value)
            self._set_prop_bool(v)
            return
        elif path == "propInt":
            v =  testbed1.api.as_struct_int(value)
            self._set_prop_int(v)
            return
        elif path == "propFloat":
            v =  testbed1.api.as_struct_float(value)
            self._set_prop_float(v)
            return
        elif path == "propString":
            v =  testbed1.api.as_struct_string(value)
            self._set_prop_string(v)
            return
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sigBool":
            param_bool =  testbed1.api.as_struct_bool(args[0])
            self.on_sig_bool.fire(param_bool)
            return
        elif path == "sigInt":
            param_int =  testbed1.api.as_struct_int(args[0])
            self.on_sig_int.fire(param_int)
            return
        elif path == "sigFloat":
            param_float =  testbed1.api.as_struct_float(args[0])
            self.on_sig_float.fire(param_float)
            return
        elif path == "sigString":
            param_string =  testbed1.api.as_struct_string(args[0])
            self.on_sig_string.fire(param_string)
            return
        logging.error("unknown signal: %s", name)

class StructArrayInterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._prop_bool = []
        self.on_prop_bool_changed = EventHook()
        self._prop_int = []
        self.on_prop_int_changed = EventHook()
        self._prop_float = []
        self.on_prop_float_changed = EventHook()
        self._prop_string = []
        self.on_prop_string_changed = EventHook()
        self.on_sig_bool = EventHook()
        self.on_sig_int = EventHook()
        self.on_sig_float = EventHook()
        self.on_sig_string = EventHook()
        self._on_is_ready= EventHook()
        self.client = ClientNode.register_sink(self)

    def _set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        self._prop_bool = value
        self.on_prop_bool_changed.fire(self._prop_bool)

    def set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        self.client.set_remote_property('testbed1.StructArrayInterface/propBool', [testbed1.api.from_struct_bool(_) for _ in value])

    def get_prop_bool(self):
        return self._prop_bool

    def _set_prop_int(self, value):
        if self._prop_int == value:
            return
        self._prop_int = value
        self.on_prop_int_changed.fire(self._prop_int)

    def set_prop_int(self, value):
        if self._prop_int == value:
            return
        self.client.set_remote_property('testbed1.StructArrayInterface/propInt', [testbed1.api.from_struct_int(_) for _ in value])

    def get_prop_int(self):
        return self._prop_int

    def _set_prop_float(self, value):
        if self._prop_float == value:
            return
        self._prop_float = value
        self.on_prop_float_changed.fire(self._prop_float)

    def set_prop_float(self, value):
        if self._prop_float == value:
            return
        self.client.set_remote_property('testbed1.StructArrayInterface/propFloat', [testbed1.api.from_struct_float(_) for _ in value])

    def get_prop_float(self):
        return self._prop_float

    def _set_prop_string(self, value):
        if self._prop_string == value:
            return
        self._prop_string = value
        self.on_prop_string_changed.fire(self._prop_string)

    def set_prop_string(self, value):
        if self._prop_string == value:
            return
        self.client.set_remote_property('testbed1.StructArrayInterface/propString', [testbed1.api.from_struct_string(_) for _ in value])

    def get_prop_string(self):
        return self._prop_string

    async def func_bool(self, param_bool: list[testbed1.api.StructBool]):
        _param_bool = [testbed1.api.from_struct_bool(struct_bool) for struct_bool in param_bool]
        args = [_param_bool]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            array_res = result.value
            return future.set_result([testbed1.api.as_struct_bool(_) for _ in array_res])
        self.client.invoke_remote(f"testbed1.StructArrayInterface/funcBool", args, func)
        return await asyncio.wait_for(future, 500)

    async def func_int(self, param_int: list[testbed1.api.StructInt]):
        _param_int = [testbed1.api.from_struct_int(struct_int) for struct_int in param_int]
        args = [_param_int]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            array_res = result.value
            return future.set_result([testbed1.api.as_struct_int(_) for _ in array_res])
        self.client.invoke_remote(f"testbed1.StructArrayInterface/funcInt", args, func)
        return await asyncio.wait_for(future, 500)

    async def func_float(self, param_float: list[testbed1.api.StructFloat]):
        _param_float = [testbed1.api.from_struct_float(struct_float) for struct_float in param_float]
        args = [_param_float]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            array_res = result.value
            return future.set_result([testbed1.api.as_struct_float(_) for _ in array_res])
        self.client.invoke_remote(f"testbed1.StructArrayInterface/funcFloat", args, func)
        return await asyncio.wait_for(future, 500)

    async def func_string(self, param_string: list[testbed1.api.StructString]):
        _param_string = [testbed1.api.from_struct_string(struct_string) for struct_string in param_string]
        args = [_param_string]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            array_res = result.value
            return future.set_result([testbed1.api.as_struct_string(_) for _ in array_res])
        self.client.invoke_remote(f"testbed1.StructArrayInterface/funcString", args, func)
        return await asyncio.wait_for(future, 500)

    def olink_object_name(self):
        return 'testbed1.StructArrayInterface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "propBool":
                v = [testbed1.api.as_struct_bool(_) for _ in props[k]]
                self._set_prop_bool(v)
            elif k == "propInt":
                v = [testbed1.api.as_struct_int(_) for _ in props[k]]
                self._set_prop_int(v)
            elif k == "propFloat":
                v = [testbed1.api.as_struct_float(_) for _ in props[k]]
                self._set_prop_float(v)
            elif k == "propString":
                v = [testbed1.api.as_struct_string(_) for _ in props[k]]
                self._set_prop_string(v)
        self._on_is_ready.fire()

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "propBool":
            v = [testbed1.api.as_struct_bool(_) for _ in value]
            self._set_prop_bool(v)
            return
        elif path == "propInt":
            v = [testbed1.api.as_struct_int(_) for _ in value]
            self._set_prop_int(v)
            return
        elif path == "propFloat":
            v = [testbed1.api.as_struct_float(_) for _ in value]
            self._set_prop_float(v)
            return
        elif path == "propString":
            v = [testbed1.api.as_struct_string(_) for _ in value]
            self._set_prop_string(v)
            return
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sigBool":
            param_bool = [testbed1.api.as_struct_bool(_) for _ in args[0]]
            self.on_sig_bool.fire(param_bool)
            return
        elif path == "sigInt":
            param_int = [testbed1.api.as_struct_int(_) for _ in args[0]]
            self.on_sig_int.fire(param_int)
            return
        elif path == "sigFloat":
            param_float = [testbed1.api.as_struct_float(_) for _ in args[0]]
            self.on_sig_float.fire(param_float)
            return
        elif path == "sigString":
            param_string = [testbed1.api.as_struct_string(_) for _ in args[0]]
            self.on_sig_string.fire(param_string)
            return
        logging.error("unknown signal: %s", name)
