from .base import BaseClient
import paho.mqtt.properties

class Client(BaseClient):
    def __init__(self, id):
        super().__init__(id)
        

    def subscribe(self, topic, callback):
        self._subscribe(topic, callback, self.pass_only_payload)

    def set_remote_property(self, topic, payload_value):
        self.client.publish(topic, payload_value, self.qos, retain = False)
        
    def subscribe_for_invoke_resp(topic, invokeCallback):
        #TODO 
        # handling invoke resp messages should be different than handling singals or properties messages
        # the user callback should get one more parameter(respId) and it should be wrapped with a function
        # that parses properties to extract the id and then calls user callback (topic, payload, respId)
        print(topic)
 
    
    def invoke_remote(self, topic, responseTopic, payload, responseId):    
        props = paho.mqtt.properties.Properties(paho.mqtt.properties.PacketTypes.PUBLISH)
        props.responseTopic=responseTopic
        props.CorrelationData = bytes(responseId)
        self.client.publish(responseTopic, payload, self.qos, retain = False, properties = props)
        print(topic)
