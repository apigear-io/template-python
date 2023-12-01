from olink.core import Name
from olink.remote import IObjectSource, RemoteNode
from {{snake .Module.Name}}_api import api
from typing import Any
import logging

{{- range .Module.Interfaces }}
{{- $class := Camel .Name }}
{{- $id := printf "%s.%s" $.Module.Name .Name }}
class {{$class}}Source(IObjectSource):
    impl: api.I{{$class}}
    def __init__(self, impl: api.I{{$class}}):
        self.impl = impl
        impl._notifier = self
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
            v = api.as_{{snake .Type}}(value)
            return self.impl.set_{{snake .Name}}(v)
        {{- else }}
            pass
        {{- end }}
{{- end }}
        logging.info("unknown property: %s", name)


    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
{{- range $idx, $o := .Operations }}
    {{- if $idx }}
        elif path == "{{.Name}}":
    {{- else }}
        if path == "{{.Name}}":
    {{- end }}
        {{- range $idx, $_ := .Params }}
            {{snake .Name}} = api.as_{{snake .Type}}(args[{{$idx}}])
        {{- end }}
            reply = self.impl.{{snake .Name}}({{pyVars .Params}})
        {{- if .Return.IsVoid }}
            return None
        {{- else }}
            return api.from_{{snake .Return.Type}}(reply)
        {{- end }}
{{- end }}      
        logging.info("unknown operation: %s", name)

    def olink_linked(self, name: str, node: "RemoteNode"):
        print('linked')

    def olink_collect_properties(self) -> object:
        props = {}
        {{- range .Properties }}
        v = self.impl.get_{{snake .Name}}()
        props["{{.Name }}"] = api.from_{{snake .Type}}(v)
        {{- end }}
        return props

    def notify_signal(self, symbol, args):
        path = Name.path_from_name(symbol)
{{- range $idx, $s := .Signals }}
    {{- if $idx }}
        elif path == "{{.Name}}":
    {{- else }}
        if path == "{{.Name}}":
    {{- end }}
        {{- range $idx, $_ := .Params }}
            {{snake .Name}} = api.from_{{snake .Type}}(args[{{$idx}}])
        {{- end }}
            return RemoteNode.notify_signal(symbol, [{{pyVars .Params}}])    
{{- end }}
        logging.info("unknown signal %s", symbol)

    def notify_property(self, symbol, value):
        path = Name.path_from_name(symbol)
{{- range $idx, $p := .Properties }}
    {{- if $idx }}
        elif path == "{{.Name}}":
    {{- else }}
        if path == "{{.Name}}":
    {{- end }}
            v = api.from_{{snake .Type}}(value)
            return RemoteNode.notify_property_change(symbol, value)
{{- end }}
        logging.info("unknown property %s", symbol)    
{{- end }}