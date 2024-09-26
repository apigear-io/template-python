
from counter.api import api
from counter.impl import Counter
from counter.olink import CounterSource, CounterSink
import counter.test_helpers.test_struct
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest
from typing import Any
import asyncio
import custom_types.api
import custom_types.test_helpers.test_struct
import extern_types.api
import extern_types.test_helpers.test_struct
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
        is_vector_changed = False
        def funProp(arguments):
            nonlocal is_vector_changed
            is_vector_changed = True
        sink.on_vector_changed += funProp
        test_value = custom_types.test_helpers.test_struct.fillTestVector3D(custom_types.api.Vector3D())

        sink.set_vector(test_value)
        assert is_vector_changed == True
        assert impl.get_vector() == test_value
        assert sink.get_vector() == test_value

    def test_extern_vector(self, olink_objects):
        pass

    @pytest.mark.asyncio
    async def test_increment(self, olink_objects):
        impl, sink = olink_objects
        await sink.increment(vec=vector3d.vector.Vector())

    @pytest.mark.asyncio
    async def test_decrement(self, olink_objects):
        impl, sink = olink_objects
        await sink.decrement(vec=custom_types.api.Vector3D())
