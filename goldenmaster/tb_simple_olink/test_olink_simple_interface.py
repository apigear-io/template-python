
from tb_simple_api import api
from tb_simple_impl import SimpleInterface
from tb_simple_olink import SimpleInterfaceSource, SimpleInterfaceSink
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest

@pytest.fixture()
def olink_objects():
    impl = SimpleInterface()
    SimpleInterfaceSource(impl)
    remote_node = RemoteNode()
    client_node = ClientNode()

    remote_node.on_write(client_node.handle_message)
    client_node.on_write(remote_node.handle_message)

    sink = SimpleInterfaceSink()
    client_node.link_remote(sink.olink_object_name())
    yield impl, sink

class TestOLinkSimpleInterface:

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

    def test_prop_int32(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_prop_int32_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop_int32(0)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop_int32() == 0
        assert sink.get_prop_int32() == 0

    def test_prop_int64(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_prop_int64_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop_int64(0)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop_int64() == 0
        assert sink.get_prop_int64() == 0

    def test_prop_float(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_prop_float_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop_float(0.0)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop_float() == 0.0
        assert sink.get_prop_float() == 0.0

    def test_prop_float32(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_prop_float32_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop_float32(0.0)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop_float32() == 0.0
        assert sink.get_prop_float32() == 0.0

    def test_prop_float64(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_prop_float64_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop_float64(0.0)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop_float64() == 0.0
        assert sink.get_prop_float64() == 0.0

    def test_prop_string(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_prop_string_changed += lambda *args: setattr(self, 'called', True)
        sink.set_prop_string("")
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_prop_string() == ""
        assert sink.get_prop_string() == ""

    def test_prop_read_only_string(self, olink_objects):
        impl, sink = olink_objects
        assert impl.get_prop_read_only_string() == ""
        assert sink.get_prop_read_only_string() == ""

    def test_sig_void(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig_void += lambda *args: setattr(self, 'called', True)
        impl._sig_void()
        assert self.called == True

    def test_sig_bool(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig_bool += lambda *args: setattr(self, 'called', True)
        impl._sig_bool(False)
        assert self.called == True

    def test_sig_int(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig_int += lambda *args: setattr(self, 'called', True)
        impl._sig_int(0)
        assert self.called == True

    def test_sig_int32(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig_int32 += lambda *args: setattr(self, 'called', True)
        impl._sig_int32(0)
        assert self.called == True

    def test_sig_int64(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig_int64 += lambda *args: setattr(self, 'called', True)
        impl._sig_int64(0)
        assert self.called == True

    def test_sig_float(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig_float += lambda *args: setattr(self, 'called', True)
        impl._sig_float(0.0)
        assert self.called == True

    def test_sig_float32(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig_float32 += lambda *args: setattr(self, 'called', True)
        impl._sig_float32(0.0)
        assert self.called == True

    def test_sig_float64(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig_float64 += lambda *args: setattr(self, 'called', True)
        impl._sig_float64(0.0)
        assert self.called == True

    def test_sig_string(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_sig_string += lambda *args: setattr(self, 'called', True)
        impl._sig_string("")
        assert self.called == True
