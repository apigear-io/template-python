
from testbed2.api import api
from testbed2.impl import NestedStruct3Interface
from testbed2.olink import NestedStruct3InterfaceSource, NestedStruct3InterfaceSink
import testbed2.test_helpers.test_struct
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest
from typing import Any
import asyncio

@pytest.fixture()
def olink_objects():
    impl = NestedStruct3Interface()
    NestedStruct3InterfaceSource(impl)
    remote_node = RemoteNode()
    client_node = ClientNode()

    remote_node.on_write(client_node.handle_message)
    client_node.on_write(remote_node.handle_message)

    sink = NestedStruct3InterfaceSink()
    client_node.link_remote(sink.olink_object_name())
    yield impl, sink

class TestOLinkNestedStruct3Interface:

    def test_prop1(self, olink_objects):
        impl, sink = olink_objects
        is_prop1_changed = False
        def funProp(arguments):
            nonlocal is_prop1_changed
            is_prop1_changed = True
        sink.on_prop1_changed += funProp
        test_value = testbed2.test_helpers.test_struct.fillTestNestedStruct1(api.NestedStruct1())

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
        test_value = testbed2.test_helpers.test_struct.fillTestNestedStruct2(api.NestedStruct2())

        sink.set_prop2(test_value)
        assert is_prop2_changed == True
        assert impl.get_prop2() == test_value
        assert sink.get_prop2() == test_value

    def test_prop3(self, olink_objects):
        impl, sink = olink_objects
        is_prop3_changed = False
        def funProp(arguments):
            nonlocal is_prop3_changed
            is_prop3_changed = True
        sink.on_prop3_changed += funProp
        test_value = testbed2.test_helpers.test_struct.fillTestNestedStruct3(api.NestedStruct3())

        sink.set_prop3(test_value)
        assert is_prop3_changed == True
        assert impl.get_prop3() == test_value
        assert sink.get_prop3() == test_value

    @pytest.mark.asyncio
    async def test_func1(self, olink_objects):
        impl, sink = olink_objects
        await sink.func1(param1=api.NestedStruct1())

    @pytest.mark.asyncio
    async def test_func2(self, olink_objects):
        impl, sink = olink_objects
        await sink.func2(param1=api.NestedStruct1(), param2=api.NestedStruct2())

    @pytest.mark.asyncio
    async def test_func3(self, olink_objects):
        impl, sink = olink_objects
        await sink.func3(param1=api.NestedStruct1(), param2=api.NestedStruct2(), param3=api.NestedStruct3())

    def test_sig1(self, olink_objects):
        impl, sink = olink_objects
        is_sig1_called = False
        local_param1_struct = testbed2.test_helpers.test_struct.fillTestNestedStruct1(api.NestedStruct1())

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
        local_param1_struct = testbed2.test_helpers.test_struct.fillTestNestedStruct1(api.NestedStruct1())
        local_param2_struct = testbed2.test_helpers.test_struct.fillTestNestedStruct2(api.NestedStruct2())

        def funSignal(param1, param2):
            assert param1 ==local_param1_struct
            assert param2 ==local_param2_struct
            nonlocal is_sig2_called
            is_sig2_called = True

        sink.on_sig2 += funSignal


        impl._sig2(local_param1_struct, local_param2_struct)
        assert is_sig2_called == True

    def test_sig3(self, olink_objects):
        impl, sink = olink_objects
        is_sig3_called = False
        local_param1_struct = testbed2.test_helpers.test_struct.fillTestNestedStruct1(api.NestedStruct1())
        local_param2_struct = testbed2.test_helpers.test_struct.fillTestNestedStruct2(api.NestedStruct2())
        local_param3_struct = testbed2.test_helpers.test_struct.fillTestNestedStruct3(api.NestedStruct3())

        def funSignal(param1, param2, param3):
            assert param1 ==local_param1_struct
            assert param2 ==local_param2_struct
            assert param3 ==local_param3_struct
            nonlocal is_sig3_called
            is_sig3_called = True

        sink.on_sig3 += funSignal


        impl._sig3(local_param1_struct, local_param2_struct, local_param3_struct)
        assert is_sig3_called == True
