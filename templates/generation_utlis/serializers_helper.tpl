{{- define "get_converter_module"}}
            {{- $module_prefix:= printf "%s.api" (snake .Module.Name ) }}
            {{- if .IsPrimitive }}
            {{- $module_prefix = "utils.base_types" }}
            {{- end}}
            {{- if (ne .Import "") }}
            {{- $module_prefix = printf "%s.api" (snake .Import ) }}
            {{- end}}
            {{- $module_prefix -}}
{{- end}}
{{- define "get_serialization_name" }}
            {{- $name:= snake .Type }}
            {{- if (eq .KindType "extern") }}
            {{- $name = snake (pyReturn "" .) }}
            {{- end}}
            {{- $name -}}
{{- end}}
