import asyncio
from typing import Any
import apigear.mqtt
from utils.eventhook import EventHook
import utils.base_types
import testbed2.api
import logging

class ManyParamInterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
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
        self.client.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.client.subscribe_for_property("testbed2/ManyParamInterface/prop/prop1", self.__set_prop1)
        self.client.subscribe_for_property("testbed2/ManyParamInterface/prop/prop2", self.__set_prop2)
        self.client.subscribe_for_property("testbed2/ManyParamInterface/prop/prop3", self.__set_prop3)
        self.client.subscribe_for_property("testbed2/ManyParamInterface/prop/prop4", self.__set_prop4)
        self.client.subscribe_for_signal("testbed2/ManyParamInterface/sig/sig1",  self.__on_sig1_signal)
        self.client.subscribe_for_signal("testbed2/ManyParamInterface/sig/sig2",  self.__on_sig2_signal)
        self.client.subscribe_for_signal("testbed2/ManyParamInterface/sig/sig3",  self.__on_sig3_signal)
        self.client.subscribe_for_signal("testbed2/ManyParamInterface/sig/sig4",  self.__on_sig4_signal)
        #TODO SUBSCRIBE FOR INVOKE RESP TOPIC

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.unsubscribe("testbed2/ManyParamInterface/prop/prop1")
        self.client.unsubscribe("testbed2/ManyParamInterface/prop/prop2")
        self.client.unsubscribe("testbed2/ManyParamInterface/prop/prop3")
        self.client.unsubscribe("testbed2/ManyParamInterface/prop/prop4")
        self.client.unsubscribe("testbed2/ManyParamInterface/sig/sig1")
        self.client.unsubscribe("testbed2/ManyParamInterface/sig/sig2")
        self.client.unsubscribe("testbed2/ManyParamInterface/sig/sig3")
        self.client.unsubscribe("testbed2/ManyParamInterface/sig/sig4")
        #TODO UNSUBSCRIBE INVOKE RESP TOPIC

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

class NestedStruct1InterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self._prop1 = testbed2.api.NestedStruct1()
        self.on_prop1_changed = EventHook()
        self.on_sig1 = EventHook()
        self.client.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.client.subscribe_for_property("testbed2/NestedStruct1Interface/prop/prop1", self.__set_prop1)
        self.client.subscribe_for_signal("testbed2/NestedStruct1Interface/sig/sig1",  self.__on_sig1_signal)
        #TODO SUBSCRIBE FOR INVOKE RESP TOPIC

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.unsubscribe("testbed2/NestedStruct1Interface/prop/prop1")
        self.client.unsubscribe("testbed2/NestedStruct1Interface/sig/sig1")
        #TODO UNSUBSCRIBE INVOKE RESP TOPIC

    def set_prop1(self, value):
        if self._prop1 == value:
            return
        topic = "testbed2/NestedStruct1Interface/set/prop1"
        self.client.set_remote_property(topic, testbed2.api.from_nested_struct1(value))

    def get_prop1(self):
        return self._prop1

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

class NestedStruct2InterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self._prop1 = testbed2.api.NestedStruct1()
        self.on_prop1_changed = EventHook()
        self._prop2 = testbed2.api.NestedStruct2()
        self.on_prop2_changed = EventHook()
        self.on_sig1 = EventHook()
        self.on_sig2 = EventHook()
        self.client.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.client.subscribe_for_property("testbed2/NestedStruct2Interface/prop/prop1", self.__set_prop1)
        self.client.subscribe_for_property("testbed2/NestedStruct2Interface/prop/prop2", self.__set_prop2)
        self.client.subscribe_for_signal("testbed2/NestedStruct2Interface/sig/sig1",  self.__on_sig1_signal)
        self.client.subscribe_for_signal("testbed2/NestedStruct2Interface/sig/sig2",  self.__on_sig2_signal)
        #TODO SUBSCRIBE FOR INVOKE RESP TOPIC

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.unsubscribe("testbed2/NestedStruct2Interface/prop/prop1")
        self.client.unsubscribe("testbed2/NestedStruct2Interface/prop/prop2")
        self.client.unsubscribe("testbed2/NestedStruct2Interface/sig/sig1")
        self.client.unsubscribe("testbed2/NestedStruct2Interface/sig/sig2")
        #TODO UNSUBSCRIBE INVOKE RESP TOPIC

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

class NestedStruct3InterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self._prop1 = testbed2.api.NestedStruct1()
        self.on_prop1_changed = EventHook()
        self._prop2 = testbed2.api.NestedStruct2()
        self.on_prop2_changed = EventHook()
        self._prop3 = testbed2.api.NestedStruct3()
        self.on_prop3_changed = EventHook()
        self.on_sig1 = EventHook()
        self.on_sig2 = EventHook()
        self.on_sig3 = EventHook()
        self.client.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.client.subscribe_for_property("testbed2/NestedStruct3Interface/prop/prop1", self.__set_prop1)
        self.client.subscribe_for_property("testbed2/NestedStruct3Interface/prop/prop2", self.__set_prop2)
        self.client.subscribe_for_property("testbed2/NestedStruct3Interface/prop/prop3", self.__set_prop3)
        self.client.subscribe_for_signal("testbed2/NestedStruct3Interface/sig/sig1",  self.__on_sig1_signal)
        self.client.subscribe_for_signal("testbed2/NestedStruct3Interface/sig/sig2",  self.__on_sig2_signal)
        self.client.subscribe_for_signal("testbed2/NestedStruct3Interface/sig/sig3",  self.__on_sig3_signal)
        #TODO SUBSCRIBE FOR INVOKE RESP TOPIC

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.unsubscribe("testbed2/NestedStruct3Interface/prop/prop1")
        self.client.unsubscribe("testbed2/NestedStruct3Interface/prop/prop2")
        self.client.unsubscribe("testbed2/NestedStruct3Interface/prop/prop3")
        self.client.unsubscribe("testbed2/NestedStruct3Interface/sig/sig1")
        self.client.unsubscribe("testbed2/NestedStruct3Interface/sig/sig2")
        self.client.unsubscribe("testbed2/NestedStruct3Interface/sig/sig3")
        #TODO UNSUBSCRIBE INVOKE RESP TOPIC

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
