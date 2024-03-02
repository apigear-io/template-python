
from tb_simple_api import api
from tb_simple_impl import NoOperationsInterface
from tb_simple_olink import NoOperationsInterfaceSource, NoOperationsInterfaceSink
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest

@pytest.fixture()
def olink_objects():
    impl = NoOperationsInterface()
    source = NoOperationsInterfaceSource(impl)
    remote_node = RemoteNode()
    client_node = ClientNode()

    remote_node.on_write(client_node.handle_message)
    client_node.on_write(remote_node.handle_message)

    sink = NoOperationsInterfaceSink()
    client_node.link_remote(sink.olink_object_name())
    yield impl, sink

class TestOLinkNoOperationsInterface:

    def test_sig_void(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig_void += lambda *args: setattr(self, 'called', True)
        impl._sig_void()
        assert self.called == True

    def test_sig_bool(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig_bool += lambda *args: setattr(self, 'called', True)
        impl._sig_bool(False)
        assert self.called == True
