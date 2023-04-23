from pydantic import BaseModel
from enum import IntEnum

{{ range .Module.Enums }}

class {{ .Name }}(IntEnum):
    {{- range .Members }}
    {{ snake .Name }} = {{ .Value }}
    {{- end }}
{{- end }}

{{- range .Module.Structs }}

class {{ Camel .Name }}(BaseModel):
    {{- range .Fields }}
    {{ snake .Name }}: {{ pyReturn "" . }}
    {{- end }}
{{- end }}

{{- range .Module.Interfaces }}
{{- $class := Camel .Name }}

class I{{ $class}}:
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
