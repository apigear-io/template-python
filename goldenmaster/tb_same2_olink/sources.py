from olink.core import Name
from olink.remote import IObjectSource, RemoteNode
import utils.base_types
import tb_same2_api
from utils.eventhook import EventHook
from typing import Any
import logging
class SameStruct1InterfaceSource(IObjectSource):
    impl: tb_same2_api.ISameStruct1Interface
    def __init__(self, impl: tb_same2_api.ISameStruct1Interface):
        self.impl = impl
        impl.on_prop1_changed += self.notify_prop1_changed
        impl.on_sig1 += self.notify_sig1
        self._on_linked = EventHook()
        self._on_unlinked = EventHook()
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "tb.same2.SameStruct1Interface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        if path == "prop1":
            v = tb_same2_api.as_struct1(value)
            return self.impl.set_prop1(v)
        logging.error("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        if path == "func1":
            param1 = tb_same2_api.as_struct1(args[0])
            reply = self.impl.func1(param1)
            return tb_same2_api.from_struct1(reply)      
        logging.error("unknown operation: %s", name)

    def olink_linked(self, name: str, node: "RemoteNode"):
        logging.info("linked: %s", name)
        self._on_linked.fire(name)

    def olink_unlinked(self, name: str, node: "RemoteNode"):
        logging.info("unlinked: %s", name)
        self._on_unlinked.fire(name)

    def olink_collect_properties(self) -> object:
        props = {}
        v = self.impl.get_prop1()
        props["prop1"] = tb_same2_api.from_struct1(v)
        return props

    def notify_sig1(self, param1: tb_same2_api.Struct1):
        _param1 = tb_same2_api.from_struct1(param1)
        return RemoteNode.notify_signal("tb.same2.SameStruct1Interface/sig1", [_param1])

    def notify_prop1_changed(self, value):
        v = tb_same2_api.from_struct1(value)
        return RemoteNode.notify_property_change("tb.same2.SameStruct1Interface/prop1", v)
class SameStruct2InterfaceSource(IObjectSource):
    impl: tb_same2_api.ISameStruct2Interface
    def __init__(self, impl: tb_same2_api.ISameStruct2Interface):
        self.impl = impl
        impl.on_prop1_changed += self.notify_prop1_changed
        impl.on_prop2_changed += self.notify_prop2_changed
        impl.on_sig1 += self.notify_sig1
        impl.on_sig2 += self.notify_sig2
        self._on_linked = EventHook()
        self._on_unlinked = EventHook()
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "tb.same2.SameStruct2Interface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        if path == "prop1":
            v = tb_same2_api.as_struct2(value)
            return self.impl.set_prop1(v)
        elif path == "prop2":
            v = tb_same2_api.as_struct2(value)
            return self.impl.set_prop2(v)
        logging.error("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        if path == "func1":
            param1 = tb_same2_api.as_struct1(args[0])
            reply = self.impl.func1(param1)
            return tb_same2_api.from_struct1(reply)
        elif path == "func2":
            param1 = tb_same2_api.as_struct1(args[0])
            param2 = tb_same2_api.as_struct2(args[1])
            reply = self.impl.func2(param1, param2)
            return tb_same2_api.from_struct1(reply)      
        logging.error("unknown operation: %s", name)

    def olink_linked(self, name: str, node: "RemoteNode"):
        logging.info("linked: %s", name)
        self._on_linked.fire(name)

    def olink_unlinked(self, name: str, node: "RemoteNode"):
        logging.info("unlinked: %s", name)
        self._on_unlinked.fire(name)

    def olink_collect_properties(self) -> object:
        props = {}
        v = self.impl.get_prop1()
        props["prop1"] = tb_same2_api.from_struct2(v)
        v = self.impl.get_prop2()
        props["prop2"] = tb_same2_api.from_struct2(v)
        return props

    def notify_sig1(self, param1: tb_same2_api.Struct1):
        _param1 = tb_same2_api.from_struct1(param1)
        return RemoteNode.notify_signal("tb.same2.SameStruct2Interface/sig1", [_param1])

    def notify_sig2(self, param1: tb_same2_api.Struct1, param2: tb_same2_api.Struct2):
        _param1 = tb_same2_api.from_struct1(param1)
        _param2 = tb_same2_api.from_struct2(param2)
        return RemoteNode.notify_signal("tb.same2.SameStruct2Interface/sig2", [_param1, _param2])

    def notify_prop1_changed(self, value):
        v = tb_same2_api.from_struct2(value)
        return RemoteNode.notify_property_change("tb.same2.SameStruct2Interface/prop1", v)

    def notify_prop2_changed(self, value):
        v = tb_same2_api.from_struct2(value)
        return RemoteNode.notify_property_change("tb.same2.SameStruct2Interface/prop2", v)
class SameEnum1InterfaceSource(IObjectSource):
    impl: tb_same2_api.ISameEnum1Interface
    def __init__(self, impl: tb_same2_api.ISameEnum1Interface):
        self.impl = impl
        impl.on_prop1_changed += self.notify_prop1_changed
        impl.on_sig1 += self.notify_sig1
        self._on_linked = EventHook()
        self._on_unlinked = EventHook()
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "tb.same2.SameEnum1Interface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        if path == "prop1":
            v = tb_same2_api.as_enum1(value)
            return self.impl.set_prop1(v)
        logging.error("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        if path == "func1":
            param1 = tb_same2_api.as_enum1(args[0])
            reply = self.impl.func1(param1)
            return tb_same2_api.from_enum1(reply)      
        logging.error("unknown operation: %s", name)

    def olink_linked(self, name: str, node: "RemoteNode"):
        logging.info("linked: %s", name)
        self._on_linked.fire(name)

    def olink_unlinked(self, name: str, node: "RemoteNode"):
        logging.info("unlinked: %s", name)
        self._on_unlinked.fire(name)

    def olink_collect_properties(self) -> object:
        props = {}
        v = self.impl.get_prop1()
        props["prop1"] = tb_same2_api.from_enum1(v)
        return props

    def notify_sig1(self, param1: tb_same2_api.Enum1):
        _param1 = tb_same2_api.from_enum1(param1)
        return RemoteNode.notify_signal("tb.same2.SameEnum1Interface/sig1", [_param1])

    def notify_prop1_changed(self, value):
        v = tb_same2_api.from_enum1(value)
        return RemoteNode.notify_property_change("tb.same2.SameEnum1Interface/prop1", v)
class SameEnum2InterfaceSource(IObjectSource):
    impl: tb_same2_api.ISameEnum2Interface
    def __init__(self, impl: tb_same2_api.ISameEnum2Interface):
        self.impl = impl
        impl.on_prop1_changed += self.notify_prop1_changed
        impl.on_prop2_changed += self.notify_prop2_changed
        impl.on_sig1 += self.notify_sig1
        impl.on_sig2 += self.notify_sig2
        self._on_linked = EventHook()
        self._on_unlinked = EventHook()
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "tb.same2.SameEnum2Interface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        if path == "prop1":
            v = tb_same2_api.as_enum1(value)
            return self.impl.set_prop1(v)
        elif path == "prop2":
            v = tb_same2_api.as_enum2(value)
            return self.impl.set_prop2(v)
        logging.error("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        if path == "func1":
            param1 = tb_same2_api.as_enum1(args[0])
            reply = self.impl.func1(param1)
            return tb_same2_api.from_enum1(reply)
        elif path == "func2":
            param1 = tb_same2_api.as_enum1(args[0])
            param2 = tb_same2_api.as_enum2(args[1])
            reply = self.impl.func2(param1, param2)
            return tb_same2_api.from_enum1(reply)      
        logging.error("unknown operation: %s", name)

    def olink_linked(self, name: str, node: "RemoteNode"):
        logging.info("linked: %s", name)
        self._on_linked.fire(name)

    def olink_unlinked(self, name: str, node: "RemoteNode"):
        logging.info("unlinked: %s", name)
        self._on_unlinked.fire(name)

    def olink_collect_properties(self) -> object:
        props = {}
        v = self.impl.get_prop1()
        props["prop1"] = tb_same2_api.from_enum1(v)
        v = self.impl.get_prop2()
        props["prop2"] = tb_same2_api.from_enum2(v)
        return props

    def notify_sig1(self, param1: tb_same2_api.Enum1):
        _param1 = tb_same2_api.from_enum1(param1)
        return RemoteNode.notify_signal("tb.same2.SameEnum2Interface/sig1", [_param1])

    def notify_sig2(self, param1: tb_same2_api.Enum1, param2: tb_same2_api.Enum2):
        _param1 = tb_same2_api.from_enum1(param1)
        _param2 = tb_same2_api.from_enum2(param2)
        return RemoteNode.notify_signal("tb.same2.SameEnum2Interface/sig2", [_param1, _param2])

    def notify_prop1_changed(self, value):
        v = tb_same2_api.from_enum1(value)
        return RemoteNode.notify_property_change("tb.same2.SameEnum2Interface/prop1", v)

    def notify_prop2_changed(self, value):
        v = tb_same2_api.from_enum2(value)
        return RemoteNode.notify_property_change("tb.same2.SameEnum2Interface/prop2", v)
