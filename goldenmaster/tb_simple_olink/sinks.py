import asyncio
from typing import Any
from olink.core import Name
from olink.client import IObjectSink, ClientNode
from tb_simple_api.shared import EventHook
from tb_simple_api import api

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
        self.client.invoke_remote('tb.simple.SimpleInterface/SimpleInterface', args, func)
        return await asyncio.wait_for(future, 500)

    def _set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        path = Name.path_from_name("propBool")
        self._prop_bool = value
        self.on_property_changed.fire(path, self._prop_bool)

    def set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        self.client.set_remote_property('tb.simple.SimpleInterface/propBool', value)

    def get_prop_bool(self):
        return self._prop_bool

    def _set_prop_int(self, value):
        if self._prop_int == value:
            return
        path = Name.path_from_name("propInt")
        self._prop_int = value
        self.on_property_changed.fire(path, self._prop_int)

    def set_prop_int(self, value):
        if self._prop_int == value:
            return
        self.client.set_remote_property('tb.simple.SimpleInterface/propInt', value)

    def get_prop_int(self):
        return self._prop_int

    def _set_prop_int32(self, value):
        if self._prop_int32 == value:
            return
        path = Name.path_from_name("propInt32")
        self._prop_int32 = value
        self.on_property_changed.fire(path, self._prop_int32)

    def set_prop_int32(self, value):
        if self._prop_int32 == value:
            return
        self.client.set_remote_property('tb.simple.SimpleInterface/propInt32', value)

    def get_prop_int32(self):
        return self._prop_int32

    def _set_prop_int64(self, value):
        if self._prop_int64 == value:
            return
        path = Name.path_from_name("propInt64")
        self._prop_int64 = value
        self.on_property_changed.fire(path, self._prop_int64)

    def set_prop_int64(self, value):
        if self._prop_int64 == value:
            return
        self.client.set_remote_property('tb.simple.SimpleInterface/propInt64', value)

    def get_prop_int64(self):
        return self._prop_int64

    def _set_prop_float(self, value):
        if self._prop_float == value:
            return
        path = Name.path_from_name("propFloat")
        self._prop_float = value
        self.on_property_changed.fire(path, self._prop_float)

    def set_prop_float(self, value):
        if self._prop_float == value:
            return
        self.client.set_remote_property('tb.simple.SimpleInterface/propFloat', value)

    def get_prop_float(self):
        return self._prop_float

    def _set_prop_float32(self, value):
        if self._prop_float32 == value:
            return
        path = Name.path_from_name("propFloat32")
        self._prop_float32 = value
        self.on_property_changed.fire(path, self._prop_float32)

    def set_prop_float32(self, value):
        if self._prop_float32 == value:
            return
        self.client.set_remote_property('tb.simple.SimpleInterface/propFloat32', value)

    def get_prop_float32(self):
        return self._prop_float32

    def _set_prop_float64(self, value):
        if self._prop_float64 == value:
            return
        path = Name.path_from_name("propFloat64")
        self._prop_float64 = value
        self.on_property_changed.fire(path, self._prop_float64)

    def set_prop_float64(self, value):
        if self._prop_float64 == value:
            return
        self.client.set_remote_property('tb.simple.SimpleInterface/propFloat64', value)

    def get_prop_float64(self):
        return self._prop_float64

    def _set_prop_string(self, value):
        if self._prop_string == value:
            return
        path = Name.path_from_name("propString")
        self._prop_string = value
        self.on_property_changed.fire(path, self._prop_string)

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
            self._prop_bool =  value
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop_bool)
        elif path == "propInt":
            self._prop_int =  value
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop_int)
        elif path == "propInt32":
            self._prop_int32 =  value
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop_int32)
        elif path == "propInt64":
            self._prop_int64 =  value
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop_int64)
        elif path == "propFloat":
            self._prop_float =  value
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop_float)
        elif path == "propFloat32":
            self._prop_float32 =  value
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop_float32)
        elif path == "propFloat64":
            self._prop_float64 =  value
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop_float64)
        elif path == "propString":
            self._prop_string =  value
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop_string)
        elif path == "propReadOnlyString":
            self._prop_read_only_string =  value
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop_read_only_string)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sigVoid":
            self.on_sig_void.fire()
        elif path == "sigBool":
            _param_bool =  args[0]
            self.on_sig_bool.fire(_param_bool)
        elif path == "sigInt":
            _param_int =  args[0]
            self.on_sig_int.fire(_param_int)
        elif path == "sigInt32":
            _param_int32 =  args[0]
            self.on_sig_int32.fire(_param_int32)
        elif path == "sigInt64":
            _param_int64 =  args[0]
            self.on_sig_int64.fire(_param_int64)
        elif path == "sigFloat":
            _param_float =  args[0]
            self.on_sig_float.fire(_param_float)
        elif path == "sigFloat32":
            _param_float32 =  args[0]
            self.on_sig_float32.fire(_param_float32)
        elif path == "sigFloat64":
            _param_float64 =  args[0]
            self.on_sig_float64.fire(_param_float64)
        elif path == "sigString":
            _param_string =  args[0]
            self.on_sig_string.fire(_param_string)

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
        self.client.invoke_remote('tb.simple.SimpleArrayInterface/SimpleArrayInterface', args, func)
        return await asyncio.wait_for(future, 500)

    def _set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        path = Name.path_from_name("propBool")
        self._prop_bool = [api.as_bool(_) for _ in value]
        self.on_property_changed.fire(path, self._prop_bool)

    def set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        self.client.set_remote_property('tb.simple.SimpleArrayInterface/propBool', [api.from_bool(_) for _ in value])

    def get_prop_bool(self):
        return self._prop_bool

    def _set_prop_int(self, value):
        if self._prop_int == value:
            return
        path = Name.path_from_name("propInt")
        self._prop_int = [api.as_int(_) for _ in value]
        self.on_property_changed.fire(path, self._prop_int)

    def set_prop_int(self, value):
        if self._prop_int == value:
            return
        self.client.set_remote_property('tb.simple.SimpleArrayInterface/propInt', [api.from_int(_) for _ in value])

    def get_prop_int(self):
        return self._prop_int

    def _set_prop_int32(self, value):
        if self._prop_int32 == value:
            return
        path = Name.path_from_name("propInt32")
        self._prop_int32 = [api.as_int32(_) for _ in value]
        self.on_property_changed.fire(path, self._prop_int32)

    def set_prop_int32(self, value):
        if self._prop_int32 == value:
            return
        self.client.set_remote_property('tb.simple.SimpleArrayInterface/propInt32', [api.from_int32(_) for _ in value])

    def get_prop_int32(self):
        return self._prop_int32

    def _set_prop_int64(self, value):
        if self._prop_int64 == value:
            return
        path = Name.path_from_name("propInt64")
        self._prop_int64 = [api.as_int64(_) for _ in value]
        self.on_property_changed.fire(path, self._prop_int64)

    def set_prop_int64(self, value):
        if self._prop_int64 == value:
            return
        self.client.set_remote_property('tb.simple.SimpleArrayInterface/propInt64', [api.from_int64(_) for _ in value])

    def get_prop_int64(self):
        return self._prop_int64

    def _set_prop_float(self, value):
        if self._prop_float == value:
            return
        path = Name.path_from_name("propFloat")
        self._prop_float = [api.as_float(_) for _ in value]
        self.on_property_changed.fire(path, self._prop_float)

    def set_prop_float(self, value):
        if self._prop_float == value:
            return
        self.client.set_remote_property('tb.simple.SimpleArrayInterface/propFloat', [api.from_float(_) for _ in value])

    def get_prop_float(self):
        return self._prop_float

    def _set_prop_float32(self, value):
        if self._prop_float32 == value:
            return
        path = Name.path_from_name("propFloat32")
        self._prop_float32 = [api.as_float32(_) for _ in value]
        self.on_property_changed.fire(path, self._prop_float32)

    def set_prop_float32(self, value):
        if self._prop_float32 == value:
            return
        self.client.set_remote_property('tb.simple.SimpleArrayInterface/propFloat32', [api.from_float32(_) for _ in value])

    def get_prop_float32(self):
        return self._prop_float32

    def _set_prop_float64(self, value):
        if self._prop_float64 == value:
            return
        path = Name.path_from_name("propFloat64")
        self._prop_float64 = [api.as_float64(_) for _ in value]
        self.on_property_changed.fire(path, self._prop_float64)

    def set_prop_float64(self, value):
        if self._prop_float64 == value:
            return
        self.client.set_remote_property('tb.simple.SimpleArrayInterface/propFloat64', [api.from_float64(_) for _ in value])

    def get_prop_float64(self):
        return self._prop_float64

    def _set_prop_string(self, value):
        if self._prop_string == value:
            return
        path = Name.path_from_name("propString")
        self._prop_string = [api.as_string(_) for _ in value]
        self.on_property_changed.fire(path, self._prop_string)

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
            self._prop_bool = [api.as_bool(_) for _ in value]
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop_bool)
        elif path == "propInt":
            self._prop_int = [api.as_int(_) for _ in value]
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop_int)
        elif path == "propInt32":
            self._prop_int32 = [api.as_int32(_) for _ in value]
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop_int32)
        elif path == "propInt64":
            self._prop_int64 = [api.as_int64(_) for _ in value]
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop_int64)
        elif path == "propFloat":
            self._prop_float = [api.as_float(_) for _ in value]
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop_float)
        elif path == "propFloat32":
            self._prop_float32 = [api.as_float32(_) for _ in value]
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop_float32)
        elif path == "propFloat64":
            self._prop_float64 = [api.as_float64(_) for _ in value]
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop_float64)
        elif path == "propString":
            self._prop_string = [api.as_string(_) for _ in value]
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop_string)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sigBool":
            _param_bool = [api.as_bool(_) for _ in args[0]]
            self.on_sig_bool.fire(_param_bool)
        elif path == "sigInt":
            _param_int = [api.as_int(_) for _ in args[0]]
            self.on_sig_int.fire(_param_int)
        elif path == "sigInt32":
            _param_int32 = [api.as_int32(_) for _ in args[0]]
            self.on_sig_int32.fire(_param_int32)
        elif path == "sigInt64":
            _param_int64 = [api.as_int64(_) for _ in args[0]]
            self.on_sig_int64.fire(_param_int64)
        elif path == "sigFloat":
            _param_float = [api.as_float(_) for _ in args[0]]
            self.on_sig_float.fire(_param_float)
        elif path == "sigFloat32":
            _param_float32 = [api.as_float32(_) for _ in args[0]]
            self.on_sig_float32.fire(_param_float32)
        elif path == "sigFloat64":
            _param_float64 = [api.as_float64(_) for _ in args[0]]
            self.on_sig_float64.fire(_param_float64)
        elif path == "sigString":
            _param_string = [api.as_string(_) for _ in args[0]]
            self.on_sig_string.fire(_param_string)

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
        self.client.invoke_remote('tb.simple.NoPropertiesInterface/NoPropertiesInterface', args, func)
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
        pass

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sigVoid":
            self.on_sig_void.fire()
        elif path == "sigBool":
            _param_bool =  args[0]
            self.on_sig_bool.fire(_param_bool)

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
        self.client.invoke_remote('tb.simple.NoOperationsInterface/NoOperationsInterface', args, func)
        return await asyncio.wait_for(future, 500)

    def _set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        path = Name.path_from_name("propBool")
        self._prop_bool = value
        self.on_property_changed.fire(path, self._prop_bool)

    def set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        self.client.set_remote_property('tb.simple.NoOperationsInterface/propBool', value)

    def get_prop_bool(self):
        return self._prop_bool

    def _set_prop_int(self, value):
        if self._prop_int == value:
            return
        path = Name.path_from_name("propInt")
        self._prop_int = value
        self.on_property_changed.fire(path, self._prop_int)

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
            self._prop_bool =  value
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop_bool)
        elif path == "propInt":
            self._prop_int =  value
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop_int)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sigVoid":
            self.on_sig_void.fire()
        elif path == "sigBool":
            _param_bool =  args[0]
            self.on_sig_bool.fire(_param_bool)

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
        self.client.invoke_remote('tb.simple.NoSignalsInterface/NoSignalsInterface', args, func)
        return await asyncio.wait_for(future, 500)

    def _set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        path = Name.path_from_name("propBool")
        self._prop_bool = value
        self.on_property_changed.fire(path, self._prop_bool)

    def set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        self.client.set_remote_property('tb.simple.NoSignalsInterface/propBool', value)

    def get_prop_bool(self):
        return self._prop_bool

    def _set_prop_int(self, value):
        if self._prop_int == value:
            return
        path = Name.path_from_name("propInt")
        self._prop_int = value
        self.on_property_changed.fire(path, self._prop_int)

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
            self._prop_bool =  value
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop_bool)
        elif path == "propInt":
            self._prop_int =  value
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop_int)

    def olink_on_signal(self, name: str, args: list[Any]):
        pass

class EmptyInterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote('tb.simple.EmptyInterface/EmptyInterface', args, func)
        return await asyncio.wait_for(future, 500)

    def olink_object_name(self):
        return 'tb.simple.EmptyInterface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        pass

    def olink_on_signal(self, name: str, args: list[Any]):
        pass
