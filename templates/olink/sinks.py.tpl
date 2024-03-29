import asyncio
from typing import Any
from olink.core import Name
from olink.client import IObjectSink, ClientNode
from {{snake .Module.Name}}_api.shared import EventHook
from {{snake .Module.Name}}_api import api
import logging

{{- $m := .Module }}
{{- range .Module.Interfaces }}
{{- $i := . }}
{{- $id := printf "%s.%s" $m.Name $i.Name }}

class {{Camel .Name}}Sink(IObjectSink):
    def __init__(self):
        super().__init__()
{{- range .Properties }}
        self._{{snake .Name}} = {{pyDefault "api." .}}
        self.on_{{snake .Name}}_changed = EventHook()
{{- end }}
{{- range .Signals }}
        self.on_{{snake .Name}} = EventHook()
{{- end }}
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args, no_wait=False):
        if no_wait:
            self.client.invoke_remote(f"{{$id}}/{name}", args, func=None)
        else:
            future = asyncio.get_running_loop().create_future()
            def func(args):
                return future.set_result(args.value)
            self.client.invoke_remote(f"{{$id}}/{name}", args, func)
            return await asyncio.wait_for(future, 500)

    {{- range .Properties }}
    {{- if not .IsReadOnly }}

    def _set_{{snake .Name}}(self, value):
        if self._{{snake .Name}} == value:
            return
        self._{{snake .Name}} = value
        self.on_{{snake .Name}}_changed.fire(self._{{snake .Name}})

    def set_{{snake .Name}}(self, value):
        if self._{{snake .Name}} == value:
            return
        {{- if .IsArray }}
        self.client.set_remote_property('{{$id}}/{{.Name}}', [api.from_{{snake .Type}}(_) for _ in value])
        {{- else }}
        self.client.set_remote_property('{{$id}}/{{.Name}}', value)
        {{- end }}
    {{- end }}

    def get_{{snake .Name}}(self):
        return self._{{snake .Name}}

    {{- end }}

    {{- range .Operations }}

    async def {{snake .Name}}({{pyParams "api." .Params}}):
        {{- range $idx, $_ := .Params }}
        {{- if .IsArray }}
        _{{snake .Name}} = [api.from_{{snake .Type}}({{snake .Type}}) for {{snake .Type}} in {{snake .Name}}]
        {{- else }}
        _{{snake .Name}} = api.from_{{snake .Type}}({{snake .Name}})
        {{- end }}
        {{- end }}
        return await self._invoke("{{.Name}}", [
            {{- range $idx, $_ := .Params -}}{{- if $idx}}, {{ end -}}
            _{{snake .Name}}
            {{- end -}}
        ]{{ if .Return.IsVoid }}, no_wait=True {{- end -}})
    {{- end }}

    def olink_object_name(self):
        return '{{$id}}'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        {{- if len .Properties}}
        for k in props:
        {{- range $idx, $o := .Properties }}
            {{- if $idx }}
            elif k == "{{.Name}}":
            {{- else }}
            if k == "{{.Name}}":
            {{- end }}
                {{- if .IsArray }}
                v = [api.as_{{snake .Type}}(_) for _ in props[k]]
                {{- else }}
                v =  api.as_{{snake .Type}}(props[k])
                {{- end }}
                self._set_{{snake .Name}}(v)
        {{- end }}
        {{- end }}

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        {{- if len .Properties }}
        path = Name.path_from_name(name)
        {{- end }}
        {{- range $idx, $o := .Properties }}
        {{- if $idx }}
        elif path == "{{.Name}}":
        {{- else }}
        if path == "{{.Name}}":
        {{- end }}
            {{- if .IsArray }}
            v = [api.as_{{snake .Type}}(_) for _ in value]
            {{- else }}
            v =  api.as_{{snake .Type}}(value)
            {{- end }}
            self._set_{{snake .Name}}(v)
            return
        {{- end }}
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        {{- if len .Signals }}
        path = Name.path_from_name(name)
        {{- end }}
        {{- range $idx, $o := .Signals }}
        {{- if $idx }}
        elif path == "{{.Name}}":
        {{- else }}
        if path == "{{.Name}}":
        {{- end }}
            {{- range $index, $_ := .Params }}
            {{- if .IsArray }}
            {{snake .Name}} = [api.as_{{snake .Type}}(_) for _ in args[{{$index}}]]
            {{- else }}
            {{snake .Name}} =  api.as_{{snake .Type}}(args[{{$index}}])
            {{- end }}
            {{- end }}
            self.on_{{snake .Name}}.fire(
            {{- range $index, $_ := .Params -}}{{- if $index}}, {{ end -}}
            {{snake .Name}}
            {{- end -}}
            )
            return
        {{- end }}
        logging.error("unknown signal: %s", name)

{{- end }}
