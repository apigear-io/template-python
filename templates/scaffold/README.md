# Python API

## Using

The API is created inside the api folder.

In the examples folder is a usable example project with tests. You can run the example using

Note: The api and example folder will always be cleaned and re-written. So don't modify the files or your changes will get lost.

cd example && python main.py

Test can be run using pytest

cd example && pytest

You can start create your own project from scratch or just copy the example folder inside the root folder and start modifying the content

Please copy the content of the example folder into your root folder and use this as starting

## Updates

When you change the origin API the api and example folder will change during the generator run. You can check in the changes in the examples folder into git to see the diff between to runs and adapt your project code accordingly. Changes can be the API has changed or you use a newer version of the templates and technical details might have changed.

## Install Dependencies

Make sure you run the latest pip

```
pip install --upgrade pip
```

For dependencies see `requirements.txt`

```
pip install --upgrade -r requirements.txt
```

## Features

## HTTP Client and Server

## WAMP Client and Service


### Client Demo

The client is in `org_example_calc/wamp/service.py`. The exact location depends on your module.

A simple main function will look like this.

```py
import random
from os import environ
import asyncio
from autobahn.asyncio.component import Component, run
import org_example_calc.wamp.client

# WAMP_SERVER=u'ws://127.0.0.1:8080/ws'
WAMP_SERVER=u'ws://raspberrypi.local:8080/ws'
WAMP_REALM=u'nexus.realm1'

comp = Component(
    transports=WAMP_SERVER,
    realm=WAMP_REALM,
)

@comp.on_join
async def joined(session, details):
    client = org_example_calc.wamp.client.CalculatorService(session)
    await client._register()

    # def onevent(msg):
    #     print("event", msg)
    # await session.subscribe(onevent, 'org.example.calc.Calculator')

    await client.clear()
    while True:
        print("state:", client._state)
        choice = random.choice(
            [client.add, client.substract, client.multiply, client.divide])
        a = random.randint(0, 10)
        resp = await choice(a)
        await asyncio.sleep(0.01)

if __name__ == '__main__':
    run([comp])
```



Service Implementation

To implement a service just implement the `service.py` inside the WAMP module folder.

```py
# org_example_calc/wamp/service.py

class CalculatorService(object):
    def __init__(self):
        self._state = shared.CalculatorState(
            total=0
        )

    def _set_listener(self, listener: shared.CalculatorEventListener):
        self._listener = listener

    def _get_state(self):
        return self._state

    def add(self, a: int):
        self._state.total += a
        # raise NotImplementedError("Calculator.add")

    def substract(self, a: int):
        self._state.total -= a
        # raise NotImplementedError("Calculator.substract")

    def multiply(self, a: int):
        self._state.total *= a
        # raise NotImplementedError("Calculator.multiply")

    def divide(self, a: int):
        if a!= 0:
            self._state.total /= a
        # raise NotImplementedError("Calculator.divide")

    def clear(self):
        self._state.total = 0
        # raise NotImplementedError("Calculator.clear")
```
