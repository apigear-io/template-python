import apigear.mqtt
import utils.base_types
import paho.mqtt.enums
import paho.mqtt.reasoncodes
import tb_empty.api
from utils.eventhook import EventHook
from typing import Any
import logging
class EmptyInterfaceServiceAdapter():
    def __init__(self, impl: tb_empty.api.IEmptyInterface, service: apigear.mqtt.Service):
        self.service = service
        self.impl = impl
        self.on_ready = EventHook()
        self.on_ready.self.fire()
