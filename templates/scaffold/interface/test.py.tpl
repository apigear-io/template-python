{{- $class := Camel .Interface.Name }}
from {{snake .Module.Name}}.api import api
from {{snake .Module.Name}}.impl import {{$class}}

{{- $system := .System}}
{{- $imports := getEmptyStringList }}
{{- range .Module.Imports }}
    {{- $current_import := .}} 
    {{- $import_name := printf "%s.api" (snake .Name) }} 
    {{- $imports = (appendList $imports $import_name) }}
        {{- range $system.Modules }}
            {{- if (eq .Name $current_import.Name) }}
                {{- range .Externs }}
                    {{- $extern := pyExtern . }}
                    {{- $imports = (appendList $imports $extern.Import) }}
                {{- end }}
            {{- end }}
    {{- end }}
{{- end }}
{{- range .Module.Externs }}
    {{- $extern := pyExtern . }}
    {{- $imports = (appendList $imports $extern.Import) }}
{{- end }}

{{- $imports = unique $imports }}
{{- range $imports }}
import {{.}}
{{- end }}

class Test{{$class}}:
{{- range .Interface.Properties }}

    def test_{{snake .Name}}(self):
        o = {{$class}}()
        {{- if not .IsReadOnly }}
        self.called = False
        o.on_{{snake .Name}}_changed += lambda *args: setattr(self, 'called', True)
        o.set_{{snake .Name}}({{ pyDefault "api." .}})
        # should not be true since we are not changing the default value
        assert self.called == False
        {{- end }}
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

{{- range .Interface.Signals }}

    def test_{{snake .Name}}(self):
        o = {{$class}}()
        self.called = False
        o.on_{{snake .Name}} += lambda *args: setattr(self, 'called', True)
        o._{{snake .Name}}(
    {{- range $idx, $p := .Params -}}
            {{- if $idx }}, {{end -}}
            {{ pyDefault "api." .}}
    {{- end -}}
        )
        assert self.called == True
{{- else }}
    pass
{{- end }}
