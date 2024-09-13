import tb_names.api
import tb_names.impl
import tb_names.mqtt
import tb_names.test_helpers.test_struct
import apigear.mqtt
import pytest
from typing import Any
import asyncio

def set_event_ready(loop, event):
    def func():
        event.set()
    loop.call_soon_threadsafe(func)

class TestMqttNamEs:

    @pytest.mark.asyncio
    async def setup_mqtt(slef):
        impl = tb_names.impl.NamEs()
        service = apigear.mqtt.Service("uniqueServiceIdTestNamEs")
        client = apigear.mqtt.Client("uniqueClientIdTestTestNamEs")
        serviceAdapter = tb_names.mqtt.NamEsServiceAdapter(impl, service)
        sink = tb_names.mqtt.NamEsClientAdapter(client)
     
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
    async def test_switch(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_switch_changed_done = asyncio.Event()
        def funProp(arguments):
            set_event_ready(loop, is_switch_changed_done )
        
        sink.on_switch_changed += funProp
        test_value = True
        
        sink.set_switch(test_value)
        await is_switch_changed_done.wait()
        assert impl.get_switch() == test_value
        assert sink.get_switch() == test_value
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_some_property(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_some_property_changed_done = asyncio.Event()
        def funProp(arguments):
            set_event_ready(loop, is_some_property_changed_done )
        
        sink.on_some_property_changed += funProp
        test_value = 1
        
        sink.set_some_property(test_value)
        await is_some_property_changed_done.wait()
        assert impl.get_some_property() == test_value
        assert sink.get_some_property() == test_value
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_some_poperty2(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_some_poperty2_changed_done = asyncio.Event()
        def funProp(arguments):
            set_event_ready(loop, is_some_poperty2_changed_done )
        
        sink.on_some_poperty2_changed += funProp
        test_value = 1
        
        sink.set_some_poperty2(test_value)
        await is_some_poperty2_changed_done.wait()
        assert impl.get_some_poperty2() == test_value
        assert sink.get_some_poperty2() == test_value
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_some_signal(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_some_signal_changed_done = asyncio.Event()

        def funSignal(some_param):
            assert some_param == True
            set_event_ready(loop, is_some_signal_changed_done )
        
        sink.on_some_signal += funSignal
        impl._some_signal(True)

        await is_some_signal_changed_done.wait()
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_some_signal2(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_some_signal2_changed_done = asyncio.Event()

        def funSignal(some_param):
            assert some_param == True
            set_event_ready(loop, is_some_signal2_changed_done )
        
        sink.on_some_signal2 += funSignal
        impl._some_signal2(True)

        await is_some_signal2_changed_done.wait()
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_some_function(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        await sink.some_function(some_param=False)

        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_some_function2(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        await sink.some_function2(some_param=False)

        await self.teardown_mqtt(client, service)
