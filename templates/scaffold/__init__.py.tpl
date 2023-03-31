{{- range .Module.Interfaces -}}
from .{{camel .Name}} import {{Camel .Name}}
{{- end }}
