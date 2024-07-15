import asyncio
from typing import Any
import apigear.mqtt
from utils.eventhook import EventHook
import utils.base_types
import testbed1.api
import logging

class StructInterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
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
        self.client.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.client.subscribe_for_property("testbed1/StructInterface/prop/propBool", self.__set_prop_bool)
        self.client.subscribe_for_property("testbed1/StructInterface/prop/propInt", self.__set_prop_int)
        self.client.subscribe_for_property("testbed1/StructInterface/prop/propFloat", self.__set_prop_float)
        self.client.subscribe_for_property("testbed1/StructInterface/prop/propString", self.__set_prop_string)
        self.client.subscribe_for_signal("testbed1/StructInterface/sig/sigBool",  self.__on_sig_bool_signal)
        self.client.subscribe_for_signal("testbed1/StructInterface/sig/sigInt",  self.__on_sig_int_signal)
        self.client.subscribe_for_signal("testbed1/StructInterface/sig/sigFloat",  self.__on_sig_float_signal)
        self.client.subscribe_for_signal("testbed1/StructInterface/sig/sigString",  self.__on_sig_string_signal)
        #TODO SUBSCRIBE FOR INVOKE RESP TOPIC

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.unsubscribe("testbed1/StructInterface/prop/propBool")
        self.client.unsubscribe("testbed1/StructInterface/prop/propInt")
        self.client.unsubscribe("testbed1/StructInterface/prop/propFloat")
        self.client.unsubscribe("testbed1/StructInterface/prop/propString")
        self.client.unsubscribe("testbed1/StructInterface/sig/sigBool")
        self.client.unsubscribe("testbed1/StructInterface/sig/sigInt")
        self.client.unsubscribe("testbed1/StructInterface/sig/sigFloat")
        self.client.unsubscribe("testbed1/StructInterface/sig/sigString")
        #TODO UNSUBSCRIBE INVOKE RESP TOPIC

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

class StructArrayInterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
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
        self.client.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.client.subscribe_for_property("testbed1/StructArrayInterface/prop/propBool", self.__set_prop_bool)
        self.client.subscribe_for_property("testbed1/StructArrayInterface/prop/propInt", self.__set_prop_int)
        self.client.subscribe_for_property("testbed1/StructArrayInterface/prop/propFloat", self.__set_prop_float)
        self.client.subscribe_for_property("testbed1/StructArrayInterface/prop/propString", self.__set_prop_string)
        self.client.subscribe_for_signal("testbed1/StructArrayInterface/sig/sigBool",  self.__on_sig_bool_signal)
        self.client.subscribe_for_signal("testbed1/StructArrayInterface/sig/sigInt",  self.__on_sig_int_signal)
        self.client.subscribe_for_signal("testbed1/StructArrayInterface/sig/sigFloat",  self.__on_sig_float_signal)
        self.client.subscribe_for_signal("testbed1/StructArrayInterface/sig/sigString",  self.__on_sig_string_signal)
        #TODO SUBSCRIBE FOR INVOKE RESP TOPIC

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.unsubscribe("testbed1/StructArrayInterface/prop/propBool")
        self.client.unsubscribe("testbed1/StructArrayInterface/prop/propInt")
        self.client.unsubscribe("testbed1/StructArrayInterface/prop/propFloat")
        self.client.unsubscribe("testbed1/StructArrayInterface/prop/propString")
        self.client.unsubscribe("testbed1/StructArrayInterface/sig/sigBool")
        self.client.unsubscribe("testbed1/StructArrayInterface/sig/sigInt")
        self.client.unsubscribe("testbed1/StructArrayInterface/sig/sigFloat")
        self.client.unsubscribe("testbed1/StructArrayInterface/sig/sigString")
        #TODO UNSUBSCRIBE INVOKE RESP TOPIC

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
