{{- range .Module.Interfaces }}
from .{{snake .Name}} import {{Camel .Name}} as {{Camel .Name}}
{{- end }}
