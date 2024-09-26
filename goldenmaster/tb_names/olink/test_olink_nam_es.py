
from tb_names.api import api
from tb_names.impl import NamEs
from tb_names.olink import NamEsSource, NamEsSink
import tb_names.test_helpers.test_struct
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest
from typing import Any
import asyncio

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
        is_switch_changed = False
        def funProp(arguments):
            nonlocal is_switch_changed
            is_switch_changed = True
        sink.on_switch_changed += funProp
        test_value = True

        sink.set_switch(test_value)
        assert is_switch_changed == True
        assert impl.get_switch() == test_value
        assert sink.get_switch() == test_value

    def test_some_property(self, olink_objects):
        impl, sink = olink_objects
        is_some_property_changed = False
        def funProp(arguments):
            nonlocal is_some_property_changed
            is_some_property_changed = True
        sink.on_some_property_changed += funProp
        test_value = 1

        sink.set_some_property(test_value)
        assert is_some_property_changed == True
        assert impl.get_some_property() == test_value
        assert sink.get_some_property() == test_value

    def test_some_poperty2(self, olink_objects):
        impl, sink = olink_objects
        is_some_poperty2_changed = False
        def funProp(arguments):
            nonlocal is_some_poperty2_changed
            is_some_poperty2_changed = True
        sink.on_some_poperty2_changed += funProp
        test_value = 1

        sink.set_some_poperty2(test_value)
        assert is_some_poperty2_changed == True
        assert impl.get_some_poperty2() == test_value
        assert sink.get_some_poperty2() == test_value

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
        is_some_signal_called = False

        def funSignal(some_param):
            assert some_param == True
            nonlocal is_some_signal_called
            is_some_signal_called = True

        sink.on_some_signal += funSignal


        impl._some_signal(True)
        assert is_some_signal_called == True

    def test_some_signal2(self, olink_objects):
        impl, sink = olink_objects
        is_some_signal2_called = False

        def funSignal(some_param):
            assert some_param == True
            nonlocal is_some_signal2_called
            is_some_signal2_called = True

        sink.on_some_signal2 += funSignal


        impl._some_signal2(True)
        assert is_some_signal2_called == True
