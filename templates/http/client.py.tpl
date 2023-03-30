import requests
import os

from {{dot .Module.Name}}.api import api
from . import shared


API_SERVER = os.getenv('API_SERVER', 'http://localhost:8000')

{{ $module := .Module }}
{{ range .Module.Interfaces }}
{{ $iface := . }}
class {{.Name}}(api.I{{.Name}}):
    def __init__(self):
        super().__init__()
{{- range .Properties }}        
        self._{{.Name}} = {{pyDefault "" .}}
{{- end }}
{{ range .Properties }}
    @property
    def {{.Name}}(self):
        return self._{{.Name}}
{{ end }}
{{- range .Operations }}
    def {{.Name}}({{pyParams "" .Params}}):
        req = shared.{{$iface.Name}}{{Camel .Name}}Request(
    {{- range $idx, $el := .Params }}
            {{if $idx}}, {{end}}{{.Name}}={{.Name}}
    {{- end }}
        )
        data = requests.post(
            f'{API_SERVER}/{{$module.Name}}/{{$iface.Name}}/{{.Name}}',
            req.json()
        )
        resp = shared.{{$iface.Name}}{{Camel .Name}}Response(**data.json())
        print(resp.json())
{{ range $iface.Properties }}
        self._{{.Name}} = resp.state.{{.Name}}
{{- end }}

{{ end }}
{{ end }}
