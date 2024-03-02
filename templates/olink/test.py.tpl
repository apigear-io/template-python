{{- $class := Camel .Interface.Name }}
from {{snake .Module.Name}}_api import api
from {{snake .Module.Name}}_impl import {{$class}}
from {{snake .Module.Name}}_olink import {{$class}}Source, {{$class}}Sink
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest

@pytest.fixture()
def olink_objects():
    impl = {{$class}}()
    source = {{$class}}Source(impl)
    remote_node = RemoteNode()
    client_node = ClientNode()

    remote_node.on_write(client_node.handle_message)
    client_node.on_write(remote_node.handle_message)

    sink = {{$class}}Sink()
    client_node.link_remote(sink.olink_object_name())
    yield impl, sink

class TestOLink{{$class}}:
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
