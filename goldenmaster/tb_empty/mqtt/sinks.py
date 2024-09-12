import asyncio
from typing import Any
import apigear.mqtt
import paho.mqtt.enums
import paho.mqtt.reasoncodes
from utils.eventhook import EventHook
import utils.base_types
import tb_empty.api
import logging

class EmptyInterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self.on_ready = EventHook()
        self.on_ready.self.fire()

    # internal functions on message handle
