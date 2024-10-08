from olink.core import Name
from olink.remote import IObjectSource, RemoteNode
import utils.base_types
{{- $current_module_api_prefix :=  printf "%s.api." (snake .Module.Name ) }}
import {{snake .Module.Name }}.api
from utils.eventhook import EventHook
from typing import Any
import logging

{{- $system := .System}}
{{- $imports := getEmptyStringList }}
{{- range .Module.Imports }}
{{- $current_import := .}} 
{{- $import_name := printf "%s.api" (snake .Name) }} 
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

{{- range .Module.Interfaces }}
{{- $ns := printf "%s.%s" $.Module.Name .Name -}}
{{- $class := Camel .Name }}
{{- $id := printf "%s.%s" $.Module.Name .Name }}
class {{$class}}Source(IObjectSource):
    impl: {{$current_module_api_prefix}}I{{$class}}
    def __init__(self, impl: {{$current_module_api_prefix}}I{{$class}}):
        self.impl = impl
{{- range $idx, $p := .Properties }}
        impl.on_{{snake .Name}}_changed += self.notify_{{snake .Name}}_changed
{{- end }}
{{- range $idx, $s := .Signals }}
        impl.on_{{snake .Name}} += self.notify_{{snake .Name}}
{{- end }}
        self._on_linked = EventHook()
        self._on_unlinked = EventHook()
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "{{$id}}"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
{{- range $idx, $p := .Properties }}
    {{- if $idx }}
        elif path == "{{.Name}}":
    {{- else }}
        if path == "{{.Name}}":
    {{- end }}
        {{- if not .IsReadOnly }}
            {{- if .IsArray }}
            v = [{{template "get_converter_module" .}}.as_{{template "get_serialization_name" .}}(_) for _ in value]
            {{- else }}
            v = {{template "get_converter_module" .}}.as_{{template "get_serialization_name" .}}(value)
            {{- end }}
            return self.impl.set_{{snake .Name}}(v)
        {{- else }}
            pass
        {{- end }}
{{- end }}
        logging.error("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
{{- range $idx, $o := .Operations }}
    {{- if $idx }}
        elif path == "{{.Name}}":
    {{- else }}
        if path == "{{.Name}}":
    {{- end }}
        {{- range $idx, $_ := .Params }}
            {{- if .IsArray }}
            {{snake .Name}} = [{{template "get_converter_module" .}}.as_{{template "get_serialization_name" .}}(_) for _ in args[{{$idx}}]]
            {{- else }}
            {{snake .Name}} = {{template "get_converter_module" .}}.as_{{template "get_serialization_name" .}}(args[{{$idx}}])
            {{- end }}
        {{- end }}
            reply = self.impl.{{snake .Name}}({{pyVars .Params}})
        {{- if .Return.IsVoid }}
            return utils.base_types.from_int(0)   
        {{- else }}
            {{- if .Return.IsArray }}
            return [{{template "get_converter_module" .Return}}.from_{{template "get_serialization_name" .Return}}(_) for _ in reply]
            {{- else }}
            return {{template "get_converter_module" .Return}}.from_{{template "get_serialization_name" .Return}}(reply)
            {{- end }}
        {{- end }}
{{- end }}      
        logging.error("unknown operation: %s", name)

    def olink_linked(self, name: str, node: "RemoteNode"):
        logging.info("linked: %s", name)
        self._on_linked.fire(name)

    def olink_unlinked(self, name: str, node: "RemoteNode"):
        logging.info("unlinked: %s", name)
        self._on_unlinked.fire(name)

    def olink_collect_properties(self) -> object:
        props = {}
        {{- range .Properties }}
        v = self.impl.get_{{snake .Name}}()
        {{- if .IsArray }}
        props["{{.Name }}"] = [{{template "get_converter_module" .}}.from_{{template "get_serialization_name" .}}(_) for _ in v]
        {{- else }}
        props["{{.Name }}"] = {{template "get_converter_module" .}}.from_{{template "get_serialization_name" .}}(v)
        {{- end }}
        {{- end }}
        return props

{{- range $idx, $s := .Signals }}

    def notify_{{snake .Name}}({{pyParams $current_module_api_prefix .Params}}):
        {{- range $idx, $_ := .Params }}
        {{- if .IsArray }}
        _{{snake .Name}} = [{{template "get_converter_module" .}}.from_{{template "get_serialization_name" .}}(_) for _ in {{snake .Name}}]
        {{- else }}
        _{{snake .Name}} = {{template "get_converter_module" .}}.from_{{template "get_serialization_name" .}}({{snake .Name}})
        {{- end }}
        {{- end }}
        return RemoteNode.notify_signal("{{$ns}}/{{.Name}}", [
            {{- range $idx, $_ := .Params -}}{{- if $idx}}, {{ end -}}
            _{{snake .Name}}
            {{- end -}}
        ])
{{- end }}

{{- range $idx, $p := .Properties }}

    def notify_{{snake .Name}}_changed(self, value):
        {{- if .IsArray }}
        v = [{{template "get_converter_module" .}}.from_{{template "get_serialization_name" .}}(_) for _ in value]
        {{- else }}
        v = {{template "get_converter_module" .}}.from_{{template "get_serialization_name" .}}(value)
        {{- end }}
        return RemoteNode.notify_property_change("{{$ns}}/{{.Name}}", v)
{{- end }}

{{- end }}
