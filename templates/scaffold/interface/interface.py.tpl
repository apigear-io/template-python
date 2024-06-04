from {{ snake .Module.Name}}.api import api
from utils.eventhook import EventHook
from typing import Iterable

{{- $class := Camel .Interface.Name }}

class {{$class}}(api.I{{$class}}):
    def __init__(self):
        super().__init__()
{{- range .Interface.Properties }}
        self._{{snake .Name}}: {{pyType "api." .}} = {{pyDefault "api." .}}
{{- end }}
{{- range .Interface.Properties }}
        self.on_{{snake .Name}}_changed: {{pyType "api." .}} = EventHook()
{{- end }}
{{- range .Interface.Signals }}
        self.on_{{snake .Name}} = EventHook()
{{- end }}

{{- range .Interface.Properties }}
    {{- if not .IsReadOnly }}

    def set_{{snake .Name}}(self, value):
        if self._{{snake .Name}} == value:
            return
        self._{{snake .Name}} = value
        self._push_{{snake .Name}}(self._{{snake .Name}})
    {{- end }}
    
    def get_{{snake .Name}}(self):
        return self._{{snake .Name}}        

    def _push_{{snake .Name}}(self, value):
        self.on_{{snake .Name}}_changed.fire(value)
{{- end }}

{{- range .Interface.Operations }}

    def {{snake .Name}}({{pyParams "api." .Params}}) -> {{pyReturn "api." .Return}}:
    {{- if .Return.IsVoid}}
        return None
    {{- else }}
        return {{pyDefault "api." .Return}}
    {{- end }}
{{- end }}

{{- range .Interface.Signals }}

    def _{{snake .Name}}({{pyParams "api." .Params }}):
        self.on_{{snake .Name}}.fire({{pyVars .Params}})
{{- end }}
