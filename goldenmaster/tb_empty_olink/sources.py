from olink.core import Name
from olink.remote import IObjectSource, RemoteNode
from tb_empty_api import api
from typing import Any
import logging
class EmptyInterfaceSource(IObjectSource):
    impl: api.IEmptyInterface
    def __init__(self, impl: api.IEmptyInterface):
        self.impl = impl
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

    def olink_collect_properties(self) -> object:
        props = {}
        return props
