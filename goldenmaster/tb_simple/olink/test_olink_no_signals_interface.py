
from tb_simple.api import api
from tb_simple.impl import NoSignalsInterface
from tb_simple.olink import NoSignalsInterfaceSource, NoSignalsInterfaceSink
import tb_simple.test_helpers.test_struct
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest
from typing import Any
import asyncio

@pytest.fixture()
def olink_objects():
    impl = NoSignalsInterface()
    NoSignalsInterfaceSource(impl)
    remote_node = RemoteNode()
    client_node = ClientNode()

    remote_node.on_write(client_node.handle_message)
    client_node.on_write(remote_node.handle_message)

    sink = NoSignalsInterfaceSink()
    client_node.link_remote(sink.olink_object_name())
    yield impl, sink

class TestOLinkNoSignalsInterface:

    def test_prop_bool(self, olink_objects):
        impl, sink = olink_objects
        is_prop_bool_changed = False
        def funProp(arguments):
            nonlocal is_prop_bool_changed
            is_prop_bool_changed = True
        sink.on_prop_bool_changed += funProp
        test_value = True

        sink.set_prop_bool(test_value)
        assert is_prop_bool_changed == True
        assert impl.get_prop_bool() == test_value
        assert sink.get_prop_bool() == test_value

    def test_prop_int(self, olink_objects):
        impl, sink = olink_objects
        is_prop_int_changed = False
        def funProp(arguments):
            nonlocal is_prop_int_changed
            is_prop_int_changed = True
        sink.on_prop_int_changed += funProp
        test_value = 1

        sink.set_prop_int(test_value)
        assert is_prop_int_changed == True
        assert impl.get_prop_int() == test_value
        assert sink.get_prop_int() == test_value

    @pytest.mark.asyncio
    async def test_func_void(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_void()

    @pytest.mark.asyncio
    async def test_func_bool(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_bool(param_bool=False)
