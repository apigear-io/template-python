from olink.core import Name
from olink.remote import IObjectSource, RemoteNode
from testbed2_api import api
from typing import Any
import logging
class ManyParamInterfaceSource(IObjectSource):
    impl: api.IManyParamInterface
    def __init__(self, impl: api.IManyParamInterface):
        self.impl = impl
        impl._notifier = self
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "testbed2.ManyParamInterface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        if path == "prop1":
            v = api.as_int(value)
            return self.impl.set_prop1(v)
        elif path == "prop2":
            v = api.as_int(value)
            return self.impl.set_prop2(v)
        elif path == "prop3":
            v = api.as_int(value)
            return self.impl.set_prop3(v)
        elif path == "prop4":
            v = api.as_int(value)
            return self.impl.set_prop4(v)
        logging.info("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        if path == "func1":
            param1 = api.as_int(args[0])
            reply = self.impl.func1(param1)
            return api.from_int(reply)
        elif path == "func2":
            param1 = api.as_int(args[0])
            param2 = api.as_int(args[1])
            reply = self.impl.func2(param1, param2)
            return api.from_int(reply)
        elif path == "func3":
            param1 = api.as_int(args[0])
            param2 = api.as_int(args[1])
            param3 = api.as_int(args[2])
            reply = self.impl.func3(param1, param2, param3)
            return api.from_int(reply)
        elif path == "func4":
            param1 = api.as_int(args[0])
            param2 = api.as_int(args[1])
            param3 = api.as_int(args[2])
            param4 = api.as_int(args[3])
            reply = self.impl.func4(param1, param2, param3, param4)
            return api.from_int(reply)      
        logging.info("unknown operation: %s", name)

    def olink_linked(self, name: str, node: "RemoteNode"):
        print('linked')

    def olink_collect_properties(self) -> object:
        props = {}
        v = self.impl.get_prop1()
        props["prop1"] = api.from_int(v)
        v = self.impl.get_prop2()
        props["prop2"] = api.from_int(v)
        v = self.impl.get_prop3()
        props["prop3"] = api.from_int(v)
        v = self.impl.get_prop4()
        props["prop4"] = api.from_int(v)
        return props

    def notify_signal(self, symbol, args):
        path = Name.path_from_name(symbol)
        if path == "sig1":
            param1 = api.from_int(args[0])
            return RemoteNode.notify_signal(symbol, [param1])
        elif path == "sig2":
            param1 = api.from_int(args[0])
            param2 = api.from_int(args[1])
            return RemoteNode.notify_signal(symbol, [param1, param2])
        elif path == "sig3":
            param1 = api.from_int(args[0])
            param2 = api.from_int(args[1])
            param3 = api.from_int(args[2])
            return RemoteNode.notify_signal(symbol, [param1, param2, param3])
        elif path == "sig4":
            param1 = api.from_int(args[0])
            param2 = api.from_int(args[1])
            param3 = api.from_int(args[2])
            param4 = api.from_int(args[3])
            return RemoteNode.notify_signal(symbol, [param1, param2, param3, param4])
        logging.info("unknown signal %s", symbol)

    def notify_property(self, symbol, value):
        path = Name.path_from_name(symbol)
        if path == "prop1":
            v = api.from_int(value)
            return RemoteNode.notify_property_change(symbol, value)
        elif path == "prop2":
            v = api.from_int(value)
            return RemoteNode.notify_property_change(symbol, value)
        elif path == "prop3":
            v = api.from_int(value)
            return RemoteNode.notify_property_change(symbol, value)
        elif path == "prop4":
            v = api.from_int(value)
            return RemoteNode.notify_property_change(symbol, value)
        logging.info("unknown property %s", symbol)
class NestedStruct1InterfaceSource(IObjectSource):
    impl: api.INestedStruct1Interface
    def __init__(self, impl: api.INestedStruct1Interface):
        self.impl = impl
        impl._notifier = self
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "testbed2.NestedStruct1Interface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        if path == "prop1":
            v = api.as_nested_struct1(value)
            return self.impl.set_prop1(v)
        logging.info("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        if path == "func1":
            param1 = api.as_nested_struct1(args[0])
            reply = self.impl.func1(param1)
            return api.from_nested_struct1(reply)      
        logging.info("unknown operation: %s", name)

    def olink_linked(self, name: str, node: "RemoteNode"):
        print('linked')

    def olink_collect_properties(self) -> object:
        props = {}
        v = self.impl.get_prop1()
        props["prop1"] = api.from_nested_struct1(v)
        return props

    def notify_signal(self, symbol, args):
        path = Name.path_from_name(symbol)
        if path == "sig1":
            param1 = api.from_nested_struct1(args[0])
            return RemoteNode.notify_signal(symbol, [param1])
        logging.info("unknown signal %s", symbol)

    def notify_property(self, symbol, value):
        path = Name.path_from_name(symbol)
        if path == "prop1":
            v = api.from_nested_struct1(value)
            return RemoteNode.notify_property_change(symbol, value)
        logging.info("unknown property %s", symbol)
class NestedStruct2InterfaceSource(IObjectSource):
    impl: api.INestedStruct2Interface
    def __init__(self, impl: api.INestedStruct2Interface):
        self.impl = impl
        impl._notifier = self
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "testbed2.NestedStruct2Interface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        if path == "prop1":
            v = api.as_nested_struct1(value)
            return self.impl.set_prop1(v)
        elif path == "prop2":
            v = api.as_nested_struct2(value)
            return self.impl.set_prop2(v)
        logging.info("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        if path == "func1":
            param1 = api.as_nested_struct1(args[0])
            reply = self.impl.func1(param1)
            return api.from_nested_struct1(reply)
        elif path == "func2":
            param1 = api.as_nested_struct1(args[0])
            param2 = api.as_nested_struct2(args[1])
            reply = self.impl.func2(param1, param2)
            return api.from_nested_struct1(reply)      
        logging.info("unknown operation: %s", name)

    def olink_linked(self, name: str, node: "RemoteNode"):
        print('linked')

    def olink_collect_properties(self) -> object:
        props = {}
        v = self.impl.get_prop1()
        props["prop1"] = api.from_nested_struct1(v)
        v = self.impl.get_prop2()
        props["prop2"] = api.from_nested_struct2(v)
        return props

    def notify_signal(self, symbol, args):
        path = Name.path_from_name(symbol)
        if path == "sig1":
            param1 = api.from_nested_struct1(args[0])
            return RemoteNode.notify_signal(symbol, [param1])
        elif path == "sig2":
            param1 = api.from_nested_struct1(args[0])
            param2 = api.from_nested_struct2(args[1])
            return RemoteNode.notify_signal(symbol, [param1, param2])
        logging.info("unknown signal %s", symbol)

    def notify_property(self, symbol, value):
        path = Name.path_from_name(symbol)
        if path == "prop1":
            v = api.from_nested_struct1(value)
            return RemoteNode.notify_property_change(symbol, value)
        elif path == "prop2":
            v = api.from_nested_struct2(value)
            return RemoteNode.notify_property_change(symbol, value)
        logging.info("unknown property %s", symbol)
class NestedStruct3InterfaceSource(IObjectSource):
    impl: api.INestedStruct3Interface
    def __init__(self, impl: api.INestedStruct3Interface):
        self.impl = impl
        impl._notifier = self
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "testbed2.NestedStruct3Interface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        if path == "prop1":
            v = api.as_nested_struct1(value)
            return self.impl.set_prop1(v)
        elif path == "prop2":
            v = api.as_nested_struct2(value)
            return self.impl.set_prop2(v)
        elif path == "prop3":
            v = api.as_nested_struct3(value)
            return self.impl.set_prop3(v)
        logging.info("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        if path == "func1":
            param1 = api.as_nested_struct1(args[0])
            reply = self.impl.func1(param1)
            return api.from_nested_struct1(reply)
        elif path == "func2":
            param1 = api.as_nested_struct1(args[0])
            param2 = api.as_nested_struct2(args[1])
            reply = self.impl.func2(param1, param2)
            return api.from_nested_struct1(reply)
        elif path == "func3":
            param1 = api.as_nested_struct1(args[0])
            param2 = api.as_nested_struct2(args[1])
            param3 = api.as_nested_struct3(args[2])
            reply = self.impl.func3(param1, param2, param3)
            return api.from_nested_struct1(reply)      
        logging.info("unknown operation: %s", name)

    def olink_linked(self, name: str, node: "RemoteNode"):
        print('linked')

    def olink_collect_properties(self) -> object:
        props = {}
        v = self.impl.get_prop1()
        props["prop1"] = api.from_nested_struct1(v)
        v = self.impl.get_prop2()
        props["prop2"] = api.from_nested_struct2(v)
        v = self.impl.get_prop3()
        props["prop3"] = api.from_nested_struct3(v)
        return props

    def notify_signal(self, symbol, args):
        path = Name.path_from_name(symbol)
        if path == "sig1":
            param1 = api.from_nested_struct1(args[0])
            return RemoteNode.notify_signal(symbol, [param1])
        elif path == "sig2":
            param1 = api.from_nested_struct1(args[0])
            param2 = api.from_nested_struct2(args[1])
            return RemoteNode.notify_signal(symbol, [param1, param2])
        elif path == "sig3":
            param1 = api.from_nested_struct1(args[0])
            param2 = api.from_nested_struct2(args[1])
            param3 = api.from_nested_struct3(args[2])
            return RemoteNode.notify_signal(symbol, [param1, param2, param3])
        logging.info("unknown signal %s", symbol)

    def notify_property(self, symbol, value):
        path = Name.path_from_name(symbol)
        if path == "prop1":
            v = api.from_nested_struct1(value)
            return RemoteNode.notify_property_change(symbol, value)
        elif path == "prop2":
            v = api.from_nested_struct2(value)
            return RemoteNode.notify_property_change(symbol, value)
        elif path == "prop3":
            v = api.from_nested_struct3(value)
            return RemoteNode.notify_property_change(symbol, value)
        logging.info("unknown property %s", symbol)