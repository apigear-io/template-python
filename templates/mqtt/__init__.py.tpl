{{- range .Module.Interfaces }}
from .sources import {{Camel .Name}}ServiceAdapter as {{Camel .Name}}ServiceAdapter
from .sinks import {{Camel .Name}}ClientAdapter as {{Camel .Name}}ClientAdapter
{{- end }}
