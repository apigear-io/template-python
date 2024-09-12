import asyncio
from typing import Any
import apigear.mqtt
import paho.mqtt.enums
import paho.mqtt.reasoncodes
from utils.eventhook import EventHook
import utils.base_types
import testbed2.api
import logging

class ManyParamInterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self.on_ready = EventHook()
        self._prop1 = 0
        self.on_prop1_changed = EventHook()
        self._prop2 = 0
        self.on_prop2_changed = EventHook()
        self._prop3 = 0
        self.on_prop3_changed = EventHook()
        self._prop4 = 0
        self.on_prop4_changed = EventHook()
        self.on_sig1 = EventHook()
        self.on_sig2 = EventHook()
        self.on_sig3 = EventHook()
        self.on_sig4 = EventHook()
        self.client.on_subscribed += self.__handle_subscribed
        self.subscription_ids = []
        self.client.on_connected += self.subscribeForTopics
        self.method_topics = self.MethodTopics(self.client.get_client_id())
        self.pending_calls = self.PendingCalls()
        self.loop = asyncio.get_event_loop()

    def subscribeForTopics(self):
        self.subscription_ids.append(self.client.subscribe_for_property("testbed2/ManyParamInterface/prop/prop1", self.__set_prop1))
        self.subscription_ids.append(self.client.subscribe_for_property("testbed2/ManyParamInterface/prop/prop2", self.__set_prop2))
        self.subscription_ids.append(self.client.subscribe_for_property("testbed2/ManyParamInterface/prop/prop3", self.__set_prop3))
        self.subscription_ids.append(self.client.subscribe_for_property("testbed2/ManyParamInterface/prop/prop4", self.__set_prop4))
        self.subscription_ids.append(self.client.subscribe_for_signal("testbed2/ManyParamInterface/sig/sig1",  self.__on_sig1_signal))
        self.subscription_ids.append(self.client.subscribe_for_signal("testbed2/ManyParamInterface/sig/sig2",  self.__on_sig2_signal))
        self.subscription_ids.append(self.client.subscribe_for_signal("testbed2/ManyParamInterface/sig/sig3",  self.__on_sig3_signal))
        self.subscription_ids.append(self.client.subscribe_for_signal("testbed2/ManyParamInterface/sig/sig4",  self.__on_sig4_signal))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func1, self.__on_func1_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func2, self.__on_func2_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func3, self.__on_func3_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func4, self.__on_func4_resp))

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.on_subscribed -= self.__handle_subscribed
        self.client.unsubscribe("testbed2/ManyParamInterface/prop/prop1")
        self.client.unsubscribe("testbed2/ManyParamInterface/prop/prop2")
        self.client.unsubscribe("testbed2/ManyParamInterface/prop/prop3")
        self.client.unsubscribe("testbed2/ManyParamInterface/prop/prop4")
        self.client.unsubscribe("testbed2/ManyParamInterface/sig/sig1")
        self.client.unsubscribe("testbed2/ManyParamInterface/sig/sig2")
        self.client.unsubscribe("testbed2/ManyParamInterface/sig/sig3")
        self.client.unsubscribe("testbed2/ManyParamInterface/sig/sig4")
        self.client.unsubscribe(self.method_topics.resp_topic_func1)
        self.client.unsubscribe(self.method_topics.resp_topic_func2)
        self.client.unsubscribe(self.method_topics.resp_topic_func3)
        self.client.unsubscribe(self.method_topics.resp_topic_func4)

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
        topic = "testbed2/ManyParamInterface/set/prop1"
        self.client.set_remote_property(topic, utils.base_types.from_int(value))

    def get_prop1(self):
        return self._prop1

    def set_prop2(self, value):
        if self._prop2 == value:
            return
        topic = "testbed2/ManyParamInterface/set/prop2"
        self.client.set_remote_property(topic, utils.base_types.from_int(value))

    def get_prop2(self):
        return self._prop2

    def set_prop3(self, value):
        if self._prop3 == value:
            return
        topic = "testbed2/ManyParamInterface/set/prop3"
        self.client.set_remote_property(topic, utils.base_types.from_int(value))

    def get_prop3(self):
        return self._prop3

    def set_prop4(self, value):
        if self._prop4 == value:
            return
        topic = "testbed2/ManyParamInterface/set/prop4"
        self.client.set_remote_property(topic, utils.base_types.from_int(value))

    def get_prop4(self):
        return self._prop4

    async def func1(self, param1: int):
        _param1 = utils.base_types.from_int(param1)
        args = [_param1]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(utils.base_types.as_int(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func1, self.method_topics.resp_topic_func1, args)
        self.pending_calls.func1[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func2(self, param1: int, param2: int):
        _param1 = utils.base_types.from_int(param1)
        _param2 = utils.base_types.from_int(param2)
        args = [_param1, _param2]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(utils.base_types.as_int(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func2, self.method_topics.resp_topic_func2, args)
        self.pending_calls.func2[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func3(self, param1: int, param2: int, param3: int):
        _param1 = utils.base_types.from_int(param1)
        _param2 = utils.base_types.from_int(param2)
        _param3 = utils.base_types.from_int(param3)
        args = [_param1, _param2, _param3]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(utils.base_types.as_int(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func3, self.method_topics.resp_topic_func3, args)
        self.pending_calls.func3[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func4(self, param1: int, param2: int, param3: int, param4: int):
        _param1 = utils.base_types.from_int(param1)
        _param2 = utils.base_types.from_int(param2)
        _param3 = utils.base_types.from_int(param3)
        _param4 = utils.base_types.from_int(param4)
        args = [_param1, _param2, _param3, _param4]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(utils.base_types.as_int(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func4, self.method_topics.resp_topic_func4, args)
        self.pending_calls.func4[call_id] = func
        return await asyncio.wait_for(future, 500)

    # internal functions on message handle

    def __set_prop1(self, data):
        value =  utils.base_types.as_int(data)
        if self._prop1 == value:
            return
        self._prop1 = value
        self.on_prop1_changed.fire(self._prop1)

    def __set_prop2(self, data):
        value =  utils.base_types.as_int(data)
        if self._prop2 == value:
            return
        self._prop2 = value
        self.on_prop2_changed.fire(self._prop2)

    def __set_prop3(self, data):
        value =  utils.base_types.as_int(data)
        if self._prop3 == value:
            return
        self._prop3 = value
        self.on_prop3_changed.fire(self._prop3)

    def __set_prop4(self, data):
        value =  utils.base_types.as_int(data)
        if self._prop4 == value:
            return
        self._prop4 = value
        self.on_prop4_changed.fire(self._prop4)

    def __on_sig1_signal(self, args: list[Any]):
        param1 =  utils.base_types.as_int(args[0])
        self.on_sig1.fire(param1)
        return

    def __on_sig2_signal(self, args: list[Any]):
        param1 =  utils.base_types.as_int(args[0])
        param2 =  utils.base_types.as_int(args[1])
        self.on_sig2.fire(param1, param2)
        return

    def __on_sig3_signal(self, args: list[Any]):
        param1 =  utils.base_types.as_int(args[0])
        param2 =  utils.base_types.as_int(args[1])
        param3 =  utils.base_types.as_int(args[2])
        self.on_sig3.fire(param1, param2, param3)
        return

    def __on_sig4_signal(self, args: list[Any]):
        param1 =  utils.base_types.as_int(args[0])
        param2 =  utils.base_types.as_int(args[1])
        param3 =  utils.base_types.as_int(args[2])
        param4 =  utils.base_types.as_int(args[3])
        self.on_sig4.fire(param1, param2, param3, param4)
        return

    def __on_func1_resp(self, value, callId):
       callback = self.pending_calls.func1.pop(callId)
       if callback != None:
           callback(value)

    def __on_func2_resp(self, value, callId):
       callback = self.pending_calls.func2.pop(callId)
       if callback != None:
           callback(value)

    def __on_func3_resp(self, value, callId):
       callback = self.pending_calls.func3.pop(callId)
       if callback != None:
           callback(value)

    def __on_func4_resp(self, value, callId):
       callback = self.pending_calls.func4.pop(callId)
       if callback != None:
           callback(value)
    class MethodTopics:
        def __init__(self, client_id):
            self.topic_func1= "testbed2/ManyParamInterface/rpc/func1"
            self.resp_topic_func1= self.topic_func1 + "/" + str(client_id) + "/result"
            self.topic_func2= "testbed2/ManyParamInterface/rpc/func2"
            self.resp_topic_func2= self.topic_func2 + "/" + str(client_id) + "/result"
            self.topic_func3= "testbed2/ManyParamInterface/rpc/func3"
            self.resp_topic_func3= self.topic_func3 + "/" + str(client_id) + "/result"
            self.topic_func4= "testbed2/ManyParamInterface/rpc/func4"
            self.resp_topic_func4= self.topic_func4 + "/" + str(client_id) + "/result"

    class PendingCalls:
        def __init__(self):
            self.func1 = {}
            self.func2 = {}
            self.func3 = {}
            self.func4 = {}

class NestedStruct1InterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self.on_ready = EventHook()
        self._prop1 = testbed2.api.NestedStruct1()
        self.on_prop1_changed = EventHook()
        self.on_sig1 = EventHook()
        self.client.on_subscribed += self.__handle_subscribed
        self.subscription_ids = []
        self.client.on_connected += self.subscribeForTopics
        self.method_topics = self.MethodTopics(self.client.get_client_id())
        self.pending_calls = self.PendingCalls()
        self.loop = asyncio.get_event_loop()

    def subscribeForTopics(self):
        self.subscription_ids.append(self.client.subscribe_for_property("testbed2/NestedStruct1Interface/prop/prop1", self.__set_prop1))
        self.subscription_ids.append(self.client.subscribe_for_signal("testbed2/NestedStruct1Interface/sig/sig1",  self.__on_sig1_signal))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func1, self.__on_func1_resp))

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.on_subscribed -= self.__handle_subscribed
        self.client.unsubscribe("testbed2/NestedStruct1Interface/prop/prop1")
        self.client.unsubscribe("testbed2/NestedStruct1Interface/sig/sig1")
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
        topic = "testbed2/NestedStruct1Interface/set/prop1"
        self.client.set_remote_property(topic, testbed2.api.from_nested_struct1(value))

    def get_prop1(self):
        return self._prop1

    async def func1(self, param1: testbed2.api.NestedStruct1):
        _param1 = testbed2.api.from_nested_struct1(param1)
        args = [_param1]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(testbed2.api.as_nested_struct1(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func1, self.method_topics.resp_topic_func1, args)
        self.pending_calls.func1[call_id] = func
        return await asyncio.wait_for(future, 500)

    # internal functions on message handle

    def __set_prop1(self, data):
        value =  testbed2.api.as_nested_struct1(data)
        if self._prop1 == value:
            return
        self._prop1 = value
        self.on_prop1_changed.fire(self._prop1)

    def __on_sig1_signal(self, args: list[Any]):
        param1 =  testbed2.api.as_nested_struct1(args[0])
        self.on_sig1.fire(param1)
        return

    def __on_func1_resp(self, value, callId):
       callback = self.pending_calls.func1.pop(callId)
       if callback != None:
           callback(value)
    class MethodTopics:
        def __init__(self, client_id):
            self.topic_func1= "testbed2/NestedStruct1Interface/rpc/func1"
            self.resp_topic_func1= self.topic_func1 + "/" + str(client_id) + "/result"

    class PendingCalls:
        def __init__(self):
            self.func1 = {}

class NestedStruct2InterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self.on_ready = EventHook()
        self._prop1 = testbed2.api.NestedStruct1()
        self.on_prop1_changed = EventHook()
        self._prop2 = testbed2.api.NestedStruct2()
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
        self.subscription_ids.append(self.client.subscribe_for_property("testbed2/NestedStruct2Interface/prop/prop1", self.__set_prop1))
        self.subscription_ids.append(self.client.subscribe_for_property("testbed2/NestedStruct2Interface/prop/prop2", self.__set_prop2))
        self.subscription_ids.append(self.client.subscribe_for_signal("testbed2/NestedStruct2Interface/sig/sig1",  self.__on_sig1_signal))
        self.subscription_ids.append(self.client.subscribe_for_signal("testbed2/NestedStruct2Interface/sig/sig2",  self.__on_sig2_signal))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func1, self.__on_func1_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func2, self.__on_func2_resp))

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.on_subscribed -= self.__handle_subscribed
        self.client.unsubscribe("testbed2/NestedStruct2Interface/prop/prop1")
        self.client.unsubscribe("testbed2/NestedStruct2Interface/prop/prop2")
        self.client.unsubscribe("testbed2/NestedStruct2Interface/sig/sig1")
        self.client.unsubscribe("testbed2/NestedStruct2Interface/sig/sig2")
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
        topic = "testbed2/NestedStruct2Interface/set/prop1"
        self.client.set_remote_property(topic, testbed2.api.from_nested_struct1(value))

    def get_prop1(self):
        return self._prop1

    def set_prop2(self, value):
        if self._prop2 == value:
            return
        topic = "testbed2/NestedStruct2Interface/set/prop2"
        self.client.set_remote_property(topic, testbed2.api.from_nested_struct2(value))

    def get_prop2(self):
        return self._prop2

    async def func1(self, param1: testbed2.api.NestedStruct1):
        _param1 = testbed2.api.from_nested_struct1(param1)
        args = [_param1]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(testbed2.api.as_nested_struct1(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func1, self.method_topics.resp_topic_func1, args)
        self.pending_calls.func1[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func2(self, param1: testbed2.api.NestedStruct1, param2: testbed2.api.NestedStruct2):
        _param1 = testbed2.api.from_nested_struct1(param1)
        _param2 = testbed2.api.from_nested_struct2(param2)
        args = [_param1, _param2]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(testbed2.api.as_nested_struct1(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func2, self.method_topics.resp_topic_func2, args)
        self.pending_calls.func2[call_id] = func
        return await asyncio.wait_for(future, 500)

    # internal functions on message handle

    def __set_prop1(self, data):
        value =  testbed2.api.as_nested_struct1(data)
        if self._prop1 == value:
            return
        self._prop1 = value
        self.on_prop1_changed.fire(self._prop1)

    def __set_prop2(self, data):
        value =  testbed2.api.as_nested_struct2(data)
        if self._prop2 == value:
            return
        self._prop2 = value
        self.on_prop2_changed.fire(self._prop2)

    def __on_sig1_signal(self, args: list[Any]):
        param1 =  testbed2.api.as_nested_struct1(args[0])
        self.on_sig1.fire(param1)
        return

    def __on_sig2_signal(self, args: list[Any]):
        param1 =  testbed2.api.as_nested_struct1(args[0])
        param2 =  testbed2.api.as_nested_struct2(args[1])
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
            self.topic_func1= "testbed2/NestedStruct2Interface/rpc/func1"
            self.resp_topic_func1= self.topic_func1 + "/" + str(client_id) + "/result"
            self.topic_func2= "testbed2/NestedStruct2Interface/rpc/func2"
            self.resp_topic_func2= self.topic_func2 + "/" + str(client_id) + "/result"

    class PendingCalls:
        def __init__(self):
            self.func1 = {}
            self.func2 = {}

class NestedStruct3InterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self.on_ready = EventHook()
        self._prop1 = testbed2.api.NestedStruct1()
        self.on_prop1_changed = EventHook()
        self._prop2 = testbed2.api.NestedStruct2()
        self.on_prop2_changed = EventHook()
        self._prop3 = testbed2.api.NestedStruct3()
        self.on_prop3_changed = EventHook()
        self.on_sig1 = EventHook()
        self.on_sig2 = EventHook()
        self.on_sig3 = EventHook()
        self.client.on_subscribed += self.__handle_subscribed
        self.subscription_ids = []
        self.client.on_connected += self.subscribeForTopics
        self.method_topics = self.MethodTopics(self.client.get_client_id())
        self.pending_calls = self.PendingCalls()
        self.loop = asyncio.get_event_loop()

    def subscribeForTopics(self):
        self.subscription_ids.append(self.client.subscribe_for_property("testbed2/NestedStruct3Interface/prop/prop1", self.__set_prop1))
        self.subscription_ids.append(self.client.subscribe_for_property("testbed2/NestedStruct3Interface/prop/prop2", self.__set_prop2))
        self.subscription_ids.append(self.client.subscribe_for_property("testbed2/NestedStruct3Interface/prop/prop3", self.__set_prop3))
        self.subscription_ids.append(self.client.subscribe_for_signal("testbed2/NestedStruct3Interface/sig/sig1",  self.__on_sig1_signal))
        self.subscription_ids.append(self.client.subscribe_for_signal("testbed2/NestedStruct3Interface/sig/sig2",  self.__on_sig2_signal))
        self.subscription_ids.append(self.client.subscribe_for_signal("testbed2/NestedStruct3Interface/sig/sig3",  self.__on_sig3_signal))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func1, self.__on_func1_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func2, self.__on_func2_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func3, self.__on_func3_resp))

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.on_subscribed -= self.__handle_subscribed
        self.client.unsubscribe("testbed2/NestedStruct3Interface/prop/prop1")
        self.client.unsubscribe("testbed2/NestedStruct3Interface/prop/prop2")
        self.client.unsubscribe("testbed2/NestedStruct3Interface/prop/prop3")
        self.client.unsubscribe("testbed2/NestedStruct3Interface/sig/sig1")
        self.client.unsubscribe("testbed2/NestedStruct3Interface/sig/sig2")
        self.client.unsubscribe("testbed2/NestedStruct3Interface/sig/sig3")
        self.client.unsubscribe(self.method_topics.resp_topic_func1)
        self.client.unsubscribe(self.method_topics.resp_topic_func2)
        self.client.unsubscribe(self.method_topics.resp_topic_func3)

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
        topic = "testbed2/NestedStruct3Interface/set/prop1"
        self.client.set_remote_property(topic, testbed2.api.from_nested_struct1(value))

    def get_prop1(self):
        return self._prop1

    def set_prop2(self, value):
        if self._prop2 == value:
            return
        topic = "testbed2/NestedStruct3Interface/set/prop2"
        self.client.set_remote_property(topic, testbed2.api.from_nested_struct2(value))

    def get_prop2(self):
        return self._prop2

    def set_prop3(self, value):
        if self._prop3 == value:
            return
        topic = "testbed2/NestedStruct3Interface/set/prop3"
        self.client.set_remote_property(topic, testbed2.api.from_nested_struct3(value))

    def get_prop3(self):
        return self._prop3

    async def func1(self, param1: testbed2.api.NestedStruct1):
        _param1 = testbed2.api.from_nested_struct1(param1)
        args = [_param1]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(testbed2.api.as_nested_struct1(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func1, self.method_topics.resp_topic_func1, args)
        self.pending_calls.func1[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func2(self, param1: testbed2.api.NestedStruct1, param2: testbed2.api.NestedStruct2):
        _param1 = testbed2.api.from_nested_struct1(param1)
        _param2 = testbed2.api.from_nested_struct2(param2)
        args = [_param1, _param2]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(testbed2.api.as_nested_struct1(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func2, self.method_topics.resp_topic_func2, args)
        self.pending_calls.func2[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func3(self, param1: testbed2.api.NestedStruct1, param2: testbed2.api.NestedStruct2, param3: testbed2.api.NestedStruct3):
        _param1 = testbed2.api.from_nested_struct1(param1)
        _param2 = testbed2.api.from_nested_struct2(param2)
        _param3 = testbed2.api.from_nested_struct3(param3)
        args = [_param1, _param2, _param3]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(testbed2.api.as_nested_struct1(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func3, self.method_topics.resp_topic_func3, args)
        self.pending_calls.func3[call_id] = func
        return await asyncio.wait_for(future, 500)

    # internal functions on message handle

    def __set_prop1(self, data):
        value =  testbed2.api.as_nested_struct1(data)
        if self._prop1 == value:
            return
        self._prop1 = value
        self.on_prop1_changed.fire(self._prop1)

    def __set_prop2(self, data):
        value =  testbed2.api.as_nested_struct2(data)
        if self._prop2 == value:
            return
        self._prop2 = value
        self.on_prop2_changed.fire(self._prop2)

    def __set_prop3(self, data):
        value =  testbed2.api.as_nested_struct3(data)
        if self._prop3 == value:
            return
        self._prop3 = value
        self.on_prop3_changed.fire(self._prop3)

    def __on_sig1_signal(self, args: list[Any]):
        param1 =  testbed2.api.as_nested_struct1(args[0])
        self.on_sig1.fire(param1)
        return

    def __on_sig2_signal(self, args: list[Any]):
        param1 =  testbed2.api.as_nested_struct1(args[0])
        param2 =  testbed2.api.as_nested_struct2(args[1])
        self.on_sig2.fire(param1, param2)
        return

    def __on_sig3_signal(self, args: list[Any]):
        param1 =  testbed2.api.as_nested_struct1(args[0])
        param2 =  testbed2.api.as_nested_struct2(args[1])
        param3 =  testbed2.api.as_nested_struct3(args[2])
        self.on_sig3.fire(param1, param2, param3)
        return

    def __on_func1_resp(self, value, callId):
       callback = self.pending_calls.func1.pop(callId)
       if callback != None:
           callback(value)

    def __on_func2_resp(self, value, callId):
       callback = self.pending_calls.func2.pop(callId)
       if callback != None:
           callback(value)

    def __on_func3_resp(self, value, callId):
       callback = self.pending_calls.func3.pop(callId)
       if callback != None:
           callback(value)
    class MethodTopics:
        def __init__(self, client_id):
            self.topic_func1= "testbed2/NestedStruct3Interface/rpc/func1"
            self.resp_topic_func1= self.topic_func1 + "/" + str(client_id) + "/result"
            self.topic_func2= "testbed2/NestedStruct3Interface/rpc/func2"
            self.resp_topic_func2= self.topic_func2 + "/" + str(client_id) + "/result"
            self.topic_func3= "testbed2/NestedStruct3Interface/rpc/func3"
            self.resp_topic_func3= self.topic_func3 + "/" + str(client_id) + "/result"

    class PendingCalls:
        def __init__(self):
            self.func1 = {}
            self.func2 = {}
            self.func3 = {}
