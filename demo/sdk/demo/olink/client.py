from asyncio.queues import Queue
from olink.client import ClientNode
import asyncio
from olink.ws import Connection


import demo

# create a client node
node = ClientNode()

# create our client ws adapter
client = Connection(node)





# register demo.Counter to the remote node
node.link_remote('demo.Counter')
# create our client api
demo.olink.sinks.CounterSink()

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
