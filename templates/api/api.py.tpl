from pydantic import BaseModel, Field
from enum import IntEnum

{{ range .Module.Enums }}

class {{Camel .Name }}(IntEnum):
    {{- range .Members }}
    {{ SNAKE .Name }} = {{ .Value }}
    {{- else }}
    pass
    {{- end }}
{{- end }}

{{- range .Module.Structs }}

class {{Camel .Name }}(BaseModel):
    {{- range .Fields }}
    {{snake .Name }}: {{pyType "" .}} = Field(None, alias="{{.Name}}")
    {{- else }}
    pass
    {{- end }}
{{- end }}

{{- range .Module.Interfaces }}

class I{{Camel .Name}}:
    def __init__(self):
        pass
    {{- range .Properties }}

    def get_{{snake .Name}}(self):
        raise NotImplementedError

    def set_{{snake .Name}}(self, value):
        raise NotImplementedError
    {{- end }}
    {{- range .Operations }}

    def {{snake .Name}}({{pyParams "" .Params}}):
        raise NotImplementedError
    {{- end }}
{{- end }}


def as_int(v):
    return int(v)

def from_int(v):
    return v

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

{{- range .Module.Enums }}

def as_{{snake .Name}}(v):
    return {{Camel .Name}}(int(v))

def from_{{snake .Name}}(v):
    return v
{{- end}}

{{- range .Module.Structs }}

def as_{{snake .Name}}(v):
    return {{Camel .Name}}.parse_obj(v)

def from_{{snake .Name}}(v):
    return v.dict()
{{- end }}

