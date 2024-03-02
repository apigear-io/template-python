
from tb_simple_api import api
from tb_simple_impl import NoSignalsInterface
from tb_simple_olink import NoSignalsInterfaceSource, NoSignalsInterfaceSink
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest

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
        self.called = False
        sink.on_prop_bool_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop_bool(False)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop_bool() == False
        assert sink.get_prop_bool() == False

    def test_prop_int(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_prop_int_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop_int(0)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop_int() == 0
        assert sink.get_prop_int() == 0
    pass
