
from tb_enum_api import api
from tb_enum_impl import EnumInterface
from tb_enum_olink import EnumInterfaceSource, EnumInterfaceSink
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest

@pytest.fixture()
def olink_objects():
    impl = EnumInterface()
    EnumInterfaceSource(impl)
    remote_node = RemoteNode()
    client_node = ClientNode()

    remote_node.on_write(client_node.handle_message)
    client_node.on_write(remote_node.handle_message)

    sink = EnumInterfaceSink()
    client_node.link_remote(sink.olink_object_name())
    yield impl, sink

class TestOLinkEnumInterface:

    def test_prop0(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_prop0_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop0(api.Enum0.VALUE0)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop0() == api.Enum0.VALUE0
        assert sink.get_prop0() == api.Enum0.VALUE0

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
        sink.set_prop2(api.Enum2.VALUE2)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop2() == api.Enum2.VALUE2
        assert sink.get_prop2() == api.Enum2.VALUE2

    def test_prop3(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_prop3_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop3(api.Enum3.VALUE3)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop3() == api.Enum3.VALUE3
        assert sink.get_prop3() == api.Enum3.VALUE3

    def test_sig0(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig0 += lambda *args: setattr(self, 'called', True)
        impl._sig0(api.Enum0.VALUE0)
        assert self.called == True

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
        impl._sig2(api.Enum2.VALUE2)
        assert self.called == True

    def test_sig3(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig3 += lambda *args: setattr(self, 'called', True)
        impl._sig3(api.Enum3.VALUE3)
        assert self.called == True
