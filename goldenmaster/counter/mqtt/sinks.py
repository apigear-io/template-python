import asyncio
from typing import Any
import apigear.mqtt
import paho.mqtt.enums
import paho.mqtt.reasoncodes
from utils.eventhook import EventHook
import utils.base_types
import counter.api
import logging
import custom_types.api
import extern_types.api
import vector3d.vector

class CounterClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self.on_ready = EventHook()
        self._vector = custom_types.api.Vector3D()
        self.on_vector_changed = EventHook()
        self._extern_vector = vector3d.vector.Vector()
        self.on_extern_vector_changed = EventHook()
        self._vector_array = []
        self.on_vector_array_changed = EventHook()
        self._extern_vector_array = []
        self.on_extern_vector_array_changed = EventHook()
        self.on_value_changed = EventHook()
        self.client.on_subscribed += self.__handle_subscribed
        self.subscription_ids = []
        self.client.on_connected += self.subscribeForTopics
        self.method_topics = self.MethodTopics(self.client.get_client_id())
        self.pending_calls = self.PendingCalls()
        self.loop = asyncio.get_event_loop()

    def subscribeForTopics(self):
        self.subscription_ids.append(self.client.subscribe_for_property("counter/Counter/prop/vector", self.__set_vector))
        self.subscription_ids.append(self.client.subscribe_for_property("counter/Counter/prop/extern_vector", self.__set_extern_vector))
        self.subscription_ids.append(self.client.subscribe_for_property("counter/Counter/prop/vectorArray", self.__set_vector_array))
        self.subscription_ids.append(self.client.subscribe_for_property("counter/Counter/prop/extern_vectorArray", self.__set_extern_vector_array))
        self.subscription_ids.append(self.client.subscribe_for_signal("counter/Counter/sig/valueChanged",  self.__on_value_changed_signal))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_increment, self.__on_increment_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_increment_array, self.__on_increment_array_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_decrement, self.__on_decrement_resp))
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_decrement_array, self.__on_decrement_array_resp))

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.on_subscribed -= self.__handle_subscribed
        self.client.unsubscribe("counter/Counter/prop/vector")
        self.client.unsubscribe("counter/Counter/prop/extern_vector")
        self.client.unsubscribe("counter/Counter/prop/vectorArray")
        self.client.unsubscribe("counter/Counter/prop/extern_vectorArray")
        self.client.unsubscribe("counter/Counter/sig/valueChanged")
        self.client.unsubscribe(self.method_topics.resp_topic_increment)
        self.client.unsubscribe(self.method_topics.resp_topic_increment_array)
        self.client.unsubscribe(self.method_topics.resp_topic_decrement)
        self.client.unsubscribe(self.method_topics.resp_topic_decrement_array)

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

    def set_vector(self, value):
        if self._vector == value:
            return
        topic = "counter/Counter/set/vector"
        self.client.set_remote_property(topic, custom_types.api.from_vector3_d(value))

    def get_vector(self):
        return self._vector

    def set_extern_vector(self, value):
        if self._extern_vector == value:
            return
        topic = "counter/Counter/set/extern_vector"
        self.client.set_remote_property(topic, extern_types.api.from_vector3d_vector_vector(value))

    def get_extern_vector(self):
        return self._extern_vector

    def set_vector_array(self, value):
        if self._vector_array == value:
            return
        topic = "counter/Counter/set/vectorArray"
        self.client.set_remote_property(topic, [custom_types.api.from_vector3_d(_) for _ in value])

    def get_vector_array(self):
        return self._vector_array

    def set_extern_vector_array(self, value):
        if self._extern_vector_array == value:
            return
        topic = "counter/Counter/set/extern_vectorArray"
        self.client.set_remote_property(topic, [extern_types.api.from_vector3d_vector_vector(_) for _ in value])

    def get_extern_vector_array(self):
        return self._extern_vector_array

    async def increment(self, vec: vector3d.vector.Vector):
        _vec = extern_types.api.from_vector3d_vector_vector(vec)
        args = [_vec]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(extern_types.api.as_vector3d_vector_vector(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_increment, self.method_topics.resp_topic_increment, args)
        self.pending_calls.increment[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def increment_array(self, vec: list[vector3d.vector.Vector]):
        _vec = [extern_types.api.from_vector3d_vector_vector(my_vector3_d) for my_vector3_d in vec]
        args = [_vec]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result([extern_types.api.as_vector3d_vector_vector(_) for _ in result])
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_increment_array, self.method_topics.resp_topic_increment_array, args)
        self.pending_calls.increment_array[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def decrement(self, vec: custom_types.api.Vector3D):
        _vec = custom_types.api.from_vector3_d(vec)
        args = [_vec]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(custom_types.api.as_vector3_d(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_decrement, self.method_topics.resp_topic_decrement, args)
        self.pending_calls.decrement[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def decrement_array(self, vec: list[custom_types.api.Vector3D]):
        _vec = [custom_types.api.from_vector3_d(vector3_d) for vector3_d in vec]
        args = [_vec]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result([custom_types.api.as_vector3_d(_) for _ in result])
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_decrement_array, self.method_topics.resp_topic_decrement_array, args)
        self.pending_calls.decrement_array[call_id] = func
        return await asyncio.wait_for(future, 500)

    # internal functions on message handle

    def __set_vector(self, data):
        value =  custom_types.api.as_vector3_d(data)
        if self._vector == value:
            return
        self._vector = value
        self.on_vector_changed.fire(self._vector)

    def __set_extern_vector(self, data):
        value =  extern_types.api.as_vector3d_vector_vector(data)
        if self._extern_vector == value:
            return
        self._extern_vector = value
        self.on_extern_vector_changed.fire(self._extern_vector)

    def __set_vector_array(self, data):
        value = [custom_types.api.as_vector3_d(_) for _ in data]
        if self._vector_array == value:
            return
        self._vector_array = value
        self.on_vector_array_changed.fire(self._vector_array)

    def __set_extern_vector_array(self, data):
        value = [extern_types.api.as_vector3d_vector_vector(_) for _ in data]
        if self._extern_vector_array == value:
            return
        self._extern_vector_array = value
        self.on_extern_vector_array_changed.fire(self._extern_vector_array)

    def __on_value_changed_signal(self, args: list[Any]):
        vector =  custom_types.api.as_vector3_d(args[0])
        extern_vector =  extern_types.api.as_vector3d_vector_vector(args[1])
        vector_array = [custom_types.api.as_vector3_d(_) for _ in args[2]]
        extern_vector_array = [extern_types.api.as_vector3d_vector_vector(_) for _ in args[3]]
        self.on_value_changed.fire(vector, extern_vector, vector_array, extern_vector_array)
        return

    def __on_increment_resp(self, value, callId):
       callback = self.pending_calls.increment.pop(callId)
       if callback != None:
           callback(value)

    def __on_increment_array_resp(self, value, callId):
       callback = self.pending_calls.increment_array.pop(callId)
       if callback != None:
           callback(value)

    def __on_decrement_resp(self, value, callId):
       callback = self.pending_calls.decrement.pop(callId)
       if callback != None:
           callback(value)

    def __on_decrement_array_resp(self, value, callId):
       callback = self.pending_calls.decrement_array.pop(callId)
       if callback != None:
           callback(value)
    class MethodTopics:
        def __init__(self, client_id):
            self.topic_increment= "counter/Counter/rpc/increment"
            self.resp_topic_increment= self.topic_increment + "/" + str(client_id) + "/result"
            self.topic_increment_array= "counter/Counter/rpc/incrementArray"
            self.resp_topic_increment_array= self.topic_increment_array + "/" + str(client_id) + "/result"
            self.topic_decrement= "counter/Counter/rpc/decrement"
            self.resp_topic_decrement= self.topic_decrement + "/" + str(client_id) + "/result"
            self.topic_decrement_array= "counter/Counter/rpc/decrementArray"
            self.resp_topic_decrement_array= self.topic_decrement_array + "/" + str(client_id) + "/result"

    class PendingCalls:
        def __init__(self):
            self.increment = {}
            self.increment_array = {}
            self.decrement = {}
            self.decrement_array = {}
