import asyncio
from typing import Any
import logging
from asyncio.queues import Queue
from starlette.applications import Starlette
from starlette.endpoints import WebSocketEndpoint, Scope, Receive, Send
from starlette.routing import WebSocketRoute
from starlette.websockets import WebSocket

from olink.remote import RemoteNode

import testbed2_olink
import testbed2_impl

import tb_enum_olink
import tb_enum_impl

import tb_same1_olink
import tb_same1_impl

import tb_same2_olink
import tb_same2_impl

import tb_simple_olink
import tb_simple_impl

import testbed1_olink
import testbed1_impl

import tb_empty_olink
import tb_empty_impl

testbed2_olink.ManyParamInterfaceSource(testbed2_impl.ManyParamInterface())
testbed2_olink.NestedStruct1InterfaceSource(testbed2_impl.NestedStruct1Interface())
testbed2_olink.NestedStruct2InterfaceSource(testbed2_impl.NestedStruct2Interface())
testbed2_olink.NestedStruct3InterfaceSource(testbed2_impl.NestedStruct3Interface())

tb_enum_olink.EnumInterfaceSource(tb_enum_impl.EnumInterface())

tb_same1_olink.SameStruct1InterfaceSource(tb_same1_impl.SameStruct1Interface())
tb_same1_olink.SameStruct2InterfaceSource(tb_same1_impl.SameStruct2Interface())
tb_same1_olink.SameEnum1InterfaceSource(tb_same1_impl.SameEnum1Interface())
tb_same1_olink.SameEnum2InterfaceSource(tb_same1_impl.SameEnum2Interface())

tb_same2_olink.SameStruct1InterfaceSource(tb_same2_impl.SameStruct1Interface())
tb_same2_olink.SameStruct2InterfaceSource(tb_same2_impl.SameStruct2Interface())
tb_same2_olink.SameEnum1InterfaceSource(tb_same2_impl.SameEnum1Interface())
tb_same2_olink.SameEnum2InterfaceSource(tb_same2_impl.SameEnum2Interface())

tb_simple_olink.SimpleInterfaceSource(tb_simple_impl.SimpleInterface())
tb_simple_olink.SimpleArrayInterfaceSource(tb_simple_impl.SimpleArrayInterface())
tb_simple_olink.NoPropertiesInterfaceSource(tb_simple_impl.NoPropertiesInterface())
tb_simple_olink.NoOperationsInterfaceSource(tb_simple_impl.NoOperationsInterface())
tb_simple_olink.NoSignalsInterfaceSource(tb_simple_impl.NoSignalsInterface())
tb_simple_olink.EmptyInterfaceSource(tb_simple_impl.EmptyInterface())

testbed1_olink.StructInterfaceSource(testbed1_impl.StructInterface())
testbed1_olink.StructArrayInterfaceSource(testbed1_impl.StructArrayInterface())

tb_empty_olink.EmptyInterfaceSource(tb_empty_impl.EmptyInterface())



class RemoteEndpoint(WebSocketEndpoint):
    def __init__(self, scope: Scope, receive: Receive, send: Send):
        super().__init__(scope, receive, send)
        self.encoding = "text"
        self.node = RemoteNode()
        self.node.on_log(lambda level, msg: logging.info(msg))
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
