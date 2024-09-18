import apigear.mqtt
import utils.base_types
import paho.mqtt.enums
import paho.mqtt.reasoncodes
{{- $current_module_api_prefix :=  printf "%s.api." (snake .Module.Name ) }}
import {{snake .Module.Name }}.api
from utils.eventhook import EventHook
from typing import Any
import logging

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

{{- range .Module.Interfaces }}
{{- $interface := . }}
{{- $ns := printf "%s.%s" $.Module.Name .Name -}}
{{- $class := Camel .Name }}
{{- $id := printf "%s.%s" $.Module.Name .Name }}
class {{$class}}ServiceAdapter():
    def __init__(self, impl: {{$current_module_api_prefix}}I{{$class}}, service: apigear.mqtt.Service):
        self.service = service
        self.impl = impl
        self.on_ready = EventHook()
{{- range $idx, $p := .Properties }}
        self.impl.on_{{snake .Name}}_changed += self.notify_{{snake .Name}}_changed
{{- end }}
{{- range $idx, $s := .Signals }}
        self.impl.on_{{snake .Name}} += self.notify_{{snake .Name}}
{{- end }}
{{- if not ((and (eq (len $interface.Operations) 0) (eq (len $interface.Properties) 0) ))}}
        self.service.on_connected += self.subscribeForTopics
        self.service.on_subscribed += self.__handle_subscribed
        self.subscription_ids = []

    def subscribeForTopics(self):
        {{- range .Properties }}
        self.subscription_ids.append(self.service.subscribe_for_property("{{$.Module.Name}}/{{$interface.Name}}/set/{{.Name}}", self.__set_{{snake .Name}}))
        {{- end }}
        {{- range  .Operations }}
        self.subscription_ids.append(self.service.subscribe_for_invoke_req("{{$.Module.Name}}/{{$interface.Name}}/rpc/{{.Name}}", self.__invoke_{{snake .Name}}))
        {{- end}}

    def __del__(self):
        self.service.on_connected -= self.subscribeForTopics
        self.service.on_subscribed -= self.__handle_subscribed
        {{- range .Properties }}
        self.service.unsubscribe("{{$.Module.Name}}/{{$interface.Name}}/set/{{.Name}}")
        {{- end }}
        {{- range .Operations }}
        self.service.unsubscribe("{{$.Module.Name}}/{{$interface.Name}}/rpc/{{.Name}}")
        {{- end}}
        {{- range $idx, $p := .Properties }}
        self.impl.on_{{snake .Name}}_changed -= self.notify_{{snake .Name}}_changed
        {{- end }}
        {{- range $idx, $s := .Signals }}
        self.impl.on_{{snake .Name}} -= self.notify_{{snake .Name}}
        {{- end }}

    def __handle_subscribed(self, msg_id: int, reason_code_list: list[paho.mqtt.reasoncodes.ReasonCode]):
        if not (msg_id in self.subscription_ids):
            return
        # Assuming the topic was subscribed only for a single channel and reason_code_list contains
        # a single entry
        if reason_code_list[0].is_failure:
            self.logging_func(paho.mqtt.enums.LogLevel.MQTT_LOG_ERROR, (f"Broker rejected subscription id {msg_id} reason: {reason_code_list[0]}"))
            return
        self.subscription_ids.remove(msg_id)
        if len(self.subscription_ids) == 0:
            self.on_ready.fire()
    {{- else}}
        self.on_ready.self.fire()
    {{- end}}

{{- range .Signals }}

    def notify_{{snake .Name}}({{pyParams $current_module_api_prefix .Params}}):
        {{- range .Params }}
        {{- if .IsArray }}
        _{{snake .Name}} = [{{template "get_converter_module" .}}.from_{{template "get_serialization_name" .}}(_) for _ in {{snake .Name}}]
        {{- else }}
        _{{snake .Name}} = {{template "get_converter_module" .}}.from_{{template "get_serialization_name" .}}({{snake .Name}})
        {{- end }}
        {{- end }}
        args = [
            {{- range $idx, $param := .Params -}}{{- if $idx}}, {{ end -}}
            _{{snake $param.Name}}
            {{- end -}}
        ]
        self.service.notify_signal("{{$.Module.Name}}/{{$interface.Name}}/sig/{{.Name}}", args)
{{- end }}

{{- range .Properties }}

    def notify_{{snake .Name}}_changed(self, value):
        {{- if .IsArray }}
        v = [{{template "get_converter_module" .}}.from_{{template "get_serialization_name" .}}(_) for _ in value]
        {{- else }}
        v = {{template "get_converter_module" .}}.from_{{template "get_serialization_name" .}}(value)
        {{- end }}
        self.service.notify_property_change("{{$.Module.Name}}/{{$interface.Name}}/prop/{{.Name}}", v)
{{- end }}

{{- range .Properties }}

    def __set_{{snake .Name}}(self, value: Any):
        {{- if not .IsReadOnly }}
            {{- if .IsArray }}
            v = [{{template "get_converter_module" .}}.as_{{template "get_serialization_name" .}}(_) for _ in value]
            {{- else }}
            v = {{template "get_converter_module" .}}.as_{{template "get_serialization_name" .}}(value)
            {{- end }}
            self.impl.set_{{snake .Name}}(v)
        {{- else }}
            pass
        {{- end }}
{{- end }}

{{- range .Operations }}

    def __invoke_{{snake .Name}}(self, args: list[Any]) -> Any:
    {{- range $idx, $_ := .Params }}
        {{- if .IsArray }}
        {{snake .Name}} = [{{template "get_converter_module" .}}.as_{{template "get_serialization_name" .}}(_) for _ in args[{{$idx}}]]
        {{- else }}
        {{snake .Name}} = {{template "get_converter_module" .}}.as_{{template "get_serialization_name" .}}(args[{{$idx}}])
        {{- end }}
    {{- end }}
        reply = self.impl.{{snake .Name}}({{pyVars .Params}})
    {{- if .Return.IsVoid }}
        return utils.base_types.from_int(0)   
    {{- else }}
        {{- if .Return.IsArray }}
        return [{{template "get_converter_module" .Return}}.from_{{template "get_serialization_name" .Return}}(_) for _ in reply]
        {{- else }}
        return {{template "get_converter_module" .Return}}.from_{{template "get_serialization_name" .Return}}(reply)
        {{- end }}
    {{- end }}
{{- end }}

{{- end }}
