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
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "{{$.Module.Name}}.{{.Name}}"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        self.impl.set_property(path, value)

    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        func = getattr(self.impl, path)
        return func(*args)

    def olink_linked(self, name: str, node: "RemoteNode"):
        print('linked')

    def olink_collect_properties(self) -> object:
        props = {}
        {{- range .Properties }}
        props["{{.Name }}"] = self.impl.get_{{snake .Name}}()
        {{- end }}
        return props
{{- end }}