
from testbed2_api import api
from testbed2_impl import NestedStruct2Interface
from testbed2_olink import NestedStruct2InterfaceSource, NestedStruct2InterfaceSink
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest

@pytest.fixture()
def olink_objects():
    impl = NestedStruct2Interface()
    NestedStruct2InterfaceSource(impl)
    remote_node = RemoteNode()
    client_node = ClientNode()

    remote_node.on_write(client_node.handle_message)
    client_node.on_write(remote_node.handle_message)

    sink = NestedStruct2InterfaceSink()
    client_node.link_remote(sink.olink_object_name())
    yield impl, sink

class TestOLinkNestedStruct2Interface:

    def test_prop1(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_prop1_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop1(api.NestedStruct1())
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop1() == api.NestedStruct1()
        assert sink.get_prop1() == api.NestedStruct1()

    def test_prop2(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_prop2_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop2(api.NestedStruct2())
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop2() == api.NestedStruct2()
        assert sink.get_prop2() == api.NestedStruct2()

    @pytest.mark.asyncio
    async def test_func1(self, olink_objects):
        impl, sink = olink_objects
        await sink.func1(param1=api.NestedStruct1())

    @pytest.mark.asyncio
    async def test_func2(self, olink_objects):
        impl, sink = olink_objects
        await sink.func2(param1=api.NestedStruct1(), param2=api.NestedStruct2())

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
