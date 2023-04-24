import asyncio
from typing import Any
import logging
from asyncio.queues import Queue
from starlette.applications import Starlette
from starlette.endpoints import WebSocketEndpoint, Scope, Receive, Send
from starlette.routing import WebSocketRoute
from starlette.websockets import WebSocket

from olink.remotenode import RemoteNode

{{- range .System.Modules }}
{{- $import := printf "%s_olink" (snake .Name)}}
import {{$import}}
{{- end }}
{{ range .System.Modules }}
{{- $import := printf "%s_olink" (snake .Name)}}

{{- range .Interfaces }}
{{$import}}.{{Camel .Name}}Source({{$import}}.{{Camel .Name}}Service())
{{- end }}
{{ end }}


class RemoteEndpoint(WebSocketEndpoint):
    def __init__(self, scope: Scope, receive: Receive, send: Send):
        super().__init__(scope, receive, send)
        self.encoding = "text"
        self.node = RemoteNode()
        self.queue = Queue()

    async def _sender(self, ws):
        logging.info("start sender")
        while True:
            msg = await self.queue.get()
            logging.info("server send %s", msg)
            await ws.send_text(msg)
            self.queue.task_done()

    async def on_connect(self, ws: WebSocket):
        logging.info("server on connect")
        asyncio.create_task(self._sender(ws))

        def writer(msg: str):
            logging.info('queue %s', msg)
            self.queue.put_nowait(msg)
        self.node.on_write(writer)
        await super().on_connect(ws)

    async def on_receive(self, ws: WebSocket, data: Any):
        logging.info("server recv %s", data)
        self.node.handle_message(data)

    async def on_disconnect(self, ws: WebSocket, close_code: int):
        await super().on_disconnect(ws, close_code)
        logging.info("server disconnect")
        self.node.on_write(None)
        await self.queue.join()
        

logging.basicConfig(level=logging.INFO)

routes = [
    WebSocketRoute("/ws", RemoteEndpoint)
]


app = Starlette(routes=routes)
