from olink.remotenode import RemoteNode

from {{snake .Module.Name}}_api import api

{{ $module := .Module }}
{{- range .Module.Interfaces }}
{{ $iface := . }}
class {{Camel .Name}}Service(object):
    def __init__(self):
        super().__init__()        
{{- range .Properties }}
        self.{{snake .Name}} = {{pyDefault "api." .}}
{{- end }}
{{- range .Properties }}
    def set_{{snake .Name}}(self, value):
        if value != self.{{snake .Name}}:
            self.{{snake .Name}} = value
            RemoteNode.notify_property_change('{{$module.Name}}.{{$iface.Name}}/{{.Name}}', value)                        
{{- end }}

{{- range .Operations }}
    def {{snake .Name}}({{pyParams "api." .Params }}):
        raise NotImplementedError()
{{- end }}

{{- range .Signals }}
    def {{snake .Name}}({{pyParams "api." .Params }}):
        RemoteNode.notify_signal('{{$module.Name}}.{{$iface.Name}}/{{.Name}}', [{{pyVars .Params}}])
{{- end }}

    async def run(self):
        pass

{{- end }}