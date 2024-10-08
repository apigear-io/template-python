import apigear.mqtt
import utils.base_types
import paho.mqtt.enums
import paho.mqtt.reasoncodes
import tb_same1.api
from utils.eventhook import EventHook
from typing import Any
import logging
class SameStruct1InterfaceServiceAdapter():
    def __init__(self, impl: tb_same1.api.ISameStruct1Interface, service: apigear.mqtt.Service):
        self.service = service
        self.impl = impl
        self.on_ready = EventHook()
        self.impl.on_prop1_changed += self.notify_prop1_changed
        self.impl.on_sig1 += self.notify_sig1
        self.service.on_connected += self.subscribeForTopics
        self.service.on_subscribed += self.__handle_subscribed
        self.subscription_ids = []

    def subscribeForTopics(self):
        self.subscription_ids.append(self.service.subscribe_for_property("tb.same1/SameStruct1Interface/set/prop1", self.__set_prop1))
        self.subscription_ids.append(self.service.subscribe_for_invoke_req("tb.same1/SameStruct1Interface/rpc/func1", self.__invoke_func1))

    def __del__(self):
        self.service.on_connected -= self.subscribeForTopics
        self.service.on_subscribed -= self.__handle_subscribed
        self.service.unsubscribe("tb.same1/SameStruct1Interface/set/prop1")
        self.service.unsubscribe("tb.same1/SameStruct1Interface/rpc/func1")
        self.impl.on_prop1_changed -= self.notify_prop1_changed
        self.impl.on_sig1 -= self.notify_sig1

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

    def __invoke_func1(self, args: list[Any]) -> Any:
        param1 = tb_same1.api.as_struct1(args[0])
        reply = self.impl.func1(param1)
        return tb_same1.api.from_struct1(reply)
class SameStruct2InterfaceServiceAdapter():
    def __init__(self, impl: tb_same1.api.ISameStruct2Interface, service: apigear.mqtt.Service):
        self.service = service
        self.impl = impl
        self.on_ready = EventHook()
        self.impl.on_prop1_changed += self.notify_prop1_changed
        self.impl.on_prop2_changed += self.notify_prop2_changed
        self.impl.on_sig1 += self.notify_sig1
        self.impl.on_sig2 += self.notify_sig2
        self.service.on_connected += self.subscribeForTopics
        self.service.on_subscribed += self.__handle_subscribed
        self.subscription_ids = []

    def subscribeForTopics(self):
        self.subscription_ids.append(self.service.subscribe_for_property("tb.same1/SameStruct2Interface/set/prop1", self.__set_prop1))
        self.subscription_ids.append(self.service.subscribe_for_property("tb.same1/SameStruct2Interface/set/prop2", self.__set_prop2))
        self.subscription_ids.append(self.service.subscribe_for_invoke_req("tb.same1/SameStruct2Interface/rpc/func1", self.__invoke_func1))
        self.subscription_ids.append(self.service.subscribe_for_invoke_req("tb.same1/SameStruct2Interface/rpc/func2", self.__invoke_func2))

    def __del__(self):
        self.service.on_connected -= self.subscribeForTopics
        self.service.on_subscribed -= self.__handle_subscribed
        self.service.unsubscribe("tb.same1/SameStruct2Interface/set/prop1")
        self.service.unsubscribe("tb.same1/SameStruct2Interface/set/prop2")
        self.service.unsubscribe("tb.same1/SameStruct2Interface/rpc/func1")
        self.service.unsubscribe("tb.same1/SameStruct2Interface/rpc/func2")
        self.impl.on_prop1_changed -= self.notify_prop1_changed
        self.impl.on_prop2_changed -= self.notify_prop2_changed
        self.impl.on_sig1 -= self.notify_sig1
        self.impl.on_sig2 -= self.notify_sig2

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

    def __invoke_func1(self, args: list[Any]) -> Any:
        param1 = tb_same1.api.as_struct1(args[0])
        reply = self.impl.func1(param1)
        return tb_same1.api.from_struct1(reply)

    def __invoke_func2(self, args: list[Any]) -> Any:
        param1 = tb_same1.api.as_struct1(args[0])
        param2 = tb_same1.api.as_struct2(args[1])
        reply = self.impl.func2(param1, param2)
        return tb_same1.api.from_struct1(reply)
class SameEnum1InterfaceServiceAdapter():
    def __init__(self, impl: tb_same1.api.ISameEnum1Interface, service: apigear.mqtt.Service):
        self.service = service
        self.impl = impl
        self.on_ready = EventHook()
        self.impl.on_prop1_changed += self.notify_prop1_changed
        self.impl.on_sig1 += self.notify_sig1
        self.service.on_connected += self.subscribeForTopics
        self.service.on_subscribed += self.__handle_subscribed
        self.subscription_ids = []

    def subscribeForTopics(self):
        self.subscription_ids.append(self.service.subscribe_for_property("tb.same1/SameEnum1Interface/set/prop1", self.__set_prop1))
        self.subscription_ids.append(self.service.subscribe_for_invoke_req("tb.same1/SameEnum1Interface/rpc/func1", self.__invoke_func1))

    def __del__(self):
        self.service.on_connected -= self.subscribeForTopics
        self.service.on_subscribed -= self.__handle_subscribed
        self.service.unsubscribe("tb.same1/SameEnum1Interface/set/prop1")
        self.service.unsubscribe("tb.same1/SameEnum1Interface/rpc/func1")
        self.impl.on_prop1_changed -= self.notify_prop1_changed
        self.impl.on_sig1 -= self.notify_sig1

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

    def __invoke_func1(self, args: list[Any]) -> Any:
        param1 = tb_same1.api.as_enum1(args[0])
        reply = self.impl.func1(param1)
        return tb_same1.api.from_enum1(reply)
class SameEnum2InterfaceServiceAdapter():
    def __init__(self, impl: tb_same1.api.ISameEnum2Interface, service: apigear.mqtt.Service):
        self.service = service
        self.impl = impl
        self.on_ready = EventHook()
        self.impl.on_prop1_changed += self.notify_prop1_changed
        self.impl.on_prop2_changed += self.notify_prop2_changed
        self.impl.on_sig1 += self.notify_sig1
        self.impl.on_sig2 += self.notify_sig2
        self.service.on_connected += self.subscribeForTopics
        self.service.on_subscribed += self.__handle_subscribed
        self.subscription_ids = []

    def subscribeForTopics(self):
        self.subscription_ids.append(self.service.subscribe_for_property("tb.same1/SameEnum2Interface/set/prop1", self.__set_prop1))
        self.subscription_ids.append(self.service.subscribe_for_property("tb.same1/SameEnum2Interface/set/prop2", self.__set_prop2))
        self.subscription_ids.append(self.service.subscribe_for_invoke_req("tb.same1/SameEnum2Interface/rpc/func1", self.__invoke_func1))
        self.subscription_ids.append(self.service.subscribe_for_invoke_req("tb.same1/SameEnum2Interface/rpc/func2", self.__invoke_func2))

    def __del__(self):
        self.service.on_connected -= self.subscribeForTopics
        self.service.on_subscribed -= self.__handle_subscribed
        self.service.unsubscribe("tb.same1/SameEnum2Interface/set/prop1")
        self.service.unsubscribe("tb.same1/SameEnum2Interface/set/prop2")
        self.service.unsubscribe("tb.same1/SameEnum2Interface/rpc/func1")
        self.service.unsubscribe("tb.same1/SameEnum2Interface/rpc/func2")
        self.impl.on_prop1_changed -= self.notify_prop1_changed
        self.impl.on_prop2_changed -= self.notify_prop2_changed
        self.impl.on_sig1 -= self.notify_sig1
        self.impl.on_sig2 -= self.notify_sig2

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

    def __invoke_func1(self, args: list[Any]) -> Any:
        param1 = tb_same1.api.as_enum1(args[0])
        reply = self.impl.func1(param1)
        return tb_same1.api.from_enum1(reply)

    def __invoke_func2(self, args: list[Any]) -> Any:
        param1 = tb_same1.api.as_enum1(args[0])
        param2 = tb_same1.api.as_enum2(args[1])
        reply = self.impl.func2(param1, param2)
        return tb_same1.api.from_enum1(reply)
