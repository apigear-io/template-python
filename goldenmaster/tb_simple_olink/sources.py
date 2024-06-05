from olink.core import Name
from olink.remote import IObjectSource, RemoteNode
import utils.base_types
import tb_simple_api
from utils.eventhook import EventHook
from typing import Any
import logging
class SimpleInterfaceSource(IObjectSource):
    impl: tb_simple_api.ISimpleInterface
    def __init__(self, impl: tb_simple_api.ISimpleInterface):
        self.impl = impl
        impl.on_prop_bool_changed += self.notify_prop_bool_changed
        impl.on_prop_int_changed += self.notify_prop_int_changed
        impl.on_prop_int32_changed += self.notify_prop_int32_changed
        impl.on_prop_int64_changed += self.notify_prop_int64_changed
        impl.on_prop_float_changed += self.notify_prop_float_changed
        impl.on_prop_float32_changed += self.notify_prop_float32_changed
        impl.on_prop_float64_changed += self.notify_prop_float64_changed
        impl.on_prop_string_changed += self.notify_prop_string_changed
        impl.on_prop_read_only_string_changed += self.notify_prop_read_only_string_changed
        impl.on_sig_void += self.notify_sig_void
        impl.on_sig_bool += self.notify_sig_bool
        impl.on_sig_int += self.notify_sig_int
        impl.on_sig_int32 += self.notify_sig_int32
        impl.on_sig_int64 += self.notify_sig_int64
        impl.on_sig_float += self.notify_sig_float
        impl.on_sig_float32 += self.notify_sig_float32
        impl.on_sig_float64 += self.notify_sig_float64
        impl.on_sig_string += self.notify_sig_string
        self._on_linked = EventHook()
        self._on_unlinked = EventHook()
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "tb.simple.SimpleInterface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        if path == "propBool":
            v = utils.base_types.as_bool(value)
            return self.impl.set_prop_bool(v)
        elif path == "propInt":
            v = utils.base_types.as_int(value)
            return self.impl.set_prop_int(v)
        elif path == "propInt32":
            v = utils.base_types.as_int32(value)
            return self.impl.set_prop_int32(v)
        elif path == "propInt64":
            v = utils.base_types.as_int64(value)
            return self.impl.set_prop_int64(v)
        elif path == "propFloat":
            v = utils.base_types.as_float(value)
            return self.impl.set_prop_float(v)
        elif path == "propFloat32":
            v = utils.base_types.as_float32(value)
            return self.impl.set_prop_float32(v)
        elif path == "propFloat64":
            v = utils.base_types.as_float64(value)
            return self.impl.set_prop_float64(v)
        elif path == "propString":
            v = utils.base_types.as_string(value)
            return self.impl.set_prop_string(v)
        elif path == "propReadOnlyString":
            pass
        logging.error("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        if path == "funcVoid":
            reply = self.impl.func_void()
            return None
        elif path == "funcBool":
            param_bool = utils.base_types.as_bool(args[0])
            reply = self.impl.func_bool(param_bool)
            return utils.base_types.from_bool(reply)
        elif path == "funcInt":
            param_int = utils.base_types.as_int(args[0])
            reply = self.impl.func_int(param_int)
            return utils.base_types.from_int(reply)
        elif path == "funcInt32":
            param_int32 = utils.base_types.as_int32(args[0])
            reply = self.impl.func_int32(param_int32)
            return utils.base_types.from_int32(reply)
        elif path == "funcInt64":
            param_int64 = utils.base_types.as_int64(args[0])
            reply = self.impl.func_int64(param_int64)
            return utils.base_types.from_int64(reply)
        elif path == "funcFloat":
            param_float = utils.base_types.as_float(args[0])
            reply = self.impl.func_float(param_float)
            return utils.base_types.from_float(reply)
        elif path == "funcFloat32":
            param_float32 = utils.base_types.as_float32(args[0])
            reply = self.impl.func_float32(param_float32)
            return utils.base_types.from_float32(reply)
        elif path == "funcFloat64":
            param_float = utils.base_types.as_float64(args[0])
            reply = self.impl.func_float64(param_float)
            return utils.base_types.from_float64(reply)
        elif path == "funcString":
            param_string = utils.base_types.as_string(args[0])
            reply = self.impl.func_string(param_string)
            return utils.base_types.from_string(reply)      
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
        props["propBool"] = utils.base_types.from_bool(v)
        v = self.impl.get_prop_int()
        props["propInt"] = utils.base_types.from_int(v)
        v = self.impl.get_prop_int32()
        props["propInt32"] = utils.base_types.from_int32(v)
        v = self.impl.get_prop_int64()
        props["propInt64"] = utils.base_types.from_int64(v)
        v = self.impl.get_prop_float()
        props["propFloat"] = utils.base_types.from_float(v)
        v = self.impl.get_prop_float32()
        props["propFloat32"] = utils.base_types.from_float32(v)
        v = self.impl.get_prop_float64()
        props["propFloat64"] = utils.base_types.from_float64(v)
        v = self.impl.get_prop_string()
        props["propString"] = utils.base_types.from_string(v)
        v = self.impl.get_prop_read_only_string()
        props["propReadOnlyString"] = utils.base_types.from_string(v)
        return props

    def notify_sig_void(self):
        return RemoteNode.notify_signal("tb.simple.SimpleInterface/sigVoid", [])

    def notify_sig_bool(self, param_bool: bool):
        _param_bool = utils.base_types.from_bool(param_bool)
        return RemoteNode.notify_signal("tb.simple.SimpleInterface/sigBool", [_param_bool])

    def notify_sig_int(self, param_int: int):
        _param_int = utils.base_types.from_int(param_int)
        return RemoteNode.notify_signal("tb.simple.SimpleInterface/sigInt", [_param_int])

    def notify_sig_int32(self, param_int32: int):
        _param_int32 = utils.base_types.from_int32(param_int32)
        return RemoteNode.notify_signal("tb.simple.SimpleInterface/sigInt32", [_param_int32])

    def notify_sig_int64(self, param_int64: int):
        _param_int64 = utils.base_types.from_int64(param_int64)
        return RemoteNode.notify_signal("tb.simple.SimpleInterface/sigInt64", [_param_int64])

    def notify_sig_float(self, param_float: float):
        _param_float = utils.base_types.from_float(param_float)
        return RemoteNode.notify_signal("tb.simple.SimpleInterface/sigFloat", [_param_float])

    def notify_sig_float32(self, param_float32: float):
        _param_float32 = utils.base_types.from_float32(param_float32)
        return RemoteNode.notify_signal("tb.simple.SimpleInterface/sigFloat32", [_param_float32])

    def notify_sig_float64(self, param_float64: float):
        _param_float64 = utils.base_types.from_float64(param_float64)
        return RemoteNode.notify_signal("tb.simple.SimpleInterface/sigFloat64", [_param_float64])

    def notify_sig_string(self, param_string: str):
        _param_string = utils.base_types.from_string(param_string)
        return RemoteNode.notify_signal("tb.simple.SimpleInterface/sigString", [_param_string])

    def notify_prop_bool_changed(self, value):
        v = utils.base_types.from_bool(value)
        return RemoteNode.notify_property_change("tb.simple.SimpleInterface/propBool", v)

    def notify_prop_int_changed(self, value):
        v = utils.base_types.from_int(value)
        return RemoteNode.notify_property_change("tb.simple.SimpleInterface/propInt", v)

    def notify_prop_int32_changed(self, value):
        v = utils.base_types.from_int32(value)
        return RemoteNode.notify_property_change("tb.simple.SimpleInterface/propInt32", v)

    def notify_prop_int64_changed(self, value):
        v = utils.base_types.from_int64(value)
        return RemoteNode.notify_property_change("tb.simple.SimpleInterface/propInt64", v)

    def notify_prop_float_changed(self, value):
        v = utils.base_types.from_float(value)
        return RemoteNode.notify_property_change("tb.simple.SimpleInterface/propFloat", v)

    def notify_prop_float32_changed(self, value):
        v = utils.base_types.from_float32(value)
        return RemoteNode.notify_property_change("tb.simple.SimpleInterface/propFloat32", v)

    def notify_prop_float64_changed(self, value):
        v = utils.base_types.from_float64(value)
        return RemoteNode.notify_property_change("tb.simple.SimpleInterface/propFloat64", v)

    def notify_prop_string_changed(self, value):
        v = utils.base_types.from_string(value)
        return RemoteNode.notify_property_change("tb.simple.SimpleInterface/propString", v)

    def notify_prop_read_only_string_changed(self, value):
        v = utils.base_types.from_string(value)
        return RemoteNode.notify_property_change("tb.simple.SimpleInterface/propReadOnlyString", v)
class SimpleArrayInterfaceSource(IObjectSource):
    impl: tb_simple_api.ISimpleArrayInterface
    def __init__(self, impl: tb_simple_api.ISimpleArrayInterface):
        self.impl = impl
        impl.on_prop_bool_changed += self.notify_prop_bool_changed
        impl.on_prop_int_changed += self.notify_prop_int_changed
        impl.on_prop_int32_changed += self.notify_prop_int32_changed
        impl.on_prop_int64_changed += self.notify_prop_int64_changed
        impl.on_prop_float_changed += self.notify_prop_float_changed
        impl.on_prop_float32_changed += self.notify_prop_float32_changed
        impl.on_prop_float64_changed += self.notify_prop_float64_changed
        impl.on_prop_string_changed += self.notify_prop_string_changed
        impl.on_sig_bool += self.notify_sig_bool
        impl.on_sig_int += self.notify_sig_int
        impl.on_sig_int32 += self.notify_sig_int32
        impl.on_sig_int64 += self.notify_sig_int64
        impl.on_sig_float += self.notify_sig_float
        impl.on_sig_float32 += self.notify_sig_float32
        impl.on_sig_float64 += self.notify_sig_float64
        impl.on_sig_string += self.notify_sig_string
        self._on_linked = EventHook()
        self._on_unlinked = EventHook()
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "tb.simple.SimpleArrayInterface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        if path == "propBool":
            v = [utils.base_types.as_bool(_) for _ in value]
            return self.impl.set_prop_bool(v)
        elif path == "propInt":
            v = [utils.base_types.as_int(_) for _ in value]
            return self.impl.set_prop_int(v)
        elif path == "propInt32":
            v = [utils.base_types.as_int32(_) for _ in value]
            return self.impl.set_prop_int32(v)
        elif path == "propInt64":
            v = [utils.base_types.as_int64(_) for _ in value]
            return self.impl.set_prop_int64(v)
        elif path == "propFloat":
            v = [utils.base_types.as_float(_) for _ in value]
            return self.impl.set_prop_float(v)
        elif path == "propFloat32":
            v = [utils.base_types.as_float32(_) for _ in value]
            return self.impl.set_prop_float32(v)
        elif path == "propFloat64":
            v = [utils.base_types.as_float64(_) for _ in value]
            return self.impl.set_prop_float64(v)
        elif path == "propString":
            v = [utils.base_types.as_string(_) for _ in value]
            return self.impl.set_prop_string(v)
        logging.error("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        if path == "funcBool":
            param_bool = [utils.base_types.as_bool(_) for _ in args[0]]
            reply = self.impl.func_bool(param_bool)
            return [utils.base_types.from_bool(_) for _ in reply]
        elif path == "funcInt":
            param_int = [utils.base_types.as_int(_) for _ in args[0]]
            reply = self.impl.func_int(param_int)
            return [utils.base_types.from_int(_) for _ in reply]
        elif path == "funcInt32":
            param_int32 = [utils.base_types.as_int32(_) for _ in args[0]]
            reply = self.impl.func_int32(param_int32)
            return [utils.base_types.from_int32(_) for _ in reply]
        elif path == "funcInt64":
            param_int64 = [utils.base_types.as_int64(_) for _ in args[0]]
            reply = self.impl.func_int64(param_int64)
            return [utils.base_types.from_int64(_) for _ in reply]
        elif path == "funcFloat":
            param_float = [utils.base_types.as_float(_) for _ in args[0]]
            reply = self.impl.func_float(param_float)
            return [utils.base_types.from_float(_) for _ in reply]
        elif path == "funcFloat32":
            param_float32 = [utils.base_types.as_float32(_) for _ in args[0]]
            reply = self.impl.func_float32(param_float32)
            return [utils.base_types.from_float32(_) for _ in reply]
        elif path == "funcFloat64":
            param_float = [utils.base_types.as_float64(_) for _ in args[0]]
            reply = self.impl.func_float64(param_float)
            return [utils.base_types.from_float64(_) for _ in reply]
        elif path == "funcString":
            param_string = [utils.base_types.as_string(_) for _ in args[0]]
            reply = self.impl.func_string(param_string)
            return [utils.base_types.from_string(_) for _ in reply]      
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
        props["propBool"] = [utils.base_types.from_bool(_) for _ in v]
        v = self.impl.get_prop_int()
        props["propInt"] = [utils.base_types.from_int(_) for _ in v]
        v = self.impl.get_prop_int32()
        props["propInt32"] = [utils.base_types.from_int32(_) for _ in v]
        v = self.impl.get_prop_int64()
        props["propInt64"] = [utils.base_types.from_int64(_) for _ in v]
        v = self.impl.get_prop_float()
        props["propFloat"] = [utils.base_types.from_float(_) for _ in v]
        v = self.impl.get_prop_float32()
        props["propFloat32"] = [utils.base_types.from_float32(_) for _ in v]
        v = self.impl.get_prop_float64()
        props["propFloat64"] = [utils.base_types.from_float64(_) for _ in v]
        v = self.impl.get_prop_string()
        props["propString"] = [utils.base_types.from_string(_) for _ in v]
        return props

    def notify_sig_bool(self, param_bool: list[bool]):
        _param_bool = [utils.base_types.api.from_bool(_) for _ in param_bool]
        return RemoteNode.notify_signal("tb.simple.SimpleArrayInterface/sigBool", [_param_bool])

    def notify_sig_int(self, param_int: list[int]):
        _param_int = [utils.base_types.api.from_int(_) for _ in param_int]
        return RemoteNode.notify_signal("tb.simple.SimpleArrayInterface/sigInt", [_param_int])

    def notify_sig_int32(self, param_int32: list[int]):
        _param_int32 = [utils.base_types.api.from_int32(_) for _ in param_int32]
        return RemoteNode.notify_signal("tb.simple.SimpleArrayInterface/sigInt32", [_param_int32])

    def notify_sig_int64(self, param_int64: list[int]):
        _param_int64 = [utils.base_types.api.from_int64(_) for _ in param_int64]
        return RemoteNode.notify_signal("tb.simple.SimpleArrayInterface/sigInt64", [_param_int64])

    def notify_sig_float(self, param_float: list[float]):
        _param_float = [utils.base_types.api.from_float(_) for _ in param_float]
        return RemoteNode.notify_signal("tb.simple.SimpleArrayInterface/sigFloat", [_param_float])

    def notify_sig_float32(self, param_float32: list[float]):
        _param_float32 = [utils.base_types.api.from_float32(_) for _ in param_float32]
        return RemoteNode.notify_signal("tb.simple.SimpleArrayInterface/sigFloat32", [_param_float32])

    def notify_sig_float64(self, param_float64: list[float]):
        _param_float64 = [utils.base_types.api.from_float64(_) for _ in param_float64]
        return RemoteNode.notify_signal("tb.simple.SimpleArrayInterface/sigFloat64", [_param_float64])

    def notify_sig_string(self, param_string: list[str]):
        _param_string = [utils.base_types.api.from_string(_) for _ in param_string]
        return RemoteNode.notify_signal("tb.simple.SimpleArrayInterface/sigString", [_param_string])

    def notify_prop_bool_changed(self, value):
        v = [utils.base_types.from_bool(_) for _ in value]
        return RemoteNode.notify_property_change("tb.simple.SimpleArrayInterface/propBool", v)

    def notify_prop_int_changed(self, value):
        v = [utils.base_types.from_int(_) for _ in value]
        return RemoteNode.notify_property_change("tb.simple.SimpleArrayInterface/propInt", v)

    def notify_prop_int32_changed(self, value):
        v = [utils.base_types.from_int32(_) for _ in value]
        return RemoteNode.notify_property_change("tb.simple.SimpleArrayInterface/propInt32", v)

    def notify_prop_int64_changed(self, value):
        v = [utils.base_types.from_int64(_) for _ in value]
        return RemoteNode.notify_property_change("tb.simple.SimpleArrayInterface/propInt64", v)

    def notify_prop_float_changed(self, value):
        v = [utils.base_types.from_float(_) for _ in value]
        return RemoteNode.notify_property_change("tb.simple.SimpleArrayInterface/propFloat", v)

    def notify_prop_float32_changed(self, value):
        v = [utils.base_types.from_float32(_) for _ in value]
        return RemoteNode.notify_property_change("tb.simple.SimpleArrayInterface/propFloat32", v)

    def notify_prop_float64_changed(self, value):
        v = [utils.base_types.from_float64(_) for _ in value]
        return RemoteNode.notify_property_change("tb.simple.SimpleArrayInterface/propFloat64", v)

    def notify_prop_string_changed(self, value):
        v = [utils.base_types.from_string(_) for _ in value]
        return RemoteNode.notify_property_change("tb.simple.SimpleArrayInterface/propString", v)
class NoPropertiesInterfaceSource(IObjectSource):
    impl: tb_simple_api.INoPropertiesInterface
    def __init__(self, impl: tb_simple_api.INoPropertiesInterface):
        self.impl = impl
        impl.on_sig_void += self.notify_sig_void
        impl.on_sig_bool += self.notify_sig_bool
        self._on_linked = EventHook()
        self._on_unlinked = EventHook()
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "tb.simple.NoPropertiesInterface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        logging.error("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        if path == "funcVoid":
            reply = self.impl.func_void()
            return None
        elif path == "funcBool":
            param_bool = utils.base_types.as_bool(args[0])
            reply = self.impl.func_bool(param_bool)
            return utils.base_types.from_bool(reply)      
        logging.error("unknown operation: %s", name)

    def olink_linked(self, name: str, node: "RemoteNode"):
        logging.info("linked: %s", name)
        self._on_linked.fire(name)

    def olink_unlinked(self, name: str, node: "RemoteNode"):
        logging.info("unlinked: %s", name)
        self._on_unlinked.fire(name)

    def olink_collect_properties(self) -> object:
        props = {}
        return props

    def notify_sig_void(self):
        return RemoteNode.notify_signal("tb.simple.NoPropertiesInterface/sigVoid", [])

    def notify_sig_bool(self, param_bool: bool):
        _param_bool = utils.base_types.from_bool(param_bool)
        return RemoteNode.notify_signal("tb.simple.NoPropertiesInterface/sigBool", [_param_bool])
class NoOperationsInterfaceSource(IObjectSource):
    impl: tb_simple_api.INoOperationsInterface
    def __init__(self, impl: tb_simple_api.INoOperationsInterface):
        self.impl = impl
        impl.on_prop_bool_changed += self.notify_prop_bool_changed
        impl.on_prop_int_changed += self.notify_prop_int_changed
        impl.on_sig_void += self.notify_sig_void
        impl.on_sig_bool += self.notify_sig_bool
        self._on_linked = EventHook()
        self._on_unlinked = EventHook()
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "tb.simple.NoOperationsInterface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        if path == "propBool":
            v = utils.base_types.as_bool(value)
            return self.impl.set_prop_bool(v)
        elif path == "propInt":
            v = utils.base_types.as_int(value)
            return self.impl.set_prop_int(v)
        logging.error("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)      
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
        props["propBool"] = utils.base_types.from_bool(v)
        v = self.impl.get_prop_int()
        props["propInt"] = utils.base_types.from_int(v)
        return props

    def notify_sig_void(self):
        return RemoteNode.notify_signal("tb.simple.NoOperationsInterface/sigVoid", [])

    def notify_sig_bool(self, param_bool: bool):
        _param_bool = utils.base_types.from_bool(param_bool)
        return RemoteNode.notify_signal("tb.simple.NoOperationsInterface/sigBool", [_param_bool])

    def notify_prop_bool_changed(self, value):
        v = utils.base_types.from_bool(value)
        return RemoteNode.notify_property_change("tb.simple.NoOperationsInterface/propBool", v)

    def notify_prop_int_changed(self, value):
        v = utils.base_types.from_int(value)
        return RemoteNode.notify_property_change("tb.simple.NoOperationsInterface/propInt", v)
class NoSignalsInterfaceSource(IObjectSource):
    impl: tb_simple_api.INoSignalsInterface
    def __init__(self, impl: tb_simple_api.INoSignalsInterface):
        self.impl = impl
        impl.on_prop_bool_changed += self.notify_prop_bool_changed
        impl.on_prop_int_changed += self.notify_prop_int_changed
        self._on_linked = EventHook()
        self._on_unlinked = EventHook()
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "tb.simple.NoSignalsInterface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        if path == "propBool":
            v = utils.base_types.as_bool(value)
            return self.impl.set_prop_bool(v)
        elif path == "propInt":
            v = utils.base_types.as_int(value)
            return self.impl.set_prop_int(v)
        logging.error("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        if path == "funcVoid":
            reply = self.impl.func_void()
            return None
        elif path == "funcBool":
            param_bool = utils.base_types.as_bool(args[0])
            reply = self.impl.func_bool(param_bool)
            return utils.base_types.from_bool(reply)      
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
        props["propBool"] = utils.base_types.from_bool(v)
        v = self.impl.get_prop_int()
        props["propInt"] = utils.base_types.from_int(v)
        return props

    def notify_prop_bool_changed(self, value):
        v = utils.base_types.from_bool(value)
        return RemoteNode.notify_property_change("tb.simple.NoSignalsInterface/propBool", v)

    def notify_prop_int_changed(self, value):
        v = utils.base_types.from_int(value)
        return RemoteNode.notify_property_change("tb.simple.NoSignalsInterface/propInt", v)
class EmptyInterfaceSource(IObjectSource):
    impl: tb_simple_api.IEmptyInterface
    def __init__(self, impl: tb_simple_api.IEmptyInterface):
        self.impl = impl
        self._on_linked = EventHook()
        self._on_unlinked = EventHook()
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "tb.simple.EmptyInterface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        logging.error("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)      
        logging.error("unknown operation: %s", name)

    def olink_linked(self, name: str, node: "RemoteNode"):
        logging.info("linked: %s", name)
        self._on_linked.fire(name)

    def olink_unlinked(self, name: str, node: "RemoteNode"):
        logging.info("unlinked: %s", name)
        self._on_unlinked.fire(name)

    def olink_collect_properties(self) -> object:
        props = {}
        return props
