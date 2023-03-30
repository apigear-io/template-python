import asyncio
from typing import Any
from asyncio.queues import Queue
from starlette.applications import Starlette
from starlette.endpoints import WebSocketEndpoint
from starlette.routing import WebSocketRoute
from starlette.websockets import WebSocket

from olink.remotenode import RemoteNode

import tb.adv.olink.sources as sources
import tb.adv.olink.services as services
# ManyParamInterface service registration
sources.ManyParamInterfaceSource(services.ManyParamInterfaceService())
# NestedStruct1Interface service registration
sources.NestedStruct1InterfaceSource(services.NestedStruct1InterfaceService())
# NestedStruct2Interface service registration
sources.NestedStruct2InterfaceSource(services.NestedStruct2InterfaceService())
# NestedStruct3Interface service registration
sources.NestedStruct3InterfaceSource(services.NestedStruct3InterfaceService())

import tb.conflict.olink.sources as sources
import tb.conflict.olink.services as services
# Conflict1 service registration
sources.Conflict1Source(services.Conflict1Service())
# Conflict2 service registration
sources.Conflict2Source(services.Conflict2Service())
# Conflict3 service registration
sources.Conflict3Source(services.Conflict3Service())
# Conflict4 service registration
sources.Conflict4Source(services.Conflict4Service())

import tb.data.olink.sources as sources
import tb.data.olink.services as services
# StructInterface service registration
sources.StructInterfaceSource(services.StructInterfaceService())
# StructArrayInterface service registration
sources.StructArrayInterfaceSource(services.StructArrayInterfaceService())

import tb.enum.olink.sources as sources
import tb.enum.olink.services as services
# EnumInterface service registration
sources.EnumInterfaceSource(services.EnumInterfaceService())

import tb.same.olink.sources as sources
import tb.same.olink.services as services
# SameStruct1Interface service registration
sources.SameStruct1InterfaceSource(services.SameStruct1InterfaceService())
# SameStruct2Interface service registration
sources.SameStruct2InterfaceSource(services.SameStruct2InterfaceService())
# SameEnum1Interface service registration
sources.SameEnum1InterfaceSource(services.SameEnum1InterfaceService())
# SameEnum2Interface service registration
sources.SameEnum2InterfaceSource(services.SameEnum2InterfaceService())

import tb.again.olink.sources as sources
import tb.again.olink.services as services
# SameStruct1Interface service registration
sources.SameStruct1InterfaceSource(services.SameStruct1InterfaceService())
# SameStruct2Interface service registration
sources.SameStruct2InterfaceSource(services.SameStruct2InterfaceService())
# SameEnum1Interface service registration
sources.SameEnum1InterfaceSource(services.SameEnum1InterfaceService())
# SameEnum2Interface service registration
sources.SameEnum2InterfaceSource(services.SameEnum2InterfaceService())

import tb.simple.olink.sources as sources
import tb.simple.olink.services as services
# SimpleInterface service registration
sources.SimpleInterfaceSource(services.SimpleInterfaceService())
# SimpleArrayInterface service registration
sources.SimpleArrayInterfaceSource(services.SimpleArrayInterfaceService())

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
