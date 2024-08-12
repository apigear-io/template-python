{{- $class := Camel .Interface.Name }}
from {{snake .Module.Name}}.api import api
from {{snake .Module.Name}}.impl import {{$class}}
from {{snake .Module.Name}}.olink import {{$class}}Source, {{$class}}Sink
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest

{{- $system := .System}}
{{- $imports := getEmptyStringList }}
{{- range .Module.Imports }}
    {{- $current_import := .}} 
    {{- $import_name := printf "%s.api" (snake .Name) }} 
    {{- $imports = (appendList $imports $import_name) }}
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
{{- range .Interface.Properties }}

    def test_{{snake .Name}}(self, olink_objects):
        impl, sink = olink_objects
        {{- if not .IsReadOnly }}
        self.called = False
        sink.on_{{snake .Name}}_changed += lambda *args: setattr(self, 'called', True)
        sink.set_{{snake .Name}}({{ pyDefault "api." .}})
        # should not be true since we are not changing the default value
        assert self.called == False
        {{- end }}
        assert impl.get_{{snake .Name}}() == {{ pyDefault "api." .}}
        assert sink.get_{{snake .Name}}() == {{ pyDefault "api." .}}
{{- else }}
    pass
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
{{- else }}
    pass
{{- end }}

{{- range .Interface.Signals }}

    def test_{{snake .Name}}(self, olink_objects):
        impl, sink = olink_objects
        self.called = False
        sink.on_{{snake .Name}} += lambda *args: setattr(self, 'called', True)
        impl._{{snake .Name}}(
    {{- range $idx, $p := .Params -}}
            {{- if $idx }}, {{end -}}
            {{ pyDefault "api." .}}
    {{- end -}}
        )
        assert self.called == True
{{- else }}
    pass
{{- end }}
