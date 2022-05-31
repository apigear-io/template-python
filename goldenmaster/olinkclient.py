from asyncio.queues import Queue
from olink.clientnode import ClientNode
import asyncio
import websockets
import org_objectapi_testbed.olink.sinks


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

# register org.objectapi.testbed.Interface1 to the remote node
node.link_remote('org.objectapi.testbed.Interface1')
# create our client api
org_objectapi_testbed.olink.sinks.Interface1Sink()

# register org.objectapi.testbed.Interface2 to the remote node
node.link_remote('org.objectapi.testbed.Interface2')
# create our client api
org_objectapi_testbed.olink.sinks.Interface2Sink()


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