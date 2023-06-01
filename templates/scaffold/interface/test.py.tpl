{{- $class := Camel .Interface.Name }}
from {{snake .Module.Name}}_api import api
from {{snake .Module.Name}}_impl import {{$class}}

class Test{{$class}}:
{{- range .Interface.Properties }}

    def test_{{snake .Name}}(self):
        o = {{$class}}()
        o.set_{{snake .Name}}({{ pyDefault "api." .}})
        assert o.get_{{snake .Name}}() == {{ pyDefault "api." .}}
{{- else }}
    pass
{{- end }}

{{- range .Interface.Operations }}

    def test_{{snake .Name}}(self):
        o = {{$class}}()
        o.{{snake .Name}}(
    {{- range $idx, $p := .Params -}}
            {{- if $idx }}, {{end -}}
            {{snake .Name}}={{ pyDefault "api." .}}
    {{- end -}}
        )
{{- else }}
    pass
{{- end }}

