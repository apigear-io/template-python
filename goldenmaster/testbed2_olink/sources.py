from olink.core import Name
from olink.remote import IObjectSource, RemoteNode
from testbed2_api import api
from testbed2_api.shared import EventHook
from typing import Any
import logging
class ManyParamInterfaceSource(IObjectSource):
    impl: api.IManyParamInterface
    def __init__(self, impl: api.IManyParamInterface):
        self.impl = impl
        impl.on_prop1_changed += self.notify_prop1_changed
        impl.on_prop2_changed += self.notify_prop2_changed
        impl.on_prop3_changed += self.notify_prop3_changed
        impl.on_prop4_changed += self.notify_prop4_changed
        impl.on_sig1 += self.notify_sig1
        impl.on_sig2 += self.notify_sig2
        impl.on_sig3 += self.notify_sig3
        impl.on_sig4 += self.notify_sig4
        self._on_linked = EventHook()
        self._on_unlinked = EventHook()
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
        logging.error("unknown property: %s", name)


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
        props["prop1"] = api.from_int(v)
        v = self.impl.get_prop2()
        props["prop2"] = api.from_int(v)
        v = self.impl.get_prop3()
        props["prop3"] = api.from_int(v)
        v = self.impl.get_prop4()
        props["prop4"] = api.from_int(v)
        return props

    def notify_sig1(self, param1: int):
        _param1 = api.from_int(param1)
        return RemoteNode.notify_signal("testbed2.ManyParamInterface/sig1", [_param1])

    def notify_sig2(self, param1: int, param2: int):
        _param1 = api.from_int(param1)
        _param2 = api.from_int(param2)
        return RemoteNode.notify_signal("testbed2.ManyParamInterface/sig2", [_param1, _param2])

    def notify_sig3(self, param1: int, param2: int, param3: int):
        _param1 = api.from_int(param1)
        _param2 = api.from_int(param2)
        _param3 = api.from_int(param3)
        return RemoteNode.notify_signal("testbed2.ManyParamInterface/sig3", [_param1, _param2, _param3])

    def notify_sig4(self, param1: int, param2: int, param3: int, param4: int):
        _param1 = api.from_int(param1)
        _param2 = api.from_int(param2)
        _param3 = api.from_int(param3)
        _param4 = api.from_int(param4)
        return RemoteNode.notify_signal("testbed2.ManyParamInterface/sig4", [_param1, _param2, _param3, _param4])

    def notify_prop1_changed(self, value):
        v = api.from_int(value)
        return RemoteNode.notify_property_change("testbed2.ManyParamInterface/prop1", v)

    def notify_prop2_changed(self, value):
        v = api.from_int(value)
        return RemoteNode.notify_property_change("testbed2.ManyParamInterface/prop2", v)

    def notify_prop3_changed(self, value):
        v = api.from_int(value)
        return RemoteNode.notify_property_change("testbed2.ManyParamInterface/prop3", v)

    def notify_prop4_changed(self, value):
        v = api.from_int(value)
        return RemoteNode.notify_property_change("testbed2.ManyParamInterface/prop4", v)
class NestedStruct1InterfaceSource(IObjectSource):
    impl: api.INestedStruct1Interface
    def __init__(self, impl: api.INestedStruct1Interface):
        self.impl = impl
        impl.on_prop1_changed += self.notify_prop1_changed
        impl.on_sig1 += self.notify_sig1
        self._on_linked = EventHook()
        self._on_unlinked = EventHook()
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "testbed2.NestedStruct1Interface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        if path == "prop1":
            v = api.as_nested_struct1(value)
            return self.impl.set_prop1(v)
        logging.error("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        if path == "func1":
            param1 = api.as_nested_struct1(args[0])
            reply = self.impl.func1(param1)
            return api.from_nested_struct1(reply)      
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
        props["prop1"] = api.from_nested_struct1(v)
        return props

    def notify_sig1(self, param1: api.NestedStruct1):
        _param1 = api.from_nested_struct1(param1)
        return RemoteNode.notify_signal("testbed2.NestedStruct1Interface/sig1", [_param1])

    def notify_prop1_changed(self, value):
        v = api.from_nested_struct1(value)
        return RemoteNode.notify_property_change("testbed2.NestedStruct1Interface/prop1", v)
class NestedStruct2InterfaceSource(IObjectSource):
    impl: api.INestedStruct2Interface
    def __init__(self, impl: api.INestedStruct2Interface):
        self.impl = impl
        impl.on_prop1_changed += self.notify_prop1_changed
        impl.on_prop2_changed += self.notify_prop2_changed
        impl.on_sig1 += self.notify_sig1
        impl.on_sig2 += self.notify_sig2
        self._on_linked = EventHook()
        self._on_unlinked = EventHook()
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
        logging.error("unknown property: %s", name)


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
        props["prop1"] = api.from_nested_struct1(v)
        v = self.impl.get_prop2()
        props["prop2"] = api.from_nested_struct2(v)
        return props

    def notify_sig1(self, param1: api.NestedStruct1):
        _param1 = api.from_nested_struct1(param1)
        return RemoteNode.notify_signal("testbed2.NestedStruct2Interface/sig1", [_param1])

    def notify_sig2(self, param1: api.NestedStruct1, param2: api.NestedStruct2):
        _param1 = api.from_nested_struct1(param1)
        _param2 = api.from_nested_struct2(param2)
        return RemoteNode.notify_signal("testbed2.NestedStruct2Interface/sig2", [_param1, _param2])

    def notify_prop1_changed(self, value):
        v = api.from_nested_struct1(value)
        return RemoteNode.notify_property_change("testbed2.NestedStruct2Interface/prop1", v)

    def notify_prop2_changed(self, value):
        v = api.from_nested_struct2(value)
        return RemoteNode.notify_property_change("testbed2.NestedStruct2Interface/prop2", v)
class NestedStruct3InterfaceSource(IObjectSource):
    impl: api.INestedStruct3Interface
    def __init__(self, impl: api.INestedStruct3Interface):
        self.impl = impl
        impl.on_prop1_changed += self.notify_prop1_changed
        impl.on_prop2_changed += self.notify_prop2_changed
        impl.on_prop3_changed += self.notify_prop3_changed
        impl.on_sig1 += self.notify_sig1
        impl.on_sig2 += self.notify_sig2
        impl.on_sig3 += self.notify_sig3
        self._on_linked = EventHook()
        self._on_unlinked = EventHook()
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
        logging.error("unknown property: %s", name)


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
        props["prop1"] = api.from_nested_struct1(v)
        v = self.impl.get_prop2()
        props["prop2"] = api.from_nested_struct2(v)
        v = self.impl.get_prop3()
        props["prop3"] = api.from_nested_struct3(v)
        return props

    def notify_sig1(self, param1: api.NestedStruct1):
        _param1 = api.from_nested_struct1(param1)
        return RemoteNode.notify_signal("testbed2.NestedStruct3Interface/sig1", [_param1])

    def notify_sig2(self, param1: api.NestedStruct1, param2: api.NestedStruct2):
        _param1 = api.from_nested_struct1(param1)
        _param2 = api.from_nested_struct2(param2)
        return RemoteNode.notify_signal("testbed2.NestedStruct3Interface/sig2", [_param1, _param2])

    def notify_sig3(self, param1: api.NestedStruct1, param2: api.NestedStruct2, param3: api.NestedStruct3):
        _param1 = api.from_nested_struct1(param1)
        _param2 = api.from_nested_struct2(param2)
        _param3 = api.from_nested_struct3(param3)
        return RemoteNode.notify_signal("testbed2.NestedStruct3Interface/sig3", [_param1, _param2, _param3])

    def notify_prop1_changed(self, value):
        v = api.from_nested_struct1(value)
        return RemoteNode.notify_property_change("testbed2.NestedStruct3Interface/prop1", v)

    def notify_prop2_changed(self, value):
        v = api.from_nested_struct2(value)
        return RemoteNode.notify_property_change("testbed2.NestedStruct3Interface/prop2", v)

    def notify_prop3_changed(self, value):
        v = api.from_nested_struct3(value)
        return RemoteNode.notify_property_change("testbed2.NestedStruct3Interface/prop3", v)
