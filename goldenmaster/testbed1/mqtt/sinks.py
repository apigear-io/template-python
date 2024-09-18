import asyncio
from typing import Any
import apigear.mqtt
import paho.mqtt.enums
import paho.mqtt.reasoncodes
from utils.eventhook import EventHook
import utils.base_types
import testbed1.api
import logging

class StructInterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self.on_ready = EventHook()
        self._prop_bool = testbed1.api.StructBool()
        self.on_prop_bool_changed = EventHook()
        self._prop_int = testbed1.api.StructInt()
        self.on_prop_int_changed = EventHook()
        self._prop_float = testbed1.api.StructFloat()
        self.on_prop_float_changed = EventHook()
        self._prop_string = testbed1.api.StructString()
        self.on_prop_string_changed = EventHook()
        self.on_sig_bool = EventHook()
        self.on_sig_int = EventHook()
        self.on_sig_float = EventHook()
        self.on_sig_string = EventHook()
        self.client.on_subscribed += self.__handle_subscribed
        self.subscription_ids = []
        self.client.on_connected += self.subscribeForTopics
        self.method_topics = self.MethodTopics(self.client.get_client_id())
        self.pending_calls = self.PendingCalls()
        self.loop = asyncio.get_event_loop()

    def subscribeForTopics(self):
        self.subscription_ids.append(self.client.subscribe_for_property("testbed1/StructInterface/prop/propBool", self.__set_prop_bool))
        self.subscription_ids.append(self.client.subscribe_for_property("testbed1/StructInterface/prop/propInt", self.__set_prop_int))
        self.subscription_ids.append(self.client.subscribe_for_property("testbed1/StructInterface/prop/propFloat", self.__set_prop_float))
        self.subscription_ids.append(self.client.subscribe_for_property("testbed1/StructInterface/prop/propString", self.__set_prop_string))
        self.subscription_ids.append(self.client.subscribe_for_signal("testbed1/StructInterface/sig/sigBool",  self.__on_sig_bool_signal))
        self.subscription_ids.append(self.client.subscribe_for_signal("testbed1/StructInterface/sig/sigInt",  self.__on_sig_int_signal))
        self.subscription_ids.append(self.client.subscribe_for_signal("testbed1/StructInterface/sig/sigFloat",  self.__on_sig_float_signal))
        self.subscription_ids.append(self.client.subscribe_for_signal("testbed1/StructInterface/sig/sigString",  self.__on_sig_string_signal))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func_bool, self.__on_func_bool_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func_int, self.__on_func_int_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func_float, self.__on_func_float_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func_string, self.__on_func_string_resp))

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.on_subscribed -= self.__handle_subscribed
        self.client.unsubscribe("testbed1/StructInterface/prop/propBool")
        self.client.unsubscribe("testbed1/StructInterface/prop/propInt")
        self.client.unsubscribe("testbed1/StructInterface/prop/propFloat")
        self.client.unsubscribe("testbed1/StructInterface/prop/propString")
        self.client.unsubscribe("testbed1/StructInterface/sig/sigBool")
        self.client.unsubscribe("testbed1/StructInterface/sig/sigInt")
        self.client.unsubscribe("testbed1/StructInterface/sig/sigFloat")
        self.client.unsubscribe("testbed1/StructInterface/sig/sigString")
        self.client.unsubscribe(self.method_topics.resp_topic_func_bool)
        self.client.unsubscribe(self.method_topics.resp_topic_func_int)
        self.client.unsubscribe(self.method_topics.resp_topic_func_float)
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
        topic = "testbed1/StructInterface/set/propBool"
        self.client.set_remote_property(topic, testbed1.api.from_struct_bool(value))

    def get_prop_bool(self):
        return self._prop_bool

    def set_prop_int(self, value):
        if self._prop_int == value:
            return
        topic = "testbed1/StructInterface/set/propInt"
        self.client.set_remote_property(topic, testbed1.api.from_struct_int(value))

    def get_prop_int(self):
        return self._prop_int

    def set_prop_float(self, value):
        if self._prop_float == value:
            return
        topic = "testbed1/StructInterface/set/propFloat"
        self.client.set_remote_property(topic, testbed1.api.from_struct_float(value))

    def get_prop_float(self):
        return self._prop_float

    def set_prop_string(self, value):
        if self._prop_string == value:
            return
        topic = "testbed1/StructInterface/set/propString"
        self.client.set_remote_property(topic, testbed1.api.from_struct_string(value))

    def get_prop_string(self):
        return self._prop_string

    async def func_bool(self, param_bool: testbed1.api.StructBool):
        _param_bool = testbed1.api.from_struct_bool(param_bool)
        args = [_param_bool]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(testbed1.api.as_struct_bool(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func_bool, self.method_topics.resp_topic_func_bool, args)
        self.pending_calls.func_bool[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func_int(self, param_int: testbed1.api.StructInt):
        _param_int = testbed1.api.from_struct_int(param_int)
        args = [_param_int]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(testbed1.api.as_struct_int(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func_int, self.method_topics.resp_topic_func_int, args)
        self.pending_calls.func_int[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func_float(self, param_float: testbed1.api.StructFloat):
        _param_float = testbed1.api.from_struct_float(param_float)
        args = [_param_float]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(testbed1.api.as_struct_float(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func_float, self.method_topics.resp_topic_func_float, args)
        self.pending_calls.func_float[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func_string(self, param_string: testbed1.api.StructString):
        _param_string = testbed1.api.from_struct_string(param_string)
        args = [_param_string]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(testbed1.api.as_struct_string(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func_string, self.method_topics.resp_topic_func_string, args)
        self.pending_calls.func_string[call_id] = func
        return await asyncio.wait_for(future, 500)

    # internal functions on message handle

    def __set_prop_bool(self, data):
        value =  testbed1.api.as_struct_bool(data)
        if self._prop_bool == value:
            return
        self._prop_bool = value
        self.on_prop_bool_changed.fire(self._prop_bool)

    def __set_prop_int(self, data):
        value =  testbed1.api.as_struct_int(data)
        if self._prop_int == value:
            return
        self._prop_int = value
        self.on_prop_int_changed.fire(self._prop_int)

    def __set_prop_float(self, data):
        value =  testbed1.api.as_struct_float(data)
        if self._prop_float == value:
            return
        self._prop_float = value
        self.on_prop_float_changed.fire(self._prop_float)

    def __set_prop_string(self, data):
        value =  testbed1.api.as_struct_string(data)
        if self._prop_string == value:
            return
        self._prop_string = value
        self.on_prop_string_changed.fire(self._prop_string)

    def __on_sig_bool_signal(self, args: list[Any]):
        param_bool =  testbed1.api.as_struct_bool(args[0])
        self.on_sig_bool.fire(param_bool)
        return

    def __on_sig_int_signal(self, args: list[Any]):
        param_int =  testbed1.api.as_struct_int(args[0])
        self.on_sig_int.fire(param_int)
        return

    def __on_sig_float_signal(self, args: list[Any]):
        param_float =  testbed1.api.as_struct_float(args[0])
        self.on_sig_float.fire(param_float)
        return

    def __on_sig_string_signal(self, args: list[Any]):
        param_string =  testbed1.api.as_struct_string(args[0])
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

    def __on_func_float_resp(self, value, callId):
       callback = self.pending_calls.func_float.pop(callId)
       if callback != None:
           callback(value)

    def __on_func_string_resp(self, value, callId):
       callback = self.pending_calls.func_string.pop(callId)
       if callback != None:
           callback(value)
    class MethodTopics:
        def __init__(self, client_id):
            self.topic_func_bool= "testbed1/StructInterface/rpc/funcBool"
            self.resp_topic_func_bool= self.topic_func_bool + "/" + str(client_id) + "/result"
            self.topic_func_int= "testbed1/StructInterface/rpc/funcInt"
            self.resp_topic_func_int= self.topic_func_int + "/" + str(client_id) + "/result"
            self.topic_func_float= "testbed1/StructInterface/rpc/funcFloat"
            self.resp_topic_func_float= self.topic_func_float + "/" + str(client_id) + "/result"
            self.topic_func_string= "testbed1/StructInterface/rpc/funcString"
            self.resp_topic_func_string= self.topic_func_string + "/" + str(client_id) + "/result"

    class PendingCalls:
        def __init__(self):
            self.func_bool = {}
            self.func_int = {}
            self.func_float = {}
            self.func_string = {}

class StructArrayInterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self.on_ready = EventHook()
        self._prop_bool = []
        self.on_prop_bool_changed = EventHook()
        self._prop_int = []
        self.on_prop_int_changed = EventHook()
        self._prop_float = []
        self.on_prop_float_changed = EventHook()
        self._prop_string = []
        self.on_prop_string_changed = EventHook()
        self.on_sig_bool = EventHook()
        self.on_sig_int = EventHook()
        self.on_sig_float = EventHook()
        self.on_sig_string = EventHook()
        self.client.on_subscribed += self.__handle_subscribed
        self.subscription_ids = []
        self.client.on_connected += self.subscribeForTopics
        self.method_topics = self.MethodTopics(self.client.get_client_id())
        self.pending_calls = self.PendingCalls()
        self.loop = asyncio.get_event_loop()

    def subscribeForTopics(self):
        self.subscription_ids.append(self.client.subscribe_for_property("testbed1/StructArrayInterface/prop/propBool", self.__set_prop_bool))
        self.subscription_ids.append(self.client.subscribe_for_property("testbed1/StructArrayInterface/prop/propInt", self.__set_prop_int))
        self.subscription_ids.append(self.client.subscribe_for_property("testbed1/StructArrayInterface/prop/propFloat", self.__set_prop_float))
        self.subscription_ids.append(self.client.subscribe_for_property("testbed1/StructArrayInterface/prop/propString", self.__set_prop_string))
        self.subscription_ids.append(self.client.subscribe_for_signal("testbed1/StructArrayInterface/sig/sigBool",  self.__on_sig_bool_signal))
        self.subscription_ids.append(self.client.subscribe_for_signal("testbed1/StructArrayInterface/sig/sigInt",  self.__on_sig_int_signal))
        self.subscription_ids.append(self.client.subscribe_for_signal("testbed1/StructArrayInterface/sig/sigFloat",  self.__on_sig_float_signal))
        self.subscription_ids.append(self.client.subscribe_for_signal("testbed1/StructArrayInterface/sig/sigString",  self.__on_sig_string_signal))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func_bool, self.__on_func_bool_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func_int, self.__on_func_int_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func_float, self.__on_func_float_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func_string, self.__on_func_string_resp))

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.on_subscribed -= self.__handle_subscribed
        self.client.unsubscribe("testbed1/StructArrayInterface/prop/propBool")
        self.client.unsubscribe("testbed1/StructArrayInterface/prop/propInt")
        self.client.unsubscribe("testbed1/StructArrayInterface/prop/propFloat")
        self.client.unsubscribe("testbed1/StructArrayInterface/prop/propString")
        self.client.unsubscribe("testbed1/StructArrayInterface/sig/sigBool")
        self.client.unsubscribe("testbed1/StructArrayInterface/sig/sigInt")
        self.client.unsubscribe("testbed1/StructArrayInterface/sig/sigFloat")
        self.client.unsubscribe("testbed1/StructArrayInterface/sig/sigString")
        self.client.unsubscribe(self.method_topics.resp_topic_func_bool)
        self.client.unsubscribe(self.method_topics.resp_topic_func_int)
        self.client.unsubscribe(self.method_topics.resp_topic_func_float)
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
        topic = "testbed1/StructArrayInterface/set/propBool"
        self.client.set_remote_property(topic, [testbed1.api.from_struct_bool(_) for _ in value])

    def get_prop_bool(self):
        return self._prop_bool

    def set_prop_int(self, value):
        if self._prop_int == value:
            return
        topic = "testbed1/StructArrayInterface/set/propInt"
        self.client.set_remote_property(topic, [testbed1.api.from_struct_int(_) for _ in value])

    def get_prop_int(self):
        return self._prop_int

    def set_prop_float(self, value):
        if self._prop_float == value:
            return
        topic = "testbed1/StructArrayInterface/set/propFloat"
        self.client.set_remote_property(topic, [testbed1.api.from_struct_float(_) for _ in value])

    def get_prop_float(self):
        return self._prop_float

    def set_prop_string(self, value):
        if self._prop_string == value:
            return
        topic = "testbed1/StructArrayInterface/set/propString"
        self.client.set_remote_property(topic, [testbed1.api.from_struct_string(_) for _ in value])

    def get_prop_string(self):
        return self._prop_string

    async def func_bool(self, param_bool: list[testbed1.api.StructBool]):
        _param_bool = [testbed1.api.from_struct_bool(struct_bool) for struct_bool in param_bool]
        args = [_param_bool]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result([testbed1.api.as_struct_bool(_) for _ in result])
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func_bool, self.method_topics.resp_topic_func_bool, args)
        self.pending_calls.func_bool[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func_int(self, param_int: list[testbed1.api.StructInt]):
        _param_int = [testbed1.api.from_struct_int(struct_int) for struct_int in param_int]
        args = [_param_int]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result([testbed1.api.as_struct_int(_) for _ in result])
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func_int, self.method_topics.resp_topic_func_int, args)
        self.pending_calls.func_int[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func_float(self, param_float: list[testbed1.api.StructFloat]):
        _param_float = [testbed1.api.from_struct_float(struct_float) for struct_float in param_float]
        args = [_param_float]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result([testbed1.api.as_struct_float(_) for _ in result])
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func_float, self.method_topics.resp_topic_func_float, args)
        self.pending_calls.func_float[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func_string(self, param_string: list[testbed1.api.StructString]):
        _param_string = [testbed1.api.from_struct_string(struct_string) for struct_string in param_string]
        args = [_param_string]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result([testbed1.api.as_struct_string(_) for _ in result])
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func_string, self.method_topics.resp_topic_func_string, args)
        self.pending_calls.func_string[call_id] = func
        return await asyncio.wait_for(future, 500)

    # internal functions on message handle

    def __set_prop_bool(self, data):
        value = [testbed1.api.as_struct_bool(_) for _ in data]
        if self._prop_bool == value:
            return
        self._prop_bool = value
        self.on_prop_bool_changed.fire(self._prop_bool)

    def __set_prop_int(self, data):
        value = [testbed1.api.as_struct_int(_) for _ in data]
        if self._prop_int == value:
            return
        self._prop_int = value
        self.on_prop_int_changed.fire(self._prop_int)

    def __set_prop_float(self, data):
        value = [testbed1.api.as_struct_float(_) for _ in data]
        if self._prop_float == value:
            return
        self._prop_float = value
        self.on_prop_float_changed.fire(self._prop_float)

    def __set_prop_string(self, data):
        value = [testbed1.api.as_struct_string(_) for _ in data]
        if self._prop_string == value:
            return
        self._prop_string = value
        self.on_prop_string_changed.fire(self._prop_string)

    def __on_sig_bool_signal(self, args: list[Any]):
        param_bool = [testbed1.api.as_struct_bool(_) for _ in args[0]]
        self.on_sig_bool.fire(param_bool)
        return

    def __on_sig_int_signal(self, args: list[Any]):
        param_int = [testbed1.api.as_struct_int(_) for _ in args[0]]
        self.on_sig_int.fire(param_int)
        return

    def __on_sig_float_signal(self, args: list[Any]):
        param_float = [testbed1.api.as_struct_float(_) for _ in args[0]]
        self.on_sig_float.fire(param_float)
        return

    def __on_sig_string_signal(self, args: list[Any]):
        param_string = [testbed1.api.as_struct_string(_) for _ in args[0]]
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

    def __on_func_float_resp(self, value, callId):
       callback = self.pending_calls.func_float.pop(callId)
       if callback != None:
           callback(value)

    def __on_func_string_resp(self, value, callId):
       callback = self.pending_calls.func_string.pop(callId)
       if callback != None:
           callback(value)
    class MethodTopics:
        def __init__(self, client_id):
            self.topic_func_bool= "testbed1/StructArrayInterface/rpc/funcBool"
            self.resp_topic_func_bool= self.topic_func_bool + "/" + str(client_id) + "/result"
            self.topic_func_int= "testbed1/StructArrayInterface/rpc/funcInt"
            self.resp_topic_func_int= self.topic_func_int + "/" + str(client_id) + "/result"
            self.topic_func_float= "testbed1/StructArrayInterface/rpc/funcFloat"
            self.resp_topic_func_float= self.topic_func_float + "/" + str(client_id) + "/result"
            self.topic_func_string= "testbed1/StructArrayInterface/rpc/funcString"
            self.resp_topic_func_string= self.topic_func_string + "/" + str(client_id) + "/result"

    class PendingCalls:
        def __init__(self):
            self.func_bool = {}
            self.func_int = {}
            self.func_float = {}
            self.func_string = {}
