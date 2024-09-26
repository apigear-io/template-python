
from tb_simple.api import api
from tb_simple.impl import SimpleInterface
from tb_simple.olink import SimpleInterfaceSource, SimpleInterfaceSink
import tb_simple.test_helpers.test_struct
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest
from typing import Any
import asyncio

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
        is_prop_bool_changed = False
        def funProp(arguments):
            nonlocal is_prop_bool_changed
            is_prop_bool_changed = True
        sink.on_prop_bool_changed += funProp
        test_value = True

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
        test_value = 1

        sink.set_prop_int(test_value)
        assert is_prop_int_changed == True
        assert impl.get_prop_int() == test_value
        assert sink.get_prop_int() == test_value

    def test_prop_int32(self, olink_objects):
        impl, sink = olink_objects
        is_prop_int32_changed = False
        def funProp(arguments):
            nonlocal is_prop_int32_changed
            is_prop_int32_changed = True
        sink.on_prop_int32_changed += funProp
        test_value = 1

        sink.set_prop_int32(test_value)
        assert is_prop_int32_changed == True
        assert impl.get_prop_int32() == test_value
        assert sink.get_prop_int32() == test_value

    def test_prop_int64(self, olink_objects):
        impl, sink = olink_objects
        is_prop_int64_changed = False
        def funProp(arguments):
            nonlocal is_prop_int64_changed
            is_prop_int64_changed = True
        sink.on_prop_int64_changed += funProp
        test_value = 1

        sink.set_prop_int64(test_value)
        assert is_prop_int64_changed == True
        assert impl.get_prop_int64() == test_value
        assert sink.get_prop_int64() == test_value

    def test_prop_float(self, olink_objects):
        impl, sink = olink_objects
        is_prop_float_changed = False
        def funProp(arguments):
            nonlocal is_prop_float_changed
            is_prop_float_changed = True
        sink.on_prop_float_changed += funProp
        test_value = 1.1

        sink.set_prop_float(test_value)
        assert is_prop_float_changed == True
        assert impl.get_prop_float() == test_value
        assert sink.get_prop_float() == test_value

    def test_prop_float32(self, olink_objects):
        impl, sink = olink_objects
        is_prop_float32_changed = False
        def funProp(arguments):
            nonlocal is_prop_float32_changed
            is_prop_float32_changed = True
        sink.on_prop_float32_changed += funProp
        test_value = 1.1

        sink.set_prop_float32(test_value)
        assert is_prop_float32_changed == True
        assert impl.get_prop_float32() == test_value
        assert sink.get_prop_float32() == test_value

    def test_prop_float64(self, olink_objects):
        impl, sink = olink_objects
        is_prop_float64_changed = False
        def funProp(arguments):
            nonlocal is_prop_float64_changed
            is_prop_float64_changed = True
        sink.on_prop_float64_changed += funProp
        test_value = 1.1

        sink.set_prop_float64(test_value)
        assert is_prop_float64_changed == True
        assert impl.get_prop_float64() == test_value
        assert sink.get_prop_float64() == test_value

    def test_prop_string(self, olink_objects):
        impl, sink = olink_objects
        is_prop_string_changed = False
        def funProp(arguments):
            nonlocal is_prop_string_changed
            is_prop_string_changed = True
        sink.on_prop_string_changed += funProp
        test_value = "xyz"

        sink.set_prop_string(test_value)
        assert is_prop_string_changed == True
        assert impl.get_prop_string() == test_value
        assert sink.get_prop_string() == test_value

    @pytest.mark.asyncio
    async def test_func_no_return_value(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_no_return_value(param_bool=False)

    @pytest.mark.asyncio
    async def test_func_bool(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_bool(param_bool=False)

    @pytest.mark.asyncio
    async def test_func_int(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_int(param_int=0)

    @pytest.mark.asyncio
    async def test_func_int32(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_int32(param_int32=0)

    @pytest.mark.asyncio
    async def test_func_int64(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_int64(param_int64=0)

    @pytest.mark.asyncio
    async def test_func_float(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_float(param_float=0.0)

    @pytest.mark.asyncio
    async def test_func_float32(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_float32(param_float32=0.0)

    @pytest.mark.asyncio
    async def test_func_float64(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_float64(param_float=0.0)

    @pytest.mark.asyncio
    async def test_func_string(self, olink_objects):
        impl, sink = olink_objects
        await sink.func_string(param_string="")

    def test_sig_bool(self, olink_objects):
        impl, sink = olink_objects
        is_sig_bool_called = False

        def funSignal(param_bool):
            assert param_bool == True
            nonlocal is_sig_bool_called
            is_sig_bool_called = True

        sink.on_sig_bool += funSignal


        impl._sig_bool(True)
        assert is_sig_bool_called == True

    def test_sig_int(self, olink_objects):
        impl, sink = olink_objects
        is_sig_int_called = False

        def funSignal(param_int):
            assert param_int == 1
            nonlocal is_sig_int_called
            is_sig_int_called = True

        sink.on_sig_int += funSignal


        impl._sig_int(1)
        assert is_sig_int_called == True

    def test_sig_int32(self, olink_objects):
        impl, sink = olink_objects
        is_sig_int32_called = False

        def funSignal(param_int32):
            assert param_int32 == 1
            nonlocal is_sig_int32_called
            is_sig_int32_called = True

        sink.on_sig_int32 += funSignal


        impl._sig_int32(1)
        assert is_sig_int32_called == True

    def test_sig_int64(self, olink_objects):
        impl, sink = olink_objects
        is_sig_int64_called = False

        def funSignal(param_int64):
            assert param_int64 == 1
            nonlocal is_sig_int64_called
            is_sig_int64_called = True

        sink.on_sig_int64 += funSignal


        impl._sig_int64(1)
        assert is_sig_int64_called == True

    def test_sig_float(self, olink_objects):
        impl, sink = olink_objects
        is_sig_float_called = False

        def funSignal(param_float):
            assert param_float == 1.1
            nonlocal is_sig_float_called
            is_sig_float_called = True

        sink.on_sig_float += funSignal


        impl._sig_float(1.1)
        assert is_sig_float_called == True

    def test_sig_float32(self, olink_objects):
        impl, sink = olink_objects
        is_sig_float32_called = False

        def funSignal(param_float32):
            assert param_float32 == 1.1
            nonlocal is_sig_float32_called
            is_sig_float32_called = True

        sink.on_sig_float32 += funSignal


        impl._sig_float32(1.1)
        assert is_sig_float32_called == True

    def test_sig_float64(self, olink_objects):
        impl, sink = olink_objects
        is_sig_float64_called = False

        def funSignal(param_float64):
            assert param_float64 == 1.1
            nonlocal is_sig_float64_called
            is_sig_float64_called = True

        sink.on_sig_float64 += funSignal


        impl._sig_float64(1.1)
        assert is_sig_float64_called == True

    def test_sig_string(self, olink_objects):
        impl, sink = olink_objects
        is_sig_string_called = False

        def funSignal(param_string):
            assert param_string == "xyz"
            nonlocal is_sig_string_called
            is_sig_string_called = True

        sink.on_sig_string += funSignal


        impl._sig_string("xyz")
        assert is_sig_string_called == True
