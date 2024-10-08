import requests
import os

from {{snake .Module.Name}}.api import api
from . import shared

{{- $system := .System}}
{{- $imports := getEmptyStringList }}
{{- range .Module.Imports }}
{{- $current_import := .}} 
{{- $import_name := printf "%s.api" (snake .Name) }} 
{{- $imports = (appendList $imports $import_name) }}
{{- range $system.Modules }}
    {{- if (eq .Name $current_import.Name) }}
    {{- range .Externs }}
    {{- $extern := pyExtern . }}
    {{- $imports = (appendList $imports $extern.Import) }}
    {{- end }}
    {{- end }}
{{- end }}
{{- end }}
{{- range .Module.Externs }}
{{- $extern := pyExtern . }}
{{- $imports = (appendList $imports $extern.Import) }}
{{- end }}

{{- $imports = unique $imports }}
{{- range $imports }}
import {{.}}
{{- end }}

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
