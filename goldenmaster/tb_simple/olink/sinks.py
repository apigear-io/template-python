import asyncio
from typing import Any
from olink.core import Name
from olink.client import IObjectSink, ClientNode
from utils.eventhook import EventHook
import utils.base_types
import tb_simple.api
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
        self.client.set_remote_property('tb.simple.SimpleInterface/propBool', utils.base_types.from_bool(value))

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
        self.client.set_remote_property('tb.simple.SimpleInterface/propInt', utils.base_types.from_int(value))

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
        self.client.set_remote_property('tb.simple.SimpleInterface/propInt32', utils.base_types.from_int32(value))

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
        self.client.set_remote_property('tb.simple.SimpleInterface/propInt64', utils.base_types.from_int64(value))

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
        self.client.set_remote_property('tb.simple.SimpleInterface/propFloat', utils.base_types.from_float(value))

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
        self.client.set_remote_property('tb.simple.SimpleInterface/propFloat32', utils.base_types.from_float32(value))

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
        self.client.set_remote_property('tb.simple.SimpleInterface/propFloat64', utils.base_types.from_float64(value))

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
        self.client.set_remote_property('tb.simple.SimpleInterface/propString', utils.base_types.from_string(value))

    def get_prop_string(self):
        return self._prop_string

    def get_prop_read_only_string(self):
        return self._prop_read_only_string

    async def func_void(self):
        args = []
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(None)
        self.client.invoke_remote(f"tb.simple.SimpleInterface/funcVoid", args, func)
        return await asyncio.wait_for(future, 500)

    async def func_bool(self, param_bool: bool):
        _param_bool = utils.base_types.from_bool(param_bool)
        args = [_param_bool]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(utils.base_types.as_bool(result.value))
        self.client.invoke_remote(f"tb.simple.SimpleInterface/funcBool", args, func)
        return await asyncio.wait_for(future, 500)

    async def func_int(self, param_int: int):
        _param_int = utils.base_types.from_int(param_int)
        args = [_param_int]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(utils.base_types.as_int(result.value))
        self.client.invoke_remote(f"tb.simple.SimpleInterface/funcInt", args, func)
        return await asyncio.wait_for(future, 500)

    async def func_int32(self, param_int32: int):
        _param_int32 = utils.base_types.from_int32(param_int32)
        args = [_param_int32]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(utils.base_types.as_int32(result.value))
        self.client.invoke_remote(f"tb.simple.SimpleInterface/funcInt32", args, func)
        return await asyncio.wait_for(future, 500)

    async def func_int64(self, param_int64: int):
        _param_int64 = utils.base_types.from_int64(param_int64)
        args = [_param_int64]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(utils.base_types.as_int64(result.value))
        self.client.invoke_remote(f"tb.simple.SimpleInterface/funcInt64", args, func)
        return await asyncio.wait_for(future, 500)

    async def func_float(self, param_float: float):
        _param_float = utils.base_types.from_float(param_float)
        args = [_param_float]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(utils.base_types.as_float(result.value))
        self.client.invoke_remote(f"tb.simple.SimpleInterface/funcFloat", args, func)
        return await asyncio.wait_for(future, 500)

    async def func_float32(self, param_float32: float):
        _param_float32 = utils.base_types.from_float32(param_float32)
        args = [_param_float32]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(utils.base_types.as_float32(result.value))
        self.client.invoke_remote(f"tb.simple.SimpleInterface/funcFloat32", args, func)
        return await asyncio.wait_for(future, 500)

    async def func_float64(self, param_float: float):
        _param_float = utils.base_types.from_float64(param_float)
        args = [_param_float]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(utils.base_types.as_float64(result.value))
        self.client.invoke_remote(f"tb.simple.SimpleInterface/funcFloat64", args, func)
        return await asyncio.wait_for(future, 500)

    async def func_string(self, param_string: str):
        _param_string = utils.base_types.from_string(param_string)
        args = [_param_string]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(utils.base_types.as_string(result.value))
        self.client.invoke_remote(f"tb.simple.SimpleInterface/funcString", args, func)
        return await asyncio.wait_for(future, 500)

    def olink_object_name(self):
        return 'tb.simple.SimpleInterface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "propBool":
                v =  utils.base_types.as_bool(props[k])
                self._set_prop_bool(v)
            elif k == "propInt":
                v =  utils.base_types.as_int(props[k])
                self._set_prop_int(v)
            elif k == "propInt32":
                v =  utils.base_types.as_int32(props[k])
                self._set_prop_int32(v)
            elif k == "propInt64":
                v =  utils.base_types.as_int64(props[k])
                self._set_prop_int64(v)
            elif k == "propFloat":
                v =  utils.base_types.as_float(props[k])
                self._set_prop_float(v)
            elif k == "propFloat32":
                v =  utils.base_types.as_float32(props[k])
                self._set_prop_float32(v)
            elif k == "propFloat64":
                v =  utils.base_types.as_float64(props[k])
                self._set_prop_float64(v)
            elif k == "propString":
                v =  utils.base_types.as_string(props[k])
                self._set_prop_string(v)
            elif k == "propReadOnlyString":
                v =  utils.base_types.as_string(props[k])
                self._set_prop_read_only_string(v)
        self._on_is_ready.fire()

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "propBool":
            v =  utils.base_types.as_bool(value)
            self._set_prop_bool(v)
            return
        elif path == "propInt":
            v =  utils.base_types.as_int(value)
            self._set_prop_int(v)
            return
        elif path == "propInt32":
            v =  utils.base_types.as_int32(value)
            self._set_prop_int32(v)
            return
        elif path == "propInt64":
            v =  utils.base_types.as_int64(value)
            self._set_prop_int64(v)
            return
        elif path == "propFloat":
            v =  utils.base_types.as_float(value)
            self._set_prop_float(v)
            return
        elif path == "propFloat32":
            v =  utils.base_types.as_float32(value)
            self._set_prop_float32(v)
            return
        elif path == "propFloat64":
            v =  utils.base_types.as_float64(value)
            self._set_prop_float64(v)
            return
        elif path == "propString":
            v =  utils.base_types.as_string(value)
            self._set_prop_string(v)
            return
        elif path == "propReadOnlyString":
            v =  utils.base_types.as_string(value)
            self._set_prop_read_only_string(v)
            return
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sigVoid":
            self.on_sig_void.fire()
            return
        elif path == "sigBool":
            param_bool =  utils.base_types.as_bool(args[0])
            self.on_sig_bool.fire(param_bool)
            return
        elif path == "sigInt":
            param_int =  utils.base_types.as_int(args[0])
            self.on_sig_int.fire(param_int)
            return
        elif path == "sigInt32":
            param_int32 =  utils.base_types.as_int32(args[0])
            self.on_sig_int32.fire(param_int32)
            return
        elif path == "sigInt64":
            param_int64 =  utils.base_types.as_int64(args[0])
            self.on_sig_int64.fire(param_int64)
            return
        elif path == "sigFloat":
            param_float =  utils.base_types.as_float(args[0])
            self.on_sig_float.fire(param_float)
            return
        elif path == "sigFloat32":
            param_float32 =  utils.base_types.as_float32(args[0])
            self.on_sig_float32.fire(param_float32)
            return
        elif path == "sigFloat64":
            param_float64 =  utils.base_types.as_float64(args[0])
            self.on_sig_float64.fire(param_float64)
            return
        elif path == "sigString":
            param_string =  utils.base_types.as_string(args[0])
            self.on_sig_string.fire(param_string)
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
        self.client.set_remote_property('tb.simple.SimpleArrayInterface/propBool', [utils.base_types.from_bool(_) for _ in value])

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
        self.client.set_remote_property('tb.simple.SimpleArrayInterface/propInt', [utils.base_types.from_int(_) for _ in value])

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
        self.client.set_remote_property('tb.simple.SimpleArrayInterface/propInt32', [utils.base_types.from_int32(_) for _ in value])

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
        self.client.set_remote_property('tb.simple.SimpleArrayInterface/propInt64', [utils.base_types.from_int64(_) for _ in value])

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
        self.client.set_remote_property('tb.simple.SimpleArrayInterface/propFloat', [utils.base_types.from_float(_) for _ in value])

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
        self.client.set_remote_property('tb.simple.SimpleArrayInterface/propFloat32', [utils.base_types.from_float32(_) for _ in value])

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
        self.client.set_remote_property('tb.simple.SimpleArrayInterface/propFloat64', [utils.base_types.from_float64(_) for _ in value])

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
        self.client.set_remote_property('tb.simple.SimpleArrayInterface/propString', [utils.base_types.from_string(_) for _ in value])

    def get_prop_string(self):
        return self._prop_string

    async def func_bool(self, param_bool: list[bool]):
        _param_bool = [utils.base_types.from_bool(bool) for bool in param_bool]
        args = [_param_bool]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            array_res = result.value
            return future.set_result([utils.base_types.as_bool(_) for _ in array_res])
        self.client.invoke_remote(f"tb.simple.SimpleArrayInterface/funcBool", args, func)
        return await asyncio.wait_for(future, 500)

    async def func_int(self, param_int: list[int]):
        _param_int = [utils.base_types.from_int(int) for int in param_int]
        args = [_param_int]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            array_res = result.value
            return future.set_result([utils.base_types.as_int(_) for _ in array_res])
        self.client.invoke_remote(f"tb.simple.SimpleArrayInterface/funcInt", args, func)
        return await asyncio.wait_for(future, 500)

    async def func_int32(self, param_int32: list[int]):
        _param_int32 = [utils.base_types.from_int32(int32) for int32 in param_int32]
        args = [_param_int32]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            array_res = result.value
            return future.set_result([utils.base_types.as_int32(_) for _ in array_res])
        self.client.invoke_remote(f"tb.simple.SimpleArrayInterface/funcInt32", args, func)
        return await asyncio.wait_for(future, 500)

    async def func_int64(self, param_int64: list[int]):
        _param_int64 = [utils.base_types.from_int64(int64) for int64 in param_int64]
        args = [_param_int64]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            array_res = result.value
            return future.set_result([utils.base_types.as_int64(_) for _ in array_res])
        self.client.invoke_remote(f"tb.simple.SimpleArrayInterface/funcInt64", args, func)
        return await asyncio.wait_for(future, 500)

    async def func_float(self, param_float: list[float]):
        _param_float = [utils.base_types.from_float(float) for float in param_float]
        args = [_param_float]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            array_res = result.value
            return future.set_result([utils.base_types.as_float(_) for _ in array_res])
        self.client.invoke_remote(f"tb.simple.SimpleArrayInterface/funcFloat", args, func)
        return await asyncio.wait_for(future, 500)

    async def func_float32(self, param_float32: list[float]):
        _param_float32 = [utils.base_types.from_float32(float32) for float32 in param_float32]
        args = [_param_float32]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            array_res = result.value
            return future.set_result([utils.base_types.as_float32(_) for _ in array_res])
        self.client.invoke_remote(f"tb.simple.SimpleArrayInterface/funcFloat32", args, func)
        return await asyncio.wait_for(future, 500)

    async def func_float64(self, param_float: list[float]):
        _param_float = [utils.base_types.from_float64(float64) for float64 in param_float]
        args = [_param_float]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            array_res = result.value
            return future.set_result([utils.base_types.as_float64(_) for _ in array_res])
        self.client.invoke_remote(f"tb.simple.SimpleArrayInterface/funcFloat64", args, func)
        return await asyncio.wait_for(future, 500)

    async def func_string(self, param_string: list[str]):
        _param_string = [utils.base_types.from_string(string) for string in param_string]
        args = [_param_string]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            array_res = result.value
            return future.set_result([utils.base_types.as_string(_) for _ in array_res])
        self.client.invoke_remote(f"tb.simple.SimpleArrayInterface/funcString", args, func)
        return await asyncio.wait_for(future, 500)

    def olink_object_name(self):
        return 'tb.simple.SimpleArrayInterface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "propBool":
                v = [utils.base_types.as_bool(_) for _ in props[k]]
                self._set_prop_bool(v)
            elif k == "propInt":
                v = [utils.base_types.as_int(_) for _ in props[k]]
                self._set_prop_int(v)
            elif k == "propInt32":
                v = [utils.base_types.as_int32(_) for _ in props[k]]
                self._set_prop_int32(v)
            elif k == "propInt64":
                v = [utils.base_types.as_int64(_) for _ in props[k]]
                self._set_prop_int64(v)
            elif k == "propFloat":
                v = [utils.base_types.as_float(_) for _ in props[k]]
                self._set_prop_float(v)
            elif k == "propFloat32":
                v = [utils.base_types.as_float32(_) for _ in props[k]]
                self._set_prop_float32(v)
            elif k == "propFloat64":
                v = [utils.base_types.as_float64(_) for _ in props[k]]
                self._set_prop_float64(v)
            elif k == "propString":
                v = [utils.base_types.as_string(_) for _ in props[k]]
                self._set_prop_string(v)
        self._on_is_ready.fire()

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "propBool":
            v = [utils.base_types.as_bool(_) for _ in value]
            self._set_prop_bool(v)
            return
        elif path == "propInt":
            v = [utils.base_types.as_int(_) for _ in value]
            self._set_prop_int(v)
            return
        elif path == "propInt32":
            v = [utils.base_types.as_int32(_) for _ in value]
            self._set_prop_int32(v)
            return
        elif path == "propInt64":
            v = [utils.base_types.as_int64(_) for _ in value]
            self._set_prop_int64(v)
            return
        elif path == "propFloat":
            v = [utils.base_types.as_float(_) for _ in value]
            self._set_prop_float(v)
            return
        elif path == "propFloat32":
            v = [utils.base_types.as_float32(_) for _ in value]
            self._set_prop_float32(v)
            return
        elif path == "propFloat64":
            v = [utils.base_types.as_float64(_) for _ in value]
            self._set_prop_float64(v)
            return
        elif path == "propString":
            v = [utils.base_types.as_string(_) for _ in value]
            self._set_prop_string(v)
            return
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sigBool":
            param_bool = [utils.base_types.as_bool(_) for _ in args[0]]
            self.on_sig_bool.fire(param_bool)
            return
        elif path == "sigInt":
            param_int = [utils.base_types.as_int(_) for _ in args[0]]
            self.on_sig_int.fire(param_int)
            return
        elif path == "sigInt32":
            param_int32 = [utils.base_types.as_int32(_) for _ in args[0]]
            self.on_sig_int32.fire(param_int32)
            return
        elif path == "sigInt64":
            param_int64 = [utils.base_types.as_int64(_) for _ in args[0]]
            self.on_sig_int64.fire(param_int64)
            return
        elif path == "sigFloat":
            param_float = [utils.base_types.as_float(_) for _ in args[0]]
            self.on_sig_float.fire(param_float)
            return
        elif path == "sigFloat32":
            param_float32 = [utils.base_types.as_float32(_) for _ in args[0]]
            self.on_sig_float32.fire(param_float32)
            return
        elif path == "sigFloat64":
            param_float64 = [utils.base_types.as_float64(_) for _ in args[0]]
            self.on_sig_float64.fire(param_float64)
            return
        elif path == "sigString":
            param_string = [utils.base_types.as_string(_) for _ in args[0]]
            self.on_sig_string.fire(param_string)
            return
        logging.error("unknown signal: %s", name)

class NoPropertiesInterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self.on_sig_void = EventHook()
        self.on_sig_bool = EventHook()
        self._on_is_ready= EventHook()
        self.client = ClientNode.register_sink(self)

    async def func_void(self):
        args = []
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(None)
        self.client.invoke_remote(f"tb.simple.NoPropertiesInterface/funcVoid", args, func)
        return await asyncio.wait_for(future, 500)

    async def func_bool(self, param_bool: bool):
        _param_bool = utils.base_types.from_bool(param_bool)
        args = [_param_bool]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(utils.base_types.as_bool(result.value))
        self.client.invoke_remote(f"tb.simple.NoPropertiesInterface/funcBool", args, func)
        return await asyncio.wait_for(future, 500)

    def olink_object_name(self):
        return 'tb.simple.NoPropertiesInterface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        self._on_is_ready.fire()

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sigVoid":
            self.on_sig_void.fire()
            return
        elif path == "sigBool":
            param_bool =  utils.base_types.as_bool(args[0])
            self.on_sig_bool.fire(param_bool)
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
        self.client.set_remote_property('tb.simple.NoOperationsInterface/propBool', utils.base_types.from_bool(value))

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
        self.client.set_remote_property('tb.simple.NoOperationsInterface/propInt', utils.base_types.from_int(value))

    def get_prop_int(self):
        return self._prop_int

    def olink_object_name(self):
        return 'tb.simple.NoOperationsInterface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "propBool":
                v =  utils.base_types.as_bool(props[k])
                self._set_prop_bool(v)
            elif k == "propInt":
                v =  utils.base_types.as_int(props[k])
                self._set_prop_int(v)
        self._on_is_ready.fire()

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "propBool":
            v =  utils.base_types.as_bool(value)
            self._set_prop_bool(v)
            return
        elif path == "propInt":
            v =  utils.base_types.as_int(value)
            self._set_prop_int(v)
            return
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sigVoid":
            self.on_sig_void.fire()
            return
        elif path == "sigBool":
            param_bool =  utils.base_types.as_bool(args[0])
            self.on_sig_bool.fire(param_bool)
            return
        logging.error("unknown signal: %s", name)

class NoSignalsInterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._prop_bool = False
        self.on_prop_bool_changed = EventHook()
        self._prop_int = 0
        self.on_prop_int_changed = EventHook()
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
        self.client.set_remote_property('tb.simple.NoSignalsInterface/propBool', utils.base_types.from_bool(value))

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
        self.client.set_remote_property('tb.simple.NoSignalsInterface/propInt', utils.base_types.from_int(value))

    def get_prop_int(self):
        return self._prop_int

    async def func_void(self):
        args = []
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(None)
        self.client.invoke_remote(f"tb.simple.NoSignalsInterface/funcVoid", args, func)
        return await asyncio.wait_for(future, 500)

    async def func_bool(self, param_bool: bool):
        _param_bool = utils.base_types.from_bool(param_bool)
        args = [_param_bool]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(utils.base_types.as_bool(result.value))
        self.client.invoke_remote(f"tb.simple.NoSignalsInterface/funcBool", args, func)
        return await asyncio.wait_for(future, 500)

    def olink_object_name(self):
        return 'tb.simple.NoSignalsInterface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "propBool":
                v =  utils.base_types.as_bool(props[k])
                self._set_prop_bool(v)
            elif k == "propInt":
                v =  utils.base_types.as_int(props[k])
                self._set_prop_int(v)
        self._on_is_ready.fire()

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "propBool":
            v =  utils.base_types.as_bool(value)
            self._set_prop_bool(v)
            return
        elif path == "propInt":
            v =  utils.base_types.as_int(value)
            self._set_prop_int(v)
            return
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        logging.error("unknown signal: %s", name)

class EmptyInterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._on_is_ready= EventHook()
        self.client = ClientNode.register_sink(self)

    def olink_object_name(self):
        return 'tb.simple.EmptyInterface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        self._on_is_ready.fire()

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        logging.error("unknown signal: %s", name)
