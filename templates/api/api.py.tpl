from pydantic import ConfigDict, BaseModel, Field
from enum import IntEnum

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


def as_int(v):
    return int(v)

def from_int(v):
    return v

def as_int32(v):
    return as_int(v)

def from_int32(v):
    return from_int(v)

def as_int64(v):
    return as_int(v)

def from_int64(v):
    return from_int(v)

def as_string(v):
    return str(v)

def from_string(v):
    return v

def as_bool(v):
    return str(v).lower() in ['true', '1', 't', 'y', 'yes']

def from_bool(v):
    return v

def as_float(v):
    return float(v)

def from_float(v):
    return v

def as_float32(v):
    return as_float(v)

def from_float32(v):
    return from_float(v)

def as_float64(v):
    return as_float(v)

def from_float64(v):
    return from_float(v)

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

