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
        #TODO SUBSCRIBE FOR INVOKE TOPIC

    def __del__(self):
        self.service.on_connected -= self.subscribeForTopics
        self.service.unsubscribe("counter/Counter/set/vector")
        self.service.unsubscribe("counter/Counter/set/extern_vector")
        #TODO UNSUBSCRIBE INVOKE TOPIC

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
