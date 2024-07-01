from .base import BaseClient
from typing import Callable, Any

class Service(BaseClient):
    def __init__(self, id):
        super().__init__(id)
        
    def subscribe_for_property(self, topic, callback: Callable[[Any], None]):
        self._subscribe(topic, callback, self.pass_only_payload)
        
    def subscribe_for_invoke_req(topic, callback):
        #TODO 
        # handling invoke resp messages should be different than handling signals or properties messages
        # the user callback should wrapped with a function that extracts the responseTopic and correlation Info
        # the method should execute user callback in async manner, the callback should return data to be sent
        # the callback wrapper should send the notifyInvokeReply 
        print("handling invoke request is not yet handled")
        
    def notify_invoke_response(self, responseTopic, payload, propsWithCorrelationData):
        self.client.publish(responseTopic, self.to_payload(payload), self.qos, retain = False, properties = propsWithCorrelationData)
 
    def notify_signal(self,topic, payload_args):
        self.client.publish(topic, self.to_payload(payload_args), self.qos, retain = False)
    
    def notify_property_change(self,topic, payload_value):
        self.client.publish(topic, self.to_payload(payload_value), self.qos, retain = True)
    