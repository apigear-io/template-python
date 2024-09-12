import apigear.mqtt
import utils.base_types
import paho.mqtt.enums
import paho.mqtt.reasoncodes
import tb_enum.api
from utils.eventhook import EventHook
from typing import Any
import logging
class EnumInterfaceServiceAdapter():
    def __init__(self, impl: tb_enum.api.IEnumInterface, service: apigear.mqtt.Service):
        self.service = service
        self.impl = impl
        self.on_ready = EventHook()
        self.impl.on_prop0_changed += self.notify_prop0_changed
        self.impl.on_prop1_changed += self.notify_prop1_changed
        self.impl.on_prop2_changed += self.notify_prop2_changed
        self.impl.on_prop3_changed += self.notify_prop3_changed
        self.impl.on_sig0 += self.notify_sig0
        self.impl.on_sig1 += self.notify_sig1
        self.impl.on_sig2 += self.notify_sig2
        self.impl.on_sig3 += self.notify_sig3
        self.service.on_connected += self.subscribeForTopics
        self.service.on_subscribed += self.__handle_subscribed
        self.subscription_ids = []

    def subscribeForTopics(self):
        self.subscription_ids.append(self.service.subscribe_for_property("tb.enum/EnumInterface/set/prop0", self.__set_prop0))
        self.subscription_ids.append(self.service.subscribe_for_property("tb.enum/EnumInterface/set/prop1", self.__set_prop1))
        self.subscription_ids.append(self.service.subscribe_for_property("tb.enum/EnumInterface/set/prop2", self.__set_prop2))
        self.subscription_ids.append(self.service.subscribe_for_property("tb.enum/EnumInterface/set/prop3", self.__set_prop3))
        self.subscription_ids.append(self.service.subscribe_for_invoke_req("tb.enum/EnumInterface/rpc/func0", self.__invoke_func0))
        self.subscription_ids.append(self.service.subscribe_for_invoke_req("tb.enum/EnumInterface/rpc/func1", self.__invoke_func1))
        self.subscription_ids.append(self.service.subscribe_for_invoke_req("tb.enum/EnumInterface/rpc/func2", self.__invoke_func2))
        self.subscription_ids.append(self.service.subscribe_for_invoke_req("tb.enum/EnumInterface/rpc/func3", self.__invoke_func3))

    def __del__(self):
        self.service.on_connected -= self.subscribeForTopics
        self.service.on_subscribed -= self.__handle_subscribed
        self.service.unsubscribe("tb.enum/EnumInterface/set/prop0")
        self.service.unsubscribe("tb.enum/EnumInterface/set/prop1")
        self.service.unsubscribe("tb.enum/EnumInterface/set/prop2")
        self.service.unsubscribe("tb.enum/EnumInterface/set/prop3")
        self.service.unsubscribe("tb.enum/EnumInterface/rpc/func0")
        self.service.unsubscribe("tb.enum/EnumInterface/rpc/func1")
        self.service.unsubscribe("tb.enum/EnumInterface/rpc/func2")
        self.service.unsubscribe("tb.enum/EnumInterface/rpc/func3")
        self.impl.on_prop0_changed -= self.notify_prop0_changed
        self.impl.on_prop1_changed -= self.notify_prop1_changed
        self.impl.on_prop2_changed -= self.notify_prop2_changed
        self.impl.on_prop3_changed -= self.notify_prop3_changed
        self.impl.on_sig0 -= self.notify_sig0
        self.impl.on_sig1 -= self.notify_sig1
        self.impl.on_sig2 -= self.notify_sig2
        self.impl.on_sig3 -= self.notify_sig3

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

    def notify_sig0(self, param0: tb_enum.api.Enum0):
        _param0 = tb_enum.api.from_enum0(param0)
        args = [_param0]
        self.service.notify_signal("tb.enum/EnumInterface/sig/sig0", args)

    def notify_sig1(self, param1: tb_enum.api.Enum1):
        _param1 = tb_enum.api.from_enum1(param1)
        args = [_param1]
        self.service.notify_signal("tb.enum/EnumInterface/sig/sig1", args)

    def notify_sig2(self, param2: tb_enum.api.Enum2):
        _param2 = tb_enum.api.from_enum2(param2)
        args = [_param2]
        self.service.notify_signal("tb.enum/EnumInterface/sig/sig2", args)

    def notify_sig3(self, param3: tb_enum.api.Enum3):
        _param3 = tb_enum.api.from_enum3(param3)
        args = [_param3]
        self.service.notify_signal("tb.enum/EnumInterface/sig/sig3", args)

    def notify_prop0_changed(self, value):
        v = tb_enum.api.from_enum0(value)
        self.service.notify_property_change("tb.enum/EnumInterface/prop/prop0", v)

    def notify_prop1_changed(self, value):
        v = tb_enum.api.from_enum1(value)
        self.service.notify_property_change("tb.enum/EnumInterface/prop/prop1", v)

    def notify_prop2_changed(self, value):
        v = tb_enum.api.from_enum2(value)
        self.service.notify_property_change("tb.enum/EnumInterface/prop/prop2", v)

    def notify_prop3_changed(self, value):
        v = tb_enum.api.from_enum3(value)
        self.service.notify_property_change("tb.enum/EnumInterface/prop/prop3", v)

    def __set_prop0(self, value: Any):
            v = tb_enum.api.as_enum0(value)
            self.impl.set_prop0(v)

    def __set_prop1(self, value: Any):
            v = tb_enum.api.as_enum1(value)
            self.impl.set_prop1(v)

    def __set_prop2(self, value: Any):
            v = tb_enum.api.as_enum2(value)
            self.impl.set_prop2(v)

    def __set_prop3(self, value: Any):
            v = tb_enum.api.as_enum3(value)
            self.impl.set_prop3(v)

    def __invoke_func0(self, args: list[Any]) -> Any:
        param0 = tb_enum.api.as_enum0(args[0])
        reply = self.impl.func0(param0)
        return tb_enum.api.from_enum0(reply)

    def __invoke_func1(self, args: list[Any]) -> Any:
        param1 = tb_enum.api.as_enum1(args[0])
        reply = self.impl.func1(param1)
        return tb_enum.api.from_enum1(reply)

    def __invoke_func2(self, args: list[Any]) -> Any:
        param2 = tb_enum.api.as_enum2(args[0])
        reply = self.impl.func2(param2)
        return tb_enum.api.from_enum2(reply)

    def __invoke_func3(self, args: list[Any]) -> Any:
        param3 = tb_enum.api.as_enum3(args[0])
        reply = self.impl.func3(param3)
        return tb_enum.api.from_enum3(reply)
