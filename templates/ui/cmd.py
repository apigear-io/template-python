# How to use: 
# python demo/ui/cmd.py --increment 1
# python demo/ui/cmd.py --decrement 2

from olink.clientnode import ClientNode
from demo.olink.client import Client

#from asyncio.queues import Queue
import asyncio
#import websockets
import demo.olink.sinks

import argparse

# create a client node
node = ClientNode()

# create our client ws adapter
client = Client(node)

# register demo.Counter to the remote node
node.link_remote('demo.Counter')
# create our client api
demo.olink.sinks.CounterSink()


async def main():
    def print_change(name, value):
        print('property changed', name, value)

    # get a sink from the registry
    # sink = node.get_sink('<module>.<interface>')
    sink = node.get_sink('demo.Counter')

    # register a property change listener
    # sink.on_property_changed += print_change
    sink.on_property_changed += print_change
    
    loop = asyncio.get_event_loop()
    
    # register a async function call
    # loop.create_task(sink.doSomething(value))

    parser = argparse.ArgumentParser(description="Send value to be incremented or decremented.")

    parser.add_argument('--increment', type=int, dest='increment', help="Increment operation")
    parser.add_argument('--decrement', type=int, dest='decrement', help="Decrement operation")

    args = parser.parse_args()

    if args.increment:
        val = args.increment
        print("Increment {0}".format(val))
        print("Result: ", val+1)
        loop.create_task(sink.increment(val))

    if args.decrement:
        val = args.decrement
        print("Decrement {0}".format(args.decrement))
        print("Result: ", val-1)
        loop.create_task(sink.decrement(val))

    loop.run_until_complete(client.connect('ws://localhost:8000/ws'))

if __name__ == '__main__':
    main()

