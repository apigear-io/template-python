from .base import BaseClient
import paho.mqtt.properties
from typing import Callable, Any 
import multiprocessing

class Client(BaseClient):
    def __init__(self, id):
        super().__init__(id)
        self.id_generator = self.IdGenerator()
        
    def subscribe_for_property(self, topic, callback: Callable[[Any], None]) -> int:
        return self._subscribe(topic, callback, self.pass_only_payload)

    def subscribe_for_signal(self, topic, callback: Callable[[list[Any]], None]) -> int:
        return self._subscribe(topic, callback, self.pass_only_payload)
        
    def invoke_resp_handler_wrapper(self,msg : paho.mqtt.client.MQTTMessage, callback ):
        payload = self.from_payload(msg.payload)
        correlationData = int.from_bytes(msg.properties.CorrelationData,"big")
        if callback != None:
            callback(payload, correlationData)
        else:
            self.logging_func(paho.mqtt.enums.LogLevel.MQTT_LOG_WARNING, f"no callback for: {msg.topic}: {msg.payload.decode()}")
              
    def subscribe_for_invoke_resp(self, topic, callback: Callable[[Any, int],None]) -> int:
        return self._subscribe(topic, callback, self.invoke_resp_handler_wrapper)

    def set_remote_property(self, topic, payload_value):
        self.client.publish(topic, self.to_payload(payload_value), self.qos, retain = False)
   
    def invoke_remote(self, topic, responseTopic, payload):    
        responseId = self.id_generator.get_unique_id()
        props = paho.mqtt.properties.Properties(paho.mqtt.properties.PacketTypes.PUBLISH)
        props.ResponseTopic = responseTopic
        props.CorrelationData = bytes([responseId])
        self.client.publish(topic, self.to_payload(payload), self.qos, retain = False, properties = props)
        return responseId
    
    class IdGenerator:
        def __init__(self):
            self.id = 0
            self.lock_manager = multiprocessing.Manager()
            self.lock = self.lock_manager.Lock()

        def get_unique_id(self):
            self.lock.acquire()
            unique_id = self.id
            self.id += 1
            self.lock.release() 
            return unique_id
