from asyncio.queues import Queue
from olink.clientnode import ClientNode
import asyncio
from olink.ws.client import Client

{{ range .System.Modules }}
import {{dot .Name}}
{{- end }}

# create a client node
node = ClientNode()

# create our client ws adapter
client = Client(node)

{{ range .System.Modules }}
{{ $module := . }}
{{ range .Interfaces }}

# register {{$module.Name}}.{{.Name}} to the remote node
node.link_remote('{{$module.Name}}.{{.Name}}')
# create our client api
{{dot $module.Name}}.olink.sinks.{{.Name}}Sink()
{{- end }}
{{- end }}

def main():
    def print_change(name, value):
        print('property changed', name, value)

    # get a sink from the registry
    # sink = node.get_sink('<module>.<interface>')
    # register a property change listener
    # sink.on_property_changed += print_change
    loop = asyncio.get_event_loop()
    # register a async function call
    # loop.create_task(sink.doSomething(value))
    loop.run_until_complete(client.connect('ws://localhost:8000/ws'))

if __name__ == '__main__':
    main()
