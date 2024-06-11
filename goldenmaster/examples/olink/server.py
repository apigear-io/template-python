import asyncio
import logging
import os
import sys

#add context - paths to modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from starlette.applications import Starlette
from starlette.routing import WebSocketRoute

from olink.remote import RemoteNode

import apigear.olink

import testbed2.olink
import testbed2.impl

import tb_enum.olink
import tb_enum.impl

import tb_same1.olink
import tb_same1.impl

import tb_same2.olink
import tb_same2.impl

import tb_simple.olink
import tb_simple.impl

import testbed1.olink
import testbed1.impl

import tb_names.olink
import tb_names.impl

import tb_empty.olink
import tb_empty.impl

testbed2.olink.ManyParamInterfaceSource(testbed2.impl.ManyParamInterface())
testbed2.olink.NestedStruct1InterfaceSource(testbed2.impl.NestedStruct1Interface())
testbed2.olink.NestedStruct2InterfaceSource(testbed2.impl.NestedStruct2Interface())
testbed2.olink.NestedStruct3InterfaceSource(testbed2.impl.NestedStruct3Interface())

tb_enum.olink.EnumInterfaceSource(tb_enum.impl.EnumInterface())

tb_same1.olink.SameStruct1InterfaceSource(tb_same1.impl.SameStruct1Interface())
tb_same1.olink.SameStruct2InterfaceSource(tb_same1.impl.SameStruct2Interface())
tb_same1.olink.SameEnum1InterfaceSource(tb_same1.impl.SameEnum1Interface())
tb_same1.olink.SameEnum2InterfaceSource(tb_same1.impl.SameEnum2Interface())

tb_same2.olink.SameStruct1InterfaceSource(tb_same2.impl.SameStruct1Interface())
tb_same2.olink.SameStruct2InterfaceSource(tb_same2.impl.SameStruct2Interface())
tb_same2.olink.SameEnum1InterfaceSource(tb_same2.impl.SameEnum1Interface())
tb_same2.olink.SameEnum2InterfaceSource(tb_same2.impl.SameEnum2Interface())

tb_simple.olink.VoidInterfaceSource(tb_simple.impl.VoidInterface())
tb_simple.olink.SimpleInterfaceSource(tb_simple.impl.SimpleInterface())
tb_simple.olink.SimpleArrayInterfaceSource(tb_simple.impl.SimpleArrayInterface())
tb_simple.olink.NoPropertiesInterfaceSource(tb_simple.impl.NoPropertiesInterface())
tb_simple.olink.NoOperationsInterfaceSource(tb_simple.impl.NoOperationsInterface())
tb_simple.olink.NoSignalsInterfaceSource(tb_simple.impl.NoSignalsInterface())

testbed1.olink.StructInterfaceSource(testbed1.impl.StructInterface())
testbed1.olink.StructArrayInterfaceSource(testbed1.impl.StructArrayInterface())

tb_names.olink.NamEsSource(tb_names.impl.NamEs())

tb_empty.olink.EmptyInterfaceSource(tb_empty.impl.EmptyInterface())


# set default log level to INFO and above
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

routes = [
    WebSocketRoute("/ws", apigear.olink.RemoteEndpoint)
]


app = Starlette(routes=routes)
