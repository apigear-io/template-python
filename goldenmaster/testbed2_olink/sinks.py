import asyncio
from typing import Any
from olink.core import Name
from olink.client import IObjectSink, ClientNode
from testbed2_api.shared import EventHook
from testbed2_api import api
import logging

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

    async def _invoke(self, name, args, no_wait=False):
        if no_wait:
            self.client.invoke_remote(f"testbed2.ManyParamInterface/{name}", args, func=None)
        else:
            future = asyncio.get_running_loop().create_future()
            def func(args):
                return future.set_result(args.value)
            self.client.invoke_remote(f"testbed2.ManyParamInterface/{name}", args, func)
            return await asyncio.wait_for(future, 500)

    def _set_prop1(self, value):
        if self._prop1 == value:
            return
        self._prop1 = value
        self.on_prop1_changed.fire(self._prop1)

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        self.client.set_remote_property('testbed2.ManyParamInterface/prop1', value)

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
        self.client.set_remote_property('testbed2.ManyParamInterface/prop2', value)

    def get_prop2(self):
        return self._prop2

    def _set_prop3(self, value):
        if self._prop3 == value:
            return
        self._prop3 = value
        self.on_prop3_changed.fire(self._prop3)

    def set_prop3(self, value):
        if self._prop3 == value:
            return
        self.client.set_remote_property('testbed2.ManyParamInterface/prop3', value)

    def get_prop3(self):
        return self._prop3

    def _set_prop4(self, value):
        if self._prop4 == value:
            return
        self._prop4 = value
        self.on_prop4_changed.fire(self._prop4)

    def set_prop4(self, value):
        if self._prop4 == value:
            return
        self.client.set_remote_property('testbed2.ManyParamInterface/prop4', value)

    def get_prop4(self):
        return self._prop4

    async def func1(self, param1: int):
        _param1 = api.from_int(param1)
        return await self._invoke("func1", [_param1])

    async def func2(self, param1: int, param2: int):
        _param1 = api.from_int(param1)
        _param2 = api.from_int(param2)
        return await self._invoke("func2", [_param1, _param2])

    async def func3(self, param1: int, param2: int, param3: int):
        _param1 = api.from_int(param1)
        _param2 = api.from_int(param2)
        _param3 = api.from_int(param3)
        return await self._invoke("func3", [_param1, _param2, _param3])

    async def func4(self, param1: int, param2: int, param3: int, param4: int):
        _param1 = api.from_int(param1)
        _param2 = api.from_int(param2)
        _param3 = api.from_int(param3)
        _param4 = api.from_int(param4)
        return await self._invoke("func4", [_param1, _param2, _param3, _param4])

    def olink_object_name(self):
        return 'testbed2.ManyParamInterface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "prop1":
                v =  api.as_int(props[k])
                self._set_prop1(v)
            elif k == "prop2":
                v =  api.as_int(props[k])
                self._set_prop2(v)
            elif k == "prop3":
                v =  api.as_int(props[k])
                self._set_prop3(v)
            elif k == "prop4":
                v =  api.as_int(props[k])
                self._set_prop4(v)

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "prop1":
            v =  api.as_int(value)
            self._set_prop1(v)
            return
        elif path == "prop2":
            v =  api.as_int(value)
            self._set_prop2(v)
            return
        elif path == "prop3":
            v =  api.as_int(value)
            self._set_prop3(v)
            return
        elif path == "prop4":
            v =  api.as_int(value)
            self._set_prop4(v)
            return
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sig1":
            param1 =  api.as_int(args[0])
            self.on_sig1.fire(param1)
            return
        elif path == "sig2":
            param1 =  api.as_int(args[0])
            param2 =  api.as_int(args[1])
            self.on_sig2.fire(param1, param2)
            return
        elif path == "sig3":
            param1 =  api.as_int(args[0])
            param2 =  api.as_int(args[1])
            param3 =  api.as_int(args[2])
            self.on_sig3.fire(param1, param2, param3)
            return
        elif path == "sig4":
            param1 =  api.as_int(args[0])
            param2 =  api.as_int(args[1])
            param3 =  api.as_int(args[2])
            param4 =  api.as_int(args[3])
            self.on_sig4.fire(param1, param2, param3, param4)
            return
        logging.error("unknown signal: %s", name)

class NestedStruct1InterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._prop1 = api.NestedStruct1()
        self.on_prop1_changed = EventHook()
        self.on_sig1 = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args, no_wait=False):
        if no_wait:
            self.client.invoke_remote(f"testbed2.NestedStruct1Interface/{name}", args, func=None)
        else:
            future = asyncio.get_running_loop().create_future()
            def func(args):
                return future.set_result(args.value)
            self.client.invoke_remote(f"testbed2.NestedStruct1Interface/{name}", args, func)
            return await asyncio.wait_for(future, 500)

    def _set_prop1(self, value):
        if self._prop1 == value:
            return
        self._prop1 = value
        self.on_prop1_changed.fire(self._prop1)

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        self.client.set_remote_property('testbed2.NestedStruct1Interface/prop1', value)

    def get_prop1(self):
        return self._prop1

    async def func1(self, param1: api.NestedStruct1):
        _param1 = api.from_nested_struct1(param1)
        return await self._invoke("func1", [_param1])

    def olink_object_name(self):
        return 'testbed2.NestedStruct1Interface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "prop1":
                v =  api.as_nested_struct1(props[k])
                self._set_prop1(v)

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "prop1":
            v =  api.as_nested_struct1(value)
            self._set_prop1(v)
            return
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sig1":
            param1 =  api.as_nested_struct1(args[0])
            self.on_sig1.fire(param1)
            return
        logging.error("unknown signal: %s", name)

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

    async def _invoke(self, name, args, no_wait=False):
        if no_wait:
            self.client.invoke_remote(f"testbed2.NestedStruct2Interface/{name}", args, func=None)
        else:
            future = asyncio.get_running_loop().create_future()
            def func(args):
                return future.set_result(args.value)
            self.client.invoke_remote(f"testbed2.NestedStruct2Interface/{name}", args, func)
            return await asyncio.wait_for(future, 500)

    def _set_prop1(self, value):
        if self._prop1 == value:
            return
        self._prop1 = value
        self.on_prop1_changed.fire(self._prop1)

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        self.client.set_remote_property('testbed2.NestedStruct2Interface/prop1', value)

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
        self.client.set_remote_property('testbed2.NestedStruct2Interface/prop2', value)

    def get_prop2(self):
        return self._prop2

    async def func1(self, param1: api.NestedStruct1):
        _param1 = api.from_nested_struct1(param1)
        return await self._invoke("func1", [_param1])

    async def func2(self, param1: api.NestedStruct1, param2: api.NestedStruct2):
        _param1 = api.from_nested_struct1(param1)
        _param2 = api.from_nested_struct2(param2)
        return await self._invoke("func2", [_param1, _param2])

    def olink_object_name(self):
        return 'testbed2.NestedStruct2Interface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "prop1":
                v =  api.as_nested_struct1(props[k])
                self._set_prop1(v)
            elif k == "prop2":
                v =  api.as_nested_struct2(props[k])
                self._set_prop2(v)

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "prop1":
            v =  api.as_nested_struct1(value)
            self._set_prop1(v)
            return
        elif path == "prop2":
            v =  api.as_nested_struct2(value)
            self._set_prop2(v)
            return
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sig1":
            param1 =  api.as_nested_struct1(args[0])
            self.on_sig1.fire(param1)
            return
        elif path == "sig2":
            param1 =  api.as_nested_struct1(args[0])
            param2 =  api.as_nested_struct2(args[1])
            self.on_sig2.fire(param1, param2)
            return
        logging.error("unknown signal: %s", name)

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

    async def _invoke(self, name, args, no_wait=False):
        if no_wait:
            self.client.invoke_remote(f"testbed2.NestedStruct3Interface/{name}", args, func=None)
        else:
            future = asyncio.get_running_loop().create_future()
            def func(args):
                return future.set_result(args.value)
            self.client.invoke_remote(f"testbed2.NestedStruct3Interface/{name}", args, func)
            return await asyncio.wait_for(future, 500)

    def _set_prop1(self, value):
        if self._prop1 == value:
            return
        self._prop1 = value
        self.on_prop1_changed.fire(self._prop1)

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        self.client.set_remote_property('testbed2.NestedStruct3Interface/prop1', value)

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
        self.client.set_remote_property('testbed2.NestedStruct3Interface/prop2', value)

    def get_prop2(self):
        return self._prop2

    def _set_prop3(self, value):
        if self._prop3 == value:
            return
        self._prop3 = value
        self.on_prop3_changed.fire(self._prop3)

    def set_prop3(self, value):
        if self._prop3 == value:
            return
        self.client.set_remote_property('testbed2.NestedStruct3Interface/prop3', value)

    def get_prop3(self):
        return self._prop3

    async def func1(self, param1: api.NestedStruct1):
        _param1 = api.from_nested_struct1(param1)
        return await self._invoke("func1", [_param1])

    async def func2(self, param1: api.NestedStruct1, param2: api.NestedStruct2):
        _param1 = api.from_nested_struct1(param1)
        _param2 = api.from_nested_struct2(param2)
        return await self._invoke("func2", [_param1, _param2])

    async def func3(self, param1: api.NestedStruct1, param2: api.NestedStruct2, param3: api.NestedStruct3):
        _param1 = api.from_nested_struct1(param1)
        _param2 = api.from_nested_struct2(param2)
        _param3 = api.from_nested_struct3(param3)
        return await self._invoke("func3", [_param1, _param2, _param3])

    def olink_object_name(self):
        return 'testbed2.NestedStruct3Interface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "prop1":
                v =  api.as_nested_struct1(props[k])
                self._set_prop1(v)
            elif k == "prop2":
                v =  api.as_nested_struct2(props[k])
                self._set_prop2(v)
            elif k == "prop3":
                v =  api.as_nested_struct3(props[k])
                self._set_prop3(v)

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "prop1":
            v =  api.as_nested_struct1(value)
            self._set_prop1(v)
            return
        elif path == "prop2":
            v =  api.as_nested_struct2(value)
            self._set_prop2(v)
            return
        elif path == "prop3":
            v =  api.as_nested_struct3(value)
            self._set_prop3(v)
            return
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "sig1":
            param1 =  api.as_nested_struct1(args[0])
            self.on_sig1.fire(param1)
            return
        elif path == "sig2":
            param1 =  api.as_nested_struct1(args[0])
            param2 =  api.as_nested_struct2(args[1])
            self.on_sig2.fire(param1, param2)
            return
        elif path == "sig3":
            param1 =  api.as_nested_struct1(args[0])
            param2 =  api.as_nested_struct2(args[1])
            param3 =  api.as_nested_struct3(args[2])
            self.on_sig3.fire(param1, param2, param3)
            return
        logging.error("unknown signal: %s", name)
