from fastapi import Depends, FastAPI, Header, HTTPException

{{ range .System.Modules }}  
import {{snake .Name }}_http
{{- end }}

app = FastAPI()

{{ range .System.Modules }}
app.include_router(
    router={{snake .Name }}_http.routes.router,
    prefix="/{{.Name}}",
)
{{ end }}