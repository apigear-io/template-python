import asyncio
from typing import Any
from olink.core import Name
from olink.client import IObjectSink, ClientNode
from utils.eventhook import EventHook
import utils.base_types
import tb_empty.api
import logging

class EmptyInterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._on_is_ready= EventHook()
        self.client = ClientNode.register_sink(self)

    def olink_object_name(self):
        return 'tb.empty.EmptyInterface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        self._on_is_ready.fire()

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        logging.error("unknown signal: %s", name)
