from asyncio.queues import Queue
from olink.clientnode import ClientNode
import asyncio
import websockets

import tb.adv
import tb.conflict
import tb.data
import tb.enum
import tb.same
import tb.again
import tb.simple

class Client:
    # message queue
    queue = Queue()
    # no node assign yet
    node = None

    def __init__(self, node):
        self.node = node
        # register a writer
        self.node.on_write(self.writer)

    def writer(self, data):
        print('writer, data')
        # write data to queue
        self.queue.put_nowait(data)

    async def _reader(self, ws):
        # handle incoming message and send to node
        while True:
            data = await ws.recv()
            self.node.handle_message(data)

    async def _sender(self, ws):
        # send all messages from the queue
        while True:
            data = await self.queue.get()
            await ws.send(data)
            self.queue.task_done()

    async def connect(self, address: str):
        # connect to the server
        async for ws in websockets.connect(address):
            print('connected')
            # register async sending and receiving of messsages
            sender_task = asyncio.create_task(self._sender(ws))
            reader_task = asyncio.create_task(self._reader(ws))
            # wait for all tasks are finished
            await asyncio.gather(sender_task, reader_task)
            # wait till queue is empty
            await self.queue.join()

# create a client node
node = ClientNode()

# create our client ws adapter
client = Client(node)





# register tb.adv.ManyParamInterface to the remote node
node.link_remote('tb.adv.ManyParamInterface')
# create our client api
tb.adv.olink.sinks.ManyParamInterfaceSink()

# register tb.adv.NestedStruct1Interface to the remote node
node.link_remote('tb.adv.NestedStruct1Interface')
# create our client api
tb.adv.olink.sinks.NestedStruct1InterfaceSink()

# register tb.adv.NestedStruct2Interface to the remote node
node.link_remote('tb.adv.NestedStruct2Interface')
# create our client api
tb.adv.olink.sinks.NestedStruct2InterfaceSink()

# register tb.adv.NestedStruct3Interface to the remote node
node.link_remote('tb.adv.NestedStruct3Interface')
# create our client api
tb.adv.olink.sinks.NestedStruct3InterfaceSink()



# register tb.conflict.Conflict1 to the remote node
node.link_remote('tb.conflict.Conflict1')
# create our client api
tb.conflict.olink.sinks.Conflict1Sink()

# register tb.conflict.Conflict2 to the remote node
node.link_remote('tb.conflict.Conflict2')
# create our client api
tb.conflict.olink.sinks.Conflict2Sink()

# register tb.conflict.Conflict3 to the remote node
node.link_remote('tb.conflict.Conflict3')
# create our client api
tb.conflict.olink.sinks.Conflict3Sink()

# register tb.conflict.Conflict4 to the remote node
node.link_remote('tb.conflict.Conflict4')
# create our client api
tb.conflict.olink.sinks.Conflict4Sink()



# register tb.data.StructInterface to the remote node
node.link_remote('tb.data.StructInterface')
# create our client api
tb.data.olink.sinks.StructInterfaceSink()

# register tb.data.StructArrayInterface to the remote node
node.link_remote('tb.data.StructArrayInterface')
# create our client api
tb.data.olink.sinks.StructArrayInterfaceSink()



# register tb.enum.EnumInterface to the remote node
node.link_remote('tb.enum.EnumInterface')
# create our client api
tb.enum.olink.sinks.EnumInterfaceSink()



# register tb.same.SameStruct1Interface to the remote node
node.link_remote('tb.same.SameStruct1Interface')
# create our client api
tb.same.olink.sinks.SameStruct1InterfaceSink()

# register tb.same.SameStruct2Interface to the remote node
node.link_remote('tb.same.SameStruct2Interface')
# create our client api
tb.same.olink.sinks.SameStruct2InterfaceSink()

# register tb.same.SameEnum1Interface to the remote node
node.link_remote('tb.same.SameEnum1Interface')
# create our client api
tb.same.olink.sinks.SameEnum1InterfaceSink()

# register tb.same.SameEnum2Interface to the remote node
node.link_remote('tb.same.SameEnum2Interface')
# create our client api
tb.same.olink.sinks.SameEnum2InterfaceSink()



# register tb.again.SameStruct1Interface to the remote node
node.link_remote('tb.again.SameStruct1Interface')
# create our client api
tb.again.olink.sinks.SameStruct1InterfaceSink()

# register tb.again.SameStruct2Interface to the remote node
node.link_remote('tb.again.SameStruct2Interface')
# create our client api
tb.again.olink.sinks.SameStruct2InterfaceSink()

# register tb.again.SameEnum1Interface to the remote node
node.link_remote('tb.again.SameEnum1Interface')
# create our client api
tb.again.olink.sinks.SameEnum1InterfaceSink()

# register tb.again.SameEnum2Interface to the remote node
node.link_remote('tb.again.SameEnum2Interface')
# create our client api
tb.again.olink.sinks.SameEnum2InterfaceSink()



# register tb.simple.SimpleInterface to the remote node
node.link_remote('tb.simple.SimpleInterface')
# create our client api
tb.simple.olink.sinks.SimpleInterfaceSink()

# register tb.simple.SimpleArrayInterface to the remote node
node.link_remote('tb.simple.SimpleArrayInterface')
# create our client api
tb.simple.olink.sinks.SimpleArrayInterfaceSink()

def main():
    def print_change(name, value):
        print('property changed', name, value)

    # get a sink from the registry
    # sink = node.get_sink('<module>.<interface>')
    # register a property change listener
    # sink.on_property_changed += print_change
    loop = asyncio.get_event_loop()
    # register a async function call
    # loop.create_task(sink.doSomething(value))
    loop.run_until_complete(client.connect('ws://localhost:8000/ws'))

if __name__ == '__main__':
    main()
