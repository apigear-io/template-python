import asyncio
from typing import Any
from olink.core import Name
from olink.client import IObjectSink, ClientNode
from tb_simple_api.shared import EventHook
from tb_simple_api import api
import logging

class SimpleInterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._prop_bool = False
        self.on_prop_bool_changed = EventHook()
        self._prop_int = 0
        self.on_prop_int_changed = EventHook()
        self._prop_int32 = 0
        self.on_prop_int32_changed = EventHook()
        self._prop_int64 = 0
        self.on_prop_int64_changed = EventHook()
        self._prop_float = 0.0
        self.on_prop_float_changed = EventHook()
        self._prop_float32 = 0.0
        self.on_prop_float32_changed = EventHook()
        self._prop_float64 = 0.0
        self.on_prop_float64_changed = EventHook()
        self._prop_string = ""
        self.on_prop_string_changed = EventHook()
        self._prop_read_only_string = ""
        self.on_prop_read_only_string_changed = EventHook()
        self.on_sig_void = EventHook()
        self.on_sig_bool = EventHook()
        self.on_sig_int = EventHook()
        self.on_sig_int32 = EventHook()
        self.on_sig_int64 = EventHook()
        self.on_sig_float = EventHook()
        self.on_sig_float32 = EventHook()
        self.on_sig_float64 = EventHook()
        self.on_sig_string = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote(f"tb.simple.SimpleInterface/{name}", args, func)
        return await asyncio.wait_for(future, 500)

    def _set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        self._prop_bool = value
        self.on_prop_bool_changed.fire(self._prop_bool)

    def set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        self.client.set_remote_property('tb.simple.SimpleInterface/propBool', value)

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
        self.client.set_remote_property('tb.simple.SimpleInterface/propInt', value)

    def get_prop_int(self):
        return self._prop_int

    def _set_prop_int32(self, value):
        if self._prop_int32 == value:
            return
        self._prop_int32 = value
        self.on_prop_int32_changed.fire(self._prop_int32)

    def set_prop_int32(self, value):
        if self._prop_int32 == value:
            return
        self.client.set_remote_property('tb.simple.SimpleInterface/propInt32', value)

    def get_prop_int32(self):
        return self._prop_int32

    def _set_prop_int64(self, value):
        if self._prop_int64 == value:
            return
        self._prop_int64 = value
        self.on_prop_int64_changed.fire(self._prop_int64)

    def set_prop_int64(self, value):
        if self._prop_int64 == value:
            return
        self.client.set_remote_property('tb.simple.SimpleInterface/propInt64', value)

    def get_prop_int64(self):
        return self._prop_int64

    def _set_prop_float(self, value):
        if self._prop_float == value:
            return
        self._prop_float = value
        self.on_prop_float_changed.fire(self._prop_float)

    def set_prop_float(self, value):
        if self._prop_float == value:
            return
        self.client.set_remote_property('tb.simple.SimpleInterface/propFloat', value)

    def get_prop_float(self):
        return self._prop_float

    def _set_prop_float32(self, value):
        if self._prop_float32 == value:
            return
        self._prop_float32 = value
        self.on_prop_float32_changed.fire(self._prop_float32)

    def set_prop_float32(self, value):
        if self._prop_float32 == value:
            return
        self.client.set_remote_property('tb.simple.SimpleInterface/propFloat32', value)

    def get_prop_float32(self):
        return self._prop_float32

    def _set_prop_float64(self, value):
        if self._prop_float64 == value:
            return
        self._prop_float64 = value
        self.on_prop_float64_changed.fire(self._prop_float64)

    def set_prop_float64(self, value):
        if self._prop_float64 == value:
            return
        self.client.set_remote_property('tb.simple.SimpleInterface/propFloat64', value)

    def get_prop_float64(self):
        return self._prop_float64

    def _set_prop_string(self, value):
        if self._prop_string == value:
            return
        self._prop_string = value
        self.on_prop_string_changed.fire(self._prop_string)

    def set_prop_string(self, value):
        if self._prop_string == value:
            return
        self.client.set_remote_property('tb.simple.SimpleInterface/propString', value)

    def get_prop_string(self):
        return self._prop_string

    def get_prop_read_only_string(self):
        return self._prop_read_only_string

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
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "propBool":
                self._set_prop_bool(props[k])
            elif k == "propInt":
                self._set_prop_int(props[k])
            elif k == "propInt32":
                self._set_prop_int32(props[k])
            elif k == "propInt64":
                self._set_prop_int64(props[k])
            elif k == "propFloat":
                self._set_prop_float(props[k])
            elif k == "propFloat32":
                self._set_prop_float32(props[k])
            elif k == "propFloat64":
                self._set_prop_float64(props[k])
            elif k == "propString":
                self._set_prop_string(props[k])
            elif k == "propReadOnlyString":
                self._set_prop_read_only_string(props[k])

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "propBool":
            v =  api.as_bool(value)
            self._set_prop_bool(v)
            return
        elif path == "propInt":
            v =  api.as_int(value)
            self._set_prop_int(v)
            return
        elif path == "propInt32":
            v =  api.as_int32(value)
            self._set_prop_int32(v)
            return
        elif path == "propInt64":
            v =  api.as_int64(value)
            self._set_prop_int64(v)
            return
        elif path == "propFloat":
            v =  api.as_float(value)
            self._set_prop_float(v)
            return
        elif path == "propFloat32":
            v =  api.as_float32(value)
            self._set_prop_float32(v)
            return
        elif path == "propFloat64":
            v =  api.as_float64(value)
            self._set_prop_float64(v)
            return
        elif path == "propString":
            v =  api.as_string(value)
            self._set_prop_string(v)
            return
        elif path == "propReadOnlyString":
            v =  api.as_string(value)
            self._set_prop_read_only_string(v)
            return
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sigVoid":
            self.on_sig_void.fire()
            return
        elif path == "sigBool":
            _param_bool =  args[0]
            self.on_sig_bool.fire(_param_bool)
            return
        elif path == "sigInt":
            _param_int =  args[0]
            self.on_sig_int.fire(_param_int)
            return
        elif path == "sigInt32":
            _param_int32 =  args[0]
            self.on_sig_int32.fire(_param_int32)
            return
        elif path == "sigInt64":
            _param_int64 =  args[0]
            self.on_sig_int64.fire(_param_int64)
            return
        elif path == "sigFloat":
            _param_float =  args[0]
            self.on_sig_float.fire(_param_float)
            return
        elif path == "sigFloat32":
            _param_float32 =  args[0]
            self.on_sig_float32.fire(_param_float32)
            return
        elif path == "sigFloat64":
            _param_float64 =  args[0]
            self.on_sig_float64.fire(_param_float64)
            return
        elif path == "sigString":
            _param_string =  args[0]
            self.on_sig_string.fire(_param_string)
            return
        logging.error("unknown signal: %s", name)

class SimpleArrayInterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._prop_bool = []
        self.on_prop_bool_changed = EventHook()
        self._prop_int = []
        self.on_prop_int_changed = EventHook()
        self._prop_int32 = []
        self.on_prop_int32_changed = EventHook()
        self._prop_int64 = []
        self.on_prop_int64_changed = EventHook()
        self._prop_float = []
        self.on_prop_float_changed = EventHook()
        self._prop_float32 = []
        self.on_prop_float32_changed = EventHook()
        self._prop_float64 = []
        self.on_prop_float64_changed = EventHook()
        self._prop_string = []
        self.on_prop_string_changed = EventHook()
        self.on_sig_bool = EventHook()
        self.on_sig_int = EventHook()
        self.on_sig_int32 = EventHook()
        self.on_sig_int64 = EventHook()
        self.on_sig_float = EventHook()
        self.on_sig_float32 = EventHook()
        self.on_sig_float64 = EventHook()
        self.on_sig_string = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote(f"tb.simple.SimpleArrayInterface/{name}", args, func)
        return await asyncio.wait_for(future, 500)

    def _set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        self._prop_bool = [api.as_bool(_) for _ in value]
        self.on_prop_bool_changed.fire(self._prop_bool)

    def set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        self.client.set_remote_property('tb.simple.SimpleArrayInterface/propBool', [api.from_bool(_) for _ in value])

    def get_prop_bool(self):
        return self._prop_bool

    def _set_prop_int(self, value):
        if self._prop_int == value:
            return
        self._prop_int = [api.as_int(_) for _ in value]
        self.on_prop_int_changed.fire(self._prop_int)

    def set_prop_int(self, value):
        if self._prop_int == value:
            return
        self.client.set_remote_property('tb.simple.SimpleArrayInterface/propInt', [api.from_int(_) for _ in value])

    def get_prop_int(self):
        return self._prop_int

    def _set_prop_int32(self, value):
        if self._prop_int32 == value:
            return
        self._prop_int32 = [api.as_int32(_) for _ in value]
        self.on_prop_int32_changed.fire(self._prop_int32)

    def set_prop_int32(self, value):
        if self._prop_int32 == value:
            return
        self.client.set_remote_property('tb.simple.SimpleArrayInterface/propInt32', [api.from_int32(_) for _ in value])

    def get_prop_int32(self):
        return self._prop_int32

    def _set_prop_int64(self, value):
        if self._prop_int64 == value:
            return
        self._prop_int64 = [api.as_int64(_) for _ in value]
        self.on_prop_int64_changed.fire(self._prop_int64)

    def set_prop_int64(self, value):
        if self._prop_int64 == value:
            return
        self.client.set_remote_property('tb.simple.SimpleArrayInterface/propInt64', [api.from_int64(_) for _ in value])

    def get_prop_int64(self):
        return self._prop_int64

    def _set_prop_float(self, value):
        if self._prop_float == value:
            return
        self._prop_float = [api.as_float(_) for _ in value]
        self.on_prop_float_changed.fire(self._prop_float)

    def set_prop_float(self, value):
        if self._prop_float == value:
            return
        self.client.set_remote_property('tb.simple.SimpleArrayInterface/propFloat', [api.from_float(_) for _ in value])

    def get_prop_float(self):
        return self._prop_float

    def _set_prop_float32(self, value):
        if self._prop_float32 == value:
            return
        self._prop_float32 = [api.as_float32(_) for _ in value]
        self.on_prop_float32_changed.fire(self._prop_float32)

    def set_prop_float32(self, value):
        if self._prop_float32 == value:
            return
        self.client.set_remote_property('tb.simple.SimpleArrayInterface/propFloat32', [api.from_float32(_) for _ in value])

    def get_prop_float32(self):
        return self._prop_float32

    def _set_prop_float64(self, value):
        if self._prop_float64 == value:
            return
        self._prop_float64 = [api.as_float64(_) for _ in value]
        self.on_prop_float64_changed.fire(self._prop_float64)

    def set_prop_float64(self, value):
        if self._prop_float64 == value:
            return
        self.client.set_remote_property('tb.simple.SimpleArrayInterface/propFloat64', [api.from_float64(_) for _ in value])

    def get_prop_float64(self):
        return self._prop_float64

    def _set_prop_string(self, value):
        if self._prop_string == value:
            return
        self._prop_string = [api.as_string(_) for _ in value]
        self.on_prop_string_changed.fire(self._prop_string)

    def set_prop_string(self, value):
        if self._prop_string == value:
            return
        self.client.set_remote_property('tb.simple.SimpleArrayInterface/propString', [api.from_string(_) for _ in value])

    def get_prop_string(self):
        return self._prop_string

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
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "propBool":
                self._set_prop_bool(props[k])
            elif k == "propInt":
                self._set_prop_int(props[k])
            elif k == "propInt32":
                self._set_prop_int32(props[k])
            elif k == "propInt64":
                self._set_prop_int64(props[k])
            elif k == "propFloat":
                self._set_prop_float(props[k])
            elif k == "propFloat32":
                self._set_prop_float32(props[k])
            elif k == "propFloat64":
                self._set_prop_float64(props[k])
            elif k == "propString":
                self._set_prop_string(props[k])

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "propBool":
            v = [api.as_bool(_) for _ in value]
            self._set_prop_bool(v)
            return
        elif path == "propInt":
            v = [api.as_int(_) for _ in value]
            self._set_prop_int(v)
            return
        elif path == "propInt32":
            v = [api.as_int32(_) for _ in value]
            self._set_prop_int32(v)
            return
        elif path == "propInt64":
            v = [api.as_int64(_) for _ in value]
            self._set_prop_int64(v)
            return
        elif path == "propFloat":
            v = [api.as_float(_) for _ in value]
            self._set_prop_float(v)
            return
        elif path == "propFloat32":
            v = [api.as_float32(_) for _ in value]
            self._set_prop_float32(v)
            return
        elif path == "propFloat64":
            v = [api.as_float64(_) for _ in value]
            self._set_prop_float64(v)
            return
        elif path == "propString":
            v = [api.as_string(_) for _ in value]
            self._set_prop_string(v)
            return
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sigBool":
            _param_bool = [api.as_bool(_) for _ in args[0]]
            self.on_sig_bool.fire(_param_bool)
            return
        elif path == "sigInt":
            _param_int = [api.as_int(_) for _ in args[0]]
            self.on_sig_int.fire(_param_int)
            return
        elif path == "sigInt32":
            _param_int32 = [api.as_int32(_) for _ in args[0]]
            self.on_sig_int32.fire(_param_int32)
            return
        elif path == "sigInt64":
            _param_int64 = [api.as_int64(_) for _ in args[0]]
            self.on_sig_int64.fire(_param_int64)
            return
        elif path == "sigFloat":
            _param_float = [api.as_float(_) for _ in args[0]]
            self.on_sig_float.fire(_param_float)
            return
        elif path == "sigFloat32":
            _param_float32 = [api.as_float32(_) for _ in args[0]]
            self.on_sig_float32.fire(_param_float32)
            return
        elif path == "sigFloat64":
            _param_float64 = [api.as_float64(_) for _ in args[0]]
            self.on_sig_float64.fire(_param_float64)
            return
        elif path == "sigString":
            _param_string = [api.as_string(_) for _ in args[0]]
            self.on_sig_string.fire(_param_string)
            return
        logging.error("unknown signal: %s", name)

class NoPropertiesInterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self.on_sig_void = EventHook()
        self.on_sig_bool = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote(f"tb.simple.NoPropertiesInterface/{name}", args, func)
        return await asyncio.wait_for(future, 500)

    async def func_void(self):
        return await self._invoke("funcVoid", [])

    async def func_bool(self, param_bool: bool):
        return await self._invoke("funcBool", [param_bool])

    def olink_object_name(self):
        return 'tb.simple.NoPropertiesInterface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sigVoid":
            self.on_sig_void.fire()
            return
        elif path == "sigBool":
            _param_bool =  args[0]
            self.on_sig_bool.fire(_param_bool)
            return
        logging.error("unknown signal: %s", name)

class NoOperationsInterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._prop_bool = False
        self.on_prop_bool_changed = EventHook()
        self._prop_int = 0
        self.on_prop_int_changed = EventHook()
        self.on_sig_void = EventHook()
        self.on_sig_bool = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote(f"tb.simple.NoOperationsInterface/{name}", args, func)
        return await asyncio.wait_for(future, 500)

    def _set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        self._prop_bool = value
        self.on_prop_bool_changed.fire(self._prop_bool)

    def set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        self.client.set_remote_property('tb.simple.NoOperationsInterface/propBool', value)

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
        self.client.set_remote_property('tb.simple.NoOperationsInterface/propInt', value)

    def get_prop_int(self):
        return self._prop_int

    def olink_object_name(self):
        return 'tb.simple.NoOperationsInterface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "propBool":
                self._set_prop_bool(props[k])
            elif k == "propInt":
                self._set_prop_int(props[k])

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "propBool":
            v =  api.as_bool(value)
            self._set_prop_bool(v)
            return
        elif path == "propInt":
            v =  api.as_int(value)
            self._set_prop_int(v)
            return
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sigVoid":
            self.on_sig_void.fire()
            return
        elif path == "sigBool":
            _param_bool =  args[0]
            self.on_sig_bool.fire(_param_bool)
            return
        logging.error("unknown signal: %s", name)

class NoSignalsInterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._prop_bool = False
        self.on_prop_bool_changed = EventHook()
        self._prop_int = 0
        self.on_prop_int_changed = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote(f"tb.simple.NoSignalsInterface/{name}", args, func)
        return await asyncio.wait_for(future, 500)

    def _set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        self._prop_bool = value
        self.on_prop_bool_changed.fire(self._prop_bool)

    def set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        self.client.set_remote_property('tb.simple.NoSignalsInterface/propBool', value)

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
        self.client.set_remote_property('tb.simple.NoSignalsInterface/propInt', value)

    def get_prop_int(self):
        return self._prop_int

    async def func_void(self):
        return await self._invoke("funcVoid", [])

    async def func_bool(self, param_bool: bool):
        return await self._invoke("funcBool", [param_bool])

    def olink_object_name(self):
        return 'tb.simple.NoSignalsInterface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "propBool":
                self._set_prop_bool(props[k])
            elif k == "propInt":
                self._set_prop_int(props[k])

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "propBool":
            v =  api.as_bool(value)
            self._set_prop_bool(v)
            return
        elif path == "propInt":
            v =  api.as_int(value)
            self._set_prop_int(v)
            return
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        logging.error("unknown signal: %s", name)

class EmptyInterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote(f"tb.simple.EmptyInterface/{name}", args, func)
        return await asyncio.wait_for(future, 500)

    def olink_object_name(self):
        return 'tb.simple.EmptyInterface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        logging.error("unknown signal: %s", name)
