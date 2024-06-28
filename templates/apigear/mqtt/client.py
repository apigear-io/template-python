import sys

import paho.mqtt.client
import paho.mqtt.enums

from asyncio.queues import Queue
from utils.eventhook import EventHook
import asyncio

class Client:
    def __init__(self):
        self.send_queue = Queue()
        self.client = paho.mqtt.client.Client(protocol=paho.mqtt.client.MQTTv5 )
        self.client.on_connect = self.on_connect
        self.client.on_subscribe = self.on_subscribed
        self.client.on_message = self.message_handling
        self._on_message = EventHook()
        self._on_connected = EventHook()
        self._on_subscribed = EventHook()

    async def disconnect(self):
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
            
    def subscribe(self, topic, qos):
        # TODO add callbacks, store
        self.client.subscribe(topic, qos)

    def message_handling(self, client, userdata, msg):
        print(f"{msg.topic}: {msg.payload.decode()}")
        self._on_message.fire()
