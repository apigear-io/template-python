from olink.core import Name
from olink.remote import IObjectSource, RemoteNode
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
        if path == "prop0":
            v = api.as_enum0(value)
            return self.impl.set_prop0(v)
        elif path == "prop1":
            v = api.as_enum1(value)
            return self.impl.set_prop1(v)
        elif path == "prop2":
            v = api.as_enum2(value)
            return self.impl.set_prop2(v)
        elif path == "prop3":
            v = api.as_enum3(value)
            return self.impl.set_prop3(v)
        logging.info("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        if path == "func0":
            param0 = api.as_enum0(args[0])
            reply = self.impl.func0(param0)
            return api.from_enum0(reply)
        elif path == "func1":
            param1 = api.as_enum1(args[0])
            reply = self.impl.func1(param1)
            return api.from_enum1(reply)
        elif path == "func2":
            param2 = api.as_enum2(args[0])
            reply = self.impl.func2(param2)
            return api.from_enum2(reply)
        elif path == "func3":
            param3 = api.as_enum3(args[0])
            reply = self.impl.func3(param3)
            return api.from_enum3(reply)      
        logging.info("unknown operation: %s", name)

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
        if path == "sig0":
            param0 = api.from_enum0(args[0])
            return RemoteNode.notify_signal(symbol, [param0])
        elif path == "sig1":
            param1 = api.from_enum1(args[0])
            return RemoteNode.notify_signal(symbol, [param1])
        elif path == "sig2":
            param2 = api.from_enum2(args[0])
            return RemoteNode.notify_signal(symbol, [param2])
        elif path == "sig3":
            param3 = api.from_enum3(args[0])
            return RemoteNode.notify_signal(symbol, [param3])
        logging.info("unknown signal %s", symbol)

    def notify_property(self, symbol, value):
        path = Name.path_from_name(symbol)
        if path == "prop0":
            v = api.from_enum0(value)
            return RemoteNode.notify_property_change(symbol, value)
        elif path == "prop1":
            v = api.from_enum1(value)
            return RemoteNode.notify_property_change(symbol, value)
        elif path == "prop2":
            v = api.from_enum2(value)
            return RemoteNode.notify_property_change(symbol, value)
        elif path == "prop3":
            v = api.from_enum3(value)
            return RemoteNode.notify_property_change(symbol, value)
        logging.info("unknown property %s", symbol)