from asyncio.queues import Queue
import asyncio
from olink.client import ClientNode
import websockets
import logging

# set default log level to INFO and above
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

class Client:
    def __init__(self, node: ClientNode):
        self.send_queue = Queue()
        self.node = node
        self.node.on_log(self._olink_log_writer)
        self.node.on_write(self._write)
        self.conn = None
        self.close_connection_request = asyncio.Event()

    def _olink_log_writer(self, level, msg):
        if level[0] == 1:
            logging.debug(msg)
        elif level[0] == 2:
            logging.info(msg)
        elif level[0] == 3:
            logging.warning(msg)
        else:
            logging.error(msg)

    def _write(self, data):
        self.send_queue.put_nowait(data)

    async def _writer(self):
        while True:
            data = await self.send_queue.get()
            if data is None:
                break
            logging.debug("client send %s", data)
            await self.conn.send(data)

    async def _reader(self):
        while True:
            try:
                data = await self.conn.recv()
                logging.debug("client recv %s", data)
                self.node.handle_message(data)
            except websockets.ConnectionClosed:
                break

    async def _disconnect(self):
        await self.close_connection_request.wait()

    async def connect(self, addr):
        async with websockets.connect(addr) as conn:
            self.conn = conn
            self.close_connection_request.clear()
            reader = asyncio.create_task(self._reader())
            writer = asyncio.create_task(self._writer())
            finish = asyncio.create_task(self._disconnect())
            try:
                _, pending = await asyncio.wait(
                    [reader, writer, finish], return_when=asyncio.FIRST_COMPLETED
                )
                # cancel pending tasks
                self.send_queue.put_nowait(None)
                for task in pending:
                    task.cancel()
            except asyncio.CancelledError:
                pass
            
    def disconnect(self):
        self.close_connection_request.set()
