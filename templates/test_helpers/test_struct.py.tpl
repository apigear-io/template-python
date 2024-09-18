import {{snake .Module.Name}}.api
{{- $system := .System}}
{{- $imports := getEmptyStringList }}
{{- range .Module.Imports }}
    {{- $current_import := .}} 
    {{- $import_name := printf "%s.api" (snake .Name) }} 
    {{- $imports = (appendList $imports $import_name) }}
    {{- $import_test_structs := printf "%s.test_helpers.test_struct" (snake .Name) }} 
    {{- $imports = (appendList $imports $import_test_structs) }}
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

{{- $apiPrefix := printf "%s.api." (snake .Module.Name) }}
{{- range .Module.Structs }}
	{{- $structName := printf "test_%s" (snake .Name)}}

def fillTest{{Camel .Name }}({{$structName}}):
{{- range .Fields }}
	{{- if .IsArray }}
	local_{{snake .Name}}_array = {{ pyDefault $apiPrefix . }}
	{{- if not ( or (eq .KindType "extern") ( or .IsPrimitive  (eq .KindType "enum") ) )}}
	element{{snake .Name}} = fillTest{{.Type}}({{ pyDefault $apiPrefix . }} )
	{{- else}}
	element{{snake .Name}} = {{ pyTestValue $apiPrefix . }}
	{{- end }}
	local_{{snake .Name}}_array.append(element{{snake .Name}})
	{{$structName}}.{{snake .Name }} = local_{{snake .Name}}_array
	{{- else if not ( or (eq .KindType "extern") ( or .IsPrimitive  (eq .KindType "enum") ) )}}
	{{$structName}}.{{snake .Name }} = fillTest{{.Type}}({{ pyDefault $apiPrefix . }});
	{{- else }}
	{{$structName}}.{{snake .Name }} = {{ pyTestValue $apiPrefix . }};
	{{- end }}
{{- end }}
	return {{$structName}}

{{- end }}
