import asyncio
import os
import sys

#add context - paths to modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from asyncio.queues import Queue
from olink.client import ClientNode
import websockets
import logging
import apigear.olink

{{ range .System.Modules }}
import {{snake .Name}}.olink
{{- end }}

# set default log level to INFO and above
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)


# create a client node
node = ClientNode()

# create our client ws adapter
client = apigear.olink.Client(node)
{{ range .System.Modules }}
{{ $module := . }}
{{ range .Interfaces }}

# create and register sink for {{$module.Name}}.{{.Name}}
sink = {{snake $module.Name}}.olink.{{.Name}}Sink()
node.link_remote(sink.olink_object_name())
{{- end }}
{{- end }}


ADDR = 'ws://localhost:8000/ws'

async def main():
    await client.connect(ADDR)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
