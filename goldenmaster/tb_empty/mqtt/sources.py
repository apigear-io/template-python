import apigear.mqtt
import utils.base_types
import tb_empty.api
from utils.eventhook import EventHook
from typing import Any
import logging
class EmptyInterfaceServiceAdapter():
    def __init__(self, impl: tb_empty.api.IEmptyInterface, service: apigear.mqtt.Service):
        self.service = service
        self.impl = impl
        self.service.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        #TODO SUBSCRIBE FOR INVOKE TOPIC

    def __del__(self):
        self.service.on_connected -= self.subscribeForTopics
        #TODO UNSUBSCRIBE INVOKE TOPIC
