
from tb_names.api import api
from tb_names.impl import NamEs
from tb_names.olink import NamEsSource, NamEsSink
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest

@pytest.fixture()
def olink_objects():
    impl = NamEs()
    NamEsSource(impl)
    remote_node = RemoteNode()
    client_node = ClientNode()

    remote_node.on_write(client_node.handle_message)
    client_node.on_write(remote_node.handle_message)

    sink = NamEsSink()
    client_node.link_remote(sink.olink_object_name())
    yield impl, sink

class TestOLinkNamEs:

    def test_switch(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_switch_changed += lambda *args: setattr(self, 'called', True)
        sink.set_switch(False)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_switch() == False
        assert sink.get_switch() == False

    def test_some_property(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_some_property_changed += lambda *args: setattr(self, 'called', True)
        sink.set_some_property(0)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_some_property() == 0
        assert sink.get_some_property() == 0

    def test_some_poperty2(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_some_poperty2_changed += lambda *args: setattr(self, 'called', True)
        sink.set_some_poperty2(0)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_some_poperty2() == 0
        assert sink.get_some_poperty2() == 0

    @pytest.mark.asyncio
    async def test_some_function(self, olink_objects):
        impl, sink = olink_objects
        await sink.some_function(some_param=False)

    @pytest.mark.asyncio
    async def test_some_function2(self, olink_objects):
        impl, sink = olink_objects
        await sink.some_function2(some_param=False)

    def test_some_signal(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_some_signal += lambda *args: setattr(self, 'called', True)
        impl._some_signal(False)
        assert self.called == True

    def test_some_signal2(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_some_signal2 += lambda *args: setattr(self, 'called', True)
        impl._some_signal2(False)
        assert self.called == True
