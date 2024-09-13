import tb_same1.api
import tb_same1.impl
import tb_same1.mqtt
import tb_same1.test_helpers.test_struct
import apigear.mqtt
import pytest
from typing import Any
import asyncio

def set_event_ready(loop, event):
    def func():
        event.set()
    loop.call_soon_threadsafe(func)

class TestMqttSameStruct1Interface:

    @pytest.mark.asyncio
    async def setup_mqtt(slef):
        impl = tb_same1.impl.SameStruct1Interface()
        service = apigear.mqtt.Service("uniqueServiceIdTestSameStruct1Interface")
        client = apigear.mqtt.Client("uniqueClientIdTestTestSameStruct1Interface")
        serviceAdapter = tb_same1.mqtt.SameStruct1InterfaceServiceAdapter(impl, service)
        sink = tb_same1.mqtt.SameStruct1InterfaceClientAdapter(client)
     
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
    async def test_prop1(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_prop1_changed_done = asyncio.Event()
        def funProp(arguments):
            set_event_ready(loop, is_prop1_changed_done )
        
        sink.on_prop1_changed += funProp
        test_value = tb_same1.test_helpers.test_struct.fillTestStruct1(tb_same1.api.Struct1())
        
        sink.set_prop1(test_value)
        await is_prop1_changed_done.wait()
        assert impl.get_prop1() == test_value
        assert sink.get_prop1() == test_value
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_sig1(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_sig1_changed_done = asyncio.Event()
        local_param1_struct = tb_same1.test_helpers.test_struct.fillTestStruct1(tb_same1.api.Struct1())

        def funSignal(param1):
            assert param1 ==local_param1_struct
            set_event_ready(loop, is_sig1_changed_done )
        
        sink.on_sig1 += funSignal
        impl._sig1(local_param1_struct)

        await is_sig1_changed_done.wait()
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_func1(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        result = await sink.func1(param1=tb_same1.api.Struct1())
        assert result == tb_same1.api.Struct1()

        await self.teardown_mqtt(client, service)
