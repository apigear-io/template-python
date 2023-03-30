from fastapi import Depends, FastAPI, Header, HTTPException

{{ range .System.Modules }}  
import {{.Name | dot }}.http.routes
{{- end }}

app = FastAPI()

{{ range .System.Modules }}
app.include_router(
    router={{.Name | dot }}.http.routes.router,
    prefix="/{{.Name}}",
)
{{ end }}