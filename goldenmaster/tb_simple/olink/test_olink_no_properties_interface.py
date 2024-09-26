
from tb_simple.api import api
from tb_simple.impl import NoPropertiesInterface
from tb_simple.olink import NoPropertiesInterfaceSource, NoPropertiesInterfaceSink
import tb_simple.test_helpers.test_struct
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest
from typing import Any
import asyncio

@pytest.fixture()
def olink_objects():
    impl = NoPropertiesInterface()
    NoPropertiesInterfaceSource(impl)
    remote_node = RemoteNode()
    client_node = ClientNode()

    remote_node.on_write(client_node.handle_message)
    client_node.on_write(remote_node.handle_message)

    sink = NoPropertiesInterfaceSink()
    client_node.link_remote(sink.olink_object_name())
    yield impl, sink

class TestOLinkNoPropertiesInterface:

    @pytest.mark.asyncio
    async def test_func_void(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_void()

    @pytest.mark.asyncio
    async def test_func_bool(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_bool(param_bool=False)

    def test_sig_void(self, olink_objects):
        impl, sink = olink_objects
        is_sig_void_called = False

        def funSignal():
            nonlocal is_sig_void_called
            is_sig_void_called = True

        sink.on_sig_void += funSignal


        impl._sig_void()
        assert is_sig_void_called == True

    def test_sig_bool(self, olink_objects):
        impl, sink = olink_objects
        is_sig_bool_called = False

        def funSignal(param_bool):
            assert param_bool == True
            nonlocal is_sig_bool_called
            is_sig_bool_called = True

        sink.on_sig_bool += funSignal


        impl._sig_bool(True)
        assert is_sig_bool_called == True
