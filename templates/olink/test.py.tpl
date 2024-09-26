{{- $class := Camel .Interface.Name }}
from {{snake .Module.Name}}.api import api
from {{snake .Module.Name}}.impl import {{$class}}
from {{snake .Module.Name}}.olink import {{$class}}Source, {{$class}}Sink
import {{snake .Module.Name}}.test_helpers.test_struct
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest
from typing import Any
import asyncio
{{- $apiPrefix := printf "api." }}

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

@pytest.fixture()
def olink_objects():
    impl = {{$class}}()
    {{$class}}Source(impl)
    remote_node = RemoteNode()
    client_node = ClientNode()

    remote_node.on_write(client_node.handle_message)
    client_node.on_write(remote_node.handle_message)

    sink = {{$class}}Sink()
    client_node.link_remote(sink.olink_object_name())
    yield impl, sink

class TestOLink{{$class}}:
{{- if (not (and (and (eq (len .Interface.Signals) 0) (eq (len .Interface.Properties) 0) ) (eq (len .Interface.Operations) 0)))}}
{{- range .Interface.Properties }}

    def test_{{snake .Name}}(self, olink_objects):
{{- if and (not .IsReadOnly) (not (eq .KindType "extern")) }}
        impl, sink = olink_objects
        is_{{snake .Name}}_changed = False
        def funProp(arguments):
            nonlocal is_{{snake .Name}}_changed
            is_{{snake .Name}}_changed = True
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
        assert is_{{snake .Name}}_changed == True
        assert impl.get_{{snake .Name}}() == test_value
        assert sink.get_{{snake .Name}}() == test_value
    {{- else }}
        pass
    {{- end }}
{{- end }}

{{- range .Interface.Operations }}

    @pytest.mark.asyncio
    async def test_{{snake .Name}}(self, olink_objects):
        impl, sink = olink_objects
        await sink.{{snake .Name}}(
    {{- range $idx, $p := .Params -}}
            {{- if $idx }}, {{end -}}
            {{snake .Name}}={{ pyDefault "api." .}}
    {{- end -}}
        )
{{- end }}

{{- range .Interface.Signals }}

    def test_{{snake .Name}}(self, olink_objects):
        impl, sink = olink_objects
        is_{{snake .Name}}_called = False


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
            nonlocal is_{{snake .Name}}_called
            is_{{snake .Name}}_called = True

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
        assert is_{{snake .Name}}_called == True

{{- end }}
{{- else }}
    pass
{{- end }}
