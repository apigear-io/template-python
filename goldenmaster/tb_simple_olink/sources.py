from olink.core.types import Name
from olink.remotenode import IObjectSource, RemoteNode
from tb_simple_api import api
from typing import Any
import logging

class SimpleInterfaceSource(IObjectSource):
    impl: api.ISimpleInterface
    def __init__(self, impl: api.ISimpleInterface):
        self.impl = impl
        impl._notifier = self
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "tb.simple.SimpleInterface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        match path:
            case "propBool":
                v = api.as_bool(value)
                self.impl.set_prop_bool(v)
            case "propInt":
                v = api.as_int(value)
                self.impl.set_prop_int(v)
            case "propFloat":
                v = api.as_float(value)
                self.impl.set_prop_float(v)
            case "propString":
                v = api.as_string(value)
                self.impl.set_prop_string(v)

    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        match path:
            case "funcBool":
                param_bool = api.as_bool(args[0])
                reply = self.impl.func_bool(param_bool)
                return api.from_bool(reply)
            case "funcInt":
                param_int = api.as_int(args[0])
                reply = self.impl.func_int(param_int)
                return api.from_int(reply)
            case "funcFloat":
                param_float = api.as_float(args[0])
                reply = self.impl.func_float(param_float)
                return api.from_float(reply)
            case "funcString":
                param_string = api.as_string(args[0])
                reply = self.impl.func_string(param_string)
                return api.from_string(reply)      
            case _:
                logging.info("unknown operation")
                return None

    def olink_linked(self, name: str, node: "RemoteNode"):
        print('linked')

    def olink_collect_properties(self) -> object:
        props = {}
        v = self.impl.get_prop_bool()
        props["propBool"] = api.from_bool(v)
        v = self.impl.get_prop_int()
        props["propInt"] = api.from_int(v)
        v = self.impl.get_prop_float()
        props["propFloat"] = api.from_float(v)
        v = self.impl.get_prop_string()
        props["propString"] = api.from_string(v)
        return props

    def notify_signal(self, symbol, args):
        path = Name.path_from_name(symbol)
        match path:
            case "sigBool":
                param_bool = api.from_bool(args[0])
                RemoteNode.notify_signal(symbol, [param_bool])
            case "sigInt":
                param_int = api.from_int(args[0])
                RemoteNode.notify_signal(symbol, [param_int])
            case "sigFloat":
                param_float = api.from_float(args[0])
                RemoteNode.notify_signal(symbol, [param_float])
            case "sigString":
                param_string = api.from_string(args[0])
                RemoteNode.notify_signal(symbol, [param_string])
            case _:
                logging.info("unknown signal %s", symbol)

    def notify_property(self, symbol, value):
        path = Name.path_from_name(symbol)
        match path:
            case "propBool":
                v = api.from_bool(value)
            case "propInt":
                v = api.from_int(value)
            case "propFloat":
                v = api.from_float(value)
            case "propString":
                v = api.from_string(value)
                RemoteNode.notify_property_change(symbol, value)
            case _:
                logging.info("unknown property %s", symbol)

class SimpleArrayInterfaceSource(IObjectSource):
    impl: api.ISimpleArrayInterface
    def __init__(self, impl: api.ISimpleArrayInterface):
        self.impl = impl
        impl._notifier = self
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "tb.simple.SimpleArrayInterface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        match path:
            case "propBool":
                v = api.as_bool(value)
                self.impl.set_prop_bool(v)
            case "propInt":
                v = api.as_int(value)
                self.impl.set_prop_int(v)
            case "propFloat":
                v = api.as_float(value)
                self.impl.set_prop_float(v)
            case "propString":
                v = api.as_string(value)
                self.impl.set_prop_string(v)

    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        match path:
            case "funcBool":
                param_bool = api.as_bool(args[0])
                reply = self.impl.func_bool(param_bool)
                return api.from_bool(reply)
            case "funcInt":
                param_int = api.as_int(args[0])
                reply = self.impl.func_int(param_int)
                return api.from_int(reply)
            case "funcFloat":
                param_float = api.as_float(args[0])
                reply = self.impl.func_float(param_float)
                return api.from_float(reply)
            case "funcString":
                param_string = api.as_string(args[0])
                reply = self.impl.func_string(param_string)
                return api.from_string(reply)      
            case _:
                logging.info("unknown operation")
                return None

    def olink_linked(self, name: str, node: "RemoteNode"):
        print('linked')

    def olink_collect_properties(self) -> object:
        props = {}
        v = self.impl.get_prop_bool()
        props["propBool"] = api.from_bool(v)
        v = self.impl.get_prop_int()
        props["propInt"] = api.from_int(v)
        v = self.impl.get_prop_float()
        props["propFloat"] = api.from_float(v)
        v = self.impl.get_prop_string()
        props["propString"] = api.from_string(v)
        return props

    def notify_signal(self, symbol, args):
        path = Name.path_from_name(symbol)
        match path:
            case "sigBool":
                param_bool = api.from_bool(args[0])
                RemoteNode.notify_signal(symbol, [param_bool])
            case "sigInt":
                param_int = api.from_int(args[0])
                RemoteNode.notify_signal(symbol, [param_int])
            case "sigFloat":
                param_float = api.from_float(args[0])
                RemoteNode.notify_signal(symbol, [param_float])
            case "sigString":
                param_string = api.from_string(args[0])
                RemoteNode.notify_signal(symbol, [param_string])
            case _:
                logging.info("unknown signal %s", symbol)

    def notify_property(self, symbol, value):
        path = Name.path_from_name(symbol)
        match path:
            case "propBool":
                v = api.from_bool(value)
            case "propInt":
                v = api.from_int(value)
            case "propFloat":
                v = api.from_float(value)
            case "propString":
                v = api.from_string(value)
                RemoteNode.notify_property_change(symbol, value)
            case _:
                logging.info("unknown property %s", symbol)