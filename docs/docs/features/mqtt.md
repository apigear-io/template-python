﻿---
sidebar_position: 3
---
import CodeBlock from '@theme/CodeBlock';
import helloWorldModuleComponent from '!!raw-loader!./data/helloworld.module.yaml';
import mqttMessagesFormat from '/files/mqtt/ApiGearMQTTv0.1.pdf';


# MQTT

:::caution
This is an experimental feature. It contains smallest working set of functionalities to adapt the generated interface for using over the network with MQTT protocol.
It doesn't include the security. The error handling is minimal. It is not production ready.
Please also check issues on github for this template.
:::

This feature purpose is not only to help you introduce MQTT protocol into your project, but also show that an existing protocol can be adapted for sharing your data in your ecosystem. When going through this document you may notice this implementation contains general client/server adapters in 📂hello-world/apigear/mqtt
and an interface specific part generated from templates for each interface in  📂hello-world/py_hello_world/io_world/mqtt. <br /> <br /> 
 This feature provides a *client* and a *server* adapter for your interfaces for the MQTT protocol. It allows you to connect different applications in the same or different technologies (check all of our [templates](/docs/sdk/intro)).<br />
 Use an *Mqtt client* instead of your interface implementation to be able to receive data from remote service.<br />
 Use an *Mqtt server adapter* to expose your interface implementation as a remote service.<br />

:::tip
The MQTT broker is not provided with implementation. To be able to run client and service you need to run a broker of your choice.
:::

### Before Start

The mqtt library needs to be installed separately, make sure you have installed all the libraries listed in requirements
```bash
`pip install --upgrade -r requirements.txt`
```

## File overview for module
 
 With an example  API

<details>
  <summary>Hello World API (click to expand)</summary>
  <CodeBlock language="yaml" showLineNumbers>{helloWorldModuleComponent}</CodeBlock>
</details>

the following file structure will be generated. The purpose and content of each file is explained below.

```bash {4,19}
📂hello-world
 ┣ 📂apigear
 ┃ ...
 ┣ 📂py_hello_world
 ┃ ┣ 📂apigear
 ┃ ┃ ┣ 📂mqtt
 ┃ ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┃ ┣ 📜client.py
 ┃ ┃ ┃ ┣ 📜service.py
 ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ 
 ┃ ┣ 📂examples
 ┃ ┣ 📂io_world
 ┃ ┃ ┣ 📂api
 ┃ ┃ ┣ 📂impl
 ┃ ┃ ┣ 📂mqtt
 ┃ ┃ ┃ ┣ 📜sinks.py
 ┃ ┃ ┃ ┣ 📜sources.py
 ┃ ┃ ┃ ┗ 📜__init__.py
 ...
```

### Python apigear - The Network Layer

When generating the mqtt feature (or any of those: olink monitor feature) you'll get an additional folder it the top most directory: the 📂hello-world/📂apigear. The 📂mqtt subfolder contains objects that implement a network layer (based on [Paho Mqtt library](https://pypi.org/project/paho-mqtt/)) for the MQTT protocol. Those are:
- Client - Adapts the MQTT client, to serve as an network endpoint for [interface client adapters](mqtt#mqtt-client-adapter). 
  Exposes:
    - methods that allow receiving data for remote service: subscribing for properties changes, signals emission and method response invocation;
    - methods that allow remote using the service: requesting property change or invoking a method.  <br />
  The client may serve many client interface adapters, even for the same interfaces (allows subscribing for same topic).
  In case many interface client adapters for same interface are connected: property changes and signals are provided to all interface client adapters, but the invoke method response will be delivered only for the one that requested it.
- Service - Adapts the MQTT client to serve as an network endpoint for [interface service adapters](mqtt#mqtt-server-adapter). 
  Exposes:
    - methods that allow receiving requests from remote clients: subscribing for properties change requests, send method invocation;
    - methods that allow publishing property change, signal, functionality to handles sending a response for method invocation requests. <br />
  This Service may be used for many, interface service adapters, but it is not recommended to use more than one interface service adapter for the same interfaces.

:::tip
Have in mind that MQTT might not be suitable for high-frequency messages especially with one mqtt client serving more than one object.
Also the brokers have limits for messages number/size queued from one client. In case you are not getting all the messages consider changing those or splitting traffic between more clients (maybe some handle the properties, some handle the methods).
:::

### MQTT Client Adapter

File `📜sinks.py` contains the remote client for the `Hello` interface  - a `HelloClientAdapter` class.<br /> 
The object is an `IHello` implementation.<br />
It requires an instance of Apigear::Mqtt::Client to work. It uses the Client to subscribe (and unsubscribe) for topics that allow receiving properties, signals and invoke responses from service.

#### Properties
The property getters (here getter `get_last`) return immediately the locally stored last received value from server. <br /> 
The property setter (here setter `set_last` ) requests setting a value on server side, local value is not changed. <br /> 
You can add handler for a property changed event (here `on_last_changed(Message)` )
When the client receives information that server changed the property, a target property (here `last`) is updated locally and all handlers added for the event are fired (in addition order) with the new value of property.

:::note
The connected interface client adapter has its local properties in sync with a service. The properties messages are retained in mqtt broker, so all already set properties are provided.
:::

#### Operations
The operations are async, and they return a coroutine awaited with a timeout of 500 seconds.<br />
The async method sends an invoke operation request to a service and waits for the response.<br />
Have in mind that this is a blocking operation.

#### Signals
You should not emit any signals from a client.
You can add a handler to any signals offered by your interface (here `void just_said(Message)` )
When a HelloClientAdapter client receives the message from server that indicates the signal was emitted it executes all added handlers to a `on_just_said` event hook.

#### Use `HelloClientAdapter`

HelloClientAdapter is an adapter of you interface to the Mqtt Client (with protocol and network layer implementation), here provided by a `apigear.mqtt.Client`.
All you need to do is to pass the `apigear.mqtt.Client` to your Interface Client Adapter, and request connecting to host when it is convenient for you.
You can find the example code for the your `Hello` MQTT client below. Remember to run a MQTT broker of your choice.

```python
import os
import sys
# add context - your relative path from this example to py_hello_world dir e.g. like this
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import apigear.mqtt
import logging
import io_world.mqtt
import io_world.api

async def main():
    # create a mqtt adapter for client side
    client = apigear.mqtt.Client("UniqueClientNameForMqttHelloExample")

    # create mqtt interface adapters for client side
    mqtt_hello = io_world.mqtt.HelloClientAdapter(client)
    await client.connect("localhost", 1883)

    # Subscribe for property changes
    def handleProperty(value):
        print("received property change");
        print(value);
    mqtt_hello.on_last_changed += handleProperty
    # or ask for change.
    local_last = io_world.api.Message();
    local_last.content = "New message"
    mqtt_hello.set_last(local_last);
    
    # Check the signals with subscribing for its change
    def handleSignal(value):
        print("received signal");
        print(value);
    mqtt_hello.on_just_said += handleSignal
    
    # Play around executing your operations
    message_to_say = io_world.api.Message()
    message_to_say.content = "Message to say"
    result = mqtt_hello.say(message_to_say, io_world.api.When.NOW)
    await result
    print("method result")
    print(result)    
    
    input("Press Enter to close")

    client.disconnect()

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
```
### MQTT Server Adapter

File `📜sources.py` contains the mqtt server side adapter for the `Hello` interface - the `HelloServiceAdapter` object.<br />
When creating the `HelloServiceAdapter` you need to provide the `apigear.mqtt.Service` and the local implementation of `IHello`, local service.<br />
`HelloServiceAdapter` object exposes the local object for remote usage with the MQTT protocol. It handles all the network requests, and calls your local object.
The mqtt client connection and communication is handled transparently, no additional actions are needed.

#### Properties
The MQTT service adapters add handlers for all the properties changes to the local implementation. On property change the generated implementation executes all added handlers.
In this example on each `last` property change the handler for `on_last_changed(Message)`, sends a message with a topic specific for this property in this interface and with value in the payload.
This happens either when you change a property directly on your local `Hello` object, or when a change property request message is received by the `HelloServiceAdapter`, which applies the property on your local `Hello` object.

#### Operations
The operations invocation which came from the clients through the network will be performed on your local `Hello` object. The result of the operation (if any) will be returned only to a client, from which the message was send, not all clients.

#### Signals
The MQTT service adapters add handlers for all the signals to the local implementation which send MQTT messages with information about signal emission with their arguments. On signal emission the generated implementation executes all handlers added for this signal.
All the signals emitted by your local `Hello` objects are forwarded to all connected clients.

#### Use `HelloServiceAdapter`

`HelloServiceAdapter` an adapter of your interface to the specific, object server side, version of Mqtt Client (with protcol and network layer implementation), here provided by a `ApiGear::Mqtt::ServiceAdapter` 
All you need to do is to pass this ServiceAdapter to your Interface Service Adapter, and request connecting to host when it is convenient for you.
You can find the example code for the your `Hello` MQTT service below. Remember to run a MQTT broker of your choice.

```python 
import os
import sys
# add context - your relative path from this example to py_hello_world dir e.g. like this
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import apigear.mqtt
import io_world.impl
import io_world.mqtt
import io_world.api

async def main():
    service = apigear.mqtt.Service("uniqueServiceIdForHelloService")
    source_io_world_hello = io_world.impl.Hello()
    serviceAdapter_io_world_hello = io_world.mqtt.HelloServiceAdapter(source_io_world_hello, service)

    await service.connect("localhost", 1883)
    
    # Set property, the change will be sent to all clients, and local handlers if any.
    local_last = io_world.api.Message();
    local_last = "New message from server"
    source_io_world_hello.set_last(local_last);

    # Emit the signal, it will be sent to all clients
    signal_message = io_world.api.Message()
    signal_message = "New message from server"
    source_io_world_hello._just_said(signal_message)
    
    input("Press Enter to close")
    service.disconnect()

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())

```
:::note
The implemented Mqtt Client (used both in apigear.mqtt.Client and apigear.mqtt.Service ) uses a thread to process network traffic. This mean, if you're having an asynchronous application, that reacting on the events inside you handlers (for all: properties, signals, operation results) may require using
`loop.call_soon_threadsafe(callback, *args)` to handle the output in your main event loop.
:::

### MQTT Messages
In case you want construct messages for client or server side on your own, please check how topics are created and how does the payload look like, check this documentS [messages format](/files/mqtt/ApiGearMQTTv0.1.pdf).
