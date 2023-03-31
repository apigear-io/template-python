from {{ snake .Module.Name}} import api
from typing import Iterable
{{- $class := .Interface.Name }}

class {{$class}}(api.{{$class}}):
{{- range .Interface.Properties }}
    {{snake .Name}}: {{pyType "api." .}} = {{pyDefault "api." .}}
{{- end }}

{{- range .Interface.Operations }}

    def {{.Name}}({{pyParams "api." .Params}}) -> {{pyReturn "api." .Return}}:
        return {{pyDefault "api." .Return}}    
{{- end }}