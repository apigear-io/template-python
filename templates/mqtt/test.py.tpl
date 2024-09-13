{{- $class := Camel .Interface.Name -}}
import {{snake .Module.Name}}.api
import {{snake .Module.Name}}.impl
import {{snake .Module.Name}}.mqtt
import {{snake .Module.Name}}.test_helpers.test_struct
import apigear.mqtt
import pytest
from typing import Any
import asyncio
{{- $apiPrefix := printf "%s.api." (snake .Module.Name) }}

{{- $system := .System}}
{{- $imports := getEmptyStringList }}
{{- range .Module.Imports }}
    {{- $current_import := .}} 
    {{- $import_name := printf "%s.api" (snake .Name) }} 
    {{- $imports = (appendList $imports $import_name) }}
    {{- $import_test_structs := printf "%s.test_helpers.test_struct" (snake .Name) }} 
    {{- $imports = (appendList $imports $import_test_structs) }}
        {{- range $system.Modules }}
            {{- if (eq .Name $current_import.Name) }}
                {{- range .Externs }}
                    {{- $extern := pyExtern . }}
                    {{- $imports = (appendList $imports $extern.Import) }}
                {{- end }}
            {{- end }}
    {{- end }}
{{- end }}
{{- range .Module.Externs }}
    {{- $extern := pyExtern . }}
    {{- $imports = (appendList $imports $extern.Import) }}
{{- end }}
{{- $imports = unique $imports }}
{{- range $imports }}
import {{.}}
{{- end }}

{{- define "get_test_struct_module"}}
            {{- $module_prefix:= printf "%s.test_helpers.test_struct" (snake .Module.Name ) }}
            {{- if (ne .Import "") }}
            {{- $module_prefix = printf "%s.test_helpers.test_struct" (snake .Import ) }}
            {{- end}}
            {{- $module_prefix -}}
{{- end}}

def set_event_ready(loop, event):
    def func():
        event.set()
    loop.call_soon_threadsafe(func)

class TestMqtt{{$class}}:

    @pytest.mark.asyncio
    async def setup_mqtt(slef):
        impl = {{snake .Module.Name}}.impl.{{$class}}()
        service = apigear.mqtt.Service("uniqueServiceIdTest{{$class}}")
        client = apigear.mqtt.Client("uniqueClientIdTestTest{{$class}}")
        serviceAdapter = {{snake .Module.Name}}.mqtt.{{$class}}ServiceAdapter(impl, service)
        sink = {{snake .Module.Name}}.mqtt.{{$class}}ClientAdapter(client)
     
        await service.connect("localhost", 1883)
        await client.connect("localhost", 1883)

        loop = asyncio.get_event_loop()

        is_client_ready = asyncio.Event()
        is_service_ready = asyncio.Event()

        def funClient():
            set_event_ready(loop, is_client_ready)
        def funServer():
            set_event_ready(loop, is_service_ready)
        sink.on_ready += funClient 
        serviceAdapter.on_ready += funServer

        async def coroutineService():
            await is_service_ready.wait()

        async def coroutineClient():
            await is_client_ready.wait()

        taskService = asyncio.create_task(coroutineService())
        taskClient = asyncio.create_task(coroutineClient())
        await asyncio.wait([taskService, taskClient], timeout=10.0, return_when=asyncio.ALL_COMPLETED)
        return impl, sink, serviceAdapter, client, service

    async def teardown_mqtt(self, service, client):
        service.disconnect()
        client.disconnect()

{{- range .Interface.Properties }}

    @pytest.mark.asyncio
    async def test_{{snake .Name}}(self):
{{- if and (not .IsReadOnly) (not (eq .KindType "extern")) }}
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_{{snake .Name}}_changed_done = asyncio.Event()
        def funProp(arguments):
            set_event_ready(loop, is_{{snake .Name}}_changed_done )
        
        sink.on_{{snake .Name}}_changed += funProp
     
	{{- if .IsArray }}
        test_value = {{ pyDefault $apiPrefix . }}
	    {{- if not ( or ( .IsPrimitive)  (eq .KindType "enum")) }}
        test_value.append({{template "get_test_struct_module" .}}.fillTest{{.Type }}({{ pyTestValue $apiPrefix . }}))
        {{- else }}  
        test_value.append({{ pyTestValue $apiPrefix .}})
        {{- end }}
	{{- else }}
        {{- if and (not .IsPrimitive) (not (eq .KindType "enum"))}}
        test_value = {{template "get_test_struct_module" .}}.fillTest{{.Type}}({{ pyDefault $apiPrefix . }})
        {{- else}}
        test_value = {{ pyTestValue $apiPrefix . }}
        {{- end }}
	{{- end }}
        
        sink.set_{{snake .Name}}(test_value)
        await is_{{snake .Name}}_changed_done.wait()
        assert impl.get_{{snake .Name}}() == test_value
        assert sink.get_{{snake .Name}}() == test_value
        await self.teardown_mqtt(client, service)
{{- else }}
        pass
{{- end }}
{{- end }}



{{- range .Interface.Signals }}

    @pytest.mark.asyncio
    async def test_{{snake .Name}}(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()
        loop = asyncio.get_event_loop()
        is_{{snake .Name}}_changed_done = asyncio.Event()

    {{- range $idx, $p := .Params -}}
        {{- if .IsArray }}
        local_{{snake .Name}}_array = {{ pyDefault $apiPrefix . }}
        {{- if not ( or (eq .KindType "extern") ( or .IsPrimitive  (eq .KindType "enum") ) )}}
        local_{{snake .Name}}_array.append({{template "get_test_struct_module" .}}.fillTest{{.Type}}({{ pyTestValue $apiPrefix . }}))
        {{- else }}
        local_{{snake .Name}}_array.append({{ pyTestValue $apiPrefix . }})
        {{- end }}
        {{- else if not ( or (eq .KindType "extern") ( or .IsPrimitive  (eq .KindType "enum") ) )}}
        local_{{snake .Name}}_struct = {{template "get_test_struct_module" .}}.fillTest{{.Type}}({{ pyDefault $apiPrefix . }})
        {{- end -}}
    {{- end }}

        def funSignal({{- range $index, $_ := .Params -}}{{- if $index}}, {{ end -}}
        {{snake .Name}}
        {{- end -}}):
        {{- range $idx, $p := .Params }}
            assert {{snake .Name}} == 
            {{- if .IsArray }} local_{{snake .Name}}_array
            {{- else if (eq .KindType "extern") }} {{ pyDefault $apiPrefix .}}
            {{- else if  ( or .IsPrimitive  (eq .KindType "enum") ) }} {{ pyTestValue $apiPrefix . }}
            {{- else -}} local_{{snake .Name}}_struct
            {{- end }}
        {{- end }}
            set_event_ready(loop, is_{{snake .Name}}_changed_done )
        
        sink.on_{{snake .Name}} += funSignal
        impl._{{snake .Name}}(
    {{- range $idx, $p := .Params -}}
            {{- if $idx }}, {{end -}}
            {{- if .IsArray }}local_{{snake .Name}}_array
            {{- else if (eq .KindType "extern") }}{{ pyDefault $apiPrefix .}}
            {{- else if  ( or .IsPrimitive  (eq .KindType "enum") ) }}{{ pyTestValue $apiPrefix . }}
            {{- else -}}
            local_{{snake .Name}}_struct
            {{- end -}}
    {{- end -}}
        )

        await is_{{snake .Name}}_changed_done.wait()
        await self.teardown_mqtt(client, service)
{{- end }}

{{- range .Interface.Operations }}

    @pytest.mark.asyncio
    async def test_{{snake .Name}}(self):
        impl, sink, serviceAdapter, client, service = await self.setup_mqtt()

        {{ if not .Return.IsVoid }}result = {{end }}await sink.{{snake .Name}}(
    {{- range $idx, $p := .Params -}}
            {{- if $idx }}, {{end -}}
            {{snake .Name}}={{ pyDefault $apiPrefix .}}
    {{- end -}}
        )
        {{- if not .Return.IsVoid }}
        assert result == {{ pyDefault $apiPrefix .Return}}
        {{- end }}

        await self.teardown_mqtt(client, service)
{{- end }}
