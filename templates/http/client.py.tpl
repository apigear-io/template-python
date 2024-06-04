import requests
import os

from {{snake .Module.Name}}.api import api
from . import shared

{{ $module := .Module }}
{{- range .Module.Interfaces }}
{{ $i := . }}
class {{Camel .Name}}(api.I{{Camel .Name}}):
    def __init__(self, url='http://localhost:8000'):
        super().__init__()
        self._url = url
{{- range .Properties }}        
        self._{{snake .Name}} = {{pyDefault "api." .}}
{{- end }}
{{- range .Properties }}
    
    def get_{{snake .Name}}(self):
        return self._{{snake .Name}}
    {{- if not .IsReadOnly }}

    def set_{{snake .Name}}(self, value):
        self._{{snake .Name}} = value
    {{- end }}
{{- end }}
{{- range .Operations }}

    def {{snake .Name}}({{pyParams "api." .Params}}):
        req = shared.{{$i.Name}}{{Camel .Name}}Request(
    {{- range $idx, $el := .Params }}
            {{if $idx}}, {{end}}{{snake .Name}}={{snake .Name}}
    {{- end }}
        )
        data = requests.post(
            f'{self.url}/{{snake $module.Name}}/{{snake $i.Name}}/{{snake .Name}}',
            req.json()
        )
        resp = shared.{{Camel $i.Name}}{{Camel .Name}}Response(**data.json())
{{- range $i.Properties }}
        self._{{snake .Name}} = resp.state.{{snake .Name}}
{{- end }}

{{- end }}
{{- end }}
