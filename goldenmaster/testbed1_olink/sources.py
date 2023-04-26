from olink.core.types import Name
from olink.remotenode import IObjectSource, RemoteNode
from testbed1_api import api
from typing import Any
import logging

class StructInterfaceSource(IObjectSource):
    impl: api.IStructInterface
    def __init__(self, impl: api.IStructInterface):
        self.impl = impl
        impl._notifier = self
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "testbed1.StructInterface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        match path:
            case "propBool":
                v = api.as_struct_bool(value)
                self.impl.set_prop_bool(v)
            case "propInt":
                v = api.as_struct_int(value)
                self.impl.set_prop_int(v)
            case "propFloat":
                v = api.as_struct_float(value)
                self.impl.set_prop_float(v)
            case "propString":
                v = api.as_struct_string(value)
                self.impl.set_prop_string(v)

    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        match path:
            case "funcBool":
                param_bool = api.as_struct_bool(args[0])
                reply = self.impl.func_bool(param_bool)
                return api.from_struct_bool(reply)
            case "funcInt":
                param_int = api.as_struct_int(args[0])
                reply = self.impl.func_int(param_int)
                return api.from_struct_bool(reply)
            case "funcFloat":
                param_float = api.as_struct_float(args[0])
                reply = self.impl.func_float(param_float)
                return api.from_struct_float(reply)
            case "funcString":
                param_string = api.as_struct_string(args[0])
                reply = self.impl.func_string(param_string)
                return api.from_struct_string(reply)      
            case _:
                logging.info("unknown operation")
                return None

    def olink_linked(self, name: str, node: "RemoteNode"):
        print('linked')

    def olink_collect_properties(self) -> object:
        props = {}
        v = self.impl.get_prop_bool()
        props["propBool"] = api.from_struct_bool(v)
        v = self.impl.get_prop_int()
        props["propInt"] = api.from_struct_int(v)
        v = self.impl.get_prop_float()
        props["propFloat"] = api.from_struct_float(v)
        v = self.impl.get_prop_string()
        props["propString"] = api.from_struct_string(v)
        return props

    def notify_signal(self, symbol, args):
        path = Name.path_from_name(symbol)
        match path:
            case "sigBool":
                param_bool = api.from_struct_bool(args[0])
                RemoteNode.notify_signal(symbol, [param_bool])
            case "sigInt":
                param_int = api.from_struct_int(args[0])
                RemoteNode.notify_signal(symbol, [param_int])
            case "sigFloat":
                param_float = api.from_struct_float(args[0])
                RemoteNode.notify_signal(symbol, [param_float])
            case "sigString":
                param_string = api.from_struct_string(args[0])
                RemoteNode.notify_signal(symbol, [param_string])
            case _:
                logging.info("unknown signal %s", symbol)

    def notify_property(self, symbol, value):
        path = Name.path_from_name(symbol)
        match path:
            case "propBool":
                v = api.from_struct_bool(value)
            case "propInt":
                v = api.from_struct_int(value)
            case "propFloat":
                v = api.from_struct_float(value)
            case "propString":
                v = api.from_struct_string(value)
                RemoteNode.notify_property_change(symbol, value)
            case _:
                logging.info("unknown property %s", symbol)

class StructArrayInterfaceSource(IObjectSource):
    impl: api.IStructArrayInterface
    def __init__(self, impl: api.IStructArrayInterface):
        self.impl = impl
        impl._notifier = self
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "testbed1.StructArrayInterface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        match path:
            case "propBool":
                v = api.as_struct_bool(value)
                self.impl.set_prop_bool(v)
            case "propInt":
                v = api.as_struct_int(value)
                self.impl.set_prop_int(v)
            case "propFloat":
                v = api.as_struct_float(value)
                self.impl.set_prop_float(v)
            case "propString":
                v = api.as_struct_string(value)
                self.impl.set_prop_string(v)

    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        match path:
            case "funcBool":
                param_bool = api.as_struct_bool(args[0])
                reply = self.impl.func_bool(param_bool)
                return api.from_struct_bool(reply)
            case "funcInt":
                param_int = api.as_struct_int(args[0])
                reply = self.impl.func_int(param_int)
                return api.from_struct_bool(reply)
            case "funcFloat":
                param_float = api.as_struct_float(args[0])
                reply = self.impl.func_float(param_float)
                return api.from_struct_bool(reply)
            case "funcString":
                param_string = api.as_struct_string(args[0])
                reply = self.impl.func_string(param_string)
                return api.from_struct_bool(reply)      
            case _:
                logging.info("unknown operation")
                return None

    def olink_linked(self, name: str, node: "RemoteNode"):
        print('linked')

    def olink_collect_properties(self) -> object:
        props = {}
        v = self.impl.get_prop_bool()
        props["propBool"] = api.from_struct_bool(v)
        v = self.impl.get_prop_int()
        props["propInt"] = api.from_struct_int(v)
        v = self.impl.get_prop_float()
        props["propFloat"] = api.from_struct_float(v)
        v = self.impl.get_prop_string()
        props["propString"] = api.from_struct_string(v)
        return props

    def notify_signal(self, symbol, args):
        path = Name.path_from_name(symbol)
        match path:
            case "sigBool":
                param_bool = api.from_struct_bool(args[0])
                RemoteNode.notify_signal(symbol, [param_bool])
            case "sigInt":
                param_int = api.from_struct_int(args[0])
                RemoteNode.notify_signal(symbol, [param_int])
            case "sigFloat":
                param_float = api.from_struct_float(args[0])
                RemoteNode.notify_signal(symbol, [param_float])
            case "sigString":
                param_string = api.from_struct_string(args[0])
                RemoteNode.notify_signal(symbol, [param_string])
            case _:
                logging.info("unknown signal %s", symbol)

    def notify_property(self, symbol, value):
        path = Name.path_from_name(symbol)
        match path:
            case "propBool":
                v = api.from_struct_bool(value)
            case "propInt":
                v = api.from_struct_int(value)
            case "propFloat":
                v = api.from_struct_float(value)
            case "propString":
                v = api.from_struct_string(value)
                RemoteNode.notify_property_change(symbol, value)
            case _:
                logging.info("unknown property %s", symbol)