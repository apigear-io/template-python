import apigear.mqtt
import utils.base_types
import paho.mqtt.enums
import paho.mqtt.reasoncodes
import tb_names.api
from utils.eventhook import EventHook
from typing import Any
import logging
class NamEsServiceAdapter():
    def __init__(self, impl: tb_names.api.INamEs, service: apigear.mqtt.Service):
        self.service = service
        self.impl = impl
        self.on_ready = EventHook()
        self.impl.on_switch_changed += self.notify_switch_changed
        self.impl.on_some_property_changed += self.notify_some_property_changed
        self.impl.on_some_poperty2_changed += self.notify_some_poperty2_changed
        self.impl.on_some_signal += self.notify_some_signal
        self.impl.on_some_signal2 += self.notify_some_signal2
        self.service.on_connected += self.subscribeForTopics
        self.service.on_subscribed += self.__handle_subscribed
        self.subscription_ids = []

    def subscribeForTopics(self):
        self.subscription_ids.append(self.service.subscribe_for_property("tb.names/Nam_Es/set/Switch", self.__set_switch))
        self.subscription_ids.append(self.service.subscribe_for_property("tb.names/Nam_Es/set/SOME_PROPERTY", self.__set_some_property))
        self.subscription_ids.append(self.service.subscribe_for_property("tb.names/Nam_Es/set/Some_Poperty2", self.__set_some_poperty2))
        self.subscription_ids.append(self.service.subscribe_for_invoke_req("tb.names/Nam_Es/rpc/SOME_FUNCTION", self.__invoke_some_function))
        self.subscription_ids.append(self.service.subscribe_for_invoke_req("tb.names/Nam_Es/rpc/Some_Function2", self.__invoke_some_function2))

    def __del__(self):
        self.service.on_connected -= self.subscribeForTopics
        self.service.on_subscribed -= self.__handle_subscribed
        self.service.unsubscribe("tb.names/Nam_Es/set/Switch")
        self.service.unsubscribe("tb.names/Nam_Es/set/SOME_PROPERTY")
        self.service.unsubscribe("tb.names/Nam_Es/set/Some_Poperty2")
        self.service.unsubscribe("tb.names/Nam_Es/rpc/SOME_FUNCTION")
        self.service.unsubscribe("tb.names/Nam_Es/rpc/Some_Function2")
        self.impl.on_switch_changed -= self.notify_switch_changed
        self.impl.on_some_property_changed -= self.notify_some_property_changed
        self.impl.on_some_poperty2_changed -= self.notify_some_poperty2_changed
        self.impl.on_some_signal -= self.notify_some_signal
        self.impl.on_some_signal2 -= self.notify_some_signal2

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

    def notify_some_signal(self, some_param: bool):
        _some_param = utils.base_types.from_bool(some_param)
        args = [_some_param]
        self.service.notify_signal("tb.names/Nam_Es/sig/SOME_SIGNAL", args)

    def notify_some_signal2(self, some_param: bool):
        _some_param = utils.base_types.from_bool(some_param)
        args = [_some_param]
        self.service.notify_signal("tb.names/Nam_Es/sig/Some_Signal2", args)

    def notify_switch_changed(self, value):
        v = utils.base_types.from_bool(value)
        self.service.notify_property_change("tb.names/Nam_Es/prop/Switch", v)

    def notify_some_property_changed(self, value):
        v = utils.base_types.from_int(value)
        self.service.notify_property_change("tb.names/Nam_Es/prop/SOME_PROPERTY", v)

    def notify_some_poperty2_changed(self, value):
        v = utils.base_types.from_int(value)
        self.service.notify_property_change("tb.names/Nam_Es/prop/Some_Poperty2", v)

    def __set_switch(self, value: Any):
            v = utils.base_types.as_bool(value)
            self.impl.set_switch(v)

    def __set_some_property(self, value: Any):
            v = utils.base_types.as_int(value)
            self.impl.set_some_property(v)

    def __set_some_poperty2(self, value: Any):
            v = utils.base_types.as_int(value)
            self.impl.set_some_poperty2(v)

    def __invoke_some_function(self, args: list[Any]) -> Any:
        some_param = utils.base_types.as_bool(args[0])
        reply = self.impl.some_function(some_param)
        return utils.base_types.from_int(0)

    def __invoke_some_function2(self, args: list[Any]) -> Any:
        some_param = utils.base_types.as_bool(args[0])
        reply = self.impl.some_function2(some_param)
        return utils.base_types.from_int(0)
