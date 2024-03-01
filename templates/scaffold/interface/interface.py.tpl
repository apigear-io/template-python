from {{ snake .Module.Name}}_api import api
from {{snake .Module.Name}}_api.shared import EventHook
from typing import Iterable
{{- $class := Camel .Interface.Name }}
{{- $ns := printf "%s.%s" $.Module.Name $.Interface.Name }}

class {{$class}}(api.I{{$class}}):
    def __init__(self, notifier=None):
        super().__init__()
        self._notifier = notifier
{{- range .Interface.Properties }}
        self._{{snake .Name}}: {{pyType "api." .}} = {{pyDefault "api." .}}
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
        self.push_{{snake .Name}}(self._{{snake .Name}})
    {{- end }}
    
    def get_{{snake .Name}}(self):
        return self._{{snake .Name}}        

    def push_{{snake .Name}}(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("{{$ns}}/{{.Name}}", value)
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
