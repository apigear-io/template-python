import asyncio
from typing import Any
import apigear.mqtt
from utils.eventhook import EventHook
import utils.base_types
import tb_names.api
import logging

class NamEsClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self._switch = False
        self.on_switch_changed = EventHook()
        self._some_property = 0
        self.on_some_property_changed = EventHook()
        self._some_poperty2 = 0
        self.on_some_poperty2_changed = EventHook()
        self.on_some_signal = EventHook()
        self.on_some_signal2 = EventHook()
        self.client.on_connected += self.subscribeForTopics
        self.method_topics = self.MethodTopics(self.client.get_client_id())
        self.pending_calls = self.PendingCalls()
        self.loop = asyncio.get_event_loop()

    def subscribeForTopics(self):
        self.client.subscribe_for_property("tb.names/Nam_Es/prop/Switch", self.__set_switch)
        self.client.subscribe_for_property("tb.names/Nam_Es/prop/SOME_PROPERTY", self.__set_some_property)
        self.client.subscribe_for_property("tb.names/Nam_Es/prop/Some_Poperty2", self.__set_some_poperty2)
        self.client.subscribe_for_signal("tb.names/Nam_Es/sig/SOME_SIGNAL",  self.__on_some_signal_signal)
        self.client.subscribe_for_signal("tb.names/Nam_Es/sig/Some_Signal2",  self.__on_some_signal2_signal)
        self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_some_function, self.__on_some_function_resp)
        self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_some_function2, self.__on_some_function2_resp)

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.unsubscribe("tb.names/Nam_Es/prop/Switch")
        self.client.unsubscribe("tb.names/Nam_Es/prop/SOME_PROPERTY")
        self.client.unsubscribe("tb.names/Nam_Es/prop/Some_Poperty2")
        self.client.unsubscribe("tb.names/Nam_Es/sig/SOME_SIGNAL")
        self.client.unsubscribe("tb.names/Nam_Es/sig/Some_Signal2")
        self.client.unsubscribe(self.method_topics.resp_topic_some_function)
        self.client.unsubscribe(self.method_topics.resp_topic_some_function2)

    def set_switch(self, value):
        if self._switch == value:
            return
        topic = "tb.names/Nam_Es/set/Switch"
        self.client.set_remote_property(topic, utils.base_types.from_bool(value))

    def get_switch(self):
        return self._switch

    def set_some_property(self, value):
        if self._some_property == value:
            return
        topic = "tb.names/Nam_Es/set/SOME_PROPERTY"
        self.client.set_remote_property(topic, utils.base_types.from_int(value))

    def get_some_property(self):
        return self._some_property

    def set_some_poperty2(self, value):
        if self._some_poperty2 == value:
            return
        topic = "tb.names/Nam_Es/set/Some_Poperty2"
        self.client.set_remote_property(topic, utils.base_types.from_int(value))

    def get_some_poperty2(self):
        return self._some_poperty2

    async def some_function(self, some_param: bool):
        _some_param = utils.base_types.from_bool(some_param)
        args = [_some_param]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(None)
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_some_function, self.method_topics.resp_topic_some_function, args)
        self.pending_calls.some_function[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def some_function2(self, some_param: bool):
        _some_param = utils.base_types.from_bool(some_param)
        args = [_some_param]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(None)
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_some_function2, self.method_topics.resp_topic_some_function2, args)
        self.pending_calls.some_function2[call_id] = func
        return await asyncio.wait_for(future, 500)

    # internal functions on message handle

    def __set_switch(self, data):
        value =  utils.base_types.as_bool(data)
        if self._switch == value:
            return
        self._switch = value
        self.on_switch_changed.fire(self._switch)

    def __set_some_property(self, data):
        value =  utils.base_types.as_int(data)
        if self._some_property == value:
            return
        self._some_property = value
        self.on_some_property_changed.fire(self._some_property)

    def __set_some_poperty2(self, data):
        value =  utils.base_types.as_int(data)
        if self._some_poperty2 == value:
            return
        self._some_poperty2 = value
        self.on_some_poperty2_changed.fire(self._some_poperty2)

    def __on_some_signal_signal(self, args: list[Any]):
        some_param =  utils.base_types.as_bool(args[0])
        self.on_some_signal.fire(some_param)
        return

    def __on_some_signal2_signal(self, args: list[Any]):
        some_param =  utils.base_types.as_bool(args[0])
        self.on_some_signal2.fire(some_param)
        return

    def __on_some_function_resp(self, value, callId):
       callback = self.pending_calls.some_function.pop(callId)
       if callback != None:
           callback(value)

    def __on_some_function2_resp(self, value, callId):
       callback = self.pending_calls.some_function2.pop(callId)
       if callback != None:
           callback(value)
    class MethodTopics:
        def __init__(self, client_id):
            self.topic_some_function= "tb.names/Nam_Es/rpc/SOME_FUNCTION"
            self.resp_topic_some_function= self.topic_some_function + "/" + str(client_id) + "/result"
            self.topic_some_function2= "tb.names/Nam_Es/rpc/Some_Function2"
            self.resp_topic_some_function2= self.topic_some_function2 + "/" + str(client_id) + "/result"

    class PendingCalls:
        def __init__(self):
            self.some_function = {}
            self.some_function2 = {}
