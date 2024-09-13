import testbed2.api
import testbed2.impl
import testbed2.mqtt
import testbed2.test_helpers.test_struct
import apigear.mqtt
import pytest
from typing import Any
import asyncio

def set_event_ready(loop, event):
    def func():
        event.set()
    loop.call_soon_threadsafe(func)

class TestMqttNestedStruct2Interface:

    @pytest.mark.asyncio
    async def setup_mqtt(slef):
        impl = testbed2.impl.NestedStruct2Interface()
        service = apigear.mqtt.Service("uniqueServiceIdTestNestedStruct2Interface")
        client = apigear.mqtt.Client("uniqueClientIdTestTestNestedStruct2Interface")
        serviceAdapter = testbed2.mqtt.NestedStruct2InterfaceServiceAdapter(impl, service)
        sink = testbed2.mqtt.NestedStruct2InterfaceClientAdapter(client)
     
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
        test_value = testbed2.test_helpers.test_struct.fillTestNestedStruct1(testbed2.api.NestedStruct1())
        
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
        test_value = testbed2.test_helpers.test_struct.fillTestNestedStruct2(testbed2.api.NestedStruct2())
        
        sink.set_prop2(test_value)
        await is_prop2_changed_done.wait()
        assert impl.get_prop2() == test_value
        assert sink.get_prop2() == test_value
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_sig1(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_sig1_changed_done = asyncio.Event()
        local_param1_struct = testbed2.test_helpers.test_struct.fillTestNestedStruct1(testbed2.api.NestedStruct1())

        def funSignal(param1):
            assert param1 ==local_param1_struct
            set_event_ready(loop, is_sig1_changed_done )
        
        sink.on_sig1 += funSignal
        impl._sig1(local_param1_struct)

        await is_sig1_changed_done.wait()
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_sig2(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_sig2_changed_done = asyncio.Event()
        local_param1_struct = testbed2.test_helpers.test_struct.fillTestNestedStruct1(testbed2.api.NestedStruct1())
        local_param2_struct = testbed2.test_helpers.test_struct.fillTestNestedStruct2(testbed2.api.NestedStruct2())

        def funSignal(param1, param2):
            assert param1 ==local_param1_struct
            assert param2 ==local_param2_struct
            set_event_ready(loop, is_sig2_changed_done )
        
        sink.on_sig2 += funSignal
        impl._sig2(local_param1_struct, local_param2_struct)

        await is_sig2_changed_done.wait()
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_func1(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        result = await sink.func1(param1=testbed2.api.NestedStruct1())
        assert result == testbed2.api.NestedStruct1()

        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_func2(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        result = await sink.func2(param1=testbed2.api.NestedStruct1(), param2=testbed2.api.NestedStruct2())
        assert result == testbed2.api.NestedStruct1()

        await self.teardown_mqtt(client, service)
