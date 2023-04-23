import asyncio
from typing import Any
import logging
from asyncio.queues import Queue
from starlette.applications import Starlette
from starlette.endpoints import WebSocketEndpoint
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
    def __init__(self):
        self.encoding = "text"
        self.node = RemoteNode()
        self.queue = Queue()

    async def _sender(self, ws):
        logging.info("start sender")
        while True:
            msg = await self.queue.get()
            await ws.send_text(msg)
            self.queue.task_done()

    async def on_connect(self, ws: WebSocket):
        logging.info("on_connect")
        asyncio.create_task(self._sender(ws))

        def writer(msg: str):
            logging.info('queue %s', msg)
            self.queue.put_nowait(msg)
        self.node.on_writer(writer)
        await super().on_connect(ws)

    async def on_receive(self, ws: WebSocket, data: Any):
        logging.info('on_receive', data)
        self.node.handle_message(data)

    async def on_disconnect(self, ws: WebSocket, close_code: int):
        await super().on_disconnect(ws, close_code)
        self.node.on_write(None)
        await self.queue.join()
        

routes = [
    WebSocketRoute("/ws", RemoteEndpoint)
]


app = Starlette(routes=routes)
