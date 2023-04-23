{{- range .Module.Interfaces }}
from .sources import {{Camel .Name}}Source as {{Camel .Name}}Source
from .sinks import {{Camel .Name}}Sink as {{Camel .Name}}Sink
from .services import {{Camel .Name}}Service as {{Camel .Name}}Service
{{- end }}