
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

    def test_vector_array(self, olink_objects):
        impl, sink = olink_objects
        is_vector_array_changed = False
        def funProp(arguments):
            nonlocal is_vector_array_changed
            is_vector_array_changed = True
        sink.on_vector_array_changed += funProp
        test_value = []
        test_value.append(custom_types.test_helpers.test_struct.fillTestVector3D(custom_types.api.Vector3D()))

        sink.set_vector_array(test_value)
        assert is_vector_array_changed == True
        assert impl.get_vector_array() == test_value
        assert sink.get_vector_array() == test_value

    def test_extern_vector_array(self, olink_objects):
        pass

    @pytest.mark.asyncio
    async def test_increment(self, olink_objects):
        impl, sink = olink_objects
        await sink.increment(vec=vector3d.vector.Vector())

    @pytest.mark.asyncio
    async def test_increment_array(self, olink_objects):
        impl, sink = olink_objects
        await sink.increment_array(vec=[])

    @pytest.mark.asyncio
    async def test_decrement(self, olink_objects):
        impl, sink = olink_objects
        await sink.decrement(vec=custom_types.api.Vector3D())

    @pytest.mark.asyncio
    async def test_decrement_array(self, olink_objects):
        impl, sink = olink_objects
        await sink.decrement_array(vec=[])

    def test_value_changed(self, olink_objects):
        impl, sink = olink_objects
        is_value_changed_called = False
        local_vector_struct = custom_types.test_helpers.test_struct.fillTestVector3D(custom_types.api.Vector3D())
        local_vector_array_array = []
        local_vector_array_array.append(custom_types.test_helpers.test_struct.fillTestVector3D(custom_types.api.Vector3D()))
        local_extern_vector_array_array = []
        local_extern_vector_array_array.append(vector3d.vector.Vector())

        def funSignal(vector, extern_vector, vector_array, extern_vector_array):
            assert vector ==local_vector_struct
            assert extern_vector == vector3d.vector.Vector()
            assert vector_array == local_vector_array_array
            assert extern_vector_array == local_extern_vector_array_array
            nonlocal is_value_changed_called
            is_value_changed_called = True

        sink.on_value_changed += funSignal


        impl._value_changed(local_vector_struct, vector3d.vector.Vector(), local_vector_array_array, local_extern_vector_array_array)
        assert is_value_changed_called == True
