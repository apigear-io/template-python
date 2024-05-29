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


# set default log level to INFO and above
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

routes = [
    WebSocketRoute("/ws", apigear.olink.RemoteEndpoint)
]


app = Starlette(routes=routes)
