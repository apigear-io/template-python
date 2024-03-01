from olink.core import Name
from olink.remote import IObjectSource, RemoteNode
from tb_same1_api import api
from typing import Any
import logging
class SameStruct1InterfaceSource(IObjectSource):
    impl: api.ISameStruct1Interface
    def __init__(self, impl: api.ISameStruct1Interface):
        self.impl = impl
        impl.on_prop1_changed += self.notify_prop1_changed
        impl.on_sig1 += self.notify_sig1
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "tb.same1.SameStruct1Interface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        if path == "prop1":
            v = api.as_struct1(value)
            return self.impl.set_prop1(v)
        logging.info("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        if path == "func1":
            param1 = api.as_struct1(args[0])
            reply = self.impl.func1(param1)
            return api.from_struct1(reply)      
        logging.info("unknown operation: %s", name)

    def olink_linked(self, name: str, node: "RemoteNode"):
        print('linked')

    def olink_collect_properties(self) -> object:
        props = {}
        v = self.impl.get_prop1()
        props["prop1"] = api.from_struct1(v)
        return props

    def notify_sig1(self, param1: api.Struct1):
        _param1 = api.from_struct1(param1)
        return RemoteNode.notify_signal("tb.same1.SameStruct1Interface/sig1", [_param1])

    def notify_prop1_changed(self, value):
        return RemoteNode.notify_property_change("tb.same1.SameStruct1Interface/prop1", api.from_struct1(value))
class SameStruct2InterfaceSource(IObjectSource):
    impl: api.ISameStruct2Interface
    def __init__(self, impl: api.ISameStruct2Interface):
        self.impl = impl
        impl.on_prop1_changed += self.notify_prop1_changed
        impl.on_prop2_changed += self.notify_prop2_changed
        impl.on_sig1 += self.notify_sig1
        impl.on_sig2 += self.notify_sig2
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "tb.same1.SameStruct2Interface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        if path == "prop1":
            v = api.as_struct2(value)
            return self.impl.set_prop1(v)
        elif path == "prop2":
            v = api.as_struct2(value)
            return self.impl.set_prop2(v)
        logging.info("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        if path == "func1":
            param1 = api.as_struct1(args[0])
            reply = self.impl.func1(param1)
            return api.from_struct1(reply)
        elif path == "func2":
            param1 = api.as_struct1(args[0])
            param2 = api.as_struct2(args[1])
            reply = self.impl.func2(param1, param2)
            return api.from_struct1(reply)      
        logging.info("unknown operation: %s", name)

    def olink_linked(self, name: str, node: "RemoteNode"):
        print('linked')

    def olink_collect_properties(self) -> object:
        props = {}
        v = self.impl.get_prop1()
        props["prop1"] = api.from_struct2(v)
        v = self.impl.get_prop2()
        props["prop2"] = api.from_struct2(v)
        return props

    def notify_sig1(self, param1: api.Struct1):
        _param1 = api.from_struct1(param1)
        return RemoteNode.notify_signal("tb.same1.SameStruct2Interface/sig1", [_param1])

    def notify_sig2(self, param1: api.Struct1, param2: api.Struct2):
        _param1 = api.from_struct1(param1)
        _param2 = api.from_struct2(param2)
        return RemoteNode.notify_signal("tb.same1.SameStruct2Interface/sig2", [_param1, _param2])

    def notify_prop1_changed(self, value):
        return RemoteNode.notify_property_change("tb.same1.SameStruct2Interface/prop1", api.from_struct2(value))

    def notify_prop2_changed(self, value):
        return RemoteNode.notify_property_change("tb.same1.SameStruct2Interface/prop2", api.from_struct2(value))
class SameEnum1InterfaceSource(IObjectSource):
    impl: api.ISameEnum1Interface
    def __init__(self, impl: api.ISameEnum1Interface):
        self.impl = impl
        impl.on_prop1_changed += self.notify_prop1_changed
        impl.on_sig1 += self.notify_sig1
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "tb.same1.SameEnum1Interface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        if path == "prop1":
            v = api.as_enum1(value)
            return self.impl.set_prop1(v)
        logging.info("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        if path == "func1":
            param1 = api.as_enum1(args[0])
            reply = self.impl.func1(param1)
            return api.from_enum1(reply)      
        logging.info("unknown operation: %s", name)

    def olink_linked(self, name: str, node: "RemoteNode"):
        print('linked')

    def olink_collect_properties(self) -> object:
        props = {}
        v = self.impl.get_prop1()
        props["prop1"] = api.from_enum1(v)
        return props

    def notify_sig1(self, param1: api.Enum1):
        _param1 = api.from_enum1(param1)
        return RemoteNode.notify_signal("tb.same1.SameEnum1Interface/sig1", [_param1])

    def notify_prop1_changed(self, value):
        return RemoteNode.notify_property_change("tb.same1.SameEnum1Interface/prop1", api.from_enum1(value))
class SameEnum2InterfaceSource(IObjectSource):
    impl: api.ISameEnum2Interface
    def __init__(self, impl: api.ISameEnum2Interface):
        self.impl = impl
        impl.on_prop1_changed += self.notify_prop1_changed
        impl.on_prop2_changed += self.notify_prop2_changed
        impl.on_sig1 += self.notify_sig1
        impl.on_sig2 += self.notify_sig2
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "tb.same1.SameEnum2Interface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        if path == "prop1":
            v = api.as_enum1(value)
            return self.impl.set_prop1(v)
        elif path == "prop2":
            v = api.as_enum2(value)
            return self.impl.set_prop2(v)
        logging.info("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        if path == "func1":
            param1 = api.as_enum1(args[0])
            reply = self.impl.func1(param1)
            return api.from_enum1(reply)
        elif path == "func2":
            param1 = api.as_enum1(args[0])
            param2 = api.as_enum2(args[1])
            reply = self.impl.func2(param1, param2)
            return api.from_enum1(reply)      
        logging.info("unknown operation: %s", name)

    def olink_linked(self, name: str, node: "RemoteNode"):
        print('linked')

    def olink_collect_properties(self) -> object:
        props = {}
        v = self.impl.get_prop1()
        props["prop1"] = api.from_enum1(v)
        v = self.impl.get_prop2()
        props["prop2"] = api.from_enum2(v)
        return props

    def notify_sig1(self, param1: api.Enum1):
        _param1 = api.from_enum1(param1)
        return RemoteNode.notify_signal("tb.same1.SameEnum2Interface/sig1", [_param1])

    def notify_sig2(self, param1: api.Enum1, param2: api.Enum2):
        _param1 = api.from_enum1(param1)
        _param2 = api.from_enum2(param2)
        return RemoteNode.notify_signal("tb.same1.SameEnum2Interface/sig2", [_param1, _param2])

    def notify_prop1_changed(self, value):
        return RemoteNode.notify_property_change("tb.same1.SameEnum2Interface/prop1", api.from_enum1(value))

    def notify_prop2_changed(self, value):
        return RemoteNode.notify_property_change("tb.same1.SameEnum2Interface/prop2", api.from_enum2(value))
