# How to use: 
# python demo/ui/cmd.py --increment 1
# python demo/ui/cmd.py --decrement 2

import argparse
import asyncio

from olink.clientnode import ClientNode
from demo.olink.client import Client
import demo.olink.sinks


# create a client node
node = ClientNode()

# create our client ws adapter
client = Client(node)

# register demo.Counter to the remote node
node.link_remote('demo.Counter')

# create our client api
demo.olink.sinks.CounterSink()

loop = asyncio.get_event_loop()

sink = node.get_sink('demo.Counter')



async def increment(value):
    for i in range(10):
        task = loop.create_task(sink.increment(value+i))
        print(f"Task name is {task.get_name()}")
        #await task # This should return value after increment but it doesn

        await asyncio.sleep(0.5)
    await client.connect('ws://localhost:8000/ws')
    

async def decrement(value):
    for i in range(10):
        loop.create_task(sink.increment(value-i))
        await asyncio.sleep(1)  
    await client.connect('ws://localhost:8000/ws')

def main():

    parser = argparse.ArgumentParser(description="Send value to be incremented or decremented.")

    parser.add_argument('--increment', type=int, dest='increment', help="Increment operation")
    parser.add_argument('--decrement', type=int, dest='decrement', help="Decrement operation")
    args = parser.parse_args()

    if args.increment:
        value = args.increment 
        loop.run_until_complete(increment(value))

    if args.decrement:
        value = args.decrement
        loop.run_until_complete(decrement(value))

if __name__ == '__main__':
    main()