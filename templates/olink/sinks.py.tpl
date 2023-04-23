import asyncio
from typing import Any
from olink.core.types import Name
from olink.clientnode import IObjectSink, ClientNode
from .shared import EventHook
from {{snake .Module.Name}}_api import api


{{- $module := .Module }}
{{- range .Module.Interfaces }}
{{- $iface := . }}
{{- $id := printf "%s.%s" $module.Name $iface.Name }}
class {{Camel .Name}}Sink(IObjectSink):
    def __init__(self):
        super().__init__()
{{- range .Properties }}
        self.{{snake .Name}} = {{pyDefault "api." .}}
{{- end }}
        self.on_property_changed = EventHook()
{{- range .Signals }}
        self.{{snake .Name}} = EventHook()
{{- end }}
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote('{{$id}}/{{.Name}}', args, func)
        return await asyncio.wait_for(future, 500)

    {{- range .Operations }}
    async def {{snake .Name}}({{pyParams "api." .Params}}):
        return await self._invoke("{{.Name}}", [{{pyVars .Params}}])
    {{- end }}

    def olink_object_name(self):
        return '{{$id}}'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        for k in props:
            setattr(self, k, props[k])

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        setattr(self, path, value)
        self.on_property_changed.fire(path, value)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        hook = getattr(self, f'on_{path}')        
        hook.fire(*args)

{{- end }}