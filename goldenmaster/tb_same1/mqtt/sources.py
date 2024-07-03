import apigear.mqtt
import utils.base_types
import tb_same1.api
from utils.eventhook import EventHook
from typing import Any
import logging
class SameStruct1InterfaceServiceAdapter():
    def __init__(self, impl: tb_same1.api.ISameStruct1Interface, service: apigear.mqtt.Service):
        self.service = service
        self.impl = impl
        self.impl.on_prop1_changed += self.notify_prop1_changed
        self.impl.on_sig1 += self.notify_sig1
        self.service.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.service.subscribe_for_property("tb.same1/SameStruct1Interface/set/prop1", self.__set_prop1)
        #TODO SUBSCRIBE FOR INVOKE TOPIC

    def __del__(self):
        self.service.on_connected -= self.subscribeForTopics
        self.service.unsubscribe("tb.same1/SameStruct1Interface/set/prop1")
        #TODO UNSUBSCRIBE INVOKE TOPIC

    def notify_sig1(self, param1: tb_same1.api.Struct1):
        _param1 = tb_same1.api.from_struct1(param1)
        args = [_param1]
        self.service.notify_signal("tb.same1/SameStruct1Interface/sig/sig1", args)

    def notify_prop1_changed(self, value):
        v = tb_same1.api.from_struct1(value)
        self.service.notify_property_change("tb.same1/SameStruct1Interface/prop/prop1", v)

    def __set_prop1(self, value: Any):
            v = tb_same1.api.as_struct1(value)
            self.impl.set_prop1(v)
class SameStruct2InterfaceServiceAdapter():
    def __init__(self, impl: tb_same1.api.ISameStruct2Interface, service: apigear.mqtt.Service):
        self.service = service
        self.impl = impl
        self.impl.on_prop1_changed += self.notify_prop1_changed
        self.impl.on_prop2_changed += self.notify_prop2_changed
        self.impl.on_sig1 += self.notify_sig1
        self.impl.on_sig2 += self.notify_sig2
        self.service.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.service.subscribe_for_property("tb.same1/SameStruct2Interface/set/prop1", self.__set_prop1)
        self.service.subscribe_for_property("tb.same1/SameStruct2Interface/set/prop2", self.__set_prop2)
        #TODO SUBSCRIBE FOR INVOKE TOPIC

    def __del__(self):
        self.service.on_connected -= self.subscribeForTopics
        self.service.unsubscribe("tb.same1/SameStruct2Interface/set/prop1")
        self.service.unsubscribe("tb.same1/SameStruct2Interface/set/prop2")
        #TODO UNSUBSCRIBE INVOKE TOPIC

    def notify_sig1(self, param1: tb_same1.api.Struct1):
        _param1 = tb_same1.api.from_struct1(param1)
        args = [_param1]
        self.service.notify_signal("tb.same1/SameStruct2Interface/sig/sig1", args)

    def notify_sig2(self, param1: tb_same1.api.Struct1, param2: tb_same1.api.Struct2):
        _param1 = tb_same1.api.from_struct1(param1)
        _param2 = tb_same1.api.from_struct2(param2)
        args = [_param1, _param2]
        self.service.notify_signal("tb.same1/SameStruct2Interface/sig/sig2", args)

    def notify_prop1_changed(self, value):
        v = tb_same1.api.from_struct2(value)
        self.service.notify_property_change("tb.same1/SameStruct2Interface/prop/prop1", v)

    def notify_prop2_changed(self, value):
        v = tb_same1.api.from_struct2(value)
        self.service.notify_property_change("tb.same1/SameStruct2Interface/prop/prop2", v)

    def __set_prop1(self, value: Any):
            v = tb_same1.api.as_struct2(value)
            self.impl.set_prop1(v)

    def __set_prop2(self, value: Any):
            v = tb_same1.api.as_struct2(value)
            self.impl.set_prop2(v)
class SameEnum1InterfaceServiceAdapter():
    def __init__(self, impl: tb_same1.api.ISameEnum1Interface, service: apigear.mqtt.Service):
        self.service = service
        self.impl = impl
        self.impl.on_prop1_changed += self.notify_prop1_changed
        self.impl.on_sig1 += self.notify_sig1
        self.service.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.service.subscribe_for_property("tb.same1/SameEnum1Interface/set/prop1", self.__set_prop1)
        #TODO SUBSCRIBE FOR INVOKE TOPIC

    def __del__(self):
        self.service.on_connected -= self.subscribeForTopics
        self.service.unsubscribe("tb.same1/SameEnum1Interface/set/prop1")
        #TODO UNSUBSCRIBE INVOKE TOPIC

    def notify_sig1(self, param1: tb_same1.api.Enum1):
        _param1 = tb_same1.api.from_enum1(param1)
        args = [_param1]
        self.service.notify_signal("tb.same1/SameEnum1Interface/sig/sig1", args)

    def notify_prop1_changed(self, value):
        v = tb_same1.api.from_enum1(value)
        self.service.notify_property_change("tb.same1/SameEnum1Interface/prop/prop1", v)

    def __set_prop1(self, value: Any):
            v = tb_same1.api.as_enum1(value)
            self.impl.set_prop1(v)
class SameEnum2InterfaceServiceAdapter():
    def __init__(self, impl: tb_same1.api.ISameEnum2Interface, service: apigear.mqtt.Service):
        self.service = service
        self.impl = impl
        self.impl.on_prop1_changed += self.notify_prop1_changed
        self.impl.on_prop2_changed += self.notify_prop2_changed
        self.impl.on_sig1 += self.notify_sig1
        self.impl.on_sig2 += self.notify_sig2
        self.service.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.service.subscribe_for_property("tb.same1/SameEnum2Interface/set/prop1", self.__set_prop1)
        self.service.subscribe_for_property("tb.same1/SameEnum2Interface/set/prop2", self.__set_prop2)
        #TODO SUBSCRIBE FOR INVOKE TOPIC

    def __del__(self):
        self.service.on_connected -= self.subscribeForTopics
        self.service.unsubscribe("tb.same1/SameEnum2Interface/set/prop1")
        self.service.unsubscribe("tb.same1/SameEnum2Interface/set/prop2")
        #TODO UNSUBSCRIBE INVOKE TOPIC

    def notify_sig1(self, param1: tb_same1.api.Enum1):
        _param1 = tb_same1.api.from_enum1(param1)
        args = [_param1]
        self.service.notify_signal("tb.same1/SameEnum2Interface/sig/sig1", args)

    def notify_sig2(self, param1: tb_same1.api.Enum1, param2: tb_same1.api.Enum2):
        _param1 = tb_same1.api.from_enum1(param1)
        _param2 = tb_same1.api.from_enum2(param2)
        args = [_param1, _param2]
        self.service.notify_signal("tb.same1/SameEnum2Interface/sig/sig2", args)

    def notify_prop1_changed(self, value):
        v = tb_same1.api.from_enum1(value)
        self.service.notify_property_change("tb.same1/SameEnum2Interface/prop/prop1", v)

    def notify_prop2_changed(self, value):
        v = tb_same1.api.from_enum2(value)
        self.service.notify_property_change("tb.same1/SameEnum2Interface/prop/prop2", v)

    def __set_prop1(self, value: Any):
            v = tb_same1.api.as_enum1(value)
            self.impl.set_prop1(v)

    def __set_prop2(self, value: Any):
            v = tb_same1.api.as_enum2(value)
            self.impl.set_prop2(v)
