from {{ snake .Module.Name}}_api import api
from typing import Iterable
{{- $class := .Interface.Name }}

class {{$class}}(api.I{{$class}}):
    def __init__(self, notifier=None):
        super().__init__()
        self._notifier = notifier
{{- range .Interface.Properties }}
        self._{{snake .Name}}: {{pyType "api." .}} = {{pyDefault "api." .}}
{{- end }}

{{- range .Interface.Properties }}

    def set_{{snake .Name}}(self, value):
        if self._{{snake .Name}} == value:
            return
        self._{{snake .Name}} = value
    
    def get_{{snake .Name}}(self):
        return self._{{snake .Name}}        

    def push_{{snake .Name}}(self, value):
        if not self._notifier:
            return
        self._notifier.notify_property("{{$.Module.Name}}.{{$.Interface.Name}}/{{.Name}}", value)
{{- end }}

{{- range .Interface.Operations }}

    def {{snake .Name}}({{pyParams "api." .Params}}) -> {{pyReturn "api." .Return}}:
        raise NotImplementedError()
{{- end }}

{{- range .Interface.Signals }}

    def {{snake .Name}}({{pyParams "api." .Params }}):
        if not self._notifier:
            return
        self._notifier.notify_signal("{{$.Module.Name}}.{{$.Interface.Name}}/{{.Name}}", [{{pyVars .Params}}])
{{- end }}
