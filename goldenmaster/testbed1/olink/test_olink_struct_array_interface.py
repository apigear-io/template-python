
from testbed1.api import api
from testbed1.impl import StructArrayInterface
from testbed1.olink import StructArrayInterfaceSource, StructArrayInterfaceSink
import testbed1.test_helpers.test_struct
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest
from typing import Any
import asyncio

@pytest.fixture()
def olink_objects():
    impl = StructArrayInterface()
    StructArrayInterfaceSource(impl)
    remote_node = RemoteNode()
    client_node = ClientNode()

    remote_node.on_write(client_node.handle_message)
    client_node.on_write(remote_node.handle_message)

    sink = StructArrayInterfaceSink()
    client_node.link_remote(sink.olink_object_name())
    yield impl, sink

class TestOLinkStructArrayInterface:

    def test_prop_bool(self, olink_objects):
        impl, sink = olink_objects
        is_prop_bool_changed = False
        def funProp(arguments):
            nonlocal is_prop_bool_changed
            is_prop_bool_changed = True
        sink.on_prop_bool_changed += funProp
        test_value = []
        test_value.append(testbed1.test_helpers.test_struct.fillTestStructBool(api.StructBool()))

        sink.set_prop_bool(test_value)
        assert is_prop_bool_changed == True
        assert impl.get_prop_bool() == test_value
        assert sink.get_prop_bool() == test_value

    def test_prop_int(self, olink_objects):
        impl, sink = olink_objects
        is_prop_int_changed = False
        def funProp(arguments):
            nonlocal is_prop_int_changed
            is_prop_int_changed = True
        sink.on_prop_int_changed += funProp
        test_value = []
        test_value.append(testbed1.test_helpers.test_struct.fillTestStructInt(api.StructInt()))

        sink.set_prop_int(test_value)
        assert is_prop_int_changed == True
        assert impl.get_prop_int() == test_value
        assert sink.get_prop_int() == test_value

    def test_prop_float(self, olink_objects):
        impl, sink = olink_objects
        is_prop_float_changed = False
        def funProp(arguments):
            nonlocal is_prop_float_changed
            is_prop_float_changed = True
        sink.on_prop_float_changed += funProp
        test_value = []
        test_value.append(testbed1.test_helpers.test_struct.fillTestStructFloat(api.StructFloat()))

        sink.set_prop_float(test_value)
        assert is_prop_float_changed == True
        assert impl.get_prop_float() == test_value
        assert sink.get_prop_float() == test_value

    def test_prop_string(self, olink_objects):
        impl, sink = olink_objects
        is_prop_string_changed = False
        def funProp(arguments):
            nonlocal is_prop_string_changed
            is_prop_string_changed = True
        sink.on_prop_string_changed += funProp
        test_value = []
        test_value.append(testbed1.test_helpers.test_struct.fillTestStructString(api.StructString()))

        sink.set_prop_string(test_value)
        assert is_prop_string_changed == True
        assert impl.get_prop_string() == test_value
        assert sink.get_prop_string() == test_value

    @pytest.mark.asyncio
    async def test_func_bool(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_bool(param_bool=[])

    @pytest.mark.asyncio
    async def test_func_int(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_int(param_int=[])

    @pytest.mark.asyncio
    async def test_func_float(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_float(param_float=[])

    @pytest.mark.asyncio
    async def test_func_string(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_string(param_string=[])

    def test_sig_bool(self, olink_objects):
        impl, sink = olink_objects
        is_sig_bool_called = False
        local_param_bool_array = []
        local_param_bool_array.append(testbed1.test_helpers.test_struct.fillTestStructBool(api.StructBool()))

        def funSignal(param_bool):
            assert param_bool == local_param_bool_array
            nonlocal is_sig_bool_called
            is_sig_bool_called = True

        sink.on_sig_bool += funSignal


        impl._sig_bool(local_param_bool_array)
        assert is_sig_bool_called == True

    def test_sig_int(self, olink_objects):
        impl, sink = olink_objects
        is_sig_int_called = False
        local_param_int_array = []
        local_param_int_array.append(testbed1.test_helpers.test_struct.fillTestStructInt(api.StructInt()))

        def funSignal(param_int):
            assert param_int == local_param_int_array
            nonlocal is_sig_int_called
            is_sig_int_called = True

        sink.on_sig_int += funSignal


        impl._sig_int(local_param_int_array)
        assert is_sig_int_called == True

    def test_sig_float(self, olink_objects):
        impl, sink = olink_objects
        is_sig_float_called = False
        local_param_float_array = []
        local_param_float_array.append(testbed1.test_helpers.test_struct.fillTestStructFloat(api.StructFloat()))

        def funSignal(param_float):
            assert param_float == local_param_float_array
            nonlocal is_sig_float_called
            is_sig_float_called = True

        sink.on_sig_float += funSignal


        impl._sig_float(local_param_float_array)
        assert is_sig_float_called == True

    def test_sig_string(self, olink_objects):
        impl, sink = olink_objects
        is_sig_string_called = False
        local_param_string_array = []
        local_param_string_array.append(testbed1.test_helpers.test_struct.fillTestStructString(api.StructString()))

        def funSignal(param_string):
            assert param_string == local_param_string_array
            nonlocal is_sig_string_called
            is_sig_string_called = True

        sink.on_sig_string += funSignal


        impl._sig_string(local_param_string_array)
        assert is_sig_string_called == True
