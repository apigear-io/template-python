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

class TestMqttSimpleInterface:

    @pytest.mark.asyncio
    async def setup_mqtt(slef):
        impl = tb_simple.impl.SimpleInterface()
        service = apigear.mqtt.Service("uniqueServiceIdTestSimpleInterface")
        client = apigear.mqtt.Client("uniqueClientIdTestTestSimpleInterface")
        serviceAdapter = tb_simple.mqtt.SimpleInterfaceServiceAdapter(impl, service)
        sink = tb_simple.mqtt.SimpleInterfaceClientAdapter(client)
     
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
    async def test_prop_int32(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_prop_int32_changed_done = asyncio.Event()
        def funProp(arguments):
            set_event_ready(loop, is_prop_int32_changed_done )
        
        sink.on_prop_int32_changed += funProp
        test_value = 1
        
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
        test_value = 1
        
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
        test_value = 1.1
        
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
        test_value = 1.1
        
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
        test_value = 1.1
        
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
        test_value = "xyz"
        
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

        def funSignal(param_bool):
            assert param_bool == True
            set_event_ready(loop, is_sig_bool_changed_done )
        
        sink.on_sig_bool += funSignal
        impl._sig_bool(True)

        await is_sig_bool_changed_done.wait()
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_sig_int(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_sig_int_changed_done = asyncio.Event()

        def funSignal(param_int):
            assert param_int == 1
            set_event_ready(loop, is_sig_int_changed_done )
        
        sink.on_sig_int += funSignal
        impl._sig_int(1)

        await is_sig_int_changed_done.wait()
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_sig_int32(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_sig_int32_changed_done = asyncio.Event()

        def funSignal(param_int32):
            assert param_int32 == 1
            set_event_ready(loop, is_sig_int32_changed_done )
        
        sink.on_sig_int32 += funSignal
        impl._sig_int32(1)

        await is_sig_int32_changed_done.wait()
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_sig_int64(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_sig_int64_changed_done = asyncio.Event()

        def funSignal(param_int64):
            assert param_int64 == 1
            set_event_ready(loop, is_sig_int64_changed_done )
        
        sink.on_sig_int64 += funSignal
        impl._sig_int64(1)

        await is_sig_int64_changed_done.wait()
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_sig_float(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_sig_float_changed_done = asyncio.Event()

        def funSignal(param_float):
            assert param_float == 1.1
            set_event_ready(loop, is_sig_float_changed_done )
        
        sink.on_sig_float += funSignal
        impl._sig_float(1.1)

        await is_sig_float_changed_done.wait()
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_sig_float32(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_sig_float32_changed_done = asyncio.Event()

        def funSignal(param_float32):
            assert param_float32 == 1.1
            set_event_ready(loop, is_sig_float32_changed_done )
        
        sink.on_sig_float32 += funSignal
        impl._sig_float32(1.1)

        await is_sig_float32_changed_done.wait()
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_sig_float64(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_sig_float64_changed_done = asyncio.Event()

        def funSignal(param_float64):
            assert param_float64 == 1.1
            set_event_ready(loop, is_sig_float64_changed_done )
        
        sink.on_sig_float64 += funSignal
        impl._sig_float64(1.1)

        await is_sig_float64_changed_done.wait()
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_sig_string(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_sig_string_changed_done = asyncio.Event()

        def funSignal(param_string):
            assert param_string == "xyz"
            set_event_ready(loop, is_sig_string_changed_done )
        
        sink.on_sig_string += funSignal
        impl._sig_string("xyz")

        await is_sig_string_changed_done.wait()
        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_func_no_return_value(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        await sink.func_no_return_value(param_bool=False)

        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_func_bool(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        result = await sink.func_bool(param_bool=False)
        assert result == False

        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_func_int(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        result = await sink.func_int(param_int=0)
        assert result == 0

        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_func_int32(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        result = await sink.func_int32(param_int32=0)
        assert result == 0

        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_func_int64(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        result = await sink.func_int64(param_int64=0)
        assert result == 0

        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_func_float(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        result = await sink.func_float(param_float=0.0)
        assert result == 0.0

        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_func_float32(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        result = await sink.func_float32(param_float32=0.0)
        assert result == 0.0

        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_func_float64(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        result = await sink.func_float64(param_float=0.0)
        assert result == 0.0

        await self.teardown_mqtt(client, service)

    @pytest.mark.asyncio
    async def test_func_string(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        result = await sink.func_string(param_string="")
        assert result == ""

        await self.teardown_mqtt(client, service)
