import asyncio
from typing import Any
import logging
from asyncio.queues import Queue
from starlette.applications import Starlette
from starlette.endpoints import WebSocketEndpoint, Scope, Receive, Send
from starlette.routing import WebSocketRoute
from starlette.websockets import WebSocket

from olink.remote import RemoteNode

{{- range .System.Modules }}
{{- $import_olink := printf "%s_olink" (snake .Name)}}
{{- $import_impl := printf "%s_impl" (snake .Name)}}

import {{$import_olink}}
import {{$import_impl}}

{{- end }}
{{ range .System.Modules }}
{{- $import_olink := printf "%s_olink" (snake .Name)}}
{{- $import_impl := printf "%s_impl" (snake .Name)}}

{{- range .Interfaces }}
{{$import_olink}}.{{Camel .Name}}Source({{$import_impl}}.{{Camel .Name}}())
{{- end }}
{{ end }}

# set default log level to INFO and above
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

class RemoteEndpoint(WebSocketEndpoint):
    def __init__(self, scope: Scope, receive: Receive, send: Send):
        super().__init__(scope, receive, send)
        self.encoding = "text"
        self.node = RemoteNode()
        self.node.on_log(self._olink_log_writer)
        self.queue = Queue()

    def _olink_log_writer(self, level, msg):
        if level[0] == 1:
            logging.debug(msg)
        elif level[0] == 2:
            logging.info(msg)
        elif level[0] == 3:
            logging.warning(msg)
        else:
            logging.error(msg)

    async def _sender(self, ws):
        logging.info("start sender")
        while True:
            msg = await self.queue.get()
            logging.debug("server send %s", msg)
            await ws.send_text(msg)
            self.queue.task_done()

    async def on_connect(self, ws: WebSocket):
        logging.info("server: %s:%d connected", ws.client.host, ws.client.port)
        asyncio.create_task(self._sender(ws))

        def writer(msg: str):
            logging.debug('queue %s', msg)
            self.queue.put_nowait(msg)
        self.node.on_write(writer)
        await super().on_connect(ws)

    async def on_receive(self, ws: WebSocket, data: Any):
        logging.debug("server recv %s", data)
        self.node.handle_message(data)

    async def on_disconnect(self, ws: WebSocket, close_code: int):
        await super().on_disconnect(ws, close_code)
        logging.info("server: %s:%d disconnected", ws.client.host, ws.client.port)
        self.node.on_write(None)
        await self.queue.join()
        

routes = [
    WebSocketRoute("/ws", RemoteEndpoint)
]


app = Starlette(routes=routes)
