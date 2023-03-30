import asyncio
from typing import Any
from asyncio.queues import Queue
from starlette.applications import Starlette
from starlette.endpoints import WebSocketEndpoint
from starlette.routing import WebSocketRoute
from starlette.websockets import WebSocket

from olink.remotenode import RemoteNode
from olink.ws import Server, SourceAdapter

{{- range .System.Modules }}

import {{dot .Name}}.olink.sources as sources
import {{dot .Name}}.olink.services as services
{{- range .Interfaces }}
# {{.Name}} service registration
sources.{{.Name}}Source(services.{{.Name}}Service())

{{- end }}
{{- end }}


if __name__ == "__main__":
    run_server("localhost", 8152)
