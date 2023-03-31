import asyncio
from typing import Any
from olink.core import Name, EventHook
from olink.client import IObjectSink, ClientNode
from {{snake .Module.Name}} import api

{{- range .Module.Interfaces }}

class {{Camel .Name}}Sink(IObjectSink):
{{- range .Properties }}
    {{snake .Name}} = {{pyDefault ".api" .}}
{{- end }}
    on_property_changed = EventHook()
{{- range .Signals }}
    on_{{snake .Name}} = EventHook()
{{- end }}

    client = None

    def __init__(self):
        self.client = ClientNode.register_sink(self)

    async def _invoke(self, name, args):
        future = asyncio.get_running_loop().create_future()
        def func(args):
            return future.set_result(args.value)
        self.client.invoke_remote(f'{{dot $.Module.Name}}.{{.Name}}/{name}', args, func)
        return await asyncio.wait_for(future, 500)

{{- range .Operations }}

    async def {{snake .Name}}({{pyParams ".api" .}}):
        return await self._invoke('{{camel .Name}}', [{{ pyVars ".api" .Params }}])

{{- end }}

    def olink_object_name(self):
        return '{{dot $.Module.Name}}.{{Camel .Name}}'

    def olink_on_init(self, name: str, props: object, node: ClientNode):
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