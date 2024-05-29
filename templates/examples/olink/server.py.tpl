import asyncio
import logging
import os
import sys

#add context - paths to modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from starlette.applications import Starlette
from starlette.routing import WebSocketRoute

from olink.remote import RemoteNode

import apigear.olink

{{- range .System.Modules }}
{{- $import_olink := printf "%s_olink" (snake .Name)}}
{{- $import_impl := printf "%s_impl" (snake .Name)}}

import {{$import_olink}}
import {{$import_impl}}

{{- end }}
{{ range .System.Modules }}
{{- $import_olink := printf "%s_olink" (snake .Name)}}
{{- $import_impl := printf "%s_impl" (snake .Name)}}

{{- range .Interfaces }}
{{$import_olink}}.{{Camel .Name}}Source({{$import_impl}}.{{Camel .Name}}())
{{- end }}
{{ end }}

# set default log level to INFO and above
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

routes = [
    WebSocketRoute("/ws", apigear.olink.RemoteEndpoint)
]


app = Starlette(routes=routes)
