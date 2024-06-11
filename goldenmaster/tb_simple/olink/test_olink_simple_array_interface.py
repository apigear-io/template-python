
from tb_simple.api import api
from tb_simple.impl import SimpleArrayInterface
from tb_simple.olink import SimpleArrayInterfaceSource, SimpleArrayInterfaceSink
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest

@pytest.fixture()
def olink_objects():
    impl = SimpleArrayInterface()
    SimpleArrayInterfaceSource(impl)
    remote_node = RemoteNode()
    client_node = ClientNode()

    remote_node.on_write(client_node.handle_message)
    client_node.on_write(remote_node.handle_message)

    sink = SimpleArrayInterfaceSink()
    client_node.link_remote(sink.olink_object_name())
    yield impl, sink

class TestOLinkSimpleArrayInterface:

    def test_prop_bool(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_prop_bool_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop_bool([])
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop_bool() == []
        assert sink.get_prop_bool() == []

    def test_prop_int(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_prop_int_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop_int([])
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop_int() == []
        assert sink.get_prop_int() == []

    def test_prop_int32(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_prop_int32_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop_int32([])
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop_int32() == []
        assert sink.get_prop_int32() == []

    def test_prop_int64(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_prop_int64_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop_int64([])
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop_int64() == []
        assert sink.get_prop_int64() == []

    def test_prop_float(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_prop_float_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop_float([])
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop_float() == []
        assert sink.get_prop_float() == []

    def test_prop_float32(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_prop_float32_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop_float32([])
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop_float32() == []
        assert sink.get_prop_float32() == []

    def test_prop_float64(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_prop_float64_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop_float64([])
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop_float64() == []
        assert sink.get_prop_float64() == []

    def test_prop_string(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_prop_string_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop_string([])
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop_string() == []
        assert sink.get_prop_string() == []

    @pytest.mark.asyncio
    async def test_func_bool(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_bool(param_bool=[])

    @pytest.mark.asyncio
    async def test_func_int(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_int(param_int=[])

    @pytest.mark.asyncio
    async def test_func_int32(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_int32(param_int32=[])

    @pytest.mark.asyncio
    async def test_func_int64(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_int64(param_int64=[])

    @pytest.mark.asyncio
    async def test_func_float(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_float(param_float=[])

    @pytest.mark.asyncio
    async def test_func_float32(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_float32(param_float32=[])

    @pytest.mark.asyncio
    async def test_func_float64(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_float64(param_float=[])

    @pytest.mark.asyncio
    async def test_func_string(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_string(param_string=[])

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

    def test_sig_int32(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig_int32 += lambda *args: setattr(self, 'called', True)
        impl._sig_int32([])
        assert self.called == True

    def test_sig_int64(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig_int64 += lambda *args: setattr(self, 'called', True)
        impl._sig_int64([])
        assert self.called == True

    def test_sig_float(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig_float += lambda *args: setattr(self, 'called', True)
        impl._sig_float([])
        assert self.called == True

    def test_sig_float32(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig_float32 += lambda *args: setattr(self, 'called', True)
        impl._sig_float32([])
        assert self.called == True

    def test_sig_float64(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig_float64 += lambda *args: setattr(self, 'called', True)
        impl._sig_float64([])
        assert self.called == True

    def test_sig_string(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig_string += lambda *args: setattr(self, 'called', True)
        impl._sig_string([])
        assert self.called == True
