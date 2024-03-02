from olink.core import Name
from olink.remote import IObjectSource, RemoteNode
from testbed1_api import api
from typing import Any
import logging
class StructInterfaceSource(IObjectSource):
    impl: api.IStructInterface
    def __init__(self, impl: api.IStructInterface):
        self.impl = impl
        impl.on_prop_bool_changed += self.notify_prop_bool_changed
        impl.on_prop_int_changed += self.notify_prop_int_changed
        impl.on_prop_float_changed += self.notify_prop_float_changed
        impl.on_prop_string_changed += self.notify_prop_string_changed
        impl.on_sig_bool += self.notify_sig_bool
        impl.on_sig_int += self.notify_sig_int
        impl.on_sig_float += self.notify_sig_float
        impl.on_sig_string += self.notify_sig_string
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "testbed1.StructInterface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        if path == "propBool":
            v = api.as_struct_bool(value)
            return self.impl.set_prop_bool(v)
        elif path == "propInt":
            v = api.as_struct_int(value)
            return self.impl.set_prop_int(v)
        elif path == "propFloat":
            v = api.as_struct_float(value)
            return self.impl.set_prop_float(v)
        elif path == "propString":
            v = api.as_struct_string(value)
            return self.impl.set_prop_string(v)
        logging.error("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        if path == "funcBool":
            param_bool = api.as_struct_bool(args[0])
            reply = self.impl.func_bool(param_bool)
            return api.from_struct_bool(reply)
        elif path == "funcInt":
            param_int = api.as_struct_int(args[0])
            reply = self.impl.func_int(param_int)
            return api.from_struct_bool(reply)
        elif path == "funcFloat":
            param_float = api.as_struct_float(args[0])
            reply = self.impl.func_float(param_float)
            return api.from_struct_float(reply)
        elif path == "funcString":
            param_string = api.as_struct_string(args[0])
            reply = self.impl.func_string(param_string)
            return api.from_struct_string(reply)      
        logging.error("unknown operation: %s", name)

    def olink_linked(self, name: str, node: "RemoteNode"):
        logging.info("linked: %s", name)

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

    def notify_sig_bool(self, param_bool: api.StructBool):
        _param_bool = api.from_struct_bool(param_bool)
        return RemoteNode.notify_signal("testbed1.StructInterface/sigBool", [_param_bool])

    def notify_sig_int(self, param_int: api.StructInt):
        _param_int = api.from_struct_int(param_int)
        return RemoteNode.notify_signal("testbed1.StructInterface/sigInt", [_param_int])

    def notify_sig_float(self, param_float: api.StructFloat):
        _param_float = api.from_struct_float(param_float)
        return RemoteNode.notify_signal("testbed1.StructInterface/sigFloat", [_param_float])

    def notify_sig_string(self, param_string: api.StructString):
        _param_string = api.from_struct_string(param_string)
        return RemoteNode.notify_signal("testbed1.StructInterface/sigString", [_param_string])

    def notify_prop_bool_changed(self, value):
        v = api.from_struct_bool(value)
        return RemoteNode.notify_property_change("testbed1.StructInterface/propBool", v)

    def notify_prop_int_changed(self, value):
        v = api.from_struct_int(value)
        return RemoteNode.notify_property_change("testbed1.StructInterface/propInt", v)

    def notify_prop_float_changed(self, value):
        v = api.from_struct_float(value)
        return RemoteNode.notify_property_change("testbed1.StructInterface/propFloat", v)

    def notify_prop_string_changed(self, value):
        v = api.from_struct_string(value)
        return RemoteNode.notify_property_change("testbed1.StructInterface/propString", v)
class StructArrayInterfaceSource(IObjectSource):
    impl: api.IStructArrayInterface
    def __init__(self, impl: api.IStructArrayInterface):
        self.impl = impl
        impl.on_prop_bool_changed += self.notify_prop_bool_changed
        impl.on_prop_int_changed += self.notify_prop_int_changed
        impl.on_prop_float_changed += self.notify_prop_float_changed
        impl.on_prop_string_changed += self.notify_prop_string_changed
        impl.on_sig_bool += self.notify_sig_bool
        impl.on_sig_int += self.notify_sig_int
        impl.on_sig_float += self.notify_sig_float
        impl.on_sig_string += self.notify_sig_string
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "testbed1.StructArrayInterface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        if path == "propBool":
            v = [api.as_struct_bool(struct_bool) for struct_bool in value]
            return self.impl.set_prop_bool(v)
        elif path == "propInt":
            v = [api.as_struct_int(struct_int) for struct_int in value]
            return self.impl.set_prop_int(v)
        elif path == "propFloat":
            v = [api.as_struct_float(struct_float) for struct_float in value]
            return self.impl.set_prop_float(v)
        elif path == "propString":
            v = [api.as_struct_string(struct_string) for struct_string in value]
            return self.impl.set_prop_string(v)
        logging.error("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        if path == "funcBool":
            param_bool = api.as_struct_bool(args[0])
            reply = self.impl.func_bool(param_bool)
            return api.from_struct_bool(reply)
        elif path == "funcInt":
            param_int = api.as_struct_int(args[0])
            reply = self.impl.func_int(param_int)
            return api.from_struct_bool(reply)
        elif path == "funcFloat":
            param_float = api.as_struct_float(args[0])
            reply = self.impl.func_float(param_float)
            return api.from_struct_bool(reply)
        elif path == "funcString":
            param_string = api.as_struct_string(args[0])
            reply = self.impl.func_string(param_string)
            return api.from_struct_bool(reply)      
        logging.error("unknown operation: %s", name)

    def olink_linked(self, name: str, node: "RemoteNode"):
        logging.info("linked: %s", name)

    def olink_collect_properties(self) -> object:
        props = {}
        v = self.impl.get_prop_bool()
        props["propBool"] = [api.from_struct_bool(struct_bool) for struct_bool in v]
        v = self.impl.get_prop_int()
        props["propInt"] = [api.from_struct_int(struct_int) for struct_int in v]
        v = self.impl.get_prop_float()
        props["propFloat"] = [api.from_struct_float(struct_float) for struct_float in v]
        v = self.impl.get_prop_string()
        props["propString"] = [api.from_struct_string(struct_string) for struct_string in v]
        return props

    def notify_sig_bool(self, param_bool: list[api.StructBool]):
        _param_bool = api.from_struct_bool(param_bool)
        return RemoteNode.notify_signal("testbed1.StructArrayInterface/sigBool", [_param_bool])

    def notify_sig_int(self, param_int: list[api.StructInt]):
        _param_int = api.from_struct_int(param_int)
        return RemoteNode.notify_signal("testbed1.StructArrayInterface/sigInt", [_param_int])

    def notify_sig_float(self, param_float: list[api.StructFloat]):
        _param_float = api.from_struct_float(param_float)
        return RemoteNode.notify_signal("testbed1.StructArrayInterface/sigFloat", [_param_float])

    def notify_sig_string(self, param_string: list[api.StructString]):
        _param_string = api.from_struct_string(param_string)
        return RemoteNode.notify_signal("testbed1.StructArrayInterface/sigString", [_param_string])

    def notify_prop_bool_changed(self, value):
        v = [api.from_struct_bool(struct_bool) for struct_bool in value]
        return RemoteNode.notify_property_change("testbed1.StructArrayInterface/propBool", v)

    def notify_prop_int_changed(self, value):
        v = [api.from_struct_int(struct_int) for struct_int in value]
        return RemoteNode.notify_property_change("testbed1.StructArrayInterface/propInt", v)

    def notify_prop_float_changed(self, value):
        v = [api.from_struct_float(struct_float) for struct_float in value]
        return RemoteNode.notify_property_change("testbed1.StructArrayInterface/propFloat", v)

    def notify_prop_string_changed(self, value):
        v = [api.from_struct_string(struct_string) for struct_string in value]
        return RemoteNode.notify_property_change("testbed1.StructArrayInterface/propString", v)
