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

class TestMqttSimpleArrayInterface:

    @pytest.mark.asyncio
    async def setup_mqtt(slef):
        impl = tb_simple.impl.SimpleArrayInterface()
        service = apigear.mqtt.Service("uniqueServiceIdTestSimpleArrayInterface")
        client = apigear.mqtt.Client("uniqueClientIdTestTestSimpleArrayInterface")
        serviceAdapter = tb_simple.mqtt.SimpleArrayInterfaceServiceAdapter(impl, service)
        sink = tb_simple.mqtt.SimpleArrayInterfaceClientAdapter(client)
     
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
        test_value = []  
        test_value.append(True)
        
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
        test_value = []  
        test_value.append(1)
        
        sink.set_prop_int(test_value)
        await is_prop_int_changed_done.wait()
        assert impl.get_prop_int() == test_value
        assert sink.get_prop_int() == test_value
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_prop_int32(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_prop_int32_changed_done = asyncio.Event()
        def funProp(arguments):
            set_event_ready(loop, is_prop_int32_changed_done )
        
        sink.on_prop_int32_changed += funProp
        test_value = []  
        test_value.append(1)
        
        sink.set_prop_int32(test_value)
        await is_prop_int32_changed_done.wait()
        assert impl.get_prop_int32() == test_value
        assert sink.get_prop_int32() == test_value
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_prop_int64(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_prop_int64_changed_done = asyncio.Event()
        def funProp(arguments):
            set_event_ready(loop, is_prop_int64_changed_done )
        
        sink.on_prop_int64_changed += funProp
        test_value = []  
        test_value.append(1)
        
        sink.set_prop_int64(test_value)
        await is_prop_int64_changed_done.wait()
        assert impl.get_prop_int64() == test_value
        assert sink.get_prop_int64() == test_value
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_prop_float(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_prop_float_changed_done = asyncio.Event()
        def funProp(arguments):
            set_event_ready(loop, is_prop_float_changed_done )
        
        sink.on_prop_float_changed += funProp
        test_value = []  
        test_value.append(1.1)
        
        sink.set_prop_float(test_value)
        await is_prop_float_changed_done.wait()
        assert impl.get_prop_float() == test_value
        assert sink.get_prop_float() == test_value
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_prop_float32(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_prop_float32_changed_done = asyncio.Event()
        def funProp(arguments):
            set_event_ready(loop, is_prop_float32_changed_done )
        
        sink.on_prop_float32_changed += funProp
        test_value = []  
        test_value.append(1.1)
        
        sink.set_prop_float32(test_value)
        await is_prop_float32_changed_done.wait()
        assert impl.get_prop_float32() == test_value
        assert sink.get_prop_float32() == test_value
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_prop_float64(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_prop_float64_changed_done = asyncio.Event()
        def funProp(arguments):
            set_event_ready(loop, is_prop_float64_changed_done )
        
        sink.on_prop_float64_changed += funProp
        test_value = []  
        test_value.append(1.1)
        
        sink.set_prop_float64(test_value)
        await is_prop_float64_changed_done.wait()
        assert impl.get_prop_float64() == test_value
        assert sink.get_prop_float64() == test_value
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_prop_string(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_prop_string_changed_done = asyncio.Event()
        def funProp(arguments):
            set_event_ready(loop, is_prop_string_changed_done )
        
        sink.on_prop_string_changed += funProp
        test_value = []  
        test_value.append("xyz")
        
        sink.set_prop_string(test_value)
        await is_prop_string_changed_done.wait()
        assert impl.get_prop_string() == test_value
        assert sink.get_prop_string() == test_value
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_prop_read_only_string(self):
        pass

    @pytest.mark.asyncio
    async def test_sig_bool(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_sig_bool_changed_done = asyncio.Event()
        local_param_bool_array = []
        local_param_bool_array.append(True)

        def funSignal(param_bool):
            assert param_bool == local_param_bool_array
            set_event_ready(loop, is_sig_bool_changed_done )
        
        sink.on_sig_bool += funSignal
        impl._sig_bool(local_param_bool_array)

        await is_sig_bool_changed_done.wait()
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_sig_int(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_sig_int_changed_done = asyncio.Event()
        local_param_int_array = []
        local_param_int_array.append(1)

        def funSignal(param_int):
            assert param_int == local_param_int_array
            set_event_ready(loop, is_sig_int_changed_done )
        
        sink.on_sig_int += funSignal
        impl._sig_int(local_param_int_array)

        await is_sig_int_changed_done.wait()
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_sig_int32(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_sig_int32_changed_done = asyncio.Event()
        local_param_int32_array = []
        local_param_int32_array.append(1)

        def funSignal(param_int32):
            assert param_int32 == local_param_int32_array
            set_event_ready(loop, is_sig_int32_changed_done )
        
        sink.on_sig_int32 += funSignal
        impl._sig_int32(local_param_int32_array)

        await is_sig_int32_changed_done.wait()
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_sig_int64(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_sig_int64_changed_done = asyncio.Event()
        local_param_int64_array = []
        local_param_int64_array.append(1)

        def funSignal(param_int64):
            assert param_int64 == local_param_int64_array
            set_event_ready(loop, is_sig_int64_changed_done )
        
        sink.on_sig_int64 += funSignal
        impl._sig_int64(local_param_int64_array)

        await is_sig_int64_changed_done.wait()
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_sig_float(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_sig_float_changed_done = asyncio.Event()
        local_param_float_array = []
        local_param_float_array.append(1.1)

        def funSignal(param_float):
            assert param_float == local_param_float_array
            set_event_ready(loop, is_sig_float_changed_done )
        
        sink.on_sig_float += funSignal
        impl._sig_float(local_param_float_array)

        await is_sig_float_changed_done.wait()
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_sig_float32(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_sig_float32_changed_done = asyncio.Event()
        local_param_floa32_array = []
        local_param_floa32_array.append(1.1)

        def funSignal(param_floa32):
            assert param_floa32 == local_param_floa32_array
            set_event_ready(loop, is_sig_float32_changed_done )
        
        sink.on_sig_float32 += funSignal
        impl._sig_float32(local_param_floa32_array)

        await is_sig_float32_changed_done.wait()
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_sig_float64(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_sig_float64_changed_done = asyncio.Event()
        local_param_float64_array = []
        local_param_float64_array.append(1.1)

        def funSignal(param_float64):
            assert param_float64 == local_param_float64_array
            set_event_ready(loop, is_sig_float64_changed_done )
        
        sink.on_sig_float64 += funSignal
        impl._sig_float64(local_param_float64_array)

        await is_sig_float64_changed_done.wait()
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_sig_string(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_sig_string_changed_done = asyncio.Event()
        local_param_string_array = []
        local_param_string_array.append("xyz")

        def funSignal(param_string):
            assert param_string == local_param_string_array
            set_event_ready(loop, is_sig_string_changed_done )
        
        sink.on_sig_string += funSignal
        impl._sig_string(local_param_string_array)

        await is_sig_string_changed_done.wait()
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_func_bool(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        result = await sink.func_bool(param_bool=[])
        assert result == []

        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_func_int(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        result = await sink.func_int(param_int=[])
        assert result == []

        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_func_int32(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        result = await sink.func_int32(param_int32=[])
        assert result == []

        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_func_int64(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        result = await sink.func_int64(param_int64=[])
        assert result == []

        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_func_float(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        result = await sink.func_float(param_float=[])
        assert result == []

        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_func_float32(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        result = await sink.func_float32(param_float32=[])
        assert result == []

        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_func_float64(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        result = await sink.func_float64(param_float=[])
        assert result == []

        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_func_string(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        result = await sink.func_string(param_string=[])
        assert result == []

        await self.teardown_mqtt(client, service)
