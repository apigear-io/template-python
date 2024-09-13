import tb_enum.api
import tb_enum.impl
import tb_enum.mqtt
import tb_enum.test_helpers.test_struct
import apigear.mqtt
import pytest
from typing import Any
import asyncio

def set_event_ready(loop, event):
    def func():
        event.set()
    loop.call_soon_threadsafe(func)

class TestMqttEnumInterface:

    @pytest.mark.asyncio
    async def setup_mqtt(slef):
        impl = tb_enum.impl.EnumInterface()
        service = apigear.mqtt.Service("uniqueServiceIdTestEnumInterface")
        client = apigear.mqtt.Client("uniqueClientIdTestTestEnumInterface")
        serviceAdapter = tb_enum.mqtt.EnumInterfaceServiceAdapter(impl, service)
        sink = tb_enum.mqtt.EnumInterfaceClientAdapter(client)
     
        await service.connect("localhost", 1883)
        await client.connect("localhost", 1883)

        loop = asyncio.get_event_loop()

        is_client_ready = asyncio.Event()
        is_service_ready = asyncio.Event()

        def funClient():
            set_event_ready(loop, is_client_ready)
        def funServer():
            set_event_ready(loop, is_service_ready)
        sink.on_ready += funClient 
        serviceAdapter.on_ready += funServer

        async def coroutineService():
            await is_service_ready.wait()

        async def coroutineClient():
            await is_client_ready.wait()

        taskService = asyncio.create_task(coroutineService())
        taskClient = asyncio.create_task(coroutineClient())
        await asyncio.wait([taskService, taskClient], timeout=10.0, return_when=asyncio.ALL_COMPLETED)
        return impl, sink, serviceAdapter, client, service

    async def teardown_mqtt(self, service, client):
        service.disconnect()
        client.disconnect()

    @pytest.mark.asyncio
    async def test_prop0(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_prop0_changed_done = asyncio.Event()
        def funProp(arguments):
            set_event_ready(loop, is_prop0_changed_done )
        
        sink.on_prop0_changed += funProp
        test_value = tb_enum.api.Enum0.VALUE1
        
        sink.set_prop0(test_value)
        await is_prop0_changed_done.wait()
        assert impl.get_prop0() == test_value
        assert sink.get_prop0() == test_value
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_prop1(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_prop1_changed_done = asyncio.Event()
        def funProp(arguments):
            set_event_ready(loop, is_prop1_changed_done )
        
        sink.on_prop1_changed += funProp
        test_value = tb_enum.api.Enum1.VALUE2
        
        sink.set_prop1(test_value)
        await is_prop1_changed_done.wait()
        assert impl.get_prop1() == test_value
        assert sink.get_prop1() == test_value
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_prop2(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_prop2_changed_done = asyncio.Event()
        def funProp(arguments):
            set_event_ready(loop, is_prop2_changed_done )
        
        sink.on_prop2_changed += funProp
        test_value = tb_enum.api.Enum2.VALUE1
        
        sink.set_prop2(test_value)
        await is_prop2_changed_done.wait()
        assert impl.get_prop2() == test_value
        assert sink.get_prop2() == test_value
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_prop3(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_prop3_changed_done = asyncio.Event()
        def funProp(arguments):
            set_event_ready(loop, is_prop3_changed_done )
        
        sink.on_prop3_changed += funProp
        test_value = tb_enum.api.Enum3.VALUE2
        
        sink.set_prop3(test_value)
        await is_prop3_changed_done.wait()
        assert impl.get_prop3() == test_value
        assert sink.get_prop3() == test_value
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_sig0(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_sig0_changed_done = asyncio.Event()

        def funSignal(param0):
            assert param0 == tb_enum.api.Enum0.VALUE1
            set_event_ready(loop, is_sig0_changed_done )
        
        sink.on_sig0 += funSignal
        impl._sig0(tb_enum.api.Enum0.VALUE1)

        await is_sig0_changed_done.wait()
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_sig1(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_sig1_changed_done = asyncio.Event()

        def funSignal(param1):
            assert param1 == tb_enum.api.Enum1.VALUE2
            set_event_ready(loop, is_sig1_changed_done )
        
        sink.on_sig1 += funSignal
        impl._sig1(tb_enum.api.Enum1.VALUE2)

        await is_sig1_changed_done.wait()
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_sig2(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_sig2_changed_done = asyncio.Event()

        def funSignal(param2):
            assert param2 == tb_enum.api.Enum2.VALUE1
            set_event_ready(loop, is_sig2_changed_done )
        
        sink.on_sig2 += funSignal
        impl._sig2(tb_enum.api.Enum2.VALUE1)

        await is_sig2_changed_done.wait()
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_sig3(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_sig3_changed_done = asyncio.Event()

        def funSignal(param3):
            assert param3 == tb_enum.api.Enum3.VALUE2
            set_event_ready(loop, is_sig3_changed_done )
        
        sink.on_sig3 += funSignal
        impl._sig3(tb_enum.api.Enum3.VALUE2)

        await is_sig3_changed_done.wait()
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_func0(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        result = await sink.func0(param0=tb_enum.api.Enum0.VALUE0)
        assert result == tb_enum.api.Enum0.VALUE0

        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_func1(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        result = await sink.func1(param1=tb_enum.api.Enum1.VALUE1)
        assert result == tb_enum.api.Enum1.VALUE1

        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_func2(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        result = await sink.func2(param2=tb_enum.api.Enum2.VALUE2)
        assert result == tb_enum.api.Enum2.VALUE2

        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_func3(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        result = await sink.func3(param3=tb_enum.api.Enum3.VALUE3)
        assert result == tb_enum.api.Enum3.VALUE3

        await self.teardown_mqtt(client, service)
