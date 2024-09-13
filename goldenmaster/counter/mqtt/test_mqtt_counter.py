import counter.api
import counter.impl
import counter.mqtt
import counter.test_helpers.test_struct
import apigear.mqtt
import pytest
from typing import Any
import asyncio
import custom_types.api
import custom_types.test_helpers.test_struct
import extern_types.api
import extern_types.test_helpers.test_struct
import vector3d.vector

def set_event_ready(loop, event):
    def func():
        event.set()
    loop.call_soon_threadsafe(func)

class TestMqttCounter:

    @pytest.mark.asyncio
    async def setup_mqtt(slef):
        impl = counter.impl.Counter()
        service = apigear.mqtt.Service("uniqueServiceIdTestCounter")
        client = apigear.mqtt.Client("uniqueClientIdTestTestCounter")
        serviceAdapter = counter.mqtt.CounterServiceAdapter(impl, service)
        sink = counter.mqtt.CounterClientAdapter(client)
     
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
    async def test_vector(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_vector_changed_done = asyncio.Event()
        def funProp(arguments):
            set_event_ready(loop, is_vector_changed_done )
        
        sink.on_vector_changed += funProp
        test_value = custom_types.test_helpers.test_struct.fillTestVector3D(custom_types.api.Vector3D())
        
        sink.set_vector(test_value)
        await is_vector_changed_done.wait()
        assert impl.get_vector() == test_value
        assert sink.get_vector() == test_value
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_extern_vector(self):
        pass

    @pytest.mark.asyncio
    async def test_increment(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        result = await sink.increment(vec=vector3d.vector.Vector())
        assert result == vector3d.vector.Vector()

        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_decrement(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        result = await sink.decrement(vec=custom_types.api.Vector3D())
        assert result == custom_types.api.Vector3D()

        await self.teardown_mqtt(client, service)
