import sys

import paho.mqtt.client
import paho.mqtt.enums

from asyncio.queues import Queue
from utils.eventhook import EventHook
import asyncio
import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

class Client:
    def __init__(self):
        self.send_queue = Queue()
        self.client = paho.mqtt.client.Client(protocol=paho.mqtt.client.MQTTv5 )
        self.client.on_connect = self.on_connect
        self.client.on_subscribe = self.on_subscribed
        self.client.on_message = self.message_handling
        self._on_connected = EventHook()
        self._on_subscribed = EventHook()
        self.topics = {}
        self.on_log(self._mqtt_log_writer)
        
    def __del__(self):
        for topic in self.topics:
            self.client.unsubscribe(topic)
        self.disconnect()

    def disconnect(self):
        #not necessary here, should be enough to have disconnect
        self.client.loop_stop()
        self.client.disconnect()
     
    def on_subscribed(self, client, userdata, mid, reason_code_list, properties):
        self._on_subscribed.fire()
        
    #TODO this should be probable setRemoteProperty etc.
    def publish(self, topic, payload, qos):
        self.client.publish(topic, payload, qos)
     
    async def connect(self, addr, port):
        self.client.loop_start()
        bind_address=""
        clean_start=True
        properties = paho.mqtt.properties.Properties(paho.mqtt.properties.PacketTypes.CONNECT)
        keepalive = 60
        self.client.connect_async(addr, port, keepalive, bind_address, clean_start, properties)
        
    def on_connect(self, client, userdata, flags, reasonCode, properties=None):
        #TODO subscribe all waiting to subscribe
        self._on_connected.fire()
            
    def subscribe(self, topic, callback):
        self.topics
        if topic not in self.topics:
            self.topics[topic] = callback
            self.client.subscribe(topic, 2)
        else:
            self.logging_func(paho.mqtt.enums.LogLevel.MQTT_LOG_WARNING, "topic already added, no callback added")
        
    def unsubscribe(self, topic):
        if topic in self.topics:
            del self.topics[topic]
            self.client.unsubscribe(topic)
        else:
            self.logging_func(paho.mqtt.enums.LogLevel.MQTT_LOG_WARNING, "topic not there, not removed")

    def message_handling(self, client, userdata, msg):
        callback = self.topics.get(msg.topic)
        if callback != None:
            callback(msg.payload.decode())    
        else:
            self.logging_func(paho.mqtt.enums.LogLevel.MQTT_LOG_WARNING, f"not handled: {msg.topic}: {msg.payload.decode()}")
        
        
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

    def on_log(self, logging_func):
        self.logging_func = logging_func
        self.client.on_log = self._on_log

    def _on_log(self, client, userdata, paho_log_level, messages):
        if self.logging_func != None:
            self.logging_func(paho_log_level, messages)