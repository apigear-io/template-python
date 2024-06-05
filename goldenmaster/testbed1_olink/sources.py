from olink.core import Name
from olink.remote import IObjectSource, RemoteNode
import utils.base_types
import testbed1_api
from utils.eventhook import EventHook
from typing import Any
import logging
class StructInterfaceSource(IObjectSource):
    impl: testbed1_api.IStructInterface
    def __init__(self, impl: testbed1_api.IStructInterface):
        self.impl = impl
        impl.on_prop_bool_changed += self.notify_prop_bool_changed
        impl.on_prop_int_changed += self.notify_prop_int_changed
        impl.on_prop_float_changed += self.notify_prop_float_changed
        impl.on_prop_string_changed += self.notify_prop_string_changed
        impl.on_sig_bool += self.notify_sig_bool
        impl.on_sig_int += self.notify_sig_int
        impl.on_sig_float += self.notify_sig_float
        impl.on_sig_string += self.notify_sig_string
        self._on_linked = EventHook()
        self._on_unlinked = EventHook()
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "testbed1.StructInterface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        if path == "propBool":
            v = testbed1_api.as_struct_bool(value)
            return self.impl.set_prop_bool(v)
        elif path == "propInt":
            v = testbed1_api.as_struct_int(value)
            return self.impl.set_prop_int(v)
        elif path == "propFloat":
            v = testbed1_api.as_struct_float(value)
            return self.impl.set_prop_float(v)
        elif path == "propString":
            v = testbed1_api.as_struct_string(value)
            return self.impl.set_prop_string(v)
        logging.error("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        if path == "funcBool":
            param_bool = testbed1_api.as_struct_bool(args[0])
            reply = self.impl.func_bool(param_bool)
            return testbed1_api.from_struct_bool(reply)
        elif path == "funcInt":
            param_int = testbed1_api.as_struct_int(args[0])
            reply = self.impl.func_int(param_int)
            return testbed1_api.from_struct_bool(reply)
        elif path == "funcFloat":
            param_float = testbed1_api.as_struct_float(args[0])
            reply = self.impl.func_float(param_float)
            return testbed1_api.from_struct_float(reply)
        elif path == "funcString":
            param_string = testbed1_api.as_struct_string(args[0])
            reply = self.impl.func_string(param_string)
            return testbed1_api.from_struct_string(reply)      
        logging.error("unknown operation: %s", name)

    def olink_linked(self, name: str, node: "RemoteNode"):
        logging.info("linked: %s", name)
        self._on_linked.fire(name)

    def olink_unlinked(self, name: str, node: "RemoteNode"):
        logging.info("unlinked: %s", name)
        self._on_unlinked.fire(name)

    def olink_collect_properties(self) -> object:
        props = {}
        v = self.impl.get_prop_bool()
        props["propBool"] = testbed1_api.from_struct_bool(v)
        v = self.impl.get_prop_int()
        props["propInt"] = testbed1_api.from_struct_int(v)
        v = self.impl.get_prop_float()
        props["propFloat"] = testbed1_api.from_struct_float(v)
        v = self.impl.get_prop_string()
        props["propString"] = testbed1_api.from_struct_string(v)
        return props

    def notify_sig_bool(self, param_bool: testbed1_api.StructBool):
        _param_bool = testbed1_api.from_struct_bool(param_bool)
        return RemoteNode.notify_signal("testbed1.StructInterface/sigBool", [_param_bool])

    def notify_sig_int(self, param_int: testbed1_api.StructInt):
        _param_int = testbed1_api.from_struct_int(param_int)
        return RemoteNode.notify_signal("testbed1.StructInterface/sigInt", [_param_int])

    def notify_sig_float(self, param_float: testbed1_api.StructFloat):
        _param_float = testbed1_api.from_struct_float(param_float)
        return RemoteNode.notify_signal("testbed1.StructInterface/sigFloat", [_param_float])

    def notify_sig_string(self, param_string: testbed1_api.StructString):
        _param_string = testbed1_api.from_struct_string(param_string)
        return RemoteNode.notify_signal("testbed1.StructInterface/sigString", [_param_string])

    def notify_prop_bool_changed(self, value):
        v = testbed1_api.from_struct_bool(value)
        return RemoteNode.notify_property_change("testbed1.StructInterface/propBool", v)

    def notify_prop_int_changed(self, value):
        v = testbed1_api.from_struct_int(value)
        return RemoteNode.notify_property_change("testbed1.StructInterface/propInt", v)

    def notify_prop_float_changed(self, value):
        v = testbed1_api.from_struct_float(value)
        return RemoteNode.notify_property_change("testbed1.StructInterface/propFloat", v)

    def notify_prop_string_changed(self, value):
        v = testbed1_api.from_struct_string(value)
        return RemoteNode.notify_property_change("testbed1.StructInterface/propString", v)
class StructArrayInterfaceSource(IObjectSource):
    impl: testbed1_api.IStructArrayInterface
    def __init__(self, impl: testbed1_api.IStructArrayInterface):
        self.impl = impl
        impl.on_prop_bool_changed += self.notify_prop_bool_changed
        impl.on_prop_int_changed += self.notify_prop_int_changed
        impl.on_prop_float_changed += self.notify_prop_float_changed
        impl.on_prop_string_changed += self.notify_prop_string_changed
        impl.on_sig_bool += self.notify_sig_bool
        impl.on_sig_int += self.notify_sig_int
        impl.on_sig_float += self.notify_sig_float
        impl.on_sig_string += self.notify_sig_string
        self._on_linked = EventHook()
        self._on_unlinked = EventHook()
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "testbed1.StructArrayInterface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        if path == "propBool":
            v = [testbed1_api.as_struct_bool(_) for _ in value]
            return self.impl.set_prop_bool(v)
        elif path == "propInt":
            v = [testbed1_api.as_struct_int(_) for _ in value]
            return self.impl.set_prop_int(v)
        elif path == "propFloat":
            v = [testbed1_api.as_struct_float(_) for _ in value]
            return self.impl.set_prop_float(v)
        elif path == "propString":
            v = [testbed1_api.as_struct_string(_) for _ in value]
            return self.impl.set_prop_string(v)
        logging.error("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        if path == "funcBool":
            param_bool = [testbed1_api.as_struct_bool(_) for _ in args[0]]
            reply = self.impl.func_bool(param_bool)
            return [testbed1_api.from_struct_bool(_) for _ in reply]
        elif path == "funcInt":
            param_int = [testbed1_api.as_struct_int(_) for _ in args[0]]
            reply = self.impl.func_int(param_int)
            return [testbed1_api.from_struct_int(_) for _ in reply]
        elif path == "funcFloat":
            param_float = [testbed1_api.as_struct_float(_) for _ in args[0]]
            reply = self.impl.func_float(param_float)
            return [testbed1_api.from_struct_float(_) for _ in reply]
        elif path == "funcString":
            param_string = [testbed1_api.as_struct_string(_) for _ in args[0]]
            reply = self.impl.func_string(param_string)
            return [testbed1_api.from_struct_string(_) for _ in reply]      
        logging.error("unknown operation: %s", name)

    def olink_linked(self, name: str, node: "RemoteNode"):
        logging.info("linked: %s", name)
        self._on_linked.fire(name)

    def olink_unlinked(self, name: str, node: "RemoteNode"):
        logging.info("unlinked: %s", name)
        self._on_unlinked.fire(name)

    def olink_collect_properties(self) -> object:
        props = {}
        v = self.impl.get_prop_bool()
        props["propBool"] = [testbed1_api.from_struct_bool(_) for _ in v]
        v = self.impl.get_prop_int()
        props["propInt"] = [testbed1_api.from_struct_int(_) for _ in v]
        v = self.impl.get_prop_float()
        props["propFloat"] = [testbed1_api.from_struct_float(_) for _ in v]
        v = self.impl.get_prop_string()
        props["propString"] = [testbed1_api.from_struct_string(_) for _ in v]
        return props

    def notify_sig_bool(self, param_bool: list[testbed1_api.StructBool]):
        _param_bool = [testbed1_api.api.from_struct_bool(_) for _ in param_bool]
        return RemoteNode.notify_signal("testbed1.StructArrayInterface/sigBool", [_param_bool])

    def notify_sig_int(self, param_int: list[testbed1_api.StructInt]):
        _param_int = [testbed1_api.api.from_struct_int(_) for _ in param_int]
        return RemoteNode.notify_signal("testbed1.StructArrayInterface/sigInt", [_param_int])

    def notify_sig_float(self, param_float: list[testbed1_api.StructFloat]):
        _param_float = [testbed1_api.api.from_struct_float(_) for _ in param_float]
        return RemoteNode.notify_signal("testbed1.StructArrayInterface/sigFloat", [_param_float])

    def notify_sig_string(self, param_string: list[testbed1_api.StructString]):
        _param_string = [testbed1_api.api.from_struct_string(_) for _ in param_string]
        return RemoteNode.notify_signal("testbed1.StructArrayInterface/sigString", [_param_string])

    def notify_prop_bool_changed(self, value):
        v = [testbed1_api.from_struct_bool(_) for _ in value]
        return RemoteNode.notify_property_change("testbed1.StructArrayInterface/propBool", v)

    def notify_prop_int_changed(self, value):
        v = [testbed1_api.from_struct_int(_) for _ in value]
        return RemoteNode.notify_property_change("testbed1.StructArrayInterface/propInt", v)

    def notify_prop_float_changed(self, value):
        v = [testbed1_api.from_struct_float(_) for _ in value]
        return RemoteNode.notify_property_change("testbed1.StructArrayInterface/propFloat", v)

    def notify_prop_string_changed(self, value):
        v = [testbed1_api.from_struct_string(_) for _ in value]
        return RemoteNode.notify_property_change("testbed1.StructArrayInterface/propString", v)
