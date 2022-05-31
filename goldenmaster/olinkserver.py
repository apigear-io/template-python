import asyncio
from typing import Any
from asyncio.queues import Queue
from starlette.applications import Starlette
from starlette.endpoints import WebSocketEndpoint
from starlette.routing import WebSocketRoute
from starlette.websockets import WebSocket

from olink.remotenode import RemoteNode
import org_objectapi_testbed.olink.sources as sources
import org_objectapi_testbed.olink.services as services

# Interface1 service registration
sources.Interface1Source(services.Interface1Service())

# Interface2 service registration
sources.Interface2Source(services.Interface2Service())


class RemoteEndpoint(WebSocketEndpoint):
    encoding = "text"
    node = RemoteNode()
    queue = Queue()

    async def sender(self, ws):
        print('start sender')
        while True:
            msg = await self.queue.get()
            print('send', msg)
            await ws.send_text(msg)
            self.queue.task_done()        

    async def on_connect(self, ws: WebSocket):
        print('on_connect')
        asyncio.create_task(self.sender(ws))

        def writer(msg: str):
            print('queue', msg)
            self.queue.put_nowait(msg)
        self.node.on_write(writer)
        await super().on_connect(ws)


    async def on_receive(self, ws: WebSocket, data: Any) -> None:
        print('on_receive', data)
        self.node.handle_message(data)

    async def on_disconnect(self, websocket: WebSocket, close_code: int) -> None:
        await super().on_disconnect(websocket, close_code)
        self.node.on_write(None)
        await self.queue.join()


routes = [
    WebSocketRoute("/ws", RemoteEndpoint)
]

app = Starlette(routes=routes)

