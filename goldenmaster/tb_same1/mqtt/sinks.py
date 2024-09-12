import asyncio
from typing import Any
import apigear.mqtt
import paho.mqtt.enums
import paho.mqtt.reasoncodes
from utils.eventhook import EventHook
import utils.base_types
import tb_same1.api
import logging

class SameStruct1InterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self.on_ready = EventHook()
        self._prop1 = tb_same1.api.Struct1()
        self.on_prop1_changed = EventHook()
        self.on_sig1 = EventHook()
        self.client.on_subscribed += self.__handle_subscribed
        self.subscription_ids = []
        self.client.on_connected += self.subscribeForTopics
        self.method_topics = self.MethodTopics(self.client.get_client_id())
        self.pending_calls = self.PendingCalls()
        self.loop = asyncio.get_event_loop()

    def subscribeForTopics(self):
        self.subscription_ids.append(self.client.subscribe_for_property("tb.same1/SameStruct1Interface/prop/prop1", self.__set_prop1))
        self.subscription_ids.append(self.client.subscribe_for_signal("tb.same1/SameStruct1Interface/sig/sig1",  self.__on_sig1_signal))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func1, self.__on_func1_resp))

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.on_subscribed -= self.__handle_subscribed
        self.client.unsubscribe("tb.same1/SameStruct1Interface/prop/prop1")
        self.client.unsubscribe("tb.same1/SameStruct1Interface/sig/sig1")
        self.client.unsubscribe(self.method_topics.resp_topic_func1)

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

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        topic = "tb.same1/SameStruct1Interface/set/prop1"
        self.client.set_remote_property(topic, tb_same1.api.from_struct1(value))

    def get_prop1(self):
        return self._prop1

    async def func1(self, param1: tb_same1.api.Struct1):
        _param1 = tb_same1.api.from_struct1(param1)
        args = [_param1]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(tb_same1.api.as_struct1(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func1, self.method_topics.resp_topic_func1, args)
        self.pending_calls.func1[call_id] = func
        return await asyncio.wait_for(future, 500)

    # internal functions on message handle

    def __set_prop1(self, data):
        value =  tb_same1.api.as_struct1(data)
        if self._prop1 == value:
            return
        self._prop1 = value
        self.on_prop1_changed.fire(self._prop1)

    def __on_sig1_signal(self, args: list[Any]):
        param1 =  tb_same1.api.as_struct1(args[0])
        self.on_sig1.fire(param1)
        return

    def __on_func1_resp(self, value, callId):
       callback = self.pending_calls.func1.pop(callId)
       if callback != None:
           callback(value)
    class MethodTopics:
        def __init__(self, client_id):
            self.topic_func1= "tb.same1/SameStruct1Interface/rpc/func1"
            self.resp_topic_func1= self.topic_func1 + "/" + str(client_id) + "/result"

    class PendingCalls:
        def __init__(self):
            self.func1 = {}

class SameStruct2InterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self.on_ready = EventHook()
        self._prop1 = tb_same1.api.Struct2()
        self.on_prop1_changed = EventHook()
        self._prop2 = tb_same1.api.Struct2()
        self.on_prop2_changed = EventHook()
        self.on_sig1 = EventHook()
        self.on_sig2 = EventHook()
        self.client.on_subscribed += self.__handle_subscribed
        self.subscription_ids = []
        self.client.on_connected += self.subscribeForTopics
        self.method_topics = self.MethodTopics(self.client.get_client_id())
        self.pending_calls = self.PendingCalls()
        self.loop = asyncio.get_event_loop()

    def subscribeForTopics(self):
        self.subscription_ids.append(self.client.subscribe_for_property("tb.same1/SameStruct2Interface/prop/prop1", self.__set_prop1))
        self.subscription_ids.append(self.client.subscribe_for_property("tb.same1/SameStruct2Interface/prop/prop2", self.__set_prop2))
        self.subscription_ids.append(self.client.subscribe_for_signal("tb.same1/SameStruct2Interface/sig/sig1",  self.__on_sig1_signal))
        self.subscription_ids.append(self.client.subscribe_for_signal("tb.same1/SameStruct2Interface/sig/sig2",  self.__on_sig2_signal))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func1, self.__on_func1_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func2, self.__on_func2_resp))

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.on_subscribed -= self.__handle_subscribed
        self.client.unsubscribe("tb.same1/SameStruct2Interface/prop/prop1")
        self.client.unsubscribe("tb.same1/SameStruct2Interface/prop/prop2")
        self.client.unsubscribe("tb.same1/SameStruct2Interface/sig/sig1")
        self.client.unsubscribe("tb.same1/SameStruct2Interface/sig/sig2")
        self.client.unsubscribe(self.method_topics.resp_topic_func1)
        self.client.unsubscribe(self.method_topics.resp_topic_func2)

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

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        topic = "tb.same1/SameStruct2Interface/set/prop1"
        self.client.set_remote_property(topic, tb_same1.api.from_struct2(value))

    def get_prop1(self):
        return self._prop1

    def set_prop2(self, value):
        if self._prop2 == value:
            return
        topic = "tb.same1/SameStruct2Interface/set/prop2"
        self.client.set_remote_property(topic, tb_same1.api.from_struct2(value))

    def get_prop2(self):
        return self._prop2

    async def func1(self, param1: tb_same1.api.Struct1):
        _param1 = tb_same1.api.from_struct1(param1)
        args = [_param1]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(tb_same1.api.as_struct1(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func1, self.method_topics.resp_topic_func1, args)
        self.pending_calls.func1[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func2(self, param1: tb_same1.api.Struct1, param2: tb_same1.api.Struct2):
        _param1 = tb_same1.api.from_struct1(param1)
        _param2 = tb_same1.api.from_struct2(param2)
        args = [_param1, _param2]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(tb_same1.api.as_struct1(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func2, self.method_topics.resp_topic_func2, args)
        self.pending_calls.func2[call_id] = func
        return await asyncio.wait_for(future, 500)

    # internal functions on message handle

    def __set_prop1(self, data):
        value =  tb_same1.api.as_struct2(data)
        if self._prop1 == value:
            return
        self._prop1 = value
        self.on_prop1_changed.fire(self._prop1)

    def __set_prop2(self, data):
        value =  tb_same1.api.as_struct2(data)
        if self._prop2 == value:
            return
        self._prop2 = value
        self.on_prop2_changed.fire(self._prop2)

    def __on_sig1_signal(self, args: list[Any]):
        param1 =  tb_same1.api.as_struct1(args[0])
        self.on_sig1.fire(param1)
        return

    def __on_sig2_signal(self, args: list[Any]):
        param1 =  tb_same1.api.as_struct1(args[0])
        param2 =  tb_same1.api.as_struct2(args[1])
        self.on_sig2.fire(param1, param2)
        return

    def __on_func1_resp(self, value, callId):
       callback = self.pending_calls.func1.pop(callId)
       if callback != None:
           callback(value)

    def __on_func2_resp(self, value, callId):
       callback = self.pending_calls.func2.pop(callId)
       if callback != None:
           callback(value)
    class MethodTopics:
        def __init__(self, client_id):
            self.topic_func1= "tb.same1/SameStruct2Interface/rpc/func1"
            self.resp_topic_func1= self.topic_func1 + "/" + str(client_id) + "/result"
            self.topic_func2= "tb.same1/SameStruct2Interface/rpc/func2"
            self.resp_topic_func2= self.topic_func2 + "/" + str(client_id) + "/result"

    class PendingCalls:
        def __init__(self):
            self.func1 = {}
            self.func2 = {}

class SameEnum1InterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self.on_ready = EventHook()
        self._prop1 = tb_same1.api.Enum1.VALUE1
        self.on_prop1_changed = EventHook()
        self.on_sig1 = EventHook()
        self.client.on_subscribed += self.__handle_subscribed
        self.subscription_ids = []
        self.client.on_connected += self.subscribeForTopics
        self.method_topics = self.MethodTopics(self.client.get_client_id())
        self.pending_calls = self.PendingCalls()
        self.loop = asyncio.get_event_loop()

    def subscribeForTopics(self):
        self.subscription_ids.append(self.client.subscribe_for_property("tb.same1/SameEnum1Interface/prop/prop1", self.__set_prop1))
        self.subscription_ids.append(self.client.subscribe_for_signal("tb.same1/SameEnum1Interface/sig/sig1",  self.__on_sig1_signal))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func1, self.__on_func1_resp))

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.on_subscribed -= self.__handle_subscribed
        self.client.unsubscribe("tb.same1/SameEnum1Interface/prop/prop1")
        self.client.unsubscribe("tb.same1/SameEnum1Interface/sig/sig1")
        self.client.unsubscribe(self.method_topics.resp_topic_func1)

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

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        topic = "tb.same1/SameEnum1Interface/set/prop1"
        self.client.set_remote_property(topic, tb_same1.api.from_enum1(value))

    def get_prop1(self):
        return self._prop1

    async def func1(self, param1: tb_same1.api.Enum1):
        _param1 = tb_same1.api.from_enum1(param1)
        args = [_param1]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(tb_same1.api.as_enum1(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func1, self.method_topics.resp_topic_func1, args)
        self.pending_calls.func1[call_id] = func
        return await asyncio.wait_for(future, 500)

    # internal functions on message handle

    def __set_prop1(self, data):
        value =  tb_same1.api.as_enum1(data)
        if self._prop1 == value:
            return
        self._prop1 = value
        self.on_prop1_changed.fire(self._prop1)

    def __on_sig1_signal(self, args: list[Any]):
        param1 =  tb_same1.api.as_enum1(args[0])
        self.on_sig1.fire(param1)
        return

    def __on_func1_resp(self, value, callId):
       callback = self.pending_calls.func1.pop(callId)
       if callback != None:
           callback(value)
    class MethodTopics:
        def __init__(self, client_id):
            self.topic_func1= "tb.same1/SameEnum1Interface/rpc/func1"
            self.resp_topic_func1= self.topic_func1 + "/" + str(client_id) + "/result"

    class PendingCalls:
        def __init__(self):
            self.func1 = {}

class SameEnum2InterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self.on_ready = EventHook()
        self._prop1 = tb_same1.api.Enum1.VALUE1
        self.on_prop1_changed = EventHook()
        self._prop2 = tb_same1.api.Enum2.VALUE1
        self.on_prop2_changed = EventHook()
        self.on_sig1 = EventHook()
        self.on_sig2 = EventHook()
        self.client.on_subscribed += self.__handle_subscribed
        self.subscription_ids = []
        self.client.on_connected += self.subscribeForTopics
        self.method_topics = self.MethodTopics(self.client.get_client_id())
        self.pending_calls = self.PendingCalls()
        self.loop = asyncio.get_event_loop()

    def subscribeForTopics(self):
        self.subscription_ids.append(self.client.subscribe_for_property("tb.same1/SameEnum2Interface/prop/prop1", self.__set_prop1))
        self.subscription_ids.append(self.client.subscribe_for_property("tb.same1/SameEnum2Interface/prop/prop2", self.__set_prop2))
        self.subscription_ids.append(self.client.subscribe_for_signal("tb.same1/SameEnum2Interface/sig/sig1",  self.__on_sig1_signal))
        self.subscription_ids.append(self.client.subscribe_for_signal("tb.same1/SameEnum2Interface/sig/sig2",  self.__on_sig2_signal))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func1, self.__on_func1_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func2, self.__on_func2_resp))

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.on_subscribed -= self.__handle_subscribed
        self.client.unsubscribe("tb.same1/SameEnum2Interface/prop/prop1")
        self.client.unsubscribe("tb.same1/SameEnum2Interface/prop/prop2")
        self.client.unsubscribe("tb.same1/SameEnum2Interface/sig/sig1")
        self.client.unsubscribe("tb.same1/SameEnum2Interface/sig/sig2")
        self.client.unsubscribe(self.method_topics.resp_topic_func1)
        self.client.unsubscribe(self.method_topics.resp_topic_func2)

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

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        topic = "tb.same1/SameEnum2Interface/set/prop1"
        self.client.set_remote_property(topic, tb_same1.api.from_enum1(value))

    def get_prop1(self):
        return self._prop1

    def set_prop2(self, value):
        if self._prop2 == value:
            return
        topic = "tb.same1/SameEnum2Interface/set/prop2"
        self.client.set_remote_property(topic, tb_same1.api.from_enum2(value))

    def get_prop2(self):
        return self._prop2

    async def func1(self, param1: tb_same1.api.Enum1):
        _param1 = tb_same1.api.from_enum1(param1)
        args = [_param1]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(tb_same1.api.as_enum1(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func1, self.method_topics.resp_topic_func1, args)
        self.pending_calls.func1[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func2(self, param1: tb_same1.api.Enum1, param2: tb_same1.api.Enum2):
        _param1 = tb_same1.api.from_enum1(param1)
        _param2 = tb_same1.api.from_enum2(param2)
        args = [_param1, _param2]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(tb_same1.api.as_enum1(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func2, self.method_topics.resp_topic_func2, args)
        self.pending_calls.func2[call_id] = func
        return await asyncio.wait_for(future, 500)

    # internal functions on message handle

    def __set_prop1(self, data):
        value =  tb_same1.api.as_enum1(data)
        if self._prop1 == value:
            return
        self._prop1 = value
        self.on_prop1_changed.fire(self._prop1)

    def __set_prop2(self, data):
        value =  tb_same1.api.as_enum2(data)
        if self._prop2 == value:
            return
        self._prop2 = value
        self.on_prop2_changed.fire(self._prop2)

    def __on_sig1_signal(self, args: list[Any]):
        param1 =  tb_same1.api.as_enum1(args[0])
        self.on_sig1.fire(param1)
        return

    def __on_sig2_signal(self, args: list[Any]):
        param1 =  tb_same1.api.as_enum1(args[0])
        param2 =  tb_same1.api.as_enum2(args[1])
        self.on_sig2.fire(param1, param2)
        return

    def __on_func1_resp(self, value, callId):
       callback = self.pending_calls.func1.pop(callId)
       if callback != None:
           callback(value)

    def __on_func2_resp(self, value, callId):
       callback = self.pending_calls.func2.pop(callId)
       if callback != None:
           callback(value)
    class MethodTopics:
        def __init__(self, client_id):
            self.topic_func1= "tb.same1/SameEnum2Interface/rpc/func1"
            self.resp_topic_func1= self.topic_func1 + "/" + str(client_id) + "/result"
            self.topic_func2= "tb.same1/SameEnum2Interface/rpc/func2"
            self.resp_topic_func2= self.topic_func2 + "/" + str(client_id) + "/result"

    class PendingCalls:
        def __init__(self):
            self.func1 = {}
            self.func2 = {}
