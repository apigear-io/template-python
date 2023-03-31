import asyncio
from asyncio.queues import Queue
from typing import Any

from olink.remote import RemoteNode, SourceAdapter
from olink.ws import run_server

{{- range .System.Modules }}
{{ $module := . }}
import {{snake .Name}}
{{- range .Interfaces }}

# {{.Name}} service registration
{{snake .Name}}_impl = {{snake $module.Name}}.{{Camel .Name}}()
{{snake .Name}}_source = SourceAdapter("{{dot $module.Name}}.{{Camel .Name}}", {{snake .Name}}_impl)
RemoteNode.register_source({{snake .Name}}_source)

{{- end }}
{{- end }}

if __name__ == "__main__":
    run_server("localhost", 8152)
