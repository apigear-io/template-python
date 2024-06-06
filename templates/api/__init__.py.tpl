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

{{- range .Module.Externs }}
{{- $extern := pyExtern . }}
{{- $func_name:= printf "%s_%s" (snake $extern.Import) (snake $extern.Name )}}
from .api import as_{{$func_name}} as as_{{$func_name}}
from .api import from_{{$func_name}} as from_{{$func_name}}
{{- end }}
