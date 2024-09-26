
from tb_same2.api import api
from tb_same2.impl import SameEnum2Interface
from tb_same2.olink import SameEnum2InterfaceSource, SameEnum2InterfaceSink
import tb_same2.test_helpers.test_struct
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest
from typing import Any
import asyncio

@pytest.fixture()
def olink_objects():
    impl = SameEnum2Interface()
    SameEnum2InterfaceSource(impl)
    remote_node = RemoteNode()
    client_node = ClientNode()

    remote_node.on_write(client_node.handle_message)
    client_node.on_write(remote_node.handle_message)

    sink = SameEnum2InterfaceSink()
    client_node.link_remote(sink.olink_object_name())
    yield impl, sink

class TestOLinkSameEnum2Interface:

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

    def test_prop2(self, olink_objects):
        impl, sink = olink_objects
        is_prop2_changed = False
        def funProp(arguments):
            nonlocal is_prop2_changed
            is_prop2_changed = True
        sink.on_prop2_changed += funProp
        test_value = api.Enum2.VALUE2

        sink.set_prop2(test_value)
        assert is_prop2_changed == True
        assert impl.get_prop2() == test_value
        assert sink.get_prop2() == test_value

    @pytest.mark.asyncio
    async def test_func1(self, olink_objects):
        impl, sink = olink_objects
        await sink.func1(param1=api.Enum1.VALUE1)

    @pytest.mark.asyncio
    async def test_func2(self, olink_objects):
        impl, sink = olink_objects
        await sink.func2(param1=api.Enum1.VALUE1, param2=api.Enum2.VALUE1)

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

    def test_sig2(self, olink_objects):
        impl, sink = olink_objects
        is_sig2_called = False

        def funSignal(param1, param2):
            assert param1 == api.Enum1.VALUE2
            assert param2 == api.Enum2.VALUE2
            nonlocal is_sig2_called
            is_sig2_called = True

        sink.on_sig2 += funSignal


        impl._sig2(api.Enum1.VALUE2, api.Enum2.VALUE2)
        assert is_sig2_called == True
