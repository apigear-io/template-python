
from tb_simple.api import api
from tb_simple.impl import VoidInterface
from tb_simple.olink import VoidInterfaceSource, VoidInterfaceSink
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest

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
    pass

    @pytest.mark.asyncio
    async def test_func_void(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_void()

    def test_sig_void(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig_void += lambda *args: setattr(self, 'called', True)
        impl._sig_void()
        assert self.called == True
