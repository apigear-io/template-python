import asyncio
from typing import Any
from olink.core.types import Name
from olink.clientnode import IObjectSink, ClientNode
from .shared import EventHook
from demo_api import api
class CounterSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self.value = 0
        self.on_property_changed = EventHook()
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote('demo.Counter/Counter', args, func)
        return await asyncio.wait_for(future, 500)
    async def increment(self):
        return await self._invoke("increment", [])
    async def decrement(self):
        return await self._invoke("decrement", [])

    def olink_object_name(self):
        return 'demo.Counter'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        for k in props:
            setattr(self, k, props[k])

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        setattr(self, path, value)
        self.on_property_changed.fire(path, value)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        hook = getattr(self, f'on_{path}')        
        hook.fire(*args)