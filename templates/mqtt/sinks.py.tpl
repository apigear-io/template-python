import asyncio
from typing import Any
import apigear.mqtt
from utils.eventhook import EventHook
import utils.base_types
{{- $current_module_api_prefix :=  printf "%s.api." (snake .Module.Name ) }}
import {{snake .Module.Name }}.api
import logging

{{- $system := .System}}
{{- $imports := getEmptyStringList }}
{{- range .Module.Imports }}
{{- $current_import := .}} 
{{- $import_name := printf "%s.api" .Name }} 
{{- $imports = (appendList $imports $import_name) }}
{{- range $system.Modules }}
    {{- if (eq .Name $current_import.Name) }}
    {{- range .Externs }}
    {{- $extern := pyExtern . }}
    {{- $imports = (appendList $imports $extern.Import) }}
    {{- end }}
    {{- end }}
{{- end }}
{{- end }}
{{- range .Module.Externs }}
{{- $extern := pyExtern . }}
{{- $imports = (appendList $imports $extern.Import) }}
{{- end }}

{{- $imports = unique $imports }}
{{- range $imports }}
import {{.}}
{{- end }}


{{- $m := .Module }}
{{- range .Module.Interfaces }}
{{- $interfaceName := .Name }}

class {{Camel .Name}}ClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
    {{- range .Properties }}
        self._{{snake .Name}} = {{pyDefault $current_module_api_prefix .}}
        self.on_{{snake .Name}}_changed = EventHook()
    {{- end }}
    {{- range .Signals }}
        self.on_{{snake .Name}} = EventHook()
    {{- end }}
        self.client.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        {{- range .Properties }}
        self.client.subscribe_for_property("{{$.Module.Name}}/{{$interfaceName}}/prop/{{.Name}}", self.__set_{{snake .Name}})
        {{- end }}
        {{- range .Signals }}
        self.client.subscribe_for_signal("{{$.Module.Name}}/{{$interfaceName}}/sig/{{.Name}}",  self.__on_{{snake .Name}}_signal)
        {{- end }}
        #TODO SUBSCRIBE FOR INVOKE RESP TOPIC

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        {{- range .Properties }}
        self.client.unsubscribe("{{$.Module.Name}}/{{$interfaceName}}/prop/{{.Name}}")
        {{- end }}
        {{- range .Signals }}
        self.client.unsubscribe("{{$.Module.Name}}/{{$interfaceName}}/sig/{{.Name}}")
        {{- end }}
        #TODO UNSUBSCRIBE INVOKE RESP TOPIC

    {{- range .Properties }}
    {{- if not .IsReadOnly }}

    def set_{{snake .Name}}(self, value):
        if self._{{snake .Name}} == value:
            return
        topic = "{{.Module.Name}}/{{$interfaceName}}/set/{{.Name}}"
        {{- if .IsArray }}
        self.client.set_remote_property(topic, [{{ template "get_converter_module" .}}.from_{{template "get_serialization_name" .}}(_) for _ in value])
        {{- else }}
        self.client.set_remote_property(topic, {{ template "get_converter_module" .}}.from_{{template "get_serialization_name" .}}(value))
        {{- end }}
    {{- end }}

    def get_{{snake .Name}}(self):
        return self._{{snake .Name}}

    {{- end }}

    # internal functions on message handle
    {{- range .Properties }}

    def __set_{{snake .Name}}(self, data):
        {{- if .IsArray }}
        value = [{{template "get_converter_module" .}}.as_{{template "get_serialization_name" .}}(_) for _ in data]
        {{- else }}
        value =  {{template "get_converter_module" .}}.as_{{template "get_serialization_name" .}}(data)
        {{- end }}
        if self._{{snake .Name}} == value:
            return
        self._{{snake .Name}} = value
        self.on_{{snake .Name}}_changed.fire(self._{{snake .Name}})
    {{- end }}

    {{- range $idx, $o := .Signals }}

    def __on_{{snake .Name}}_signal(self, args: list[Any]):
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

{{- end}}
