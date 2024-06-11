import asyncio
import os
import sys

#add context - paths to modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from asyncio.queues import Queue
from olink.client import ClientNode
import websockets
import logging
import apigear.olink


import testbed2.olink
import tb_enum.olink
import tb_same1.olink
import tb_same2.olink
import tb_simple.olink
import testbed1.olink
import tb_names.olink
import tb_empty.olink

# set default log level to INFO and above
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)


# create a client node
node = ClientNode()

# create our client ws adapter
client = apigear.olink.Client(node)




# create and register sink for testbed2.ManyParamInterface
sink = testbed2.olink.ManyParamInterfaceSink()
node.link_remote(sink.olink_object_name())

# create and register sink for testbed2.NestedStruct1Interface
sink = testbed2.olink.NestedStruct1InterfaceSink()
node.link_remote(sink.olink_object_name())

# create and register sink for testbed2.NestedStruct2Interface
sink = testbed2.olink.NestedStruct2InterfaceSink()
node.link_remote(sink.olink_object_name())

# create and register sink for testbed2.NestedStruct3Interface
sink = testbed2.olink.NestedStruct3InterfaceSink()
node.link_remote(sink.olink_object_name())



# create and register sink for tb.enum.EnumInterface
sink = tb_enum.olink.EnumInterfaceSink()
node.link_remote(sink.olink_object_name())



# create and register sink for tb.same1.SameStruct1Interface
sink = tb_same1.olink.SameStruct1InterfaceSink()
node.link_remote(sink.olink_object_name())

# create and register sink for tb.same1.SameStruct2Interface
sink = tb_same1.olink.SameStruct2InterfaceSink()
node.link_remote(sink.olink_object_name())

# create and register sink for tb.same1.SameEnum1Interface
sink = tb_same1.olink.SameEnum1InterfaceSink()
node.link_remote(sink.olink_object_name())

# create and register sink for tb.same1.SameEnum2Interface
sink = tb_same1.olink.SameEnum2InterfaceSink()
node.link_remote(sink.olink_object_name())



# create and register sink for tb.same2.SameStruct1Interface
sink = tb_same2.olink.SameStruct1InterfaceSink()
node.link_remote(sink.olink_object_name())

# create and register sink for tb.same2.SameStruct2Interface
sink = tb_same2.olink.SameStruct2InterfaceSink()
node.link_remote(sink.olink_object_name())

# create and register sink for tb.same2.SameEnum1Interface
sink = tb_same2.olink.SameEnum1InterfaceSink()
node.link_remote(sink.olink_object_name())

# create and register sink for tb.same2.SameEnum2Interface
sink = tb_same2.olink.SameEnum2InterfaceSink()
node.link_remote(sink.olink_object_name())



# create and register sink for tb.simple.VoidInterface
sink = tb_simple.olink.VoidInterfaceSink()
node.link_remote(sink.olink_object_name())

# create and register sink for tb.simple.SimpleInterface
sink = tb_simple.olink.SimpleInterfaceSink()
node.link_remote(sink.olink_object_name())

# create and register sink for tb.simple.SimpleArrayInterface
sink = tb_simple.olink.SimpleArrayInterfaceSink()
node.link_remote(sink.olink_object_name())

# create and register sink for tb.simple.NoPropertiesInterface
sink = tb_simple.olink.NoPropertiesInterfaceSink()
node.link_remote(sink.olink_object_name())

# create and register sink for tb.simple.NoOperationsInterface
sink = tb_simple.olink.NoOperationsInterfaceSink()
node.link_remote(sink.olink_object_name())

# create and register sink for tb.simple.NoSignalsInterface
sink = tb_simple.olink.NoSignalsInterfaceSink()
node.link_remote(sink.olink_object_name())



# create and register sink for testbed1.StructInterface
sink = testbed1.olink.StructInterfaceSink()
node.link_remote(sink.olink_object_name())

# create and register sink for testbed1.StructArrayInterface
sink = testbed1.olink.StructArrayInterfaceSink()
node.link_remote(sink.olink_object_name())



# create and register sink for tb.names.Nam_Es
sink = tb_names.olink.Nam_EsSink()
node.link_remote(sink.olink_object_name())



# create and register sink for tb.empty.EmptyInterface
sink = tb_empty.olink.EmptyInterfaceSink()
node.link_remote(sink.olink_object_name())


ADDR = 'ws://localhost:8000/ws'

async def main():
    await client.connect(ADDR)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
