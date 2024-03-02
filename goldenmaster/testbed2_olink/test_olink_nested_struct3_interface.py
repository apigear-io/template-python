
from testbed2_api import api
from testbed2_impl import NestedStruct3Interface
from testbed2_olink import NestedStruct3InterfaceSource, NestedStruct3InterfaceSink
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest

@pytest.fixture()
def olink_objects():
    impl = NestedStruct3Interface()
    source = NestedStruct3InterfaceSource(impl)
    remote_node = RemoteNode()
    client_node = ClientNode()

    remote_node.on_write(client_node.handle_message)
    client_node.on_write(remote_node.handle_message)

    sink = NestedStruct3InterfaceSink()
    client_node.link_remote(sink.olink_object_name())
    yield impl, sink

class TestOLinkNestedStruct3Interface:

    def test_sig1(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig1 += lambda *args: setattr(self, 'called', True)
        impl._sig1(api.NestedStruct1())
        assert self.called == True

    def test_sig2(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig2 += lambda *args: setattr(self, 'called', True)
        impl._sig2(api.NestedStruct1(), api.NestedStruct2())
        assert self.called == True

    def test_sig3(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig3 += lambda *args: setattr(self, 'called', True)
        impl._sig3(api.NestedStruct1(), api.NestedStruct2(), api.NestedStruct3())
        assert self.called == True
