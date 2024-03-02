
from testbed2_api import api
from testbed2_impl import ManyParamInterface
from testbed2_olink import ManyParamInterfaceSource, ManyParamInterfaceSink
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest

@pytest.fixture()
def olink_objects():
    impl = ManyParamInterface()
    ManyParamInterfaceSource(impl)
    remote_node = RemoteNode()
    client_node = ClientNode()

    remote_node.on_write(client_node.handle_message)
    client_node.on_write(remote_node.handle_message)

    sink = ManyParamInterfaceSink()
    client_node.link_remote(sink.olink_object_name())
    yield impl, sink

class TestOLinkManyParamInterface:

    def test_prop1(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_prop1_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop1(0)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop1() == 0
        assert sink.get_prop1() == 0

    def test_prop2(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_prop2_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop2(0)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop2() == 0
        assert sink.get_prop2() == 0

    def test_prop3(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_prop3_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop3(0)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop3() == 0
        assert sink.get_prop3() == 0

    def test_prop4(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_prop4_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop4(0)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop4() == 0
        assert sink.get_prop4() == 0

    def test_sig1(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig1 += lambda *args: setattr(self, 'called', True)
        impl._sig1(0)
        assert self.called == True

    def test_sig2(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig2 += lambda *args: setattr(self, 'called', True)
        impl._sig2(0, 0)
        assert self.called == True

    def test_sig3(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig3 += lambda *args: setattr(self, 'called', True)
        impl._sig3(0, 0, 0)
        assert self.called == True

    def test_sig4(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig4 += lambda *args: setattr(self, 'called', True)
        impl._sig4(0, 0, 0, 0)
        assert self.called == True
