from olink.core import Name
from olink.remote import IObjectSource, RemoteNode
import utils.base_types
import tb_names.api
from utils.eventhook import EventHook
from typing import Any
import logging
class NamEsSource(IObjectSource):
    impl: tb_names.api.INamEs
    def __init__(self, impl: tb_names.api.INamEs):
        self.impl = impl
        impl.on_switch_changed += self.notify_switch_changed
        impl.on_some_property_changed += self.notify_some_property_changed
        impl.on_some_poperty2_changed += self.notify_some_poperty2_changed
        impl.on_some_signal += self.notify_some_signal
        impl.on_some_signal2 += self.notify_some_signal2
        self._on_linked = EventHook()
        self._on_unlinked = EventHook()
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "tb.names.Nam_Es"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        if path == "Switch":
            v = utils.base_types.as_bool(value)
            return self.impl.set_switch(v)
        elif path == "SOME_PROPERTY":
            v = utils.base_types.as_int(value)
            return self.impl.set_some_property(v)
        elif path == "Some_Poperty2":
            v = utils.base_types.as_int(value)
            return self.impl.set_some_poperty2(v)
        logging.error("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        if path == "SOME_FUNCTION":
            some_param = utils.base_types.as_bool(args[0])
            reply = self.impl.some_function(some_param)
            return utils.base_types.from_int(0)
        elif path == "Some_Function2":
            some_param = utils.base_types.as_bool(args[0])
            reply = self.impl.some_function2(some_param)
            return utils.base_types.from_int(0)      
        logging.error("unknown operation: %s", name)

    def olink_linked(self, name: str, node: "RemoteNode"):
        logging.info("linked: %s", name)
        self._on_linked.fire(name)

    def olink_unlinked(self, name: str, node: "RemoteNode"):
        logging.info("unlinked: %s", name)
        self._on_unlinked.fire(name)

    def olink_collect_properties(self) -> object:
        props = {}
        v = self.impl.get_switch()
        props["Switch"] = utils.base_types.from_bool(v)
        v = self.impl.get_some_property()
        props["SOME_PROPERTY"] = utils.base_types.from_int(v)
        v = self.impl.get_some_poperty2()
        props["Some_Poperty2"] = utils.base_types.from_int(v)
        return props

    def notify_some_signal(self, some_param: bool):
        _some_param = utils.base_types.from_bool(some_param)
        return RemoteNode.notify_signal("tb.names.Nam_Es/SOME_SIGNAL", [_some_param])

    def notify_some_signal2(self, some_param: bool):
        _some_param = utils.base_types.from_bool(some_param)
        return RemoteNode.notify_signal("tb.names.Nam_Es/Some_Signal2", [_some_param])

    def notify_switch_changed(self, value):
        v = utils.base_types.from_bool(value)
        return RemoteNode.notify_property_change("tb.names.Nam_Es/Switch", v)

    def notify_some_property_changed(self, value):
        v = utils.base_types.from_int(value)
        return RemoteNode.notify_property_change("tb.names.Nam_Es/SOME_PROPERTY", v)

    def notify_some_poperty2_changed(self, value):
        v = utils.base_types.from_int(value)
        return RemoteNode.notify_property_change("tb.names.Nam_Es/Some_Poperty2", v)
