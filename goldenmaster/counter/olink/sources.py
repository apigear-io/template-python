from olink.core import Name
from olink.remote import IObjectSource, RemoteNode
import utils.base_types
import counter.api
from utils.eventhook import EventHook
from typing import Any
import logging
import custom_types.api
import extern_types.api
import vector3d.vector
class CounterSource(IObjectSource):
    impl: counter.api.ICounter
    def __init__(self, impl: counter.api.ICounter):
        self.impl = impl
        impl.on_vector_changed += self.notify_vector_changed
        impl.on_extern_vector_changed += self.notify_extern_vector_changed
        self._on_linked = EventHook()
        self._on_unlinked = EventHook()
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "counter.Counter"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        if path == "vector":
            v = custom_types.api.as_vector3_d(value)
            return self.impl.set_vector(v)
        elif path == "extern_vector":
            v = extern_types.api.as_vector3d_vector_vector(value)
            return self.impl.set_extern_vector(v)
        logging.error("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        if path == "increment":
            vec = extern_types.api.as_vector3d_vector_vector(args[0])
            reply = self.impl.increment(vec)
            return extern_types.api.from_vector3d_vector_vector(reply)
        elif path == "decrement":
            vec = custom_types.api.as_vector3_d(args[0])
            reply = self.impl.decrement(vec)
            return custom_types.api.from_vector3_d(reply)      
        logging.error("unknown operation: %s", name)

    def olink_linked(self, name: str, node: "RemoteNode"):
        logging.info("linked: %s", name)
        self._on_linked.fire(name)

    def olink_unlinked(self, name: str, node: "RemoteNode"):
        logging.info("unlinked: %s", name)
        self._on_unlinked.fire(name)

    def olink_collect_properties(self) -> object:
        props = {}
        v = self.impl.get_vector()
        props["vector"] = custom_types.api.from_vector3_d(v)
        v = self.impl.get_extern_vector()
        props["extern_vector"] = extern_types.api.from_vector3d_vector_vector(v)
        return props

    def notify_vector_changed(self, value):
        v = custom_types.api.from_vector3_d(value)
        return RemoteNode.notify_property_change("counter.Counter/vector", v)

    def notify_extern_vector_changed(self, value):
        v = extern_types.api.from_vector3d_vector_vector(value)
        return RemoteNode.notify_property_change("counter.Counter/extern_vector", v)
