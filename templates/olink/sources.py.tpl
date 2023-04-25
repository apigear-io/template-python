from olink.core.types import Name
from olink.remotenode import IObjectSource, RemoteNode
from {{snake .Module.Name}}_api import api
from typing import Any

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
        self.impl.set_property(path, value)

    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        func = getattr(self.impl, path)
        if not callable(func):
            raise Exception(f"not callable {name}")
        if args is None:
            return func()
        return func(*args)

    def olink_linked(self, name: str, node: "RemoteNode"):
        print('linked')

    def olink_collect_properties(self) -> object:
        props = {}
        {{- range .Properties }}
        props["{{.Name }}"] = self.impl.get_{{snake .Name}}()
        {{- end }}
        return props

    def notify_signal(self, symbol, args):
        RemoteNode.notify_signal(symbol, args)

    def notify_property(self, symbol, value):
        RemoteNode.notify_property_change(symbol, value)

    
{{- end }}