from .base import BaseClient
import paho.mqtt.properties
from typing import Callable, Any 


class Client(BaseClient):
    def __init__(self, id):
        super().__init__(id)
        
    def subscribe_for_property(self, topic, callback: Callable[[Any], None]):
        self._subscribe(topic, callback, self.pass_only_payload)

    def subscribe_for_signal(self, topic, callback: Callable[[list[Any]], None]):
        self._subscribe(topic, callback, self.pass_only_payload)

    def set_remote_property(self, topic, payload_value):
        self.client.publish(topic, self.to_payload(payload_value), self.qos, retain = False)
        
    def subscribe_for_invoke_resp(topic, invokeCallback):
        #TODO 
        # handling invoke resp messages should be different than handling signals or properties messages
        # the user callback should get one more parameter(respId) and it should be wrapped with a function
        # that parses properties to extract the id and then calls user callback (topic, payload, respId)
        print(topic)
 
    
    def invoke_remote(self, topic, responseTopic, payload, responseId):    
        props = paho.mqtt.properties.Properties(paho.mqtt.properties.PacketTypes.PUBLISH)
        props.responseTopic=responseTopic
        props.CorrelationData = bytes(responseId)
        self.client.publish(responseTopic,  self.to_payload(payload), self.qos, retain = False, properties = props)
        print(topic)
