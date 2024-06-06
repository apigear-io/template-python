import asyncio
from typing import Any
from olink.core import Name
from olink.client import IObjectSink, ClientNode
from utils.eventhook import EventHook
import utils.base_types
{{- $current_module_api_prefix :=  printf "%s.api." (snake .Module.Name ) }}
import {{snake .Module.Name }}.api
import logging

{{- define "get_converter_module"}}
            {{- $module_prefix:= printf "%s.api" (snake .Module.Name ) }}
            {{- if .IsPrimitive }}
            {{- $module_prefix = "utils.base_types" }}
            {{- end}}
            {{- if (ne .Import "") }}
            {{- $module_prefix = printf "%s.api" (snake .Import ) }}
            {{- end}}
            {{- $module_prefix -}}
{{- end}}
{{- define "get_serialization_name" }}
            {{- $name:= snake .Type }}
            {{- if (eq .KindType "extern") }}
            {{- $name = snake (pyReturn "" .) }}
            {{- end}}
            {{- $name -}}
{{- end}}

{{- $system := .System}}
{{- range .Module.Imports }}
{{- $current_import := .}} 
import {{.Name}}.api 
{{- range $system.Modules }}
    {{- if (eq .Name $current_import.Name) }}
    {{- range .Externs }}
    {{- $extern := pyExtern . }}
import {{$extern.Import}} 
    {{- end }}
    {{- end }}
{{- end }}
{{- end }}


{{- $m := .Module }}
{{- range .Module.Interfaces }}
{{- $i := . }}
{{- $id := printf "%s.%s" $m.Name $i.Name }}

class {{Camel .Name}}Sink(IObjectSink):
    def __init__(self):
        super().__init__()
{{- range .Properties }}
        self._{{snake .Name}} = {{pyDefault $current_module_api_prefix .}}
        self.on_{{snake .Name}}_changed = EventHook()
{{- end }}
{{- range .Signals }}
        self.on_{{snake .Name}} = EventHook()
{{- end }}
        self._on_is_ready= EventHook()
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
        self.client.set_remote_property('{{$id}}/{{.Name}}', [{{ template "get_converter_module" .}}.from_{{template "get_serialization_name" .}}(_) for _ in value])
        {{- else }}
        self.client.set_remote_property('{{$id}}/{{.Name}}', value)
        {{- end }}
    {{- end }}

    def get_{{snake .Name}}(self):
        return self._{{snake .Name}}

    {{- end }}

    {{- range .Operations }}

    async def {{snake .Name}}({{pyParams $current_module_api_prefix .Params}}):
        {{- range $idx, $_ := .Params }}
        {{- if .IsArray }}
        _{{snake .Name}} = [{{template "get_converter_module" .}}.from_{{template "get_serialization_name" .}}({{snake .Type}}) for {{snake .Type}} in {{snake .Name}}]
        {{- else }}
        _{{snake .Name}} = {{template "get_converter_module" .}}.from_{{template "get_serialization_name" .}}({{snake .Name}})
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
                v = [{{template "get_converter_module" .}}.as_{{template "get_serialization_name" .}}(_) for _ in props[k]]
                {{- else }}
                v =  {{template "get_converter_module" .}}.as_{{template "get_serialization_name" .}}(props[k])
                {{- end }}
                self._set_{{snake .Name}}(v)
        {{- end }}
        {{- end }}
        self._on_is_ready.fire()

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
            v = [{{template "get_converter_module" .}}.as_{{template "get_serialization_name" .}}(_) for _ in value]
            {{- else }}
            v =  {{template "get_converter_module" .}}.as_{{template "get_serialization_name" .}}(value)
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
            {{snake .Name}} = [{{template "get_converter_module" .}}.as_{{template "get_serialization_name" .}}(_) for _ in args[{{$index}}]]
            {{- else }}
            {{snake .Name}} =  {{template "get_converter_module" .}}.as_{{template "get_serialization_name" .}}(args[{{$index}}])
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
