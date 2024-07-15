import asyncio
from typing import Any
import apigear.mqtt
from utils.eventhook import EventHook
import utils.base_types
import counter.api
import logging
import custom_types.api
import extern_types.api
import vector3d.vector

class CounterClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self._vector = custom_types.api.Vector3D()
        self.on_vector_changed = EventHook()
        self._extern_vector = vector3d.vector.Vector()
        self.on_extern_vector_changed = EventHook()
        self.client.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.client.subscribe_for_property("counter/Counter/prop/vector", self.__set_vector)
        self.client.subscribe_for_property("counter/Counter/prop/extern_vector", self.__set_extern_vector)
        #TODO SUBSCRIBE FOR INVOKE RESP TOPIC

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.unsubscribe("counter/Counter/prop/vector")
        self.client.unsubscribe("counter/Counter/prop/extern_vector")
        #TODO UNSUBSCRIBE INVOKE RESP TOPIC

    def set_vector(self, value):
        if self._vector == value:
            return
        topic = "counter/Counter/set/vector"
        self.client.set_remote_property(topic, custom_types.api.from_vector3_d(value))

    def get_vector(self):
        return self._vector

    def set_extern_vector(self, value):
        if self._extern_vector == value:
            return
        topic = "counter/Counter/set/extern_vector"
        self.client.set_remote_property(topic, extern_types.api.from_vector3d_vector_vector(value))

    def get_extern_vector(self):
        return self._extern_vector

    # internal functions on message handle

    def __set_vector(self, data):
        value =  custom_types.api.as_vector3_d(data)
        if self._vector == value:
            return
        self._vector = value
        self.on_vector_changed.fire(self._vector)

    def __set_extern_vector(self, data):
        value =  extern_types.api.as_vector3d_vector_vector(data)
        if self._extern_vector == value:
            return
        self._extern_vector = value
        self.on_extern_vector_changed.fire(self._extern_vector)
