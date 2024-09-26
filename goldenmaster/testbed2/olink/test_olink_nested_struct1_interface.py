
from testbed2.api import api
from testbed2.impl import NestedStruct1Interface
from testbed2.olink import NestedStruct1InterfaceSource, NestedStruct1InterfaceSink
import testbed2.test_helpers.test_struct
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest
from typing import Any
import asyncio

@pytest.fixture()
def olink_objects():
    impl = NestedStruct1Interface()
    NestedStruct1InterfaceSource(impl)
    remote_node = RemoteNode()
    client_node = ClientNode()

    remote_node.on_write(client_node.handle_message)
    client_node.on_write(remote_node.handle_message)

    sink = NestedStruct1InterfaceSink()
    client_node.link_remote(sink.olink_object_name())
    yield impl, sink

class TestOLinkNestedStruct1Interface:

    def test_prop1(self, olink_objects):
        impl, sink = olink_objects
        is_prop1_changed = False
        def funProp(arguments):
            nonlocal is_prop1_changed
            is_prop1_changed = True
        sink.on_prop1_changed += funProp
        test_value = testbed2.test_helpers.test_struct.fillTestNestedStruct1(api.NestedStruct1())

        sink.set_prop1(test_value)
        assert is_prop1_changed == True
        assert impl.get_prop1() == test_value
        assert sink.get_prop1() == test_value

    @pytest.mark.asyncio
    async def test_func1(self, olink_objects):
        impl, sink = olink_objects
        await sink.func1(param1=api.NestedStruct1())

    def test_sig1(self, olink_objects):
        impl, sink = olink_objects
        is_sig1_called = False
        local_param1_struct = testbed2.test_helpers.test_struct.fillTestNestedStruct1(api.NestedStruct1())

        def funSignal(param1):
            assert param1 ==local_param1_struct
            nonlocal is_sig1_called
            is_sig1_called = True

        sink.on_sig1 += funSignal


        impl._sig1(local_param1_struct)
        assert is_sig1_called == True
