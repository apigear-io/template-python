
from testbed1_api import api
from testbed1_impl import StructArrayInterface
from testbed1_olink import StructArrayInterfaceSource, StructArrayInterfaceSink
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest

@pytest.fixture()
def olink_objects():
    impl = StructArrayInterface()
    source = StructArrayInterfaceSource(impl)
    remote_node = RemoteNode()
    client_node = ClientNode()

    remote_node.on_write(client_node.handle_message)
    client_node.on_write(remote_node.handle_message)

    sink = StructArrayInterfaceSink()
    client_node.link_remote(sink.olink_object_name())
    yield impl, sink

class TestOLinkStructArrayInterface:

    def test_sig_bool(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig_bool += lambda *args: setattr(self, 'called', True)
        impl._sig_bool([])
        assert self.called == True

    def test_sig_int(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig_int += lambda *args: setattr(self, 'called', True)
        impl._sig_int([])
        assert self.called == True

    def test_sig_float(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig_float += lambda *args: setattr(self, 'called', True)
        impl._sig_float([])
        assert self.called == True

    def test_sig_string(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig_string += lambda *args: setattr(self, 'called', True)
        impl._sig_string([])
        assert self.called == True
