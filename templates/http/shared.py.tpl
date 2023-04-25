from pydantic import BaseModel
from typing import Iterable
from {{dot .Module.Name}}_api import api

{{- range .Module.Interfaces }}
{{ $iface := . }}
class {{Camel .Name}}State(BaseModel):
{{- range .Properties }}
    {{.Name}}: {{ pyReturn "api." . }}
{{- else }}
    pass
{{- end }}

{{- range .Operations }}

# method {{$iface.Name}}.{{.Name}}
class {{$iface.Name}}{{Camel .Name}}Request(BaseModel):
{{- range .Params }}
    {{.Name}}: {{ pyReturn "api." . }}
{{- else }}
    pass
{{- end }} {{/* range .Params */}}

class {{$iface.Name}}{{Camel .Name}}Response(BaseModel):
    result: {{pyReturn "api." .Return}}
    state: {{$iface.Name}}State
{{- end }} 
{{- end }}


