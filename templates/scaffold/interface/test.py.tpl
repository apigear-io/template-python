{{- $class := Camel .Interface.Name }}
from {{snake .Module.Name}}_api import api
from {{snake .Module.Name}}_impl import {{$class}}

class Test{{$class}}:
{{- range .Interface.Operations }}

    def test_{{snake .Name}}(self):
        o = {{$class}}()
        o.{{snake .Name}}(
    {{- range .Params -}}
            {{ pyDefault "api." .}},
    {{- end -}}
        )
{{- else }}
    pass
{{- end }}

