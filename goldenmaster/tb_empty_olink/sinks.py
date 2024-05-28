import asyncio
from typing import Any
from olink.core import Name
from olink.client import IObjectSink, ClientNode
from utils.eventhook import EventHook
from tb_empty_api import api
import logging

class EmptyInterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._on_is_ready= EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args, no_wait=False):
        if no_wait:
            self.client.invoke_remote(f"tb.empty.EmptyInterface/{name}", args, func=None)
        else:
            future = asyncio.get_running_loop().create_future()
            def func(args):
                return future.set_result(args.value)
            self.client.invoke_remote(f"tb.empty.EmptyInterface/{name}", args, func)
            return await asyncio.wait_for(future, 500)

    def olink_object_name(self):
        return 'tb.empty.EmptyInterface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        self._on_is_ready.fire()

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        logging.error("unknown signal: %s", name)
