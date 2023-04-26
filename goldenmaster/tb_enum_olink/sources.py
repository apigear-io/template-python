from olink.core.types import Name
from olink.remotenode import IObjectSource, RemoteNode
from tb_enum_api import api
from typing import Any
import logging

class EnumInterfaceSource(IObjectSource):
    impl: api.IEnumInterface
    def __init__(self, impl: api.IEnumInterface):
        self.impl = impl
        impl._notifier = self
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "tb.enum.EnumInterface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        match path:
            case "prop0":
                v = api.as_enum0(value)
                self.impl.set_prop0(v)
            case "prop1":
                v = api.as_enum1(value)
                self.impl.set_prop1(v)
            case "prop2":
                v = api.as_enum2(value)
                self.impl.set_prop2(v)
            case "prop3":
                v = api.as_enum3(value)
                self.impl.set_prop3(v)

    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        match path:
            case "func0":
                param0 = api.as_enum0(args[0])
                reply = self.impl.func0(param0)
                return api.from_enum0(reply)
            case "func1":
                param1 = api.as_enum1(args[0])
                reply = self.impl.func1(param1)
                return api.from_enum1(reply)
            case "func2":
                param2 = api.as_enum2(args[0])
                reply = self.impl.func2(param2)
                return api.from_enum2(reply)
            case "func3":
                param3 = api.as_enum3(args[0])
                reply = self.impl.func3(param3)
                return api.from_enum3(reply)      
            case _:
                logging.info("unknown operation")
                return None

    def olink_linked(self, name: str, node: "RemoteNode"):
        print('linked')

    def olink_collect_properties(self) -> object:
        props = {}
        v = self.impl.get_prop0()
        props["prop0"] = api.from_enum0(v)
        v = self.impl.get_prop1()
        props["prop1"] = api.from_enum1(v)
        v = self.impl.get_prop2()
        props["prop2"] = api.from_enum2(v)
        v = self.impl.get_prop3()
        props["prop3"] = api.from_enum3(v)
        return props

    def notify_signal(self, symbol, args):
        path = Name.path_from_name(symbol)
        match path:
            case "sig0":
                param0 = api.from_enum0(args[0])
                RemoteNode.notify_signal(symbol, [param0])
            case "sig1":
                param1 = api.from_enum1(args[0])
                RemoteNode.notify_signal(symbol, [param1])
            case "sig2":
                param2 = api.from_enum2(args[0])
                RemoteNode.notify_signal(symbol, [param2])
            case "sig3":
                param3 = api.from_enum3(args[0])
                RemoteNode.notify_signal(symbol, [param3])
            case _:
                logging.info("unknown signal %s", symbol)

    def notify_property(self, symbol, value):
        path = Name.path_from_name(symbol)
        match path:
            case "prop0":
                v = api.from_enum0(value)
            case "prop1":
                v = api.from_enum1(value)
            case "prop2":
                v = api.from_enum2(value)
            case "prop3":
                v = api.from_enum3(value)
                RemoteNode.notify_property_change(symbol, value)
            case _:
                logging.info("unknown property %s", symbol)