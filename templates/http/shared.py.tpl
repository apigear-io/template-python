from pydantic import BaseModel, Field
from typing import Iterable
from {{dot .Module.Name}}_api import api

{{- range .Module.Interfaces }}
{{ $iface := . }}
class {{Camel .Name}}State(BaseModel):
{{- range .Properties }}
    {{snake .Name }}: {{pyType "api." .}} = Field(default={{pyDefault "api." .}}, alias="{{.Name}}")
{{- else }}
    pass
{{- end }}

{{- range .Operations }}

# method {{$iface.Name}}.{{.Name}}
class {{$iface.Name}}{{Camel .Name}}Request(BaseModel):
{{- range .Params }}
    {{snake .Name }}: {{pyType "api." .}} = Field(default={{pyDefault "api." .}}, alias="{{.Name}}")
{{- else }}
    pass
{{- end }} {{/* range .Params */}}

class {{$iface.Name}}{{Camel .Name}}Response(BaseModel):
    result: {{pyReturn "api." .Return}}
    state: {{$iface.Name}}State
{{- end }} 
{{- end }}



