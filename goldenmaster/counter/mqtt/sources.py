import apigear.mqtt
import utils.base_types
import paho.mqtt.enums
import paho.mqtt.reasoncodes
import counter.api
from utils.eventhook import EventHook
from typing import Any
import logging
import custom_types.api
import extern_types.api
import vector3d.vector
class CounterServiceAdapter():
    def __init__(self, impl: counter.api.ICounter, service: apigear.mqtt.Service):
        self.service = service
        self.impl = impl
        self.on_ready = EventHook()
        self.impl.on_vector_changed += self.notify_vector_changed
        self.impl.on_extern_vector_changed += self.notify_extern_vector_changed
        self.service.on_connected += self.subscribeForTopics
        self.service.on_subscribed += self.__handle_subscribed
        self.subscription_ids = []

    def subscribeForTopics(self):
        self.subscription_ids.append(self.service.subscribe_for_property("counter/Counter/set/vector", self.__set_vector))
        self.subscription_ids.append(self.service.subscribe_for_property("counter/Counter/set/extern_vector", self.__set_extern_vector))
        self.subscription_ids.append(self.service.subscribe_for_invoke_req("counter/Counter/rpc/increment", self.__invoke_increment))
        self.subscription_ids.append(self.service.subscribe_for_invoke_req("counter/Counter/rpc/decrement", self.__invoke_decrement))

    def __del__(self):
        self.service.on_connected -= self.subscribeForTopics
        self.service.on_subscribed -= self.__handle_subscribed
        self.service.unsubscribe("counter/Counter/set/vector")
        self.service.unsubscribe("counter/Counter/set/extern_vector")
        self.service.unsubscribe("counter/Counter/rpc/increment")
        self.service.unsubscribe("counter/Counter/rpc/decrement")
        self.impl.on_vector_changed -= self.notify_vector_changed
        self.impl.on_extern_vector_changed -= self.notify_extern_vector_changed

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

    def notify_vector_changed(self, value):
        v = custom_types.api.from_vector3_d(value)
        self.service.notify_property_change("counter/Counter/prop/vector", v)

    def notify_extern_vector_changed(self, value):
        v = extern_types.api.from_vector3d_vector_vector(value)
        self.service.notify_property_change("counter/Counter/prop/extern_vector", v)

    def __set_vector(self, value: Any):
            v = custom_types.api.as_vector3_d(value)
            self.impl.set_vector(v)

    def __set_extern_vector(self, value: Any):
            v = extern_types.api.as_vector3d_vector_vector(value)
            self.impl.set_extern_vector(v)

    def __invoke_increment(self, args: list[Any]) -> Any:
        vec = extern_types.api.as_vector3d_vector_vector(args[0])
        reply = self.impl.increment(vec)
        return extern_types.api.from_vector3d_vector_vector(reply)

    def __invoke_decrement(self, args: list[Any]) -> Any:
        vec = custom_types.api.as_vector3_d(args[0])
        reply = self.impl.decrement(vec)
        return custom_types.api.from_vector3_d(reply)
