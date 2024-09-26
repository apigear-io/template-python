
from tb_same1.api import api
from tb_same1.impl import SameEnum1Interface
from tb_same1.olink import SameEnum1InterfaceSource, SameEnum1InterfaceSink
import tb_same1.test_helpers.test_struct
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest
from typing import Any
import asyncio

@pytest.fixture()
def olink_objects():
    impl = SameEnum1Interface()
    SameEnum1InterfaceSource(impl)
    remote_node = RemoteNode()
    client_node = ClientNode()

    remote_node.on_write(client_node.handle_message)
    client_node.on_write(remote_node.handle_message)

    sink = SameEnum1InterfaceSink()
    client_node.link_remote(sink.olink_object_name())
    yield impl, sink

class TestOLinkSameEnum1Interface:

    def test_prop1(self, olink_objects):
        impl, sink = olink_objects
        is_prop1_changed = False
        def funProp(arguments):
            nonlocal is_prop1_changed
            is_prop1_changed = True
        sink.on_prop1_changed += funProp
        test_value = api.Enum1.VALUE2

        sink.set_prop1(test_value)
        assert is_prop1_changed == True
        assert impl.get_prop1() == test_value
        assert sink.get_prop1() == test_value

    @pytest.mark.asyncio
    async def test_func1(self, olink_objects):
        impl, sink = olink_objects
        await sink.func1(param1=api.Enum1.VALUE1)

    def test_sig1(self, olink_objects):
        impl, sink = olink_objects
        is_sig1_called = False

        def funSignal(param1):
            assert param1 == api.Enum1.VALUE2
            nonlocal is_sig1_called
            is_sig1_called = True

        sink.on_sig1 += funSignal


        impl._sig1(api.Enum1.VALUE2)
        assert is_sig1_called == True
