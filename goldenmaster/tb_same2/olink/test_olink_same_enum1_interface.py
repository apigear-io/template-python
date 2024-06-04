
from tb_same2.api import api
from tb_same2.impl import SameEnum1Interface
from tb_same2.olink import SameEnum1InterfaceSource, SameEnum1InterfaceSink
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest

@pytest.fixture()
def olink_objects():
    impl = SameEnum1Interface()
    SameEnum1InterfaceSource(impl)
    remote_node = RemoteNode()
    client_node = ClientNode()

    remote_node.on_write(client_node.handle_message)
    client_node.on_write(remote_node.handle_message)

    sink = SameEnum1InterfaceSink()
    client_node.link_remote(sink.olink_object_name())
    yield impl, sink

class TestOLinkSameEnum1Interface:

    def test_prop1(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_prop1_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop1(api.Enum1.VALUE1)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop1() == api.Enum1.VALUE1
        assert sink.get_prop1() == api.Enum1.VALUE1

    @pytest.mark.asyncio
    async def test_func1(self, olink_objects):
        impl, sink = olink_objects
        await sink.func1(param1=api.Enum1.VALUE1)

    def test_sig1(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig1 += lambda *args: setattr(self, 'called', True)
        impl._sig1(api.Enum1.VALUE1)
        assert self.called == True
