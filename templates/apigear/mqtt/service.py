from .base import BaseClient
import paho.mqtt.properties
import paho.mqtt.client

class Service(BaseClient):
    def __init__(self, id):
        super().__init__(id)
        
    def subscribe(self, topic, callback):
        self._subscribe(topic, callback, self.pass_only_payload)
    
    def invoke_handler_wrapper(self,msg : paho.mqtt.client.MQTTMessage, callback ):
        payload = msg.payload.decode()
        result = callback(payload)
        properties = paho.mqtt.properties.Properties(paho.mqtt.properties.PacketTypes.PUBLISH)
        properties.CorrelationData = msg.properties.CorrelationData
        self.notify_invoke_response(msg.properties.ResponseTopic, result, properties)
              
    def subscribe_for_invoke_req(self, topic, callback):
        self._subscribe(topic, callback, self.invoke_handler_wrapper)
        
    def notify_invoke_response(self, responseTopic, payload, propsWithCorrelationData):
        self.client.publish(responseTopic, payload, self.qos, retain = False, properties = propsWithCorrelationData)
 
    def notify_signal(self,topic, payload_args):
        self.client.publish(topic, payload_args, self.qos, retain = False)
    
    def notify_property_change(self,topic, payload_value):
        self.client.publish(topic, payload_value, self.qos, retain = True)
    