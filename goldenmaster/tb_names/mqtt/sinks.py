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

    def subscribeForTopics(self):
        self.client.subscribe_for_property("tb.names/Nam_Es/prop/Switch", self.__set_switch)
        self.client.subscribe_for_property("tb.names/Nam_Es/prop/SOME_PROPERTY", self.__set_some_property)
        self.client.subscribe_for_property("tb.names/Nam_Es/prop/Some_Poperty2", self.__set_some_poperty2)
        self.client.subscribe_for_signal("tb.names/Nam_Es/sig/SOME_SIGNAL",  self.__on_some_signal_signal)
        self.client.subscribe_for_signal("tb.names/Nam_Es/sig/Some_Signal2",  self.__on_some_signal2_signal)
        #TODO SUBSCRIBE FOR INVOKE RESP TOPIC

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.unsubscribe("tb.names/Nam_Es/prop/Switch")
        self.client.unsubscribe("tb.names/Nam_Es/prop/SOME_PROPERTY")
        self.client.unsubscribe("tb.names/Nam_Es/prop/Some_Poperty2")
        self.client.unsubscribe("tb.names/Nam_Es/sig/SOME_SIGNAL")
        self.client.unsubscribe("tb.names/Nam_Es/sig/Some_Signal2")
        #TODO UNSUBSCRIBE INVOKE RESP TOPIC

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
