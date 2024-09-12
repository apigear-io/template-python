import apigear.mqtt
import utils.base_types
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
        self.impl.on_vector_changed += self.notify_vector_changed
        self.impl.on_extern_vector_changed += self.notify_extern_vector_changed
        self.service.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.service.subscribe_for_property("counter/Counter/set/vector", self.__set_vector)
        self.service.subscribe_for_property("counter/Counter/set/extern_vector", self.__set_extern_vector)
        self.service.subscribe_for_invoke_req("counter/Counter/rpc/increment", self.__invoke_increment)
        self.service.subscribe_for_invoke_req("counter/Counter/rpc/decrement", self.__invoke_decrement)

    def __del__(self):
        self.service.on_connected -= self.subscribeForTopics
        self.service.unsubscribe("counter/Counter/set/vector")
        self.service.unsubscribe("counter/Counter/set/extern_vector")
        self.service.unsubscribe("counter/Counter/rpc/increment")
        self.service.unsubscribe("counter/Counter/rpc/decrement")
        self.impl.on_vector_changed -= self.notify_vector_changed
        self.impl.on_extern_vector_changed -= self.notify_extern_vector_changed

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
