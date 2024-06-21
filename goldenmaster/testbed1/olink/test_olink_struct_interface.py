
from testbed1.api import api
from testbed1.impl import StructInterface
from testbed1.olink import StructInterfaceSource, StructInterfaceSink
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest

@pytest.fixture()
def olink_objects():
    impl = StructInterface()
    StructInterfaceSource(impl)
    remote_node = RemoteNode()
    client_node = ClientNode()

    remote_node.on_write(client_node.handle_message)
    client_node.on_write(remote_node.handle_message)

    sink = StructInterfaceSink()
    client_node.link_remote(sink.olink_object_name())
    yield impl, sink

class TestOLinkStructInterface:

    def test_prop_bool(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_prop_bool_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop_bool(api.StructBool())
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop_bool() == api.StructBool()
        assert sink.get_prop_bool() == api.StructBool()

    def test_prop_int(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_prop_int_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop_int(api.StructInt())
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop_int() == api.StructInt()
        assert sink.get_prop_int() == api.StructInt()

    def test_prop_float(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_prop_float_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop_float(api.StructFloat())
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop_float() == api.StructFloat()
        assert sink.get_prop_float() == api.StructFloat()

    def test_prop_string(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_prop_string_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop_string(api.StructString())
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop_string() == api.StructString()
        assert sink.get_prop_string() == api.StructString()

    @pytest.mark.asyncio
    async def test_func_bool(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_bool(param_bool=api.StructBool())

    @pytest.mark.asyncio
    async def test_func_int(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_int(param_int=api.StructInt())

    @pytest.mark.asyncio
    async def test_func_float(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_float(param_float=api.StructFloat())

    @pytest.mark.asyncio
    async def test_func_string(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_string(param_string=api.StructString())

    def test_sig_bool(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig_bool += lambda *args: setattr(self, 'called', True)
        impl._sig_bool(api.StructBool())
        assert self.called == True

    def test_sig_int(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig_int += lambda *args: setattr(self, 'called', True)
        impl._sig_int(api.StructInt())
        assert self.called == True

    def test_sig_float(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig_float += lambda *args: setattr(self, 'called', True)
        impl._sig_float(api.StructFloat())
        assert self.called == True

    def test_sig_string(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig_string += lambda *args: setattr(self, 'called', True)
        impl._sig_string(api.StructString())
        assert self.called == True
