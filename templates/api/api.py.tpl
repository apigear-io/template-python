from pydantic import BaseModel
from enum import IntEnum

{{ range .Module.Enums }}

class {{ .Name }}(IntEnum):
    {{- range .Members }}
    {{ .Name }} = {{ .Value }}
    {{- end }}
{{- end }}
{{- range .Module.Structs }}

class {{ .Name }}(BaseModel):
    {{- range .Fields }}
    {{ .Name }}: {{ pyReturn "" . }}
    {{- end }}
{{- end }}
{{- range .Module.Interfaces }}

class {{ .Name }}(BaseModel):
    {{- range .Properties }}
    {{ .Name }}: {{ pyReturn "" .}}
    {{- end }}
    {{- range .Operations }}

    def {{ .Name }}({{pyParams "" .Params }}):
        raise NotImplementedError
    {{- end }}
{{- end }}
