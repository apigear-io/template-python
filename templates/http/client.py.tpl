import requests
import os

from {{snake .Module.Name}}_api import api
from . import shared

{{ $module := .Module }}
{{- range .Module.Interfaces }}
{{ $iface := . }}
class {{Camel .Name}}(api.I{{Camel .Name}}):
    def __init__(self, url='http://localhost:8000'):
        super().__init__()
        self._url = url
{{- range .Properties }}        
        self._{{snake .Name}} = {{pyDefault "" .}}
{{- end }}
{{- range .Properties }}
    
    def get_{{snake .Name}}(self):
        return self._{{snake .Name}}

    def set_{{snake .Name}}(self, value):
        self._{{snake .Name}} = value
{{- end }}
{{- range .Operations }}
    def {{snake .Name}}({{pyParams "" .Params}}):
        req = shared.{{$iface.Name}}{{Camel .Name}}Request(
    {{- range $idx, $el := .Params }}
            {{if $idx}}, {{end}}{{.Name}}={{.Name}}
    {{- end }}
        )
        data = requests.post(
            f'{self.url}/{{$module.Name}}/{{$iface.Name}}/{{.Name}}',
            req.json()
        )
        resp = shared.{{Camel $iface.Name}}{{Camel .Name}}Response(**data.json())
        print(resp.json())
{{- range $iface.Properties }}
        self._{{snake .Name}} = resp.state.{{snake .Name}}
{{- end }}

{{- end }}
{{- end }}
