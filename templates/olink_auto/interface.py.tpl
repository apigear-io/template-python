from {{ snake .Module.Name}} import api
from typing import Iterable
{{- $class := .Interface.Name }}

class {{$class}}(api.I{{$class}}):
    def __init__(self):
        super().__init__()        
{{- range .Interface.Properties }}
        _{{snake .Name}}: {{pyType "api." .}} = {{pyDefault "api." .}}
{{- end }}

{{- range .Interface.Properties }}
    def set_{{snake .Name}}(self, value):
        if self._{{snake .Name}} == value:
            return
        self._{{snake .Name}} = value
    
    def get_{{snake .Name}}(self):
        return self._{{snake .Name}}        
{{- end }}

{{- range .Interface.Operations }}
    def {{snake .Name}}({{pyParams "api." .Params}}) -> {{pyReturn "api." .Return}}:
        return {{pyDefault "api." .Return}}
{{- end }}
