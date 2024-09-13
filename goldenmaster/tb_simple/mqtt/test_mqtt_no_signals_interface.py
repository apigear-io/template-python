import tb_simple.api
import tb_simple.impl
import tb_simple.mqtt
import tb_simple.test_helpers.test_struct
import apigear.mqtt
import pytest
from typing import Any
import asyncio

def set_event_ready(loop, event):
    def func():
        event.set()
    loop.call_soon_threadsafe(func)

class TestMqttNoSignalsInterface:

    @pytest.mark.asyncio
    async def setup_mqtt(slef):
        impl = tb_simple.impl.NoSignalsInterface()
        service = apigear.mqtt.Service("uniqueServiceIdTestNoSignalsInterface")
        client = apigear.mqtt.Client("uniqueClientIdTestTestNoSignalsInterface")
        serviceAdapter = tb_simple.mqtt.NoSignalsInterfaceServiceAdapter(impl, service)
        sink = tb_simple.mqtt.NoSignalsInterfaceClientAdapter(client)
     
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
    async def test_prop_bool(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_prop_bool_changed_done = asyncio.Event()
        def funProp(arguments):
            set_event_ready(loop, is_prop_bool_changed_done )
        
        sink.on_prop_bool_changed += funProp
        test_value = True
        
        sink.set_prop_bool(test_value)
        await is_prop_bool_changed_done.wait()
        assert impl.get_prop_bool() == test_value
        assert sink.get_prop_bool() == test_value
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_prop_int(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_prop_int_changed_done = asyncio.Event()
        def funProp(arguments):
            set_event_ready(loop, is_prop_int_changed_done )
        
        sink.on_prop_int_changed += funProp
        test_value = 1
        
        sink.set_prop_int(test_value)
        await is_prop_int_changed_done.wait()
        assert impl.get_prop_int() == test_value
        assert sink.get_prop_int() == test_value
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_func_void(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        await sink.func_void()

        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_func_bool(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        result = await sink.func_bool(param_bool=False)
        assert result == False

        await self.teardown_mqtt(client, service)
