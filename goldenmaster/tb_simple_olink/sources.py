from olink.core import Name
from olink.remote import IObjectSource, RemoteNode
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
        if path == "propBool":
            v = api.as_bool(value)
            return self.impl.set_prop_bool(v)
        elif path == "propInt":
            v = api.as_int(value)
            return self.impl.set_prop_int(v)
        elif path == "propInt32":
            v = api.as_int32(value)
            return self.impl.set_prop_int32(v)
        elif path == "propInt64":
            v = api.as_int64(value)
            return self.impl.set_prop_int64(v)
        elif path == "propFloat":
            v = api.as_float(value)
            return self.impl.set_prop_float(v)
        elif path == "propFloat32":
            v = api.as_float32(value)
            return self.impl.set_prop_float32(v)
        elif path == "propFloat64":
            v = api.as_float64(value)
            return self.impl.set_prop_float64(v)
        elif path == "propString":
            v = api.as_string(value)
            return self.impl.set_prop_string(v)
        elif path == "propReadOnlyString":
            pass
        logging.info("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        if path == "funcVoid":
            reply = self.impl.func_void()
            return None
        elif path == "funcBool":
            param_bool = api.as_bool(args[0])
            reply = self.impl.func_bool(param_bool)
            return api.from_bool(reply)
        elif path == "funcInt":
            param_int = api.as_int(args[0])
            reply = self.impl.func_int(param_int)
            return api.from_int(reply)
        elif path == "funcInt32":
            param_int32 = api.as_int32(args[0])
            reply = self.impl.func_int32(param_int32)
            return api.from_int32(reply)
        elif path == "funcInt64":
            param_int64 = api.as_int64(args[0])
            reply = self.impl.func_int64(param_int64)
            return api.from_int64(reply)
        elif path == "funcFloat":
            param_float = api.as_float(args[0])
            reply = self.impl.func_float(param_float)
            return api.from_float(reply)
        elif path == "funcFloat32":
            param_float32 = api.as_float32(args[0])
            reply = self.impl.func_float32(param_float32)
            return api.from_float32(reply)
        elif path == "funcFloat64":
            param_float = api.as_float64(args[0])
            reply = self.impl.func_float64(param_float)
            return api.from_float64(reply)
        elif path == "funcString":
            param_string = api.as_string(args[0])
            reply = self.impl.func_string(param_string)
            return api.from_string(reply)      
        logging.info("unknown operation: %s", name)

    def olink_linked(self, name: str, node: "RemoteNode"):
        print('linked')

    def olink_collect_properties(self) -> object:
        props = {}
        v = self.impl.get_prop_bool()
        props["propBool"] = api.from_bool(v)
        v = self.impl.get_prop_int()
        props["propInt"] = api.from_int(v)
        v = self.impl.get_prop_int32()
        props["propInt32"] = api.from_int32(v)
        v = self.impl.get_prop_int64()
        props["propInt64"] = api.from_int64(v)
        v = self.impl.get_prop_float()
        props["propFloat"] = api.from_float(v)
        v = self.impl.get_prop_float32()
        props["propFloat32"] = api.from_float32(v)
        v = self.impl.get_prop_float64()
        props["propFloat64"] = api.from_float64(v)
        v = self.impl.get_prop_string()
        props["propString"] = api.from_string(v)
        v = self.impl.get_prop_read_only_string()
        props["propReadOnlyString"] = api.from_string(v)
        return props

    def notify_signal(self, symbol, args):
        path = Name.path_from_name(symbol)
        if path == "sigVoid":
            return RemoteNode.notify_signal(symbol, [])
        elif path == "sigBool":
            param_bool = api.from_bool(args[0])
            return RemoteNode.notify_signal(symbol, [param_bool])
        elif path == "sigInt":
            param_int = api.from_int(args[0])
            return RemoteNode.notify_signal(symbol, [param_int])
        elif path == "sigInt32":
            param_int32 = api.from_int32(args[0])
            return RemoteNode.notify_signal(symbol, [param_int32])
        elif path == "sigInt64":
            param_int64 = api.from_int64(args[0])
            return RemoteNode.notify_signal(symbol, [param_int64])
        elif path == "sigFloat":
            param_float = api.from_float(args[0])
            return RemoteNode.notify_signal(symbol, [param_float])
        elif path == "sigFloat32":
            param_float32 = api.from_float32(args[0])
            return RemoteNode.notify_signal(symbol, [param_float32])
        elif path == "sigFloat64":
            param_float64 = api.from_float64(args[0])
            return RemoteNode.notify_signal(symbol, [param_float64])
        elif path == "sigString":
            param_string = api.from_string(args[0])
            return RemoteNode.notify_signal(symbol, [param_string])
        logging.info("unknown signal %s", symbol)

    def notify_property(self, symbol, value):
        path = Name.path_from_name(symbol)
        if path == "propBool":
            v = api.from_bool(value)
            return RemoteNode.notify_property_change(symbol, v)
        elif path == "propInt":
            v = api.from_int(value)
            return RemoteNode.notify_property_change(symbol, v)
        elif path == "propInt32":
            v = api.from_int32(value)
            return RemoteNode.notify_property_change(symbol, v)
        elif path == "propInt64":
            v = api.from_int64(value)
            return RemoteNode.notify_property_change(symbol, v)
        elif path == "propFloat":
            v = api.from_float(value)
            return RemoteNode.notify_property_change(symbol, v)
        elif path == "propFloat32":
            v = api.from_float32(value)
            return RemoteNode.notify_property_change(symbol, v)
        elif path == "propFloat64":
            v = api.from_float64(value)
            return RemoteNode.notify_property_change(symbol, v)
        elif path == "propString":
            v = api.from_string(value)
            return RemoteNode.notify_property_change(symbol, v)
        elif path == "propReadOnlyString":
            v = api.from_string(value)
            return RemoteNode.notify_property_change(symbol, v)
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
        if path == "propBool":
            v = api.as_bool(value)
            return self.impl.set_prop_bool(v)
        elif path == "propInt":
            v = api.as_int(value)
            return self.impl.set_prop_int(v)
        elif path == "propInt32":
            v = api.as_int32(value)
            return self.impl.set_prop_int32(v)
        elif path == "propInt64":
            v = api.as_int64(value)
            return self.impl.set_prop_int64(v)
        elif path == "propFloat":
            v = api.as_float(value)
            return self.impl.set_prop_float(v)
        elif path == "propFloat32":
            v = api.as_float32(value)
            return self.impl.set_prop_float32(v)
        elif path == "propFloat64":
            v = api.as_float64(value)
            return self.impl.set_prop_float64(v)
        elif path == "propString":
            v = api.as_string(value)
            return self.impl.set_prop_string(v)
        logging.info("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        if path == "funcBool":
            param_bool = api.as_bool(args[0])
            reply = self.impl.func_bool(param_bool)
            return api.from_bool(reply)
        elif path == "funcInt":
            param_int = api.as_int(args[0])
            reply = self.impl.func_int(param_int)
            return api.from_int(reply)
        elif path == "funcInt32":
            param_int32 = api.as_int32(args[0])
            reply = self.impl.func_int32(param_int32)
            return api.from_int32(reply)
        elif path == "funcInt64":
            param_int64 = api.as_int64(args[0])
            reply = self.impl.func_int64(param_int64)
            return api.from_int64(reply)
        elif path == "funcFloat":
            param_float = api.as_float(args[0])
            reply = self.impl.func_float(param_float)
            return api.from_float(reply)
        elif path == "funcFloat32":
            param_float32 = api.as_float32(args[0])
            reply = self.impl.func_float32(param_float32)
            return api.from_float32(reply)
        elif path == "funcFloat64":
            param_float = api.as_float64(args[0])
            reply = self.impl.func_float64(param_float)
            return api.from_float64(reply)
        elif path == "funcString":
            param_string = api.as_string(args[0])
            reply = self.impl.func_string(param_string)
            return api.from_string(reply)      
        logging.info("unknown operation: %s", name)

    def olink_linked(self, name: str, node: "RemoteNode"):
        print('linked')

    def olink_collect_properties(self) -> object:
        props = {}
        v = self.impl.get_prop_bool()
        props["propBool"] = api.from_bool(v)
        v = self.impl.get_prop_int()
        props["propInt"] = api.from_int(v)
        v = self.impl.get_prop_int32()
        props["propInt32"] = api.from_int32(v)
        v = self.impl.get_prop_int64()
        props["propInt64"] = api.from_int64(v)
        v = self.impl.get_prop_float()
        props["propFloat"] = api.from_float(v)
        v = self.impl.get_prop_float32()
        props["propFloat32"] = api.from_float32(v)
        v = self.impl.get_prop_float64()
        props["propFloat64"] = api.from_float64(v)
        v = self.impl.get_prop_string()
        props["propString"] = api.from_string(v)
        return props

    def notify_signal(self, symbol, args):
        path = Name.path_from_name(symbol)
        if path == "sigBool":
            param_bool = api.from_bool(args[0])
            return RemoteNode.notify_signal(symbol, [param_bool])
        elif path == "sigInt":
            param_int = api.from_int(args[0])
            return RemoteNode.notify_signal(symbol, [param_int])
        elif path == "sigInt32":
            param_int32 = api.from_int32(args[0])
            return RemoteNode.notify_signal(symbol, [param_int32])
        elif path == "sigInt64":
            param_int64 = api.from_int64(args[0])
            return RemoteNode.notify_signal(symbol, [param_int64])
        elif path == "sigFloat":
            param_float = api.from_float(args[0])
            return RemoteNode.notify_signal(symbol, [param_float])
        elif path == "sigFloat32":
            param_float32 = api.from_float32(args[0])
            return RemoteNode.notify_signal(symbol, [param_float32])
        elif path == "sigFloat64":
            param_float64 = api.from_float64(args[0])
            return RemoteNode.notify_signal(symbol, [param_float64])
        elif path == "sigString":
            param_string = api.from_string(args[0])
            return RemoteNode.notify_signal(symbol, [param_string])
        logging.info("unknown signal %s", symbol)

    def notify_property(self, symbol, value):
        path = Name.path_from_name(symbol)
        if path == "propBool":
            v = api.from_bool(value)
            return RemoteNode.notify_property_change(symbol, v)
        elif path == "propInt":
            v = api.from_int(value)
            return RemoteNode.notify_property_change(symbol, v)
        elif path == "propInt32":
            v = api.from_int32(value)
            return RemoteNode.notify_property_change(symbol, v)
        elif path == "propInt64":
            v = api.from_int64(value)
            return RemoteNode.notify_property_change(symbol, v)
        elif path == "propFloat":
            v = api.from_float(value)
            return RemoteNode.notify_property_change(symbol, v)
        elif path == "propFloat32":
            v = api.from_float32(value)
            return RemoteNode.notify_property_change(symbol, v)
        elif path == "propFloat64":
            v = api.from_float64(value)
            return RemoteNode.notify_property_change(symbol, v)
        elif path == "propString":
            v = api.from_string(value)
            return RemoteNode.notify_property_change(symbol, v)
        logging.info("unknown property %s", symbol)
class NoPropertiesInterfaceSource(IObjectSource):
    impl: api.INoPropertiesInterface
    def __init__(self, impl: api.INoPropertiesInterface):
        self.impl = impl
        impl._notifier = self
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "tb.simple.NoPropertiesInterface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        logging.info("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        if path == "funcVoid":
            reply = self.impl.func_void()
            return None
        elif path == "funcBool":
            param_bool = api.as_bool(args[0])
            reply = self.impl.func_bool(param_bool)
            return api.from_bool(reply)      
        logging.info("unknown operation: %s", name)

    def olink_linked(self, name: str, node: "RemoteNode"):
        print('linked')

    def olink_collect_properties(self) -> object:
        props = {}
        return props

    def notify_signal(self, symbol, args):
        path = Name.path_from_name(symbol)
        if path == "sigVoid":
            return RemoteNode.notify_signal(symbol, [])
        elif path == "sigBool":
            param_bool = api.from_bool(args[0])
            return RemoteNode.notify_signal(symbol, [param_bool])
        logging.info("unknown signal %s", symbol)

    def notify_property(self, symbol, value):
        path = Name.path_from_name(symbol)
        logging.info("unknown property %s", symbol)
class NoOperationsInterfaceSource(IObjectSource):
    impl: api.INoOperationsInterface
    def __init__(self, impl: api.INoOperationsInterface):
        self.impl = impl
        impl._notifier = self
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "tb.simple.NoOperationsInterface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        if path == "propBool":
            v = api.as_bool(value)
            return self.impl.set_prop_bool(v)
        elif path == "propInt":
            v = api.as_int(value)
            return self.impl.set_prop_int(v)
        logging.info("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)      
        logging.info("unknown operation: %s", name)

    def olink_linked(self, name: str, node: "RemoteNode"):
        print('linked')

    def olink_collect_properties(self) -> object:
        props = {}
        v = self.impl.get_prop_bool()
        props["propBool"] = api.from_bool(v)
        v = self.impl.get_prop_int()
        props["propInt"] = api.from_int(v)
        return props

    def notify_signal(self, symbol, args):
        path = Name.path_from_name(symbol)
        if path == "sigVoid":
            return RemoteNode.notify_signal(symbol, [])
        elif path == "sigBool":
            param_bool = api.from_bool(args[0])
            return RemoteNode.notify_signal(symbol, [param_bool])
        logging.info("unknown signal %s", symbol)

    def notify_property(self, symbol, value):
        path = Name.path_from_name(symbol)
        if path == "propBool":
            v = api.from_bool(value)
            return RemoteNode.notify_property_change(symbol, v)
        elif path == "propInt":
            v = api.from_int(value)
            return RemoteNode.notify_property_change(symbol, v)
        logging.info("unknown property %s", symbol)
class NoSignalsInterfaceSource(IObjectSource):
    impl: api.INoSignalsInterface
    def __init__(self, impl: api.INoSignalsInterface):
        self.impl = impl
        impl._notifier = self
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "tb.simple.NoSignalsInterface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        if path == "propBool":
            v = api.as_bool(value)
            return self.impl.set_prop_bool(v)
        elif path == "propInt":
            v = api.as_int(value)
            return self.impl.set_prop_int(v)
        logging.info("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        if path == "funcVoid":
            reply = self.impl.func_void()
            return None
        elif path == "funcBool":
            param_bool = api.as_bool(args[0])
            reply = self.impl.func_bool(param_bool)
            return api.from_bool(reply)      
        logging.info("unknown operation: %s", name)

    def olink_linked(self, name: str, node: "RemoteNode"):
        print('linked')

    def olink_collect_properties(self) -> object:
        props = {}
        v = self.impl.get_prop_bool()
        props["propBool"] = api.from_bool(v)
        v = self.impl.get_prop_int()
        props["propInt"] = api.from_int(v)
        return props

    def notify_signal(self, symbol, args):
        path = Name.path_from_name(symbol)
        logging.info("unknown signal %s", symbol)

    def notify_property(self, symbol, value):
        path = Name.path_from_name(symbol)
        if path == "propBool":
            v = api.from_bool(value)
            return RemoteNode.notify_property_change(symbol, v)
        elif path == "propInt":
            v = api.from_int(value)
            return RemoteNode.notify_property_change(symbol, v)
        logging.info("unknown property %s", symbol)
class EmptyInterfaceSource(IObjectSource):
    impl: api.IEmptyInterface
    def __init__(self, impl: api.IEmptyInterface):
        self.impl = impl
        impl._notifier = self
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "tb.simple.EmptyInterface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        logging.info("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)      
        logging.info("unknown operation: %s", name)

    def olink_linked(self, name: str, node: "RemoteNode"):
        print('linked')

    def olink_collect_properties(self) -> object:
        props = {}
        return props

    def notify_signal(self, symbol, args):
        path = Name.path_from_name(symbol)
        logging.info("unknown signal %s", symbol)

    def notify_property(self, symbol, value):
        path = Name.path_from_name(symbol)
        logging.info("unknown property %s", symbol)