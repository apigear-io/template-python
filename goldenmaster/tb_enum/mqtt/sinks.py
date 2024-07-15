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

    def subscribeForTopics(self):
        self.client.subscribe_for_property("tb.enum/EnumInterface/prop/prop0", self.__set_prop0)
        self.client.subscribe_for_property("tb.enum/EnumInterface/prop/prop1", self.__set_prop1)
        self.client.subscribe_for_property("tb.enum/EnumInterface/prop/prop2", self.__set_prop2)
        self.client.subscribe_for_property("tb.enum/EnumInterface/prop/prop3", self.__set_prop3)
        self.client.subscribe_for_signal("tb.enum/EnumInterface/sig/sig0",  self.__on_sig0_signal)
        self.client.subscribe_for_signal("tb.enum/EnumInterface/sig/sig1",  self.__on_sig1_signal)
        self.client.subscribe_for_signal("tb.enum/EnumInterface/sig/sig2",  self.__on_sig2_signal)
        self.client.subscribe_for_signal("tb.enum/EnumInterface/sig/sig3",  self.__on_sig3_signal)
        #TODO SUBSCRIBE FOR INVOKE RESP TOPIC

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
        #TODO UNSUBSCRIBE INVOKE RESP TOPIC

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
