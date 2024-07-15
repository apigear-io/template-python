import asyncio
from typing import Any
import apigear.mqtt
from utils.eventhook import EventHook
import utils.base_types
import tb_same1.api
import logging

class SameStruct1InterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self._prop1 = tb_same1.api.Struct1()
        self.on_prop1_changed = EventHook()
        self.on_sig1 = EventHook()
        self.client.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.client.subscribe_for_property("tb.same1/SameStruct1Interface/prop/prop1", self.__set_prop1)
        self.client.subscribe_for_signal("tb.same1/SameStruct1Interface/sig/sig1",  self.__on_sig1_signal)
        #TODO SUBSCRIBE FOR INVOKE RESP TOPIC

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.unsubscribe("tb.same1/SameStruct1Interface/prop/prop1")
        self.client.unsubscribe("tb.same1/SameStruct1Interface/sig/sig1")
        #TODO UNSUBSCRIBE INVOKE RESP TOPIC

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        topic = "tb.same1/SameStruct1Interface/set/prop1"
        self.client.set_remote_property(topic, tb_same1.api.from_struct1(value))

    def get_prop1(self):
        return self._prop1

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

class SameStruct2InterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self._prop1 = tb_same1.api.Struct2()
        self.on_prop1_changed = EventHook()
        self._prop2 = tb_same1.api.Struct2()
        self.on_prop2_changed = EventHook()
        self.on_sig1 = EventHook()
        self.on_sig2 = EventHook()
        self.client.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.client.subscribe_for_property("tb.same1/SameStruct2Interface/prop/prop1", self.__set_prop1)
        self.client.subscribe_for_property("tb.same1/SameStruct2Interface/prop/prop2", self.__set_prop2)
        self.client.subscribe_for_signal("tb.same1/SameStruct2Interface/sig/sig1",  self.__on_sig1_signal)
        self.client.subscribe_for_signal("tb.same1/SameStruct2Interface/sig/sig2",  self.__on_sig2_signal)
        #TODO SUBSCRIBE FOR INVOKE RESP TOPIC

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.unsubscribe("tb.same1/SameStruct2Interface/prop/prop1")
        self.client.unsubscribe("tb.same1/SameStruct2Interface/prop/prop2")
        self.client.unsubscribe("tb.same1/SameStruct2Interface/sig/sig1")
        self.client.unsubscribe("tb.same1/SameStruct2Interface/sig/sig2")
        #TODO UNSUBSCRIBE INVOKE RESP TOPIC

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

class SameEnum1InterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self._prop1 = tb_same1.api.Enum1.VALUE1
        self.on_prop1_changed = EventHook()
        self.on_sig1 = EventHook()
        self.client.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.client.subscribe_for_property("tb.same1/SameEnum1Interface/prop/prop1", self.__set_prop1)
        self.client.subscribe_for_signal("tb.same1/SameEnum1Interface/sig/sig1",  self.__on_sig1_signal)
        #TODO SUBSCRIBE FOR INVOKE RESP TOPIC

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.unsubscribe("tb.same1/SameEnum1Interface/prop/prop1")
        self.client.unsubscribe("tb.same1/SameEnum1Interface/sig/sig1")
        #TODO UNSUBSCRIBE INVOKE RESP TOPIC

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        topic = "tb.same1/SameEnum1Interface/set/prop1"
        self.client.set_remote_property(topic, tb_same1.api.from_enum1(value))

    def get_prop1(self):
        return self._prop1

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

class SameEnum2InterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self._prop1 = tb_same1.api.Enum1.VALUE1
        self.on_prop1_changed = EventHook()
        self._prop2 = tb_same1.api.Enum2.VALUE1
        self.on_prop2_changed = EventHook()
        self.on_sig1 = EventHook()
        self.on_sig2 = EventHook()
        self.client.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.client.subscribe_for_property("tb.same1/SameEnum2Interface/prop/prop1", self.__set_prop1)
        self.client.subscribe_for_property("tb.same1/SameEnum2Interface/prop/prop2", self.__set_prop2)
        self.client.subscribe_for_signal("tb.same1/SameEnum2Interface/sig/sig1",  self.__on_sig1_signal)
        self.client.subscribe_for_signal("tb.same1/SameEnum2Interface/sig/sig2",  self.__on_sig2_signal)
        #TODO SUBSCRIBE FOR INVOKE RESP TOPIC

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.unsubscribe("tb.same1/SameEnum2Interface/prop/prop1")
        self.client.unsubscribe("tb.same1/SameEnum2Interface/prop/prop2")
        self.client.unsubscribe("tb.same1/SameEnum2Interface/sig/sig1")
        self.client.unsubscribe("tb.same1/SameEnum2Interface/sig/sig2")
        #TODO UNSUBSCRIBE INVOKE RESP TOPIC

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
