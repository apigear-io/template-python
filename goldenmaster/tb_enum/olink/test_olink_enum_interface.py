
from tb_enum.api import api
from tb_enum.impl import EnumInterface
from tb_enum.olink import EnumInterfaceSource, EnumInterfaceSink
import tb_enum.test_helpers.test_struct
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest
from typing import Any
import asyncio

@pytest.fixture()
def olink_objects():
    impl = EnumInterface()
    EnumInterfaceSource(impl)
    remote_node = RemoteNode()
    client_node = ClientNode()

    remote_node.on_write(client_node.handle_message)
    client_node.on_write(remote_node.handle_message)

    sink = EnumInterfaceSink()
    client_node.link_remote(sink.olink_object_name())
    yield impl, sink

class TestOLinkEnumInterface:

    def test_prop0(self, olink_objects):
        impl, sink = olink_objects
        is_prop0_changed = False
        def funProp(arguments):
            nonlocal is_prop0_changed
            is_prop0_changed = True
        sink.on_prop0_changed += funProp
        test_value = api.Enum0.VALUE1

        sink.set_prop0(test_value)
        assert is_prop0_changed == True
        assert impl.get_prop0() == test_value
        assert sink.get_prop0() == test_value

    def test_prop1(self, olink_objects):
        impl, sink = olink_objects
        is_prop1_changed = False
        def funProp(arguments):
            nonlocal is_prop1_changed
            is_prop1_changed = True
        sink.on_prop1_changed += funProp
        test_value = api.Enum1.VALUE2

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
        test_value = api.Enum2.VALUE1

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
        test_value = api.Enum3.VALUE2

        sink.set_prop3(test_value)
        assert is_prop3_changed == True
        assert impl.get_prop3() == test_value
        assert sink.get_prop3() == test_value

    @pytest.mark.asyncio
    async def test_func0(self, olink_objects):
        impl, sink = olink_objects
        await sink.func0(param0=api.Enum0.VALUE0)

    @pytest.mark.asyncio
    async def test_func1(self, olink_objects):
        impl, sink = olink_objects
        await sink.func1(param1=api.Enum1.VALUE1)

    @pytest.mark.asyncio
    async def test_func2(self, olink_objects):
        impl, sink = olink_objects
        await sink.func2(param2=api.Enum2.VALUE2)

    @pytest.mark.asyncio
    async def test_func3(self, olink_objects):
        impl, sink = olink_objects
        await sink.func3(param3=api.Enum3.VALUE3)

    def test_sig0(self, olink_objects):
        impl, sink = olink_objects
        is_sig0_called = False

        def funSignal(param0):
            assert param0 == api.Enum0.VALUE1
            nonlocal is_sig0_called
            is_sig0_called = True

        sink.on_sig0 += funSignal


        impl._sig0(api.Enum0.VALUE1)
        assert is_sig0_called == True

    def test_sig1(self, olink_objects):
        impl, sink = olink_objects
        is_sig1_called = False

        def funSignal(param1):
            assert param1 == api.Enum1.VALUE2
            nonlocal is_sig1_called
            is_sig1_called = True

        sink.on_sig1 += funSignal


        impl._sig1(api.Enum1.VALUE2)
        assert is_sig1_called == True

    def test_sig2(self, olink_objects):
        impl, sink = olink_objects
        is_sig2_called = False

        def funSignal(param2):
            assert param2 == api.Enum2.VALUE1
            nonlocal is_sig2_called
            is_sig2_called = True

        sink.on_sig2 += funSignal


        impl._sig2(api.Enum2.VALUE1)
        assert is_sig2_called == True

    def test_sig3(self, olink_objects):
        impl, sink = olink_objects
        is_sig3_called = False

        def funSignal(param3):
            assert param3 == api.Enum3.VALUE2
            nonlocal is_sig3_called
            is_sig3_called = True

        sink.on_sig3 += funSignal


        impl._sig3(api.Enum3.VALUE2)
        assert is_sig3_called == True
