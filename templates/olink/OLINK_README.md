# ObjectLink for Python

## Server

Implement the services, see the files in the `*_impl` folders.

Run the server with uvicorn

```py
uvicorn olink_server:app
```

If server is not run on the local device or on a different port, specify `0.0.0.0` as source address and the preferred port

```py
uvicorn olink_server:app --host 0.0.0.0 --port 8080
```

## Client

use the `olinkclient.py` implementation as a starting point.

```py
# create a node
node = ClientNode()
# attach node to ws client
client = Client(node)

# demo.Calc sink registration
sink = demo.olink.sinks.CalcSink()
node.link_remote(sink.olink_object_name())

def main():
    def print_change(name, value):
        print('property changed', name, value)

    sink = node.get_object_sink('demo.Calc')
    sink.on_property_changed += print_change

    # get event loop
    loop = asyncio.get_event_loop()

    # schedule some calls
    loop.create_task(sink.add(10))
    loop.create_task(sink.add(11))
    loop.create_task(sink.add(12))

    # run the event loop
    loop.run_until_complete(client.connect('ws://localhost:8000/ws'))

if __name__ == '__main__':
    main()
```
