import testbed1.api
import testbed1.impl
import testbed1.mqtt
import testbed1.test_helpers.test_struct
import apigear.mqtt
import pytest
from typing import Any
import asyncio

def set_event_ready(loop, event):
    def func():
        event.set()
    loop.call_soon_threadsafe(func)

class TestMqttStructInterface:

    @pytest.mark.asyncio
    async def setup_mqtt(slef):
        impl = testbed1.impl.StructInterface()
        service = apigear.mqtt.Service("uniqueServiceIdTestStructInterface")
        client = apigear.mqtt.Client("uniqueClientIdTestTestStructInterface")
        serviceAdapter = testbed1.mqtt.StructInterfaceServiceAdapter(impl, service)
        sink = testbed1.mqtt.StructInterfaceClientAdapter(client)
     
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
        test_value = testbed1.test_helpers.test_struct.fillTestStructBool(testbed1.api.StructBool())
        
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
        test_value = testbed1.test_helpers.test_struct.fillTestStructInt(testbed1.api.StructInt())
        
        sink.set_prop_int(test_value)
        await is_prop_int_changed_done.wait()
        assert impl.get_prop_int() == test_value
        assert sink.get_prop_int() == test_value
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_prop_float(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_prop_float_changed_done = asyncio.Event()
        def funProp(arguments):
            set_event_ready(loop, is_prop_float_changed_done )
        
        sink.on_prop_float_changed += funProp
        test_value = testbed1.test_helpers.test_struct.fillTestStructFloat(testbed1.api.StructFloat())
        
        sink.set_prop_float(test_value)
        await is_prop_float_changed_done.wait()
        assert impl.get_prop_float() == test_value
        assert sink.get_prop_float() == test_value
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_prop_string(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_prop_string_changed_done = asyncio.Event()
        def funProp(arguments):
            set_event_ready(loop, is_prop_string_changed_done )
        
        sink.on_prop_string_changed += funProp
        test_value = testbed1.test_helpers.test_struct.fillTestStructString(testbed1.api.StructString())
        
        sink.set_prop_string(test_value)
        await is_prop_string_changed_done.wait()
        assert impl.get_prop_string() == test_value
        assert sink.get_prop_string() == test_value
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_sig_bool(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_sig_bool_changed_done = asyncio.Event()
        local_param_bool_struct = testbed1.test_helpers.test_struct.fillTestStructBool(testbed1.api.StructBool())

        def funSignal(param_bool):
            assert param_bool ==local_param_bool_struct
            set_event_ready(loop, is_sig_bool_changed_done )
        
        sink.on_sig_bool += funSignal
        impl._sig_bool(local_param_bool_struct)

        await is_sig_bool_changed_done.wait()
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_sig_int(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_sig_int_changed_done = asyncio.Event()
        local_param_int_struct = testbed1.test_helpers.test_struct.fillTestStructInt(testbed1.api.StructInt())

        def funSignal(param_int):
            assert param_int ==local_param_int_struct
            set_event_ready(loop, is_sig_int_changed_done )
        
        sink.on_sig_int += funSignal
        impl._sig_int(local_param_int_struct)

        await is_sig_int_changed_done.wait()
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_sig_float(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_sig_float_changed_done = asyncio.Event()
        local_param_float_struct = testbed1.test_helpers.test_struct.fillTestStructFloat(testbed1.api.StructFloat())

        def funSignal(param_float):
            assert param_float ==local_param_float_struct
            set_event_ready(loop, is_sig_float_changed_done )
        
        sink.on_sig_float += funSignal
        impl._sig_float(local_param_float_struct)

        await is_sig_float_changed_done.wait()
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_sig_string(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_sig_string_changed_done = asyncio.Event()
        local_param_string_struct = testbed1.test_helpers.test_struct.fillTestStructString(testbed1.api.StructString())

        def funSignal(param_string):
            assert param_string ==local_param_string_struct
            set_event_ready(loop, is_sig_string_changed_done )
        
        sink.on_sig_string += funSignal
        impl._sig_string(local_param_string_struct)

        await is_sig_string_changed_done.wait()
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_func_bool(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        result = await sink.func_bool(param_bool=testbed1.api.StructBool())
        assert result == testbed1.api.StructBool()

        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_func_int(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        result = await sink.func_int(param_int=testbed1.api.StructInt())
        assert result == testbed1.api.StructInt()

        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_func_float(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        result = await sink.func_float(param_float=testbed1.api.StructFloat())
        assert result == testbed1.api.StructFloat()

        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_func_string(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        result = await sink.func_string(param_string=testbed1.api.StructString())
        assert result == testbed1.api.StructString()

        await self.teardown_mqtt(client, service)
