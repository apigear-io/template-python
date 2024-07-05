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

    # internal functions on message handle
