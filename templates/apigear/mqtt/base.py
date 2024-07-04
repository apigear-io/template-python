import sys

import paho.mqtt.client
import paho.mqtt.enums

from asyncio.queues import Queue
from utils.eventhook import EventHook
import asyncio
import logging
from typing import Callable, Any 

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

class BaseClient:
    def __init__(self, id):
        self.send_queue = Queue()
        self.client = paho.mqtt.client.Client(protocol=paho.mqtt.client.MQTTv5, client_id = id)
        self.client.on_connect = self.__on_connect
        self.client.on_subscribe = self.__on_subscribed
        self.client.on_message = self.__message_handling
        self.on_connected = EventHook()
        self.on_subscribed = EventHook()
        self.topics = {}
        self.on_log(self._mqtt_log_writer)
        self.qos = 2
        
    def __del__(self):
        for topic in self.topics:
            self.client.unsubscribe(topic)
        self.disconnect()

    def disconnect(self):
        #not necessary here, should be enough to have disconnect
        self.client.loop_stop()
        self.client.disconnect()
     
    async def connect(self, addr, port):
        self.client.loop_start()
        bind_address=""
        #TODO - should it be clean start?
        # True: all messages, published by other publishers will be retained in broker untill this  subscriber explicitly unsubscribed
        ## all the messages to publish from this client will be stored anyway and sent on reconnect ( if this is not expected reinitialise needs to be called along with re-subscription)
        clean_start=False
        properties = paho.mqtt.properties.Properties(paho.mqtt.properties.PacketTypes.CONNECT)
        keepalive = 60
        self.client.connect_async(addr, port, keepalive, bind_address, clean_start, properties)

    def _subscribe(self, topic, callback, callback_wrapper = None):
        if topic not in self.topics:
            self.topics[topic] = (callback, callback_wrapper)
            self.client.subscribe(topic, self.qos)
        else:
            self.logging_func(paho.mqtt.enums.LogLevel.MQTT_LOG_WARNING, "topic already added, no callback added")
        
    def unsubscribe(self, topic):
        if topic in self.topics:
            del self.topics[topic]
            self.client.unsubscribe(topic)
        else:
            self.logging_func(paho.mqtt.enums.LogLevel.MQTT_LOG_WARNING, "topic not there, not removed")
       
    def publish(self, topic, payload, qos):
        self.client.publish(topic, payload, qos)

    def on_log(self, logging_func):
        self.logging_func = logging_func
        self.client.on_log = self.__on_log
        
    def __on_connect(self, client, userdata, flags, reasonCode, properties=None):
        #TODO subscribe all waiting to subscribe
        self.on_connected.fire()
            
    def __message_handling(self, client, userdata, msg):
        callback, callback_wrapper = self.topics.get(msg.topic)
        if callback_wrapper != None:
            callback_wrapper(msg, callback)
        elif callback != None:
            callback(msg)    
        else:
            self.logging_func(paho.mqtt.enums.LogLevel.MQTT_LOG_WARNING, f"not handled: {msg.topic}: {msg.payload.decode()}")
            
    def pass_only_payload(self, msg, callback: Callable[[Any], None]):
        if callback != None:
            callback(msg.payload.decode())    
        else:
            self.logging_func(paho.mqtt.enums.LogLevel.MQTT_LOG_WARNING, f"not handled: {msg.topic}: {msg.payload.decode()}")

    def __on_subscribed(self, client, userdata, mid, reason_code_list, properties):
        self.on_subscribed.fire()        
        
    def _mqtt_log_writer(self, level, msg):
       if level == paho.mqtt.enums.LogLevel.MQTT_LOG_DEBUG:
           logging.debug(msg)
       elif level == paho.mqtt.enums.LogLevel.MQTT_LOG_INFO:
           logging.info(msg)
       elif level == paho.mqtt.enums.LogLevel.MQTT_LOG_NOTICE:
           logging.info(msg)
       elif level == paho.mqtt.enums.LogLevel.MQTT_LOG_WARNING:
           logging.warning(msg)
       else:
           logging.error(msg)

    def __on_log(self, client, userdata, paho_log_level, messages):
        if self.logging_func != None:
            self.logging_func(paho_log_level, messages)
    
    def get_client_id(self):
        return self.client._client_id
