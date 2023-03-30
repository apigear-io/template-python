from {{ dot .Module.Name}}.api import api
from typing import Iterable
{{- $class := .Interface.Name }}

class {{$class}}(api.I{{$class}}):
    def __init__(self):
{{- range .Interface.Properties }}
        self.__{{.Name}}: {{pyReturn "api." .}} = {{pyDefault "api." .}}
{{- else }}
        pass
{{- end }}
{{- range .Interface.Properties }}

    @property
    def {{.Name}}(self):
        return self.__{{.Name}}
{{- end }}
{{- range .Interface.Operations }}

    def {{.Name}}({{pyParams "api." .Params}}) -> {{pyReturn "api." .Return}}:
        return {{pyDefault "api." .Return}}    
{{- end }}