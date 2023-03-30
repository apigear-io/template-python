from fastapi import APIRouter

{{ $m := .Module}}
{{ range .Module.Interfaces }}
from {{ dot $m.Name }} import {{ .Name }}
{{- end }}

from . import shared

router = APIRouter()

{{ range .Module.Interfaces }}
{{ snake .Name }} = {{ .Name }}()
{{- end }}

{{ range $i := .Module.Interfaces }}
{{ range .Operations }}
@router.post(
    "/{{ snake $i.Name }}/{{ .Name }}", 
    response_model=shared.{{ $i.Name }}{{Camel .Name }}Response
)
async def {{snake $i.Name}}_{{camel .Name}}(params: shared.{{$i.Name}}{{Camel .Name}}Request):
    result = {{snake $i.Name}}.{{.Name}}({{ range $idx, $e := .Params }}{{if $idx }}, {{end}}params.{{.Name}}{{end}})
    state = shared.{{$i.Name}}State(
        {{- range $i.Properties }}
        {{ .Name }} = {{ snake $i.Name }}.{{ .Name }},
        {{- end }}
    )
    response = shared.{{$i.Name}}{{Camel .Name}}Response(
        result=result,
        state=state
    )
    return response
{{ end }}
{{ end }}
