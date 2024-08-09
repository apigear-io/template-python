{{- $features := .Features -}}
pydantic==2.*
pytest
pytest-asyncio
{{- if $features.http }}
fastapi
{{- end}}
{{- if $features.olink }}
starlette
uvicorn
websockets
olink-core @ git+https://github.com/apigear-io/objectlink-core-python.git@v0.3.3
{{- end}}
{{- if $features.mqtt }}
paho-mqtt
{{- end}}
