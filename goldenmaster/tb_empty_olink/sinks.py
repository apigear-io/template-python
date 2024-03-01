import asyncio
from typing import Any
from olink.core import Name
from olink.client import IObjectSink, ClientNode
from tb_empty_api.shared import EventHook
from tb_empty_api import api

class EmptyInterfaceSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote('tb.empty.EmptyInterface/EmptyInterface', args, func)
        return await asyncio.wait_for(future, 500)

    def olink_object_name(self):
        return 'tb.empty.EmptyInterface'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        pass

    def olink_on_signal(self, name: str, args: list[Any]):
        pass
