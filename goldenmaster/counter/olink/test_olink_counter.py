
from counter.api import api
from counter.impl import Counter
from counter.olink import CounterSource, CounterSink
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest
import custom_types.api
import extern_types.api
import vector3d.vector

@pytest.fixture()
def olink_objects():
    impl = Counter()
    CounterSource(impl)
    remote_node = RemoteNode()
    client_node = ClientNode()

    remote_node.on_write(client_node.handle_message)
    client_node.on_write(remote_node.handle_message)

    sink = CounterSink()
    client_node.link_remote(sink.olink_object_name())
    yield impl, sink

class TestOLinkCounter:

    def test_vector(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_vector_changed += lambda *args: setattr(self, 'called', True)
        sink.set_vector(custom_types.api.Vector3D())
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_vector() == custom_types.api.Vector3D()
        assert sink.get_vector() == custom_types.api.Vector3D()

    def test_extern_vector(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_extern_vector_changed += lambda *args: setattr(self, 'called', True)
        sink.set_extern_vector(vector3d.vector.Vector())
        # should not be true since we are not changing the default value
        assert self.called == False
        assert impl.get_extern_vector() == vector3d.vector.Vector()
        assert sink.get_extern_vector() == vector3d.vector.Vector()

    @pytest.mark.asyncio
    async def test_increment(self, olink_objects):
        impl, sink = olink_objects
        await sink.increment(vec=vector3d.vector.Vector())

    @pytest.mark.asyncio
    async def test_decrement(self, olink_objects):
        impl, sink = olink_objects
        await sink.decrement(vec=custom_types.api.Vector3D())
    pass
