
from testbed2.api import api
from testbed2.impl import ManyParamInterface
from testbed2.olink import ManyParamInterfaceSource, ManyParamInterfaceSink
import testbed2.test_helpers.test_struct
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest
from typing import Any
import asyncio

@pytest.fixture()
def olink_objects():
    impl = ManyParamInterface()
    ManyParamInterfaceSource(impl)
    remote_node = RemoteNode()
    client_node = ClientNode()

    remote_node.on_write(client_node.handle_message)
    client_node.on_write(remote_node.handle_message)

    sink = ManyParamInterfaceSink()
    client_node.link_remote(sink.olink_object_name())
    yield impl, sink

class TestOLinkManyParamInterface:

    def test_prop1(self, olink_objects):
        impl, sink = olink_objects
        is_prop1_changed = False
        def funProp(arguments):
            nonlocal is_prop1_changed
            is_prop1_changed = True
        sink.on_prop1_changed += funProp
        test_value = 1

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
        test_value = 1

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
        test_value = 1

        sink.set_prop3(test_value)
        assert is_prop3_changed == True
        assert impl.get_prop3() == test_value
        assert sink.get_prop3() == test_value

    def test_prop4(self, olink_objects):
        impl, sink = olink_objects
        is_prop4_changed = False
        def funProp(arguments):
            nonlocal is_prop4_changed
            is_prop4_changed = True
        sink.on_prop4_changed += funProp
        test_value = 1

        sink.set_prop4(test_value)
        assert is_prop4_changed == True
        assert impl.get_prop4() == test_value
        assert sink.get_prop4() == test_value

    @pytest.mark.asyncio
    async def test_func1(self, olink_objects):
        impl, sink = olink_objects
        await sink.func1(param1=0)

    @pytest.mark.asyncio
    async def test_func2(self, olink_objects):
        impl, sink = olink_objects
        await sink.func2(param1=0, param2=0)

    @pytest.mark.asyncio
    async def test_func3(self, olink_objects):
        impl, sink = olink_objects
        await sink.func3(param1=0, param2=0, param3=0)

    @pytest.mark.asyncio
    async def test_func4(self, olink_objects):
        impl, sink = olink_objects
        await sink.func4(param1=0, param2=0, param3=0, param4=0)

    def test_sig1(self, olink_objects):
        impl, sink = olink_objects
        is_sig1_called = False

        def funSignal(param1):
            assert param1 == 1
            nonlocal is_sig1_called
            is_sig1_called = True

        sink.on_sig1 += funSignal


        impl._sig1(1)
        assert is_sig1_called == True

    def test_sig2(self, olink_objects):
        impl, sink = olink_objects
        is_sig2_called = False

        def funSignal(param1, param2):
            assert param1 == 1
            assert param2 == 1
            nonlocal is_sig2_called
            is_sig2_called = True

        sink.on_sig2 += funSignal


        impl._sig2(1, 1)
        assert is_sig2_called == True

    def test_sig3(self, olink_objects):
        impl, sink = olink_objects
        is_sig3_called = False

        def funSignal(param1, param2, param3):
            assert param1 == 1
            assert param2 == 1
            assert param3 == 1
            nonlocal is_sig3_called
            is_sig3_called = True

        sink.on_sig3 += funSignal


        impl._sig3(1, 1, 1)
        assert is_sig3_called == True

    def test_sig4(self, olink_objects):
        impl, sink = olink_objects
        is_sig4_called = False

        def funSignal(param1, param2, param3, param4):
            assert param1 == 1
            assert param2 == 1
            assert param3 == 1
            assert param4 == 1
            nonlocal is_sig4_called
            is_sig4_called = True

        sink.on_sig4 += funSignal


        impl._sig4(1, 1, 1, 1)
        assert is_sig4_called == True
