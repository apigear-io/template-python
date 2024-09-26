
from tb_simple.api import api
from tb_simple.impl import VoidInterface
from tb_simple.olink import VoidInterfaceSource, VoidInterfaceSink
import tb_simple.test_helpers.test_struct
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest
from typing import Any
import asyncio

@pytest.fixture()
def olink_objects():
    impl = VoidInterface()
    VoidInterfaceSource(impl)
    remote_node = RemoteNode()
    client_node = ClientNode()

    remote_node.on_write(client_node.handle_message)
    client_node.on_write(remote_node.handle_message)

    sink = VoidInterfaceSink()
    client_node.link_remote(sink.olink_object_name())
    yield impl, sink

class TestOLinkVoidInterface:

    @pytest.mark.asyncio
    async def test_func_void(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_void()

    def test_sig_void(self, olink_objects):
        impl, sink = olink_objects
        is_sig_void_called = False

        def funSignal():
            nonlocal is_sig_void_called
            is_sig_void_called = True

        sink.on_sig_void += funSignal


        impl._sig_void()
        assert is_sig_void_called == True
