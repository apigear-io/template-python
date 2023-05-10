from fastapi import APIRouter
{{- $m := .Module}}
from . import shared

router = APIRouter()

{{ range $i := .Module.Interfaces }}
{{ snake $i.Name }} = shared.{{Camel $i.Name }}State()
{{- end }}

{{ range $i := .Module.Interfaces }}
{{ range .Operations }}
@router.post(
    "/{{snake $m.Name}}/{{ snake $i.Name }}/{{ snake .Name }}", 
    response_model=shared.{{ Camel $i.Name }}{{Camel .Name }}Response
)
async def {{snake $i.Name}}_{{camel .Name}}(params: shared.{{$i.Name}}{{Camel .Name}}Request):
    result = {{snake $i.Name}}.{{.Name}}({{ range $idx, $e := .Params }}{{if $idx }}, {{end}}params.{{snake .Name}}{{end}})
    state = shared.{{Camel $i.Name}}State(
        {{- range $i.Properties }}
        {{snake  .Name }} = {{ snake $i.Name }}.{{ snake .Name }},
        {{- end }}
    )
    response = shared.{{$i.Name}}{{Camel .Name}}Response(
        result=result,
        state=state
    )
    return response
{{ end }}
{{ end }}
