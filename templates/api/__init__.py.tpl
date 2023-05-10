{{- range .Module.Enums }}
from .api import {{Camel  .Name }} as {{Camel  .Name }}
{{- end }}

{{- range .Module.Structs }}
from .api import {{Camel  .Name }} as {{Camel  .Name }}
{{- end }}

{{- range .Module.Interfaces }}
from .api import I{{Camel  .Name }} as I{{Camel  .Name }}
{{- end }}