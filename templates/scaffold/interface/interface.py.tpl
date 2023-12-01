from {{ snake .Module.Name}}_api import api
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

    def {{snake .Name}}({{pyParams "api." .Params }}):
        if not self._notifier:
            return
        self._notifier.notify_signal("{{$ns}}/{{.Name}}", [{{pyVars .Params}}])
{{- end }}
