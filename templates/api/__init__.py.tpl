{{- range .Module.Enums }}
from .api import {{Camel  .Name }} as {{Camel  .Name }}
from .api import as_{{snake .Name}} as as_{{snake .Name}}
from .api import from_{{snake .Name}} as from_{{snake .Name}}
{{- end }}

{{- range .Module.Structs }}
from .api import {{Camel  .Name }} as {{Camel  .Name }}
from .api import as_{{snake .Name}} as as_{{snake .Name}}
from .api import from_{{snake .Name}} as from_{{snake .Name}}
{{- end }}

{{- range .Module.Interfaces }}
from .api import I{{Camel  .Name }} as I{{Camel  .Name }}
{{- end }}
