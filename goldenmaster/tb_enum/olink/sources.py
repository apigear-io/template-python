from olink.core import Name
from olink.remote import IObjectSource, RemoteNode
import utils.base_types
import tb_enum.api
from utils.eventhook import EventHook
from typing import Any
import logging
class EnumInterfaceSource(IObjectSource):
    impl: tb_enum.api.IEnumInterface
    def __init__(self, impl: tb_enum.api.IEnumInterface):
        self.impl = impl
        impl.on_prop0_changed += self.notify_prop0_changed
        impl.on_prop1_changed += self.notify_prop1_changed
        impl.on_prop2_changed += self.notify_prop2_changed
        impl.on_prop3_changed += self.notify_prop3_changed
        impl.on_sig0 += self.notify_sig0
        impl.on_sig1 += self.notify_sig1
        impl.on_sig2 += self.notify_sig2
        impl.on_sig3 += self.notify_sig3
        self._on_linked = EventHook()
        self._on_unlinked = EventHook()
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "tb.enum.EnumInterface"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        if path == "prop0":
            v = tb_enum.api.as_enum0(value)
            return self.impl.set_prop0(v)
        elif path == "prop1":
            v = tb_enum.api.as_enum1(value)
            return self.impl.set_prop1(v)
        elif path == "prop2":
            v = tb_enum.api.as_enum2(value)
            return self.impl.set_prop2(v)
        elif path == "prop3":
            v = tb_enum.api.as_enum3(value)
            return self.impl.set_prop3(v)
        logging.error("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        if path == "func0":
            param0 = tb_enum.api.as_enum0(args[0])
            reply = self.impl.func0(param0)
            return tb_enum.api.from_enum0(reply)
        elif path == "func1":
            param1 = tb_enum.api.as_enum1(args[0])
            reply = self.impl.func1(param1)
            return tb_enum.api.from_enum1(reply)
        elif path == "func2":
            param2 = tb_enum.api.as_enum2(args[0])
            reply = self.impl.func2(param2)
            return tb_enum.api.from_enum2(reply)
        elif path == "func3":
            param3 = tb_enum.api.as_enum3(args[0])
            reply = self.impl.func3(param3)
            return tb_enum.api.from_enum3(reply)      
        logging.error("unknown operation: %s", name)

    def olink_linked(self, name: str, node: "RemoteNode"):
        logging.info("linked: %s", name)
        self._on_linked.fire(name)

    def olink_unlinked(self, name: str, node: "RemoteNode"):
        logging.info("unlinked: %s", name)
        self._on_unlinked.fire(name)

    def olink_collect_properties(self) -> object:
        props = {}
        v = self.impl.get_prop0()
        props["prop0"] = tb_enum.api.from_enum0(v)
        v = self.impl.get_prop1()
        props["prop1"] = tb_enum.api.from_enum1(v)
        v = self.impl.get_prop2()
        props["prop2"] = tb_enum.api.from_enum2(v)
        v = self.impl.get_prop3()
        props["prop3"] = tb_enum.api.from_enum3(v)
        return props

    def notify_sig0(self, param0: tb_enum.api.Enum0):
        _param0 = tb_enum.api.from_enum0(param0)
        return RemoteNode.notify_signal("tb.enum.EnumInterface/sig0", [_param0])

    def notify_sig1(self, param1: tb_enum.api.Enum1):
        _param1 = tb_enum.api.from_enum1(param1)
        return RemoteNode.notify_signal("tb.enum.EnumInterface/sig1", [_param1])

    def notify_sig2(self, param2: tb_enum.api.Enum2):
        _param2 = tb_enum.api.from_enum2(param2)
        return RemoteNode.notify_signal("tb.enum.EnumInterface/sig2", [_param2])

    def notify_sig3(self, param3: tb_enum.api.Enum3):
        _param3 = tb_enum.api.from_enum3(param3)
        return RemoteNode.notify_signal("tb.enum.EnumInterface/sig3", [_param3])

    def notify_prop0_changed(self, value):
        v = tb_enum.api.from_enum0(value)
        return RemoteNode.notify_property_change("tb.enum.EnumInterface/prop0", v)

    def notify_prop1_changed(self, value):
        v = tb_enum.api.from_enum1(value)
        return RemoteNode.notify_property_change("tb.enum.EnumInterface/prop1", v)

    def notify_prop2_changed(self, value):
        v = tb_enum.api.from_enum2(value)
        return RemoteNode.notify_property_change("tb.enum.EnumInterface/prop2", v)

    def notify_prop3_changed(self, value):
        v = tb_enum.api.from_enum3(value)
        return RemoteNode.notify_property_change("tb.enum.EnumInterface/prop3", v)
