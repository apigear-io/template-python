from asyncio.queues import Queue
import asyncio
from olink.client import ClientNode
import websockets
import logging


import testbed2_olink
import tb_enum_olink
import tb_same1_olink
import tb_same2_olink
import tb_simple_olink
import testbed1_olink
import tb_empty_olink

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

# create a client node
node = ClientNode()

# create our client ws adapter
client = Client(node)




# create and register sink for testbed2.ManyParamInterface
sink = testbed2_olink.ManyParamInterfaceSink()
node.link_remote(sink.olink_object_name())

# create and register sink for testbed2.NestedStruct1Interface
sink = testbed2_olink.NestedStruct1InterfaceSink()
node.link_remote(sink.olink_object_name())

# create and register sink for testbed2.NestedStruct2Interface
sink = testbed2_olink.NestedStruct2InterfaceSink()
node.link_remote(sink.olink_object_name())

# create and register sink for testbed2.NestedStruct3Interface
sink = testbed2_olink.NestedStruct3InterfaceSink()
node.link_remote(sink.olink_object_name())



# create and register sink for tb.enum.EnumInterface
sink = tb_enum_olink.EnumInterfaceSink()
node.link_remote(sink.olink_object_name())



# create and register sink for tb.same1.SameStruct1Interface
sink = tb_same1_olink.SameStruct1InterfaceSink()
node.link_remote(sink.olink_object_name())

# create and register sink for tb.same1.SameStruct2Interface
sink = tb_same1_olink.SameStruct2InterfaceSink()
node.link_remote(sink.olink_object_name())

# create and register sink for tb.same1.SameEnum1Interface
sink = tb_same1_olink.SameEnum1InterfaceSink()
node.link_remote(sink.olink_object_name())

# create and register sink for tb.same1.SameEnum2Interface
sink = tb_same1_olink.SameEnum2InterfaceSink()
node.link_remote(sink.olink_object_name())



# create and register sink for tb.same2.SameStruct1Interface
sink = tb_same2_olink.SameStruct1InterfaceSink()
node.link_remote(sink.olink_object_name())

# create and register sink for tb.same2.SameStruct2Interface
sink = tb_same2_olink.SameStruct2InterfaceSink()
node.link_remote(sink.olink_object_name())

# create and register sink for tb.same2.SameEnum1Interface
sink = tb_same2_olink.SameEnum1InterfaceSink()
node.link_remote(sink.olink_object_name())

# create and register sink for tb.same2.SameEnum2Interface
sink = tb_same2_olink.SameEnum2InterfaceSink()
node.link_remote(sink.olink_object_name())



# create and register sink for tb.simple.SimpleInterface
sink = tb_simple_olink.SimpleInterfaceSink()
node.link_remote(sink.olink_object_name())

# create and register sink for tb.simple.SimpleArrayInterface
sink = tb_simple_olink.SimpleArrayInterfaceSink()
node.link_remote(sink.olink_object_name())

# create and register sink for tb.simple.NoPropertiesInterface
sink = tb_simple_olink.NoPropertiesInterfaceSink()
node.link_remote(sink.olink_object_name())

# create and register sink for tb.simple.NoOperationsInterface
sink = tb_simple_olink.NoOperationsInterfaceSink()
node.link_remote(sink.olink_object_name())

# create and register sink for tb.simple.NoSignalsInterface
sink = tb_simple_olink.NoSignalsInterfaceSink()
node.link_remote(sink.olink_object_name())

# create and register sink for tb.simple.EmptyInterface
sink = tb_simple_olink.EmptyInterfaceSink()
node.link_remote(sink.olink_object_name())



# create and register sink for testbed1.StructInterface
sink = testbed1_olink.StructInterfaceSink()
node.link_remote(sink.olink_object_name())

# create and register sink for testbed1.StructArrayInterface
sink = testbed1_olink.StructArrayInterfaceSink()
node.link_remote(sink.olink_object_name())



# create and register sink for tb.empty.EmptyInterface
sink = tb_empty_olink.EmptyInterfaceSink()
node.link_remote(sink.olink_object_name())


ADDR = 'ws://localhost:8000/ws'

async def main():
    await client.connect(ADDR)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
