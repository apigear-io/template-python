from olink.core import Name
from olink.remote import IObjectSource, RemoteNode
import utils.base_types
import tb_empty.api
from utils.eventhook import EventHook
from typing import Any
import logging
class EmptyInterfaceSource(IObjectSource):
    impl: tb_empty.api.IEmptyInterface
    def __init__(self, impl: tb_empty.api.IEmptyInterface):
        self.impl = impl
        self._on_linked = EventHook()
        self._on_unlinked = EventHook()
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "tb.empty.EmptyInterface"

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
