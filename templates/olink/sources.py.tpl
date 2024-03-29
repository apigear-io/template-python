from olink.core import Name
from olink.remote import IObjectSource, RemoteNode
from {{snake .Module.Name}}_api import api
from typing import Any
import logging

{{- range .Module.Interfaces }}
{{- $ns := printf "%s.%s" $.Module.Name .Name -}}
{{- $class := Camel .Name }}
{{- $id := printf "%s.%s" $.Module.Name .Name }}
class {{$class}}Source(IObjectSource):
    impl: api.I{{$class}}
    def __init__(self, impl: api.I{{$class}}):
        self.impl = impl
{{- range $idx, $p := .Properties }}
        impl.on_{{snake .Name}}_changed += self.notify_{{snake .Name}}_changed
{{- end }}
{{- range $idx, $s := .Signals }}
        impl.on_{{snake .Name}} += self.notify_{{snake .Name}}
{{- end }}
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
            v = [api.as_{{snake .Type}}(_) for _ in value]
            {{- else }}
            v = api.as_{{snake .Type}}(value)
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
            {{snake .Name}} = [api.as_{{snake .Type}}(_) for _ in args[{{$idx}}]]
            {{- else }}
            {{snake .Name}} = api.as_{{snake .Type}}(args[{{$idx}}])
            {{- end }}
        {{- end }}
            reply = self.impl.{{snake .Name}}({{pyVars .Params}})
        {{- if .Return.IsVoid }}
            return None
        {{- else }}
            return api.from_{{snake .Return.Type}}(reply)
        {{- end }}
{{- end }}      
        logging.error("unknown operation: %s", name)

    def olink_linked(self, name: str, node: "RemoteNode"):
        logging.info("linked: %s", name)

    def olink_collect_properties(self) -> object:
        props = {}
        {{- range .Properties }}
        v = self.impl.get_{{snake .Name}}()
        {{- if .IsArray }}
        props["{{.Name }}"] = [api.from_{{snake .Type}}(_) for _ in v]
        {{- else }}
        props["{{.Name }}"] = api.from_{{snake .Type}}(v)
        {{- end }}
        {{- end }}
        return props

{{- range $idx, $s := .Signals }}

    def notify_{{snake .Name}}({{pyParams "api." .Params}}):
        {{- range $idx, $_ := .Params }}
        {{- if .IsArray }}
        _{{snake .Name}} = [api.from_{{snake .Type}}(_) for _ in {{snake .Name}}]
        {{- else }}
        _{{snake .Name}} = api.from_{{snake .Type}}({{snake .Name}})
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
        v = [api.from_{{snake .Type}}(_) for _ in value]
        {{- else }}
        v = api.from_{{snake .Type}}(value)
        {{- end }}
        return RemoteNode.notify_property_change("{{$ns}}/{{.Name}}", v)
{{- end }}

{{- end }}
