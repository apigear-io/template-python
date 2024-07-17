import asyncio
import logging
import os
import sys

#add context - paths to modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import apigear.mqtt
{{- $system := .System}}
{{- $imports := getEmptyStringList }}
{{- range .System.Modules }}
{{- $import_mqtt := printf "%s.mqtt" (snake .Name) }} 
{{- $import_impl := printf "%s.impl" (snake .Name) }} 
{{- $import_api := printf "%s.api" (snake .Name) }} 
{{- $imports = (appendList $imports $import_mqtt) }}
{{- $imports = (appendList $imports $import_impl) }}
{{- $imports = (appendList $imports $import_api) }}
    {{- range .Externs }}
    {{- $extern := pyExtern . }}
    {{- $imports = (appendList $imports $extern.Import) }}
    {{- end }}
{{- end }}

{{- $imports = unique $imports }}
{{- range $imports }}
import {{.}}
{{- end }}


# set default log level to INFO and above
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

# REMEMBER TO RUN A BROKER OF YOUR CHOICE
async def main():
    service = apigear.mqtt.Service("uniqueServiceIdTestIntProperty")

{{- range .System.Modules }}
{{- $module := . }}
{{- $import_mqtt := printf "%s.mqtt" (snake $module.Name)}}
{{- $import_impl := printf "%s.impl" (snake $module.Name)}}
{{- range .Interfaces }}
    source_{{snake $module.Name}}_{{snake .Name}} = {{$import_impl}}.{{Camel .Name}}()
    serviceAdapter_{{snake $module.Name}}_{{snake .Name}} = {{$import_mqtt}}.{{Camel .Name}}ServiceAdapter(source_{{snake $module.Name}}_{{snake .Name}}, service)
{{- end }}
{{ end }}

    await service.connect("localhost", 1883)
    # do some actions here, wait for messages, send messages like:
    {{ $propertyExampleReady := 0 -}}
    {{ $signalExampleReady := 0 -}}
    {{- range.System.Modules -}}
    {{- $module := . -}}
    {{- range $module.Interfaces -}}
    {{- $interface := . -}}
    {{- $class := printf "source_%s_%s" (snake $module.Name) (snake .Name) -}}
{{- if (and (eq $propertyExampleReady  0)  (len $interface.Properties) )}}
    {{- $property := (index $interface.Properties 0) }}
    # You can add local handlers for property handling
    def handleProperty(value):
        print("property changed");
        print(value);
    {{$class}}.on_{{snake $property.Name}}_changed += handleProperty
    # Set property, the change will be sent to all clients, and local handlers
    # Have in mind that the value should be different than current (which probably is default) for the message to be sent
    {{- $module_prefix := printf "%s.api." (snake $module.Name)}}
    local_{{$property.Name}} = {{pyDefault $module_prefix $property}};
    {{$class}}.set_{{snake $property.Name}}(local_{{$property.Name}});
    {{ $propertyExampleReady = 1}}
{{- end }}
{{- if (and (eq $signalExampleReady  0)  (len $interface.Signals))}}
    # Emit the signal, it will be sent to all clients
    {{- $signal := (index $interface.Signals 0 ) }}
    def handleSignal(value):
        print("received signal");
        print(value);
    {{$class}}.on_{{snake $signal.Name}} += handleSignal
    {{- $module_prefix := printf "%s.api." (snake $module.Name)}}
    {{$class}}._{{snake $signal.Name}}(
                {{- range $i, $e := $signal.Params }}
                    {{- if $i }}, {{ end }}{{pyDefault  $module_prefix $e}}
                {{- end }}   {{- /* end range operation param*/ -}} )
    {{ $signalExampleReady = 1}}
{{- end }}
{{- if (and $signalExampleReady  $propertyExampleReady)}}
    {{- break}}
{{- end }}
{{- end}}{{/* end range over interfaces*/}}
{{- if (and $signalExampleReady  $propertyExampleReady)}}
    {{- break}}
{{- end }}
{{- end}}{{/* end range over modules*/}}
    input("Press Enter to close")
    service.disconnect()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())

