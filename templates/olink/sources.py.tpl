from olink.core.types import Name
from olink.remotenode import IObjectSource, RemoteNode
from {{snake .Module.Name}}_api import api
from typing import Any
import logging

{{- range .Module.Interfaces }}
{{- $class := Camel .Name }}

class {{$class}}Source(IObjectSource):
    impl: api.I{{$class}}
    def __init__(self, impl: api.I{{$class}}):
        self.impl = impl
        impl._notifier = self
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "{{$.Module.Name}}.{{.Name}}"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        match path:
{{- range .Properties }}
            case "{{.Name}}":
                v = api.as_{{snake .Type}}(value)
                self.impl.set_{{snake .Name}}(v)
{{- end }}

    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        match path:
{{- range .Operations }}
            case "{{.Name}}":
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
            case _:
                logging.info("unknown operation")
                return None

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
        match path:
{{- range .Signals }}
            case "{{.Name}}":
            {{- range $idx, $_ := .Params }}
                {{snake .Name}} = api.from_{{snake .Type}}(args[{{$idx}}])
            {{- end }}
                RemoteNode.notify_signal(symbol, [{{pyVars .Params}}])    
{{- end }}
            case _:
                logging.info("unknown signal %s", symbol)

    def notify_property(self, symbol, value):
        path = Name.path_from_name(symbol)
        match path:
{{- range .Properties }}
            case "{{.Name}}":
                v = api.from_{{snake .Type}}(value)
{{- end }}
                RemoteNode.notify_property_change(symbol, value)
            case _:
                logging.info("unknown property %s", symbol)

    
{{- end }}