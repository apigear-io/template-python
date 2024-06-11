
from tb_same1.api import api
from tb_same1.impl import SameEnum2Interface
from tb_same1.olink import SameEnum2InterfaceSource, SameEnum2InterfaceSink
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest

@pytest.fixture()
def olink_objects():
    impl = SameEnum2Interface()
    SameEnum2InterfaceSource(impl)
    remote_node = RemoteNode()
    client_node = ClientNode()

    remote_node.on_write(client_node.handle_message)
    client_node.on_write(remote_node.handle_message)

    sink = SameEnum2InterfaceSink()
    client_node.link_remote(sink.olink_object_name())
    yield impl, sink

class TestOLinkSameEnum2Interface:

    def test_prop1(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_prop1_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop1(api.Enum1.VALUE1)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop1() == api.Enum1.VALUE1
        assert sink.get_prop1() == api.Enum1.VALUE1

    def test_prop2(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_prop2_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop2(api.Enum2.VALUE1)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop2() == api.Enum2.VALUE1
        assert sink.get_prop2() == api.Enum2.VALUE1

    @pytest.mark.asyncio
    async def test_func1(self, olink_objects):
        impl, sink = olink_objects
        await sink.func1(param1=api.Enum1.VALUE1)

    @pytest.mark.asyncio
    async def test_func2(self, olink_objects):
        impl, sink = olink_objects
        await sink.func2(param1=api.Enum1.VALUE1, param2=api.Enum2.VALUE1)

    def test_sig1(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig1 += lambda *args: setattr(self, 'called', True)
        impl._sig1(api.Enum1.VALUE1)
        assert self.called == True

    def test_sig2(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig2 += lambda *args: setattr(self, 'called', True)
        impl._sig2(api.Enum1.VALUE1, api.Enum2.VALUE1)
        assert self.called == True
