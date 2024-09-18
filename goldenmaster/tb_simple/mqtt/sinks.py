import asyncio
from typing import Any
import apigear.mqtt
import paho.mqtt.enums
import paho.mqtt.reasoncodes
from utils.eventhook import EventHook
import utils.base_types
import tb_simple.api
import logging

class VoidInterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self.on_ready = EventHook()
        self.on_sig_void = EventHook()
        self.client.on_subscribed += self.__handle_subscribed
        self.subscription_ids = []
        self.client.on_connected += self.subscribeForTopics
        self.method_topics = self.MethodTopics(self.client.get_client_id())
        self.pending_calls = self.PendingCalls()
        self.loop = asyncio.get_event_loop()

    def subscribeForTopics(self):
        self.subscription_ids.append(self.client.subscribe_for_signal("tb.simple/VoidInterface/sig/sigVoid",  self.__on_sig_void_signal))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func_void, self.__on_func_void_resp))

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.on_subscribed -= self.__handle_subscribed
        self.client.unsubscribe("tb.simple/VoidInterface/sig/sigVoid")
        self.client.unsubscribe(self.method_topics.resp_topic_func_void)

    def __handle_subscribed(self, msg_id: int, reason_code_list: list[paho.mqtt.reasoncodes.ReasonCode]):
        if not (msg_id in self.subscription_ids):
            return
        # Assuming the topic was subscribed only for a single channel and reason_code_list contains
        # a single entry
        if reason_code_list[0].is_failure:
            self.logging_func(paho.mqtt.enums.LogLevel.MQTT_LOG_ERROR, (f"Broker rejected subscription id {msg_id} reason: {reason_code_list[0]}"))
            return
        self.subscription_ids.remove(msg_id)
        if len(self.subscription_ids) == 0:
            self.on_ready.fire()

    async def func_void(self):
        args = []
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(None)
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func_void, self.method_topics.resp_topic_func_void, args)
        self.pending_calls.func_void[call_id] = func
        return await asyncio.wait_for(future, 500)

    # internal functions on message handle

    def __on_sig_void_signal(self, args: list[Any]):
        self.on_sig_void.fire()
        return

    def __on_func_void_resp(self, value, callId):
       callback = self.pending_calls.func_void.pop(callId)
       if callback != None:
           callback(value)
    class MethodTopics:
        def __init__(self, client_id):
            self.topic_func_void= "tb.simple/VoidInterface/rpc/funcVoid"
            self.resp_topic_func_void= self.topic_func_void + "/" + str(client_id) + "/result"

    class PendingCalls:
        def __init__(self):
            self.func_void = {}

class SimpleInterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self.on_ready = EventHook()
        self._prop_bool = False
        self.on_prop_bool_changed = EventHook()
        self._prop_int = 0
        self.on_prop_int_changed = EventHook()
        self._prop_int32 = 0
        self.on_prop_int32_changed = EventHook()
        self._prop_int64 = 0
        self.on_prop_int64_changed = EventHook()
        self._prop_float = 0.0
        self.on_prop_float_changed = EventHook()
        self._prop_float32 = 0.0
        self.on_prop_float32_changed = EventHook()
        self._prop_float64 = 0.0
        self.on_prop_float64_changed = EventHook()
        self._prop_string = ""
        self.on_prop_string_changed = EventHook()
        self.on_sig_bool = EventHook()
        self.on_sig_int = EventHook()
        self.on_sig_int32 = EventHook()
        self.on_sig_int64 = EventHook()
        self.on_sig_float = EventHook()
        self.on_sig_float32 = EventHook()
        self.on_sig_float64 = EventHook()
        self.on_sig_string = EventHook()
        self.client.on_subscribed += self.__handle_subscribed
        self.subscription_ids = []
        self.client.on_connected += self.subscribeForTopics
        self.method_topics = self.MethodTopics(self.client.get_client_id())
        self.pending_calls = self.PendingCalls()
        self.loop = asyncio.get_event_loop()

    def subscribeForTopics(self):
        self.subscription_ids.append(self.client.subscribe_for_property("tb.simple/SimpleInterface/prop/propBool", self.__set_prop_bool))
        self.subscription_ids.append(self.client.subscribe_for_property("tb.simple/SimpleInterface/prop/propInt", self.__set_prop_int))
        self.subscription_ids.append(self.client.subscribe_for_property("tb.simple/SimpleInterface/prop/propInt32", self.__set_prop_int32))
        self.subscription_ids.append(self.client.subscribe_for_property("tb.simple/SimpleInterface/prop/propInt64", self.__set_prop_int64))
        self.subscription_ids.append(self.client.subscribe_for_property("tb.simple/SimpleInterface/prop/propFloat", self.__set_prop_float))
        self.subscription_ids.append(self.client.subscribe_for_property("tb.simple/SimpleInterface/prop/propFloat32", self.__set_prop_float32))
        self.subscription_ids.append(self.client.subscribe_for_property("tb.simple/SimpleInterface/prop/propFloat64", self.__set_prop_float64))
        self.subscription_ids.append(self.client.subscribe_for_property("tb.simple/SimpleInterface/prop/propString", self.__set_prop_string))
        self.subscription_ids.append(self.client.subscribe_for_signal("tb.simple/SimpleInterface/sig/sigBool",  self.__on_sig_bool_signal))
        self.subscription_ids.append(self.client.subscribe_for_signal("tb.simple/SimpleInterface/sig/sigInt",  self.__on_sig_int_signal))
        self.subscription_ids.append(self.client.subscribe_for_signal("tb.simple/SimpleInterface/sig/sigInt32",  self.__on_sig_int32_signal))
        self.subscription_ids.append(self.client.subscribe_for_signal("tb.simple/SimpleInterface/sig/sigInt64",  self.__on_sig_int64_signal))
        self.subscription_ids.append(self.client.subscribe_for_signal("tb.simple/SimpleInterface/sig/sigFloat",  self.__on_sig_float_signal))
        self.subscription_ids.append(self.client.subscribe_for_signal("tb.simple/SimpleInterface/sig/sigFloat32",  self.__on_sig_float32_signal))
        self.subscription_ids.append(self.client.subscribe_for_signal("tb.simple/SimpleInterface/sig/sigFloat64",  self.__on_sig_float64_signal))
        self.subscription_ids.append(self.client.subscribe_for_signal("tb.simple/SimpleInterface/sig/sigString",  self.__on_sig_string_signal))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func_no_return_value, self.__on_func_no_return_value_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func_bool, self.__on_func_bool_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func_int, self.__on_func_int_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func_int32, self.__on_func_int32_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func_int64, self.__on_func_int64_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func_float, self.__on_func_float_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func_float32, self.__on_func_float32_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func_float64, self.__on_func_float64_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func_string, self.__on_func_string_resp))

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.on_subscribed -= self.__handle_subscribed
        self.client.unsubscribe("tb.simple/SimpleInterface/prop/propBool")
        self.client.unsubscribe("tb.simple/SimpleInterface/prop/propInt")
        self.client.unsubscribe("tb.simple/SimpleInterface/prop/propInt32")
        self.client.unsubscribe("tb.simple/SimpleInterface/prop/propInt64")
        self.client.unsubscribe("tb.simple/SimpleInterface/prop/propFloat")
        self.client.unsubscribe("tb.simple/SimpleInterface/prop/propFloat32")
        self.client.unsubscribe("tb.simple/SimpleInterface/prop/propFloat64")
        self.client.unsubscribe("tb.simple/SimpleInterface/prop/propString")
        self.client.unsubscribe("tb.simple/SimpleInterface/sig/sigBool")
        self.client.unsubscribe("tb.simple/SimpleInterface/sig/sigInt")
        self.client.unsubscribe("tb.simple/SimpleInterface/sig/sigInt32")
        self.client.unsubscribe("tb.simple/SimpleInterface/sig/sigInt64")
        self.client.unsubscribe("tb.simple/SimpleInterface/sig/sigFloat")
        self.client.unsubscribe("tb.simple/SimpleInterface/sig/sigFloat32")
        self.client.unsubscribe("tb.simple/SimpleInterface/sig/sigFloat64")
        self.client.unsubscribe("tb.simple/SimpleInterface/sig/sigString")
        self.client.unsubscribe(self.method_topics.resp_topic_func_no_return_value)
        self.client.unsubscribe(self.method_topics.resp_topic_func_bool)
        self.client.unsubscribe(self.method_topics.resp_topic_func_int)
        self.client.unsubscribe(self.method_topics.resp_topic_func_int32)
        self.client.unsubscribe(self.method_topics.resp_topic_func_int64)
        self.client.unsubscribe(self.method_topics.resp_topic_func_float)
        self.client.unsubscribe(self.method_topics.resp_topic_func_float32)
        self.client.unsubscribe(self.method_topics.resp_topic_func_float64)
        self.client.unsubscribe(self.method_topics.resp_topic_func_string)

    def __handle_subscribed(self, msg_id: int, reason_code_list: list[paho.mqtt.reasoncodes.ReasonCode]):
        if not (msg_id in self.subscription_ids):
            return
        # Assuming the topic was subscribed only for a single channel and reason_code_list contains
        # a single entry
        if reason_code_list[0].is_failure:
            self.logging_func(paho.mqtt.enums.LogLevel.MQTT_LOG_ERROR, (f"Broker rejected subscription id {msg_id} reason: {reason_code_list[0]}"))
            return
        self.subscription_ids.remove(msg_id)
        if len(self.subscription_ids) == 0:
            self.on_ready.fire()

    def set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        topic = "tb.simple/SimpleInterface/set/propBool"
        self.client.set_remote_property(topic, utils.base_types.from_bool(value))

    def get_prop_bool(self):
        return self._prop_bool

    def set_prop_int(self, value):
        if self._prop_int == value:
            return
        topic = "tb.simple/SimpleInterface/set/propInt"
        self.client.set_remote_property(topic, utils.base_types.from_int(value))

    def get_prop_int(self):
        return self._prop_int

    def set_prop_int32(self, value):
        if self._prop_int32 == value:
            return
        topic = "tb.simple/SimpleInterface/set/propInt32"
        self.client.set_remote_property(topic, utils.base_types.from_int32(value))

    def get_prop_int32(self):
        return self._prop_int32

    def set_prop_int64(self, value):
        if self._prop_int64 == value:
            return
        topic = "tb.simple/SimpleInterface/set/propInt64"
        self.client.set_remote_property(topic, utils.base_types.from_int64(value))

    def get_prop_int64(self):
        return self._prop_int64

    def set_prop_float(self, value):
        if self._prop_float == value:
            return
        topic = "tb.simple/SimpleInterface/set/propFloat"
        self.client.set_remote_property(topic, utils.base_types.from_float(value))

    def get_prop_float(self):
        return self._prop_float

    def set_prop_float32(self, value):
        if self._prop_float32 == value:
            return
        topic = "tb.simple/SimpleInterface/set/propFloat32"
        self.client.set_remote_property(topic, utils.base_types.from_float32(value))

    def get_prop_float32(self):
        return self._prop_float32

    def set_prop_float64(self, value):
        if self._prop_float64 == value:
            return
        topic = "tb.simple/SimpleInterface/set/propFloat64"
        self.client.set_remote_property(topic, utils.base_types.from_float64(value))

    def get_prop_float64(self):
        return self._prop_float64

    def set_prop_string(self, value):
        if self._prop_string == value:
            return
        topic = "tb.simple/SimpleInterface/set/propString"
        self.client.set_remote_property(topic, utils.base_types.from_string(value))

    def get_prop_string(self):
        return self._prop_string

    async def func_no_return_value(self, param_bool: bool):
        _param_bool = utils.base_types.from_bool(param_bool)
        args = [_param_bool]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(None)
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func_no_return_value, self.method_topics.resp_topic_func_no_return_value, args)
        self.pending_calls.func_no_return_value[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func_bool(self, param_bool: bool):
        _param_bool = utils.base_types.from_bool(param_bool)
        args = [_param_bool]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(utils.base_types.as_bool(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func_bool, self.method_topics.resp_topic_func_bool, args)
        self.pending_calls.func_bool[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func_int(self, param_int: int):
        _param_int = utils.base_types.from_int(param_int)
        args = [_param_int]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(utils.base_types.as_int(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func_int, self.method_topics.resp_topic_func_int, args)
        self.pending_calls.func_int[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func_int32(self, param_int32: int):
        _param_int32 = utils.base_types.from_int32(param_int32)
        args = [_param_int32]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(utils.base_types.as_int32(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func_int32, self.method_topics.resp_topic_func_int32, args)
        self.pending_calls.func_int32[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func_int64(self, param_int64: int):
        _param_int64 = utils.base_types.from_int64(param_int64)
        args = [_param_int64]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(utils.base_types.as_int64(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func_int64, self.method_topics.resp_topic_func_int64, args)
        self.pending_calls.func_int64[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func_float(self, param_float: float):
        _param_float = utils.base_types.from_float(param_float)
        args = [_param_float]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(utils.base_types.as_float(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func_float, self.method_topics.resp_topic_func_float, args)
        self.pending_calls.func_float[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func_float32(self, param_float32: float):
        _param_float32 = utils.base_types.from_float32(param_float32)
        args = [_param_float32]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(utils.base_types.as_float32(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func_float32, self.method_topics.resp_topic_func_float32, args)
        self.pending_calls.func_float32[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func_float64(self, param_float: float):
        _param_float = utils.base_types.from_float64(param_float)
        args = [_param_float]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(utils.base_types.as_float64(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func_float64, self.method_topics.resp_topic_func_float64, args)
        self.pending_calls.func_float64[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func_string(self, param_string: str):
        _param_string = utils.base_types.from_string(param_string)
        args = [_param_string]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(utils.base_types.as_string(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func_string, self.method_topics.resp_topic_func_string, args)
        self.pending_calls.func_string[call_id] = func
        return await asyncio.wait_for(future, 500)

    # internal functions on message handle

    def __set_prop_bool(self, data):
        value =  utils.base_types.as_bool(data)
        if self._prop_bool == value:
            return
        self._prop_bool = value
        self.on_prop_bool_changed.fire(self._prop_bool)

    def __set_prop_int(self, data):
        value =  utils.base_types.as_int(data)
        if self._prop_int == value:
            return
        self._prop_int = value
        self.on_prop_int_changed.fire(self._prop_int)

    def __set_prop_int32(self, data):
        value =  utils.base_types.as_int32(data)
        if self._prop_int32 == value:
            return
        self._prop_int32 = value
        self.on_prop_int32_changed.fire(self._prop_int32)

    def __set_prop_int64(self, data):
        value =  utils.base_types.as_int64(data)
        if self._prop_int64 == value:
            return
        self._prop_int64 = value
        self.on_prop_int64_changed.fire(self._prop_int64)

    def __set_prop_float(self, data):
        value =  utils.base_types.as_float(data)
        if self._prop_float == value:
            return
        self._prop_float = value
        self.on_prop_float_changed.fire(self._prop_float)

    def __set_prop_float32(self, data):
        value =  utils.base_types.as_float32(data)
        if self._prop_float32 == value:
            return
        self._prop_float32 = value
        self.on_prop_float32_changed.fire(self._prop_float32)

    def __set_prop_float64(self, data):
        value =  utils.base_types.as_float64(data)
        if self._prop_float64 == value:
            return
        self._prop_float64 = value
        self.on_prop_float64_changed.fire(self._prop_float64)

    def __set_prop_string(self, data):
        value =  utils.base_types.as_string(data)
        if self._prop_string == value:
            return
        self._prop_string = value
        self.on_prop_string_changed.fire(self._prop_string)

    def __on_sig_bool_signal(self, args: list[Any]):
        param_bool =  utils.base_types.as_bool(args[0])
        self.on_sig_bool.fire(param_bool)
        return

    def __on_sig_int_signal(self, args: list[Any]):
        param_int =  utils.base_types.as_int(args[0])
        self.on_sig_int.fire(param_int)
        return

    def __on_sig_int32_signal(self, args: list[Any]):
        param_int32 =  utils.base_types.as_int32(args[0])
        self.on_sig_int32.fire(param_int32)
        return

    def __on_sig_int64_signal(self, args: list[Any]):
        param_int64 =  utils.base_types.as_int64(args[0])
        self.on_sig_int64.fire(param_int64)
        return

    def __on_sig_float_signal(self, args: list[Any]):
        param_float =  utils.base_types.as_float(args[0])
        self.on_sig_float.fire(param_float)
        return

    def __on_sig_float32_signal(self, args: list[Any]):
        param_float32 =  utils.base_types.as_float32(args[0])
        self.on_sig_float32.fire(param_float32)
        return

    def __on_sig_float64_signal(self, args: list[Any]):
        param_float64 =  utils.base_types.as_float64(args[0])
        self.on_sig_float64.fire(param_float64)
        return

    def __on_sig_string_signal(self, args: list[Any]):
        param_string =  utils.base_types.as_string(args[0])
        self.on_sig_string.fire(param_string)
        return

    def __on_func_no_return_value_resp(self, value, callId):
       callback = self.pending_calls.func_no_return_value.pop(callId)
       if callback != None:
           callback(value)

    def __on_func_bool_resp(self, value, callId):
       callback = self.pending_calls.func_bool.pop(callId)
       if callback != None:
           callback(value)

    def __on_func_int_resp(self, value, callId):
       callback = self.pending_calls.func_int.pop(callId)
       if callback != None:
           callback(value)

    def __on_func_int32_resp(self, value, callId):
       callback = self.pending_calls.func_int32.pop(callId)
       if callback != None:
           callback(value)

    def __on_func_int64_resp(self, value, callId):
       callback = self.pending_calls.func_int64.pop(callId)
       if callback != None:
           callback(value)

    def __on_func_float_resp(self, value, callId):
       callback = self.pending_calls.func_float.pop(callId)
       if callback != None:
           callback(value)

    def __on_func_float32_resp(self, value, callId):
       callback = self.pending_calls.func_float32.pop(callId)
       if callback != None:
           callback(value)

    def __on_func_float64_resp(self, value, callId):
       callback = self.pending_calls.func_float64.pop(callId)
       if callback != None:
           callback(value)

    def __on_func_string_resp(self, value, callId):
       callback = self.pending_calls.func_string.pop(callId)
       if callback != None:
           callback(value)
    class MethodTopics:
        def __init__(self, client_id):
            self.topic_func_no_return_value= "tb.simple/SimpleInterface/rpc/funcNoReturnValue"
            self.resp_topic_func_no_return_value= self.topic_func_no_return_value + "/" + str(client_id) + "/result"
            self.topic_func_bool= "tb.simple/SimpleInterface/rpc/funcBool"
            self.resp_topic_func_bool= self.topic_func_bool + "/" + str(client_id) + "/result"
            self.topic_func_int= "tb.simple/SimpleInterface/rpc/funcInt"
            self.resp_topic_func_int= self.topic_func_int + "/" + str(client_id) + "/result"
            self.topic_func_int32= "tb.simple/SimpleInterface/rpc/funcInt32"
            self.resp_topic_func_int32= self.topic_func_int32 + "/" + str(client_id) + "/result"
            self.topic_func_int64= "tb.simple/SimpleInterface/rpc/funcInt64"
            self.resp_topic_func_int64= self.topic_func_int64 + "/" + str(client_id) + "/result"
            self.topic_func_float= "tb.simple/SimpleInterface/rpc/funcFloat"
            self.resp_topic_func_float= self.topic_func_float + "/" + str(client_id) + "/result"
            self.topic_func_float32= "tb.simple/SimpleInterface/rpc/funcFloat32"
            self.resp_topic_func_float32= self.topic_func_float32 + "/" + str(client_id) + "/result"
            self.topic_func_float64= "tb.simple/SimpleInterface/rpc/funcFloat64"
            self.resp_topic_func_float64= self.topic_func_float64 + "/" + str(client_id) + "/result"
            self.topic_func_string= "tb.simple/SimpleInterface/rpc/funcString"
            self.resp_topic_func_string= self.topic_func_string + "/" + str(client_id) + "/result"

    class PendingCalls:
        def __init__(self):
            self.func_no_return_value = {}
            self.func_bool = {}
            self.func_int = {}
            self.func_int32 = {}
            self.func_int64 = {}
            self.func_float = {}
            self.func_float32 = {}
            self.func_float64 = {}
            self.func_string = {}

class SimpleArrayInterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self.on_ready = EventHook()
        self._prop_bool = []
        self.on_prop_bool_changed = EventHook()
        self._prop_int = []
        self.on_prop_int_changed = EventHook()
        self._prop_int32 = []
        self.on_prop_int32_changed = EventHook()
        self._prop_int64 = []
        self.on_prop_int64_changed = EventHook()
        self._prop_float = []
        self.on_prop_float_changed = EventHook()
        self._prop_float32 = []
        self.on_prop_float32_changed = EventHook()
        self._prop_float64 = []
        self.on_prop_float64_changed = EventHook()
        self._prop_string = []
        self.on_prop_string_changed = EventHook()
        self._prop_read_only_string = ""
        self.on_prop_read_only_string_changed = EventHook()
        self.on_sig_bool = EventHook()
        self.on_sig_int = EventHook()
        self.on_sig_int32 = EventHook()
        self.on_sig_int64 = EventHook()
        self.on_sig_float = EventHook()
        self.on_sig_float32 = EventHook()
        self.on_sig_float64 = EventHook()
        self.on_sig_string = EventHook()
        self.client.on_subscribed += self.__handle_subscribed
        self.subscription_ids = []
        self.client.on_connected += self.subscribeForTopics
        self.method_topics = self.MethodTopics(self.client.get_client_id())
        self.pending_calls = self.PendingCalls()
        self.loop = asyncio.get_event_loop()

    def subscribeForTopics(self):
        self.subscription_ids.append(self.client.subscribe_for_property("tb.simple/SimpleArrayInterface/prop/propBool", self.__set_prop_bool))
        self.subscription_ids.append(self.client.subscribe_for_property("tb.simple/SimpleArrayInterface/prop/propInt", self.__set_prop_int))
        self.subscription_ids.append(self.client.subscribe_for_property("tb.simple/SimpleArrayInterface/prop/propInt32", self.__set_prop_int32))
        self.subscription_ids.append(self.client.subscribe_for_property("tb.simple/SimpleArrayInterface/prop/propInt64", self.__set_prop_int64))
        self.subscription_ids.append(self.client.subscribe_for_property("tb.simple/SimpleArrayInterface/prop/propFloat", self.__set_prop_float))
        self.subscription_ids.append(self.client.subscribe_for_property("tb.simple/SimpleArrayInterface/prop/propFloat32", self.__set_prop_float32))
        self.subscription_ids.append(self.client.subscribe_for_property("tb.simple/SimpleArrayInterface/prop/propFloat64", self.__set_prop_float64))
        self.subscription_ids.append(self.client.subscribe_for_property("tb.simple/SimpleArrayInterface/prop/propString", self.__set_prop_string))
        self.subscription_ids.append(self.client.subscribe_for_property("tb.simple/SimpleArrayInterface/prop/propReadOnlyString", self.__set_prop_read_only_string))
        self.subscription_ids.append(self.client.subscribe_for_signal("tb.simple/SimpleArrayInterface/sig/sigBool",  self.__on_sig_bool_signal))
        self.subscription_ids.append(self.client.subscribe_for_signal("tb.simple/SimpleArrayInterface/sig/sigInt",  self.__on_sig_int_signal))
        self.subscription_ids.append(self.client.subscribe_for_signal("tb.simple/SimpleArrayInterface/sig/sigInt32",  self.__on_sig_int32_signal))
        self.subscription_ids.append(self.client.subscribe_for_signal("tb.simple/SimpleArrayInterface/sig/sigInt64",  self.__on_sig_int64_signal))
        self.subscription_ids.append(self.client.subscribe_for_signal("tb.simple/SimpleArrayInterface/sig/sigFloat",  self.__on_sig_float_signal))
        self.subscription_ids.append(self.client.subscribe_for_signal("tb.simple/SimpleArrayInterface/sig/sigFloat32",  self.__on_sig_float32_signal))
        self.subscription_ids.append(self.client.subscribe_for_signal("tb.simple/SimpleArrayInterface/sig/sigFloat64",  self.__on_sig_float64_signal))
        self.subscription_ids.append(self.client.subscribe_for_signal("tb.simple/SimpleArrayInterface/sig/sigString",  self.__on_sig_string_signal))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func_bool, self.__on_func_bool_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func_int, self.__on_func_int_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func_int32, self.__on_func_int32_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func_int64, self.__on_func_int64_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func_float, self.__on_func_float_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func_float32, self.__on_func_float32_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func_float64, self.__on_func_float64_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func_string, self.__on_func_string_resp))

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.on_subscribed -= self.__handle_subscribed
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/prop/propBool")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/prop/propInt")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/prop/propInt32")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/prop/propInt64")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/prop/propFloat")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/prop/propFloat32")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/prop/propFloat64")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/prop/propString")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/prop/propReadOnlyString")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/sig/sigBool")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/sig/sigInt")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/sig/sigInt32")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/sig/sigInt64")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/sig/sigFloat")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/sig/sigFloat32")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/sig/sigFloat64")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/sig/sigString")
        self.client.unsubscribe(self.method_topics.resp_topic_func_bool)
        self.client.unsubscribe(self.method_topics.resp_topic_func_int)
        self.client.unsubscribe(self.method_topics.resp_topic_func_int32)
        self.client.unsubscribe(self.method_topics.resp_topic_func_int64)
        self.client.unsubscribe(self.method_topics.resp_topic_func_float)
        self.client.unsubscribe(self.method_topics.resp_topic_func_float32)
        self.client.unsubscribe(self.method_topics.resp_topic_func_float64)
        self.client.unsubscribe(self.method_topics.resp_topic_func_string)

    def __handle_subscribed(self, msg_id: int, reason_code_list: list[paho.mqtt.reasoncodes.ReasonCode]):
        if not (msg_id in self.subscription_ids):
            return
        # Assuming the topic was subscribed only for a single channel and reason_code_list contains
        # a single entry
        if reason_code_list[0].is_failure:
            self.logging_func(paho.mqtt.enums.LogLevel.MQTT_LOG_ERROR, (f"Broker rejected subscription id {msg_id} reason: {reason_code_list[0]}"))
            return
        self.subscription_ids.remove(msg_id)
        if len(self.subscription_ids) == 0:
            self.on_ready.fire()

    def set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        topic = "tb.simple/SimpleArrayInterface/set/propBool"
        self.client.set_remote_property(topic, [utils.base_types.from_bool(_) for _ in value])

    def get_prop_bool(self):
        return self._prop_bool

    def set_prop_int(self, value):
        if self._prop_int == value:
            return
        topic = "tb.simple/SimpleArrayInterface/set/propInt"
        self.client.set_remote_property(topic, [utils.base_types.from_int(_) for _ in value])

    def get_prop_int(self):
        return self._prop_int

    def set_prop_int32(self, value):
        if self._prop_int32 == value:
            return
        topic = "tb.simple/SimpleArrayInterface/set/propInt32"
        self.client.set_remote_property(topic, [utils.base_types.from_int32(_) for _ in value])

    def get_prop_int32(self):
        return self._prop_int32

    def set_prop_int64(self, value):
        if self._prop_int64 == value:
            return
        topic = "tb.simple/SimpleArrayInterface/set/propInt64"
        self.client.set_remote_property(topic, [utils.base_types.from_int64(_) for _ in value])

    def get_prop_int64(self):
        return self._prop_int64

    def set_prop_float(self, value):
        if self._prop_float == value:
            return
        topic = "tb.simple/SimpleArrayInterface/set/propFloat"
        self.client.set_remote_property(topic, [utils.base_types.from_float(_) for _ in value])

    def get_prop_float(self):
        return self._prop_float

    def set_prop_float32(self, value):
        if self._prop_float32 == value:
            return
        topic = "tb.simple/SimpleArrayInterface/set/propFloat32"
        self.client.set_remote_property(topic, [utils.base_types.from_float32(_) for _ in value])

    def get_prop_float32(self):
        return self._prop_float32

    def set_prop_float64(self, value):
        if self._prop_float64 == value:
            return
        topic = "tb.simple/SimpleArrayInterface/set/propFloat64"
        self.client.set_remote_property(topic, [utils.base_types.from_float64(_) for _ in value])

    def get_prop_float64(self):
        return self._prop_float64

    def set_prop_string(self, value):
        if self._prop_string == value:
            return
        topic = "tb.simple/SimpleArrayInterface/set/propString"
        self.client.set_remote_property(topic, [utils.base_types.from_string(_) for _ in value])

    def get_prop_string(self):
        return self._prop_string

    def get_prop_read_only_string(self):
        return self._prop_read_only_string

    async def func_bool(self, param_bool: list[bool]):
        _param_bool = [utils.base_types.from_bool(bool) for bool in param_bool]
        args = [_param_bool]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result([utils.base_types.as_bool(_) for _ in result])
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func_bool, self.method_topics.resp_topic_func_bool, args)
        self.pending_calls.func_bool[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func_int(self, param_int: list[int]):
        _param_int = [utils.base_types.from_int(int) for int in param_int]
        args = [_param_int]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result([utils.base_types.as_int(_) for _ in result])
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func_int, self.method_topics.resp_topic_func_int, args)
        self.pending_calls.func_int[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func_int32(self, param_int32: list[int]):
        _param_int32 = [utils.base_types.from_int32(int32) for int32 in param_int32]
        args = [_param_int32]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result([utils.base_types.as_int32(_) for _ in result])
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func_int32, self.method_topics.resp_topic_func_int32, args)
        self.pending_calls.func_int32[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func_int64(self, param_int64: list[int]):
        _param_int64 = [utils.base_types.from_int64(int64) for int64 in param_int64]
        args = [_param_int64]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result([utils.base_types.as_int64(_) for _ in result])
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func_int64, self.method_topics.resp_topic_func_int64, args)
        self.pending_calls.func_int64[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func_float(self, param_float: list[float]):
        _param_float = [utils.base_types.from_float(float) for float in param_float]
        args = [_param_float]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result([utils.base_types.as_float(_) for _ in result])
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func_float, self.method_topics.resp_topic_func_float, args)
        self.pending_calls.func_float[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func_float32(self, param_float32: list[float]):
        _param_float32 = [utils.base_types.from_float32(float32) for float32 in param_float32]
        args = [_param_float32]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result([utils.base_types.as_float32(_) for _ in result])
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func_float32, self.method_topics.resp_topic_func_float32, args)
        self.pending_calls.func_float32[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func_float64(self, param_float: list[float]):
        _param_float = [utils.base_types.from_float64(float64) for float64 in param_float]
        args = [_param_float]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result([utils.base_types.as_float64(_) for _ in result])
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func_float64, self.method_topics.resp_topic_func_float64, args)
        self.pending_calls.func_float64[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func_string(self, param_string: list[str]):
        _param_string = [utils.base_types.from_string(string) for string in param_string]
        args = [_param_string]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result([utils.base_types.as_string(_) for _ in result])
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func_string, self.method_topics.resp_topic_func_string, args)
        self.pending_calls.func_string[call_id] = func
        return await asyncio.wait_for(future, 500)

    # internal functions on message handle

    def __set_prop_bool(self, data):
        value = [utils.base_types.as_bool(_) for _ in data]
        if self._prop_bool == value:
            return
        self._prop_bool = value
        self.on_prop_bool_changed.fire(self._prop_bool)

    def __set_prop_int(self, data):
        value = [utils.base_types.as_int(_) for _ in data]
        if self._prop_int == value:
            return
        self._prop_int = value
        self.on_prop_int_changed.fire(self._prop_int)

    def __set_prop_int32(self, data):
        value = [utils.base_types.as_int32(_) for _ in data]
        if self._prop_int32 == value:
            return
        self._prop_int32 = value
        self.on_prop_int32_changed.fire(self._prop_int32)

    def __set_prop_int64(self, data):
        value = [utils.base_types.as_int64(_) for _ in data]
        if self._prop_int64 == value:
            return
        self._prop_int64 = value
        self.on_prop_int64_changed.fire(self._prop_int64)

    def __set_prop_float(self, data):
        value = [utils.base_types.as_float(_) for _ in data]
        if self._prop_float == value:
            return
        self._prop_float = value
        self.on_prop_float_changed.fire(self._prop_float)

    def __set_prop_float32(self, data):
        value = [utils.base_types.as_float32(_) for _ in data]
        if self._prop_float32 == value:
            return
        self._prop_float32 = value
        self.on_prop_float32_changed.fire(self._prop_float32)

    def __set_prop_float64(self, data):
        value = [utils.base_types.as_float64(_) for _ in data]
        if self._prop_float64 == value:
            return
        self._prop_float64 = value
        self.on_prop_float64_changed.fire(self._prop_float64)

    def __set_prop_string(self, data):
        value = [utils.base_types.as_string(_) for _ in data]
        if self._prop_string == value:
            return
        self._prop_string = value
        self.on_prop_string_changed.fire(self._prop_string)

    def __set_prop_read_only_string(self, data):
        value =  utils.base_types.as_string(data)
        if self._prop_read_only_string == value:
            return
        self._prop_read_only_string = value
        self.on_prop_read_only_string_changed.fire(self._prop_read_only_string)

    def __on_sig_bool_signal(self, args: list[Any]):
        param_bool = [utils.base_types.as_bool(_) for _ in args[0]]
        self.on_sig_bool.fire(param_bool)
        return

    def __on_sig_int_signal(self, args: list[Any]):
        param_int = [utils.base_types.as_int(_) for _ in args[0]]
        self.on_sig_int.fire(param_int)
        return

    def __on_sig_int32_signal(self, args: list[Any]):
        param_int32 = [utils.base_types.as_int32(_) for _ in args[0]]
        self.on_sig_int32.fire(param_int32)
        return

    def __on_sig_int64_signal(self, args: list[Any]):
        param_int64 = [utils.base_types.as_int64(_) for _ in args[0]]
        self.on_sig_int64.fire(param_int64)
        return

    def __on_sig_float_signal(self, args: list[Any]):
        param_float = [utils.base_types.as_float(_) for _ in args[0]]
        self.on_sig_float.fire(param_float)
        return

    def __on_sig_float32_signal(self, args: list[Any]):
        param_floa32 = [utils.base_types.as_float32(_) for _ in args[0]]
        self.on_sig_float32.fire(param_floa32)
        return

    def __on_sig_float64_signal(self, args: list[Any]):
        param_float64 = [utils.base_types.as_float64(_) for _ in args[0]]
        self.on_sig_float64.fire(param_float64)
        return

    def __on_sig_string_signal(self, args: list[Any]):
        param_string = [utils.base_types.as_string(_) for _ in args[0]]
        self.on_sig_string.fire(param_string)
        return

    def __on_func_bool_resp(self, value, callId):
       callback = self.pending_calls.func_bool.pop(callId)
       if callback != None:
           callback(value)

    def __on_func_int_resp(self, value, callId):
       callback = self.pending_calls.func_int.pop(callId)
       if callback != None:
           callback(value)

    def __on_func_int32_resp(self, value, callId):
       callback = self.pending_calls.func_int32.pop(callId)
       if callback != None:
           callback(value)

    def __on_func_int64_resp(self, value, callId):
       callback = self.pending_calls.func_int64.pop(callId)
       if callback != None:
           callback(value)

    def __on_func_float_resp(self, value, callId):
       callback = self.pending_calls.func_float.pop(callId)
       if callback != None:
           callback(value)

    def __on_func_float32_resp(self, value, callId):
       callback = self.pending_calls.func_float32.pop(callId)
       if callback != None:
           callback(value)

    def __on_func_float64_resp(self, value, callId):
       callback = self.pending_calls.func_float64.pop(callId)
       if callback != None:
           callback(value)

    def __on_func_string_resp(self, value, callId):
       callback = self.pending_calls.func_string.pop(callId)
       if callback != None:
           callback(value)
    class MethodTopics:
        def __init__(self, client_id):
            self.topic_func_bool= "tb.simple/SimpleArrayInterface/rpc/funcBool"
            self.resp_topic_func_bool= self.topic_func_bool + "/" + str(client_id) + "/result"
            self.topic_func_int= "tb.simple/SimpleArrayInterface/rpc/funcInt"
            self.resp_topic_func_int= self.topic_func_int + "/" + str(client_id) + "/result"
            self.topic_func_int32= "tb.simple/SimpleArrayInterface/rpc/funcInt32"
            self.resp_topic_func_int32= self.topic_func_int32 + "/" + str(client_id) + "/result"
            self.topic_func_int64= "tb.simple/SimpleArrayInterface/rpc/funcInt64"
            self.resp_topic_func_int64= self.topic_func_int64 + "/" + str(client_id) + "/result"
            self.topic_func_float= "tb.simple/SimpleArrayInterface/rpc/funcFloat"
            self.resp_topic_func_float= self.topic_func_float + "/" + str(client_id) + "/result"
            self.topic_func_float32= "tb.simple/SimpleArrayInterface/rpc/funcFloat32"
            self.resp_topic_func_float32= self.topic_func_float32 + "/" + str(client_id) + "/result"
            self.topic_func_float64= "tb.simple/SimpleArrayInterface/rpc/funcFloat64"
            self.resp_topic_func_float64= self.topic_func_float64 + "/" + str(client_id) + "/result"
            self.topic_func_string= "tb.simple/SimpleArrayInterface/rpc/funcString"
            self.resp_topic_func_string= self.topic_func_string + "/" + str(client_id) + "/result"

    class PendingCalls:
        def __init__(self):
            self.func_bool = {}
            self.func_int = {}
            self.func_int32 = {}
            self.func_int64 = {}
            self.func_float = {}
            self.func_float32 = {}
            self.func_float64 = {}
            self.func_string = {}

class NoPropertiesInterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self.on_ready = EventHook()
        self.on_sig_void = EventHook()
        self.on_sig_bool = EventHook()
        self.client.on_subscribed += self.__handle_subscribed
        self.subscription_ids = []
        self.client.on_connected += self.subscribeForTopics
        self.method_topics = self.MethodTopics(self.client.get_client_id())
        self.pending_calls = self.PendingCalls()
        self.loop = asyncio.get_event_loop()

    def subscribeForTopics(self):
        self.subscription_ids.append(self.client.subscribe_for_signal("tb.simple/NoPropertiesInterface/sig/sigVoid",  self.__on_sig_void_signal))
        self.subscription_ids.append(self.client.subscribe_for_signal("tb.simple/NoPropertiesInterface/sig/sigBool",  self.__on_sig_bool_signal))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func_void, self.__on_func_void_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func_bool, self.__on_func_bool_resp))

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.on_subscribed -= self.__handle_subscribed
        self.client.unsubscribe("tb.simple/NoPropertiesInterface/sig/sigVoid")
        self.client.unsubscribe("tb.simple/NoPropertiesInterface/sig/sigBool")
        self.client.unsubscribe(self.method_topics.resp_topic_func_void)
        self.client.unsubscribe(self.method_topics.resp_topic_func_bool)

    def __handle_subscribed(self, msg_id: int, reason_code_list: list[paho.mqtt.reasoncodes.ReasonCode]):
        if not (msg_id in self.subscription_ids):
            return
        # Assuming the topic was subscribed only for a single channel and reason_code_list contains
        # a single entry
        if reason_code_list[0].is_failure:
            self.logging_func(paho.mqtt.enums.LogLevel.MQTT_LOG_ERROR, (f"Broker rejected subscription id {msg_id} reason: {reason_code_list[0]}"))
            return
        self.subscription_ids.remove(msg_id)
        if len(self.subscription_ids) == 0:
            self.on_ready.fire()

    async def func_void(self):
        args = []
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(None)
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func_void, self.method_topics.resp_topic_func_void, args)
        self.pending_calls.func_void[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func_bool(self, param_bool: bool):
        _param_bool = utils.base_types.from_bool(param_bool)
        args = [_param_bool]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(utils.base_types.as_bool(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func_bool, self.method_topics.resp_topic_func_bool, args)
        self.pending_calls.func_bool[call_id] = func
        return await asyncio.wait_for(future, 500)

    # internal functions on message handle

    def __on_sig_void_signal(self, args: list[Any]):
        self.on_sig_void.fire()
        return

    def __on_sig_bool_signal(self, args: list[Any]):
        param_bool =  utils.base_types.as_bool(args[0])
        self.on_sig_bool.fire(param_bool)
        return

    def __on_func_void_resp(self, value, callId):
       callback = self.pending_calls.func_void.pop(callId)
       if callback != None:
           callback(value)

    def __on_func_bool_resp(self, value, callId):
       callback = self.pending_calls.func_bool.pop(callId)
       if callback != None:
           callback(value)
    class MethodTopics:
        def __init__(self, client_id):
            self.topic_func_void= "tb.simple/NoPropertiesInterface/rpc/funcVoid"
            self.resp_topic_func_void= self.topic_func_void + "/" + str(client_id) + "/result"
            self.topic_func_bool= "tb.simple/NoPropertiesInterface/rpc/funcBool"
            self.resp_topic_func_bool= self.topic_func_bool + "/" + str(client_id) + "/result"

    class PendingCalls:
        def __init__(self):
            self.func_void = {}
            self.func_bool = {}

class NoOperationsInterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self.on_ready = EventHook()
        self._prop_bool = False
        self.on_prop_bool_changed = EventHook()
        self._prop_int = 0
        self.on_prop_int_changed = EventHook()
        self.on_sig_void = EventHook()
        self.on_sig_bool = EventHook()
        self.client.on_subscribed += self.__handle_subscribed
        self.subscription_ids = []
        self.client.on_connected += self.subscribeForTopics
        self.loop = asyncio.get_event_loop()

    def subscribeForTopics(self):
        self.subscription_ids.append(self.client.subscribe_for_property("tb.simple/NoOperationsInterface/prop/propBool", self.__set_prop_bool))
        self.subscription_ids.append(self.client.subscribe_for_property("tb.simple/NoOperationsInterface/prop/propInt", self.__set_prop_int))
        self.subscription_ids.append(self.client.subscribe_for_signal("tb.simple/NoOperationsInterface/sig/sigVoid",  self.__on_sig_void_signal))
        self.subscription_ids.append(self.client.subscribe_for_signal("tb.simple/NoOperationsInterface/sig/sigBool",  self.__on_sig_bool_signal))

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.on_subscribed -= self.__handle_subscribed
        self.client.unsubscribe("tb.simple/NoOperationsInterface/prop/propBool")
        self.client.unsubscribe("tb.simple/NoOperationsInterface/prop/propInt")
        self.client.unsubscribe("tb.simple/NoOperationsInterface/sig/sigVoid")
        self.client.unsubscribe("tb.simple/NoOperationsInterface/sig/sigBool")

    def __handle_subscribed(self, msg_id: int, reason_code_list: list[paho.mqtt.reasoncodes.ReasonCode]):
        if not (msg_id in self.subscription_ids):
            return
        # Assuming the topic was subscribed only for a single channel and reason_code_list contains
        # a single entry
        if reason_code_list[0].is_failure:
            self.logging_func(paho.mqtt.enums.LogLevel.MQTT_LOG_ERROR, (f"Broker rejected subscription id {msg_id} reason: {reason_code_list[0]}"))
            return
        self.subscription_ids.remove(msg_id)
        if len(self.subscription_ids) == 0:
            self.on_ready.fire()

    def set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        topic = "tb.simple/NoOperationsInterface/set/propBool"
        self.client.set_remote_property(topic, utils.base_types.from_bool(value))

    def get_prop_bool(self):
        return self._prop_bool

    def set_prop_int(self, value):
        if self._prop_int == value:
            return
        topic = "tb.simple/NoOperationsInterface/set/propInt"
        self.client.set_remote_property(topic, utils.base_types.from_int(value))

    def get_prop_int(self):
        return self._prop_int

    # internal functions on message handle

    def __set_prop_bool(self, data):
        value =  utils.base_types.as_bool(data)
        if self._prop_bool == value:
            return
        self._prop_bool = value
        self.on_prop_bool_changed.fire(self._prop_bool)

    def __set_prop_int(self, data):
        value =  utils.base_types.as_int(data)
        if self._prop_int == value:
            return
        self._prop_int = value
        self.on_prop_int_changed.fire(self._prop_int)

    def __on_sig_void_signal(self, args: list[Any]):
        self.on_sig_void.fire()
        return

    def __on_sig_bool_signal(self, args: list[Any]):
        param_bool =  utils.base_types.as_bool(args[0])
        self.on_sig_bool.fire(param_bool)
        return

class NoSignalsInterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self.on_ready = EventHook()
        self._prop_bool = False
        self.on_prop_bool_changed = EventHook()
        self._prop_int = 0
        self.on_prop_int_changed = EventHook()
        self.client.on_subscribed += self.__handle_subscribed
        self.subscription_ids = []
        self.client.on_connected += self.subscribeForTopics
        self.method_topics = self.MethodTopics(self.client.get_client_id())
        self.pending_calls = self.PendingCalls()
        self.loop = asyncio.get_event_loop()

    def subscribeForTopics(self):
        self.subscription_ids.append(self.client.subscribe_for_property("tb.simple/NoSignalsInterface/prop/propBool", self.__set_prop_bool))
        self.subscription_ids.append(self.client.subscribe_for_property("tb.simple/NoSignalsInterface/prop/propInt", self.__set_prop_int))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func_void, self.__on_func_void_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func_bool, self.__on_func_bool_resp))

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.on_subscribed -= self.__handle_subscribed
        self.client.unsubscribe("tb.simple/NoSignalsInterface/prop/propBool")
        self.client.unsubscribe("tb.simple/NoSignalsInterface/prop/propInt")
        self.client.unsubscribe(self.method_topics.resp_topic_func_void)
        self.client.unsubscribe(self.method_topics.resp_topic_func_bool)

    def __handle_subscribed(self, msg_id: int, reason_code_list: list[paho.mqtt.reasoncodes.ReasonCode]):
        if not (msg_id in self.subscription_ids):
            return
        # Assuming the topic was subscribed only for a single channel and reason_code_list contains
        # a single entry
        if reason_code_list[0].is_failure:
            self.logging_func(paho.mqtt.enums.LogLevel.MQTT_LOG_ERROR, (f"Broker rejected subscription id {msg_id} reason: {reason_code_list[0]}"))
            return
        self.subscription_ids.remove(msg_id)
        if len(self.subscription_ids) == 0:
            self.on_ready.fire()

    def set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        topic = "tb.simple/NoSignalsInterface/set/propBool"
        self.client.set_remote_property(topic, utils.base_types.from_bool(value))

    def get_prop_bool(self):
        return self._prop_bool

    def set_prop_int(self, value):
        if self._prop_int == value:
            return
        topic = "tb.simple/NoSignalsInterface/set/propInt"
        self.client.set_remote_property(topic, utils.base_types.from_int(value))

    def get_prop_int(self):
        return self._prop_int

    async def func_void(self):
        args = []
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(None)
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func_void, self.method_topics.resp_topic_func_void, args)
        self.pending_calls.func_void[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func_bool(self, param_bool: bool):
        _param_bool = utils.base_types.from_bool(param_bool)
        args = [_param_bool]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(utils.base_types.as_bool(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func_bool, self.method_topics.resp_topic_func_bool, args)
        self.pending_calls.func_bool[call_id] = func
        return await asyncio.wait_for(future, 500)

    # internal functions on message handle

    def __set_prop_bool(self, data):
        value =  utils.base_types.as_bool(data)
        if self._prop_bool == value:
            return
        self._prop_bool = value
        self.on_prop_bool_changed.fire(self._prop_bool)

    def __set_prop_int(self, data):
        value =  utils.base_types.as_int(data)
        if self._prop_int == value:
            return
        self._prop_int = value
        self.on_prop_int_changed.fire(self._prop_int)

    def __on_func_void_resp(self, value, callId):
       callback = self.pending_calls.func_void.pop(callId)
       if callback != None:
           callback(value)

    def __on_func_bool_resp(self, value, callId):
       callback = self.pending_calls.func_bool.pop(callId)
       if callback != None:
           callback(value)
    class MethodTopics:
        def __init__(self, client_id):
            self.topic_func_void= "tb.simple/NoSignalsInterface/rpc/funcVoid"
            self.resp_topic_func_void= self.topic_func_void + "/" + str(client_id) + "/result"
            self.topic_func_bool= "tb.simple/NoSignalsInterface/rpc/funcBool"
            self.resp_topic_func_bool= self.topic_func_bool + "/" + str(client_id) + "/result"

    class PendingCalls:
        def __init__(self):
            self.func_void = {}
            self.func_bool = {}
