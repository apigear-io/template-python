import asyncio
from typing import Any
import apigear.mqtt
import paho.mqtt.enums
import paho.mqtt.reasoncodes
from utils.eventhook import EventHook
import utils.base_types
{{- $current_module_api_prefix :=  printf "%s.api." (snake .Module.Name ) }}
import {{snake .Module.Name }}.api
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


{{- $m := .Module }}
{{- range .Module.Interfaces }}
{{- $interface := . }}
{{- $interfaceName := .Name }}

class {{Camel .Name}}ClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self.on_ready = EventHook()
    {{- range .Properties }}
        self._{{snake .Name}} = {{pyDefault $current_module_api_prefix .}}
        self.on_{{snake .Name}}_changed = EventHook()
    {{- end }}
    {{- range .Signals }}
        self.on_{{snake .Name}} = EventHook()
    {{- end }}
    {{- if (not (and (and (eq (len $interface.Signals) 0) (eq (len $interface.Properties) 0) ) (eq (len $interface.Operations) 0)))}}
        self.client.on_subscribed += self.__handle_subscribed
        self.subscription_ids = []
        self.client.on_connected += self.subscribeForTopics
        {{- if (ne (len $interface.Operations) 0) }}
        self.method_topics = self.MethodTopics(self.client.get_client_id())
        self.pending_calls = self.PendingCalls()
        {{- end}}
        self.loop = asyncio.get_event_loop()

    def subscribeForTopics(self):
        {{- range .Properties }}
        self.subscription_ids.append(self.client.subscribe_for_property("{{$.Module.Name}}/{{$interfaceName}}/prop/{{.Name}}", self.__set_{{snake .Name}}))
        {{- end }}
        {{- range .Signals }}
        self.subscription_ids.append(self.client.subscribe_for_signal("{{$.Module.Name}}/{{$interfaceName}}/sig/{{.Name}}",  self.__on_{{snake .Name}}_signal))
        {{- end }}
        {{- range .Operations }}
        self.subscription_ids.append(self.client.subscribe_for_invoke_resp(self.method_topics.resp_topic_{{snake .Name}}, self.__on_{{snake .Name}}_resp))
        {{- end }}

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.on_subscribed -= self.__handle_subscribed
        {{- range .Properties }}
        self.client.unsubscribe("{{$.Module.Name}}/{{$interfaceName}}/prop/{{.Name}}")
        {{- end }}
        {{- range .Signals }}
        self.client.unsubscribe("{{$.Module.Name}}/{{$interfaceName}}/sig/{{.Name}}")
        {{- end }}
        {{- range .Operations }}
        self.client.unsubscribe(self.method_topics.resp_topic_{{snake .Name}})
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

    {{- range .Properties }}
    {{- if not .IsReadOnly }}

    def set_{{snake .Name}}(self, value):
        if self._{{snake .Name}} == value:
            return
        topic = "{{.Module.Name}}/{{$interfaceName}}/set/{{.Name}}"
        {{- if .IsArray }}
        self.client.set_remote_property(topic, [{{ template "get_converter_module" .}}.from_{{template "get_serialization_name" .}}(_) for _ in value])
        {{- else }}
        self.client.set_remote_property(topic, {{ template "get_converter_module" .}}.from_{{template "get_serialization_name" .}}(value))
        {{- end }}
    {{- end }}

    def get_{{snake .Name}}(self):
        return self._{{snake .Name}}

    {{- end }}


    {{- range .Operations }}

    async def {{snake .Name}}({{pyParams $current_module_api_prefix .Params}}):
        {{- range $idx, $_ := .Params }}
        {{- if .IsArray }}
        _{{snake .Name}} = [{{template "get_converter_module" .}}.from_{{template "get_serialization_name" .}}({{snake .Type}}) for {{snake .Type}} in {{snake .Name}}]
        {{- else }}
        _{{snake .Name}} = {{template "get_converter_module" .}}.from_{{template "get_serialization_name" .}}({{snake .Name}})
        {{- end }}
        {{- end }}
        args = [
            {{- range $idx, $_ := .Params -}}{{- if $idx}}, {{ end -}}
            _{{snake .Name}}
            {{- end -}}]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            def set_future_callback():
            {{- if .Return.IsVoid }}
                future.set_result(None)
            {{- else}}
                future.set_result({{template "get_converter_module" .Return}}.as_{{template "get_serialization_name" .Return}}(result))
            {{- end}}
            return self.loop.call_soon_threadsafe(set_future_callback)
        call_id = self.client.invoke_remote(self.method_topics.topic_{{snake .Name}}, self.method_topics.resp_topic_{{snake .Name}}, args)
        self.pending_calls.{{snake .Name}}[call_id] = func
        return await asyncio.wait_for(future, 500)
    {{- end }}

    # internal functions on message handle
    {{- range .Properties }}

    def __set_{{snake .Name}}(self, data):
        {{- if .IsArray }}
        value = [{{template "get_converter_module" .}}.as_{{template "get_serialization_name" .}}(_) for _ in data]
        {{- else }}
        value =  {{template "get_converter_module" .}}.as_{{template "get_serialization_name" .}}(data)
        {{- end }}
        if self._{{snake .Name}} == value:
            return
        self._{{snake .Name}} = value
        self.on_{{snake .Name}}_changed.fire(self._{{snake .Name}})
    {{- end }}

    {{- range $idx, $o := .Signals }}

    def __on_{{snake .Name}}_signal(self, args: list[Any]):
        {{- range $index, $_ := .Params }}
        {{- if .IsArray }}
        {{snake .Name}} = [{{template "get_converter_module" .}}.as_{{template "get_serialization_name" .}}(_) for _ in args[{{$index}}]]
        {{- else }}
        {{snake .Name}} =  {{template "get_converter_module" .}}.as_{{template "get_serialization_name" .}}(args[{{$index}}])
        {{- end }}
        {{- end }}
        self.on_{{snake .Name}}.fire(
        {{- range $index, $_ := .Params -}}{{- if $index}}, {{ end -}}
        {{snake .Name}}
        {{- end -}}
        )
        return
    {{- end }}

    {{- range .Operations }}

    def __on_{{snake .Name}}_resp(self, value, callId):
       callback = self.pending_calls.{{snake .Name}}.pop(callId)
       if callback != None:
           callback(value)
    {{- end }}

    {{- if (ne (len $interface.Operations) 0)}}
    class MethodTopics:
        def __init__(self, client_id):
            {{- range .Operations }}
            self.topic_{{snake .Name}}= "{{$.Module.Name}}/{{$interfaceName}}/rpc/{{.Name}}"
            self.resp_topic_{{snake .Name}}= self.topic_{{snake .Name}} + "/" + str(client_id) + "/result"
            {{- end}}

    class PendingCalls:
        def __init__(self):
            {{- range .Operations }}
            self.{{snake .Name}} = {}
            {{- end}}
    {{- end}}

{{- end}}
