
from tb_same2.api import api
from tb_same2.impl import SameStruct2Interface
from tb_same2.olink import SameStruct2InterfaceSource, SameStruct2InterfaceSink
import tb_same2.test_helpers.test_struct
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest
from typing import Any
import asyncio

@pytest.fixture()
def olink_objects():
    impl = SameStruct2Interface()
    SameStruct2InterfaceSource(impl)
    remote_node = RemoteNode()
    client_node = ClientNode()

    remote_node.on_write(client_node.handle_message)
    client_node.on_write(remote_node.handle_message)

    sink = SameStruct2InterfaceSink()
    client_node.link_remote(sink.olink_object_name())
    yield impl, sink

class TestOLinkSameStruct2Interface:

    def test_prop1(self, olink_objects):
        impl, sink = olink_objects
        is_prop1_changed = False
        def funProp(arguments):
            nonlocal is_prop1_changed
            is_prop1_changed = True
        sink.on_prop1_changed += funProp
        test_value = tb_same2.test_helpers.test_struct.fillTestStruct2(api.Struct2())

        sink.set_prop1(test_value)
        assert is_prop1_changed == True
        assert impl.get_prop1() == test_value
        assert sink.get_prop1() == test_value

    def test_prop2(self, olink_objects):
        impl, sink = olink_objects
        is_prop2_changed = False
        def funProp(arguments):
            nonlocal is_prop2_changed
            is_prop2_changed = True
        sink.on_prop2_changed += funProp
        test_value = tb_same2.test_helpers.test_struct.fillTestStruct2(api.Struct2())

        sink.set_prop2(test_value)
        assert is_prop2_changed == True
        assert impl.get_prop2() == test_value
        assert sink.get_prop2() == test_value

    @pytest.mark.asyncio
    async def test_func1(self, olink_objects):
        impl, sink = olink_objects
        await sink.func1(param1=api.Struct1())

    @pytest.mark.asyncio
    async def test_func2(self, olink_objects):
        impl, sink = olink_objects
        await sink.func2(param1=api.Struct1(), param2=api.Struct2())

    def test_sig1(self, olink_objects):
        impl, sink = olink_objects
        is_sig1_called = False
        local_param1_struct = tb_same2.test_helpers.test_struct.fillTestStruct1(api.Struct1())

        def funSignal(param1):
            assert param1 ==local_param1_struct
            nonlocal is_sig1_called
            is_sig1_called = True

        sink.on_sig1 += funSignal


        impl._sig1(local_param1_struct)
        assert is_sig1_called == True

    def test_sig2(self, olink_objects):
        impl, sink = olink_objects
        is_sig2_called = False
        local_param1_struct = tb_same2.test_helpers.test_struct.fillTestStruct1(api.Struct1())
        local_param2_struct = tb_same2.test_helpers.test_struct.fillTestStruct2(api.Struct2())

        def funSignal(param1, param2):
            assert param1 ==local_param1_struct
            assert param2 ==local_param2_struct
            nonlocal is_sig2_called
            is_sig2_called = True

        sink.on_sig2 += funSignal


        impl._sig2(local_param1_struct, local_param2_struct)
        assert is_sig2_called == True
