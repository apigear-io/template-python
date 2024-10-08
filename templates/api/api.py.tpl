from pydantic import ConfigDict, BaseModel, Field
from enum import IntEnum
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

class EnhancedModel(BaseModel):
    """This model is used to enforce the json encoding by alias"""
    model_config = ConfigDict(populate_by_name=True)

    def model_dump(self, **kwargs):
        kwargs.setdefault('by_alias', True)
        return super().model_dump(**kwargs)

    def __init__(self, **kw):
        super().__init__(**kw)

{{- range .Module.Enums }}

class {{Camel .Name }}(IntEnum):
    {{- range .Members }}
    {{ SNAKE .Name }} = {{ .Value }}
    {{- else }}
    pass
    {{- end }}
{{- end }}

{{- range .Module.Structs }}
{{- $struct := . }}

class {{Camel .Name }}(EnhancedModel):
    {{- range $struct.Fields }}
    {{- if eq .KindType "struct" }}
    {{snake .Name }}: {{pyType "" .}} = Field(default_factory=lambda :{{pyDefault "" .}}, alias="{{.Name}}")
    {{- else }}
    {{snake .Name }}: {{pyType "" .}} = Field(default={{pyDefault "" .}}, alias="{{.Name}}")
    {{- end }}
    {{- else }}
    pass
    {{- end }}

    {{- if $struct.Fields }}

    def __init__(self, **kw):
        super().__init__(**kw)
    {{- end}}
{{- end }}

{{- range .Module.Interfaces }}
{{- $Interface := . }}

class I{{Camel .Name}}:
    def __init__(self):
        pass
    {{- range .Properties }}

    def get_{{snake .Name}}(self):
        raise NotImplementedError("Method {{$.Module.Name}}/{{snake $Interface.Name}}:get_{{snake .Name}} is not implemented.")
    {{- if not .IsReadOnly }}

    def set_{{snake .Name}}(self, value):
        raise NotImplementedError("Method {{$.Module.Name}}/{{snake $Interface.Name}}:set_{{snake .Name}} is not implemented.")
    {{- end }}
    {{- end }}
    {{- range .Operations }}

    def {{snake .Name}}({{pyParams "" .Params}}):
        raise NotImplementedError("Method {{$.Module.Name}}/{{snake $Interface.Name}}:{{snake .Name}} is not implemented.")
    {{- end }}
{{- end }}

{{- range .Module.Enums }}

def as_{{snake .Name}}(v):
    return {{Camel .Name}}(int(v))

def from_{{snake .Name}}(v):
    return v
{{- end}}

{{- range .Module.Structs }}

def as_{{snake .Name}}(v):
    return {{Camel .Name}}.model_validate(v)

def from_{{snake .Name}}(v):
    return v.model_dump()
{{- end }}

{{- range .Module.Externs }}
{{- $extern := pyExtern . }}
{{- $func_name:= printf "%s_%s" (snake $extern.Import) (snake $extern.Name )}}
def as_{{$func_name}}(v):
    {{ $default_val := $extern.Default }}
    {{- if (eq $default_val "") }}
    deserialized = {{$extern.Import}}.{{$extern.Name}}()
    {{- else -}}
    deserialized = {{ $default_val }}
    {{- end}}
    # deserialize your {{$extern.Import}}.{{$extern.Name}} from json string
    return deserialized

def from_{{$func_name}}(v):
    serialized = ""
    #serialize your {{$extern.Import}}.{{$extern.Name}} here to json string
    return serialized
{{- end }}

