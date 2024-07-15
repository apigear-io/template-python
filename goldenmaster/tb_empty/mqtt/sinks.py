import asyncio
from typing import Any
import apigear.mqtt
from utils.eventhook import EventHook
import utils.base_types
import tb_empty.api
import logging

class EmptyInterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self.client.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        #TODO SUBSCRIBE FOR INVOKE RESP TOPIC

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        #TODO UNSUBSCRIBE INVOKE RESP TOPIC

    # internal functions on message handle
