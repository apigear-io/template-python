import asyncio
import os
import sys

#add context - paths to modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import apigear.mqtt
import logging

{{- $system := .System}}
{{- $imports := getEmptyStringList }}
{{- range .System.Modules }}
{{- $import_mqtt := printf "%s.mqtt" (snake .Name) }} 
{{- $import_api := printf "%s.api" (snake .Name) }} 
{{- $imports = (appendList $imports $import_mqtt) }}
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
    # create a mqtt adapter for client side
    client = apigear.mqtt.Client("uniqueClientIdTestIntProperty")

    # create mqtt interface adapters for client side
{{- range .System.Modules }}
{{- $module := . }}
{{- range .Interfaces }}
    sink_{{snake $module.Name}}{{snake .Name}} = {{snake $module.Name}}.mqtt.{{Camel .Name}}ClientAdapter(client)
{{- end }}
{{- end }}
    await client.connect("localhost", 1883)

    {{ $propertyExampleReady := 0 -}}
    {{ $signalExampleReady := 0 -}}
    {{ $operationExampleReady := 0 -}}
    {{- range.System.Modules -}}
    {{- $module := . -}}
    {{- range $module.Interfaces -}}
    {{- $interface := . -}}
    {{- $class := printf "sink_%s%s" (snake $module.Name) (snake .Name) -}}
{{- if (and (eq $propertyExampleReady  0)  (len $interface.Properties) )}}
    {{- $property := (index $interface.Properties 0) }}
    # Try out properties: subscribe for changes
    def handleProperty(value):
        print("received property change");
        print(value);
    {{$class}}.on_{{snake $property.Name}}_changed += handleProperty
    # or ask for change.
    # Have in mind that the value should be different than current (which probably is default) for the message to be sent
    {{- $module_prefix := printf "%s.api." (snake $module.Name)}}
    local_{{$property.Name}} = {{pyDefault $module_prefix $property}};
    {{$class}}.set_{{snake $property.Name}}(local_{{$property.Name}});
    {{ $propertyExampleReady = 1}}
{{- end }}
{{- if (and (eq $signalExampleReady  0)  (len $interface.Signals))}}
    # Check the signals with subscribing for its change
    {{- $signal := (index $interface.Signals 0 ) }}
    def handleSignal(value):
        print("received signal");
        print(value);
    {{$class}}.on_{{snake $signal.Name}} += handleSignal
    {{ $signalExampleReady = 1}}
{{- end }}

{{- if ( and (eq $operationExampleReady  0) (len $interface.Operations))}}
    {{- $operation := (index $interface.Operations 0) }}
    # Play around executing your operations
    {{- $module_prefix := printf "%s.api." (snake $module.Name)}}
    result = {{$class}}.{{snake $operation.Name}}(
                {{- range $i, $param := $operation.Params }}
                    {{- if $i }}, {{ end }}{{pyDefault  $module_prefix $param}}
                {{- end }}   {{- /* end range operation param*/ -}} )
    await result
    print("method reuslt")
    print(result)    
    {{ $operationExampleReady = 1}}
{{- end }}
{{- if (and (and $operationExampleReady  $signalExampleReady)  $propertyExampleReady)}}
    {{- break}}
{{- end }}
{{- end}}{{/* end range over interfaces*/}}
{{- if (and (and $operationExampleReady  $signalExampleReady)  $propertyExampleReady)}}
    {{- break}}
{{- end }}
{{- end}}{{/* end range over modules*/}}
    input("Press Enter to close")

    client.disconnect()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())

