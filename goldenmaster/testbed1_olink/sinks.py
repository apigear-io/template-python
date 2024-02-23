import asyncio
from typing import Any
from olink.core import Name
from olink.client import IObjectSink, ClientNode
from testbed1_api.shared import EventHook
from testbed1_api import api

class StructInterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._prop_bool = api.StructBool()
        self.on_prop_bool_changed = EventHook()
        self._prop_int = api.StructInt()
        self.on_prop_int_changed = EventHook()
        self._prop_float = api.StructFloat()
        self.on_prop_float_changed = EventHook()
        self._prop_string = api.StructString()
        self.on_prop_string_changed = EventHook()
        self.on_sig_bool = EventHook()
        self.on_sig_int = EventHook()
        self.on_sig_float = EventHook()
        self.on_sig_string = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote('testbed1.StructInterface/StructInterface', args, func)
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
        self.client.set_remote_property('testbed1.StructInterface/propBool', value)

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
        self.client.set_remote_property('testbed1.StructInterface/propInt', value)

    def get_prop_int(self):
        return self._prop_int

    def _set_prop_float(self, value):
        if self._prop_float == value:
            return
        path = Name.path_from_name("propFloat")
        self._prop_float = value
        self.on_property_changed.fire(path, self._prop_float)

    def set_prop_float(self, value):
        if self._prop_float == value:
            return
        self.client.set_remote_property('testbed1.StructInterface/propFloat', value)

    def get_prop_float(self):
        return self._prop_float

    def _set_prop_string(self, value):
        if self._prop_string == value:
            return
        path = Name.path_from_name("propString")
        self._prop_string = value
        self.on_property_changed.fire(path, self._prop_string)

    def set_prop_string(self, value):
        if self._prop_string == value:
            return
        self.client.set_remote_property('testbed1.StructInterface/propString', value)

    def get_prop_string(self):
        return self._prop_string

    async def func_bool(self, param_bool: api.StructBool):
        return await self._invoke("funcBool", [param_bool])

    async def func_int(self, param_int: api.StructInt):
        return await self._invoke("funcInt", [param_int])

    async def func_float(self, param_float: api.StructFloat):
        return await self._invoke("funcFloat", [param_float])

    async def func_string(self, param_string: api.StructString):
        return await self._invoke("funcString", [param_string])

    def olink_object_name(self):
        return 'testbed1.StructInterface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "propBool":
                self._set_prop_bool(props[k])
            elif k == "propInt":
                self._set_prop_int(props[k])
            elif k == "propFloat":
                self._set_prop_float(props[k])
            elif k == "propString":
                self._set_prop_string(props[k])

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
        elif path == "propFloat":
            self._prop_float =  value
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop_float)
        elif path == "propString":
            self._prop_string =  value
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop_string)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        hook = getattr(self, f'on_{path}')
        hook.fire(*args)

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
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote('testbed1.StructArrayInterface/StructArrayInterface', args, func)
        return await asyncio.wait_for(future, 500)

    def _set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        path = Name.path_from_name("propBool")
        self._prop_bool = [api.as_struct_bool(_) for _ in value]
        self.on_property_changed.fire(path, self._prop_bool)

    def set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        self.client.set_remote_property('testbed1.StructArrayInterface/propBool', [api.from_struct_bool(_) for _ in value])

    def get_prop_bool(self):
        return self._prop_bool

    def _set_prop_int(self, value):
        if self._prop_int == value:
            return
        path = Name.path_from_name("propInt")
        self._prop_int = [api.as_struct_int(_) for _ in value]
        self.on_property_changed.fire(path, self._prop_int)

    def set_prop_int(self, value):
        if self._prop_int == value:
            return
        self.client.set_remote_property('testbed1.StructArrayInterface/propInt', [api.from_struct_int(_) for _ in value])

    def get_prop_int(self):
        return self._prop_int

    def _set_prop_float(self, value):
        if self._prop_float == value:
            return
        path = Name.path_from_name("propFloat")
        self._prop_float = [api.as_struct_float(_) for _ in value]
        self.on_property_changed.fire(path, self._prop_float)

    def set_prop_float(self, value):
        if self._prop_float == value:
            return
        self.client.set_remote_property('testbed1.StructArrayInterface/propFloat', [api.from_struct_float(_) for _ in value])

    def get_prop_float(self):
        return self._prop_float

    def _set_prop_string(self, value):
        if self._prop_string == value:
            return
        path = Name.path_from_name("propString")
        self._prop_string = [api.as_struct_string(_) for _ in value]
        self.on_property_changed.fire(path, self._prop_string)

    def set_prop_string(self, value):
        if self._prop_string == value:
            return
        self.client.set_remote_property('testbed1.StructArrayInterface/propString', [api.from_struct_string(_) for _ in value])

    def get_prop_string(self):
        return self._prop_string

    async def func_bool(self, param_bool: list[api.StructBool]):
        return await self._invoke("funcBool", [param_bool])

    async def func_int(self, param_int: list[api.StructInt]):
        return await self._invoke("funcInt", [param_int])

    async def func_float(self, param_float: list[api.StructFloat]):
        return await self._invoke("funcFloat", [param_float])

    async def func_string(self, param_string: list[api.StructString]):
        return await self._invoke("funcString", [param_string])

    def olink_object_name(self):
        return 'testbed1.StructArrayInterface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "propBool":
                self._set_prop_bool(props[k])
            elif k == "propInt":
                self._set_prop_int(props[k])
            elif k == "propFloat":
                self._set_prop_float(props[k])
            elif k == "propString":
                self._set_prop_string(props[k])

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "propBool":
            self._prop_bool = [api.as_struct_bool(_) for _ in value]
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop_bool)
        elif path == "propInt":
            self._prop_int = [api.as_struct_int(_) for _ in value]
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop_int)
        elif path == "propFloat":
            self._prop_float = [api.as_struct_float(_) for _ in value]
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop_float)
        elif path == "propString":
            self._prop_string = [api.as_struct_string(_) for _ in value]
            hook = getattr(self, f'on_{path}_changed')
            hook.fire(self._prop_string)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        hook = getattr(self, f'on_{path}')
        hook.fire(*args)