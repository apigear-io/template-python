# ObjectLink for Python

## Client

use the `olinkclient.py` implementation as a starting point.

```py
# create a node
node = ClientNode()
# attach node to ws client
client = Client(node)

# demo.Calc sink registration
node.link_remote('demo.Calc')
demo.olink.sinks.CalcSink()

def main():
    def print_change(name, value):
        print('property changed', name, value)

    sink = node.get_sink('demo.Counter')
    sink.on_property_changed += print_change

    # get event loop
    loop = asyncio.get_event_loop()

    # schedule some calls
    loop.create_task(sink.increment(1))
    loop.create_task(sink.decrement(2))

    # run the event loop
    loop.run_until_complete(client.connect('ws://localhost:8000/ws'))

if __name__ == '__main__':
    main()
```

## Server

implement the services, see `services.py`

run the server with uvicorn

```py
uvicorn olinkserver:app
```