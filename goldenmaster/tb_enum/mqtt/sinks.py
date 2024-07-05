import asyncio
from typing import Any
import apigear.mqtt
from utils.eventhook import EventHook
import utils.base_types
import tb_enum.api
import logging

class EnumInterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self._prop0 = tb_enum.api.Enum0.VALUE0
        self.on_prop0_changed = EventHook()
        self._prop1 = tb_enum.api.Enum1.VALUE1
        self.on_prop1_changed = EventHook()
        self._prop2 = tb_enum.api.Enum2.VALUE2
        self.on_prop2_changed = EventHook()
        self._prop3 = tb_enum.api.Enum3.VALUE3
        self.on_prop3_changed = EventHook()
        self.on_sig0 = EventHook()
        self.on_sig1 = EventHook()
        self.on_sig2 = EventHook()
        self.on_sig3 = EventHook()
        self.client.on_connected += self.subscribeForTopics
        self.method_topics = self.MethodTopics(self.client.get_client_id())
        self.pending_calls = self.PendingCalls()
        self.loop = asyncio.get_event_loop()

    def subscribeForTopics(self):
        self.client.subscribe_for_property("tb.enum/EnumInterface/prop/prop0", self.__set_prop0)
        self.client.subscribe_for_property("tb.enum/EnumInterface/prop/prop1", self.__set_prop1)
        self.client.subscribe_for_property("tb.enum/EnumInterface/prop/prop2", self.__set_prop2)
        self.client.subscribe_for_property("tb.enum/EnumInterface/prop/prop3", self.__set_prop3)
        self.client.subscribe_for_signal("tb.enum/EnumInterface/sig/sig0",  self.__on_sig0_signal)
        self.client.subscribe_for_signal("tb.enum/EnumInterface/sig/sig1",  self.__on_sig1_signal)
        self.client.subscribe_for_signal("tb.enum/EnumInterface/sig/sig2",  self.__on_sig2_signal)
        self.client.subscribe_for_signal("tb.enum/EnumInterface/sig/sig3",  self.__on_sig3_signal)
        self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func0, self.__on_func0_resp)
        self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func1, self.__on_func1_resp)
        self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func2, self.__on_func2_resp)
        self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_func3, self.__on_func3_resp)

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.unsubscribe("tb.enum/EnumInterface/prop/prop0")
        self.client.unsubscribe("tb.enum/EnumInterface/prop/prop1")
        self.client.unsubscribe("tb.enum/EnumInterface/prop/prop2")
        self.client.unsubscribe("tb.enum/EnumInterface/prop/prop3")
        self.client.unsubscribe("tb.enum/EnumInterface/sig/sig0")
        self.client.unsubscribe("tb.enum/EnumInterface/sig/sig1")
        self.client.unsubscribe("tb.enum/EnumInterface/sig/sig2")
        self.client.unsubscribe("tb.enum/EnumInterface/sig/sig3")
        self.client.unsubscribe(self.method_topics.resp_topic_func0)
        self.client.unsubscribe(self.method_topics.resp_topic_func1)
        self.client.unsubscribe(self.method_topics.resp_topic_func2)
        self.client.unsubscribe(self.method_topics.resp_topic_func3)

    def set_prop0(self, value):
        if self._prop0 == value:
            return
        topic = "tb.enum/EnumInterface/set/prop0"
        self.client.set_remote_property(topic, tb_enum.api.from_enum0(value))

    def get_prop0(self):
        return self._prop0

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        topic = "tb.enum/EnumInterface/set/prop1"
        self.client.set_remote_property(topic, tb_enum.api.from_enum1(value))

    def get_prop1(self):
        return self._prop1

    def set_prop2(self, value):
        if self._prop2 == value:
            return
        topic = "tb.enum/EnumInterface/set/prop2"
        self.client.set_remote_property(topic, tb_enum.api.from_enum2(value))

    def get_prop2(self):
        return self._prop2

    def set_prop3(self, value):
        if self._prop3 == value:
            return
        topic = "tb.enum/EnumInterface/set/prop3"
        self.client.set_remote_property(topic, tb_enum.api.from_enum3(value))

    def get_prop3(self):
        return self._prop3

    async def func0(self, param0: tb_enum.api.Enum0):
        _param0 = tb_enum.api.from_enum0(param0)
        args = [_param0]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(tb_enum.api.as_enum0(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func0, self.method_topics.resp_topic_func0, args)
        self.pending_calls.func0[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func1(self, param1: tb_enum.api.Enum1):
        _param1 = tb_enum.api.from_enum1(param1)
        args = [_param1]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(tb_enum.api.as_enum1(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func1, self.method_topics.resp_topic_func1, args)
        self.pending_calls.func1[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func2(self, param2: tb_enum.api.Enum2):
        _param2 = tb_enum.api.from_enum2(param2)
        args = [_param2]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(tb_enum.api.as_enum2(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func2, self.method_topics.resp_topic_func2, args)
        self.pending_calls.func2[call_id] = func
        return await asyncio.wait_for(future, 500)

    async def func3(self, param3: tb_enum.api.Enum3):
        _param3 = tb_enum.api.from_enum3(param3)
        args = [_param3]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
                future.set_result(tb_enum.api.as_enum3(result))
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_func3, self.method_topics.resp_topic_func3, args)
        self.pending_calls.func3[call_id] = func
        return await asyncio.wait_for(future, 500)

    # internal functions on message handle

    def __set_prop0(self, data):
        value =  tb_enum.api.as_enum0(data)
        if self._prop0 == value:
            return
        self._prop0 = value
        self.on_prop0_changed.fire(self._prop0)

    def __set_prop1(self, data):
        value =  tb_enum.api.as_enum1(data)
        if self._prop1 == value:
            return
        self._prop1 = value
        self.on_prop1_changed.fire(self._prop1)

    def __set_prop2(self, data):
        value =  tb_enum.api.as_enum2(data)
        if self._prop2 == value:
            return
        self._prop2 = value
        self.on_prop2_changed.fire(self._prop2)

    def __set_prop3(self, data):
        value =  tb_enum.api.as_enum3(data)
        if self._prop3 == value:
            return
        self._prop3 = value
        self.on_prop3_changed.fire(self._prop3)

    def __on_sig0_signal(self, args: list[Any]):
        param0 =  tb_enum.api.as_enum0(args[0])
        self.on_sig0.fire(param0)
        return

    def __on_sig1_signal(self, args: list[Any]):
        param1 =  tb_enum.api.as_enum1(args[0])
        self.on_sig1.fire(param1)
        return

    def __on_sig2_signal(self, args: list[Any]):
        param2 =  tb_enum.api.as_enum2(args[0])
        self.on_sig2.fire(param2)
        return

    def __on_sig3_signal(self, args: list[Any]):
        param3 =  tb_enum.api.as_enum3(args[0])
        self.on_sig3.fire(param3)
        return

    def __on_func0_resp(self, value, callId):
       callback = self.pending_calls.func0.pop(callId)
       if callback != None:
           callback(value)

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
            self.topic_func0= "tb.enum/EnumInterface/rpc/func0"
            self.resp_topic_func0= self.topic_func0 + "/" + str(client_id) + "/result"
            self.topic_func1= "tb.enum/EnumInterface/rpc/func1"
            self.resp_topic_func1= self.topic_func1 + "/" + str(client_id) + "/result"
            self.topic_func2= "tb.enum/EnumInterface/rpc/func2"
            self.resp_topic_func2= self.topic_func2 + "/" + str(client_id) + "/result"
            self.topic_func3= "tb.enum/EnumInterface/rpc/func3"
            self.resp_topic_func3= self.topic_func3 + "/" + str(client_id) + "/result"

    class PendingCalls:
        def __init__(self):
            self.func0 = {}
            self.func1 = {}
            self.func2 = {}
            self.func3 = {}
