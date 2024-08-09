from .base import BaseClient
from typing import Callable, Any
import paho.mqtt.properties
import paho.mqtt.client

class Service(BaseClient):
    def __init__(self, id):
        super().__init__(id)
        
    def subscribe_for_property(self, topic, callback: Callable[[Any], None]):
        self._subscribe(topic, callback, self.pass_only_payload)
    
    def invoke_handler_wrapper(self, msg : paho.mqtt.client.MQTTMessage, callback):
        payload = self.from_payload(msg.payload)
        result = ""
        if callback != None:
            result = callback(payload)
        else:
            self.logging_func(paho.mqtt.enums.LogLevel.MQTT_LOG_WARNING, f"no callback for: {msg.topic}: {msg.payload.decode()}")
        properties = paho.mqtt.properties.Properties(paho.mqtt.properties.PacketTypes.PUBLISH)
        properties.CorrelationData = msg.properties.CorrelationData
        self.notify_invoke_response(msg.properties.ResponseTopic, result, properties)
              
    def subscribe_for_invoke_req(self, topic, callback: Callable[[list[Any]], None]):
        self._subscribe(topic, callback, self.invoke_handler_wrapper)
        
    def notify_invoke_response(self, responseTopic, payload, propsWithCorrelationData):
        self.client.publish(responseTopic, self.to_payload(payload), self.qos, retain = False, properties = propsWithCorrelationData)
 
    def notify_signal(self,topic, payload_args):
        self.client.publish(topic, self.to_payload(payload_args), self.qos, retain = False)
    
    def notify_property_change(self,topic, payload_value):
        self.client.publish(topic, self.to_payload(payload_value), self.qos, retain = True)
    