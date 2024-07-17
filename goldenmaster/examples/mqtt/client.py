import asyncio
import os
import sys

#add context - paths to modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import apigear.mqtt
import logging
import counter.api
import counter.mqtt
import custom_types.api
import custom_types.mqtt
import extern_types.api
import extern_types.mqtt
import tb_empty.api
import tb_empty.mqtt
import tb_enum.api
import tb_enum.mqtt
import tb_names.api
import tb_names.mqtt
import tb_same1.api
import tb_same1.mqtt
import tb_same2.api
import tb_same2.mqtt
import tb_simple.api
import tb_simple.mqtt
import testbed1.api
import testbed1.mqtt
import testbed2.api
import testbed2.mqtt
import vector3d.vector

# set default log level to INFO and above
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)


# REMEMBER TO RUN A BROKER OF YOUR CHOICE
async def main():
    # create a mqtt adapter for client side
    client = apigear.mqtt.Client("uniqueClientIdTestIntProperty")

    # create mqtt interface adapters for client side
    sink_testbed2many_param_interface = testbed2.mqtt.ManyParamInterfaceClientAdapter(client)
    sink_testbed2nested_struct1_interface = testbed2.mqtt.NestedStruct1InterfaceClientAdapter(client)
    sink_testbed2nested_struct2_interface = testbed2.mqtt.NestedStruct2InterfaceClientAdapter(client)
    sink_testbed2nested_struct3_interface = testbed2.mqtt.NestedStruct3InterfaceClientAdapter(client)
    sink_tb_enumenum_interface = tb_enum.mqtt.EnumInterfaceClientAdapter(client)
    sink_tb_same1same_struct1_interface = tb_same1.mqtt.SameStruct1InterfaceClientAdapter(client)
    sink_tb_same1same_struct2_interface = tb_same1.mqtt.SameStruct2InterfaceClientAdapter(client)
    sink_tb_same1same_enum1_interface = tb_same1.mqtt.SameEnum1InterfaceClientAdapter(client)
    sink_tb_same1same_enum2_interface = tb_same1.mqtt.SameEnum2InterfaceClientAdapter(client)
    sink_tb_same2same_struct1_interface = tb_same2.mqtt.SameStruct1InterfaceClientAdapter(client)
    sink_tb_same2same_struct2_interface = tb_same2.mqtt.SameStruct2InterfaceClientAdapter(client)
    sink_tb_same2same_enum1_interface = tb_same2.mqtt.SameEnum1InterfaceClientAdapter(client)
    sink_tb_same2same_enum2_interface = tb_same2.mqtt.SameEnum2InterfaceClientAdapter(client)
    sink_tb_simplevoid_interface = tb_simple.mqtt.VoidInterfaceClientAdapter(client)
    sink_tb_simplesimple_interface = tb_simple.mqtt.SimpleInterfaceClientAdapter(client)
    sink_tb_simplesimple_array_interface = tb_simple.mqtt.SimpleArrayInterfaceClientAdapter(client)
    sink_tb_simpleno_properties_interface = tb_simple.mqtt.NoPropertiesInterfaceClientAdapter(client)
    sink_tb_simpleno_operations_interface = tb_simple.mqtt.NoOperationsInterfaceClientAdapter(client)
    sink_tb_simpleno_signals_interface = tb_simple.mqtt.NoSignalsInterfaceClientAdapter(client)
    sink_testbed1struct_interface = testbed1.mqtt.StructInterfaceClientAdapter(client)
    sink_testbed1struct_array_interface = testbed1.mqtt.StructArrayInterfaceClientAdapter(client)
    sink_tb_namesnam_es = tb_names.mqtt.NamEsClientAdapter(client)
    sink_countercounter = counter.mqtt.CounterClientAdapter(client)
    sink_tb_emptyempty_interface = tb_empty.mqtt.EmptyInterfaceClientAdapter(client)
    await client.connect("localhost", 1883)

    
    # Try out properties: subscribe for changes
    def handleProperty(value):
        print("received property change");
        print(value);
    sink_testbed2many_param_interface.on_prop1_changed += handleProperty
    # or ask for change.
    # Have in mind that the value should be different than current (which probably is default) for the message to be sent
    local_prop1 = 0;
    sink_testbed2many_param_interface.set_prop1(local_prop1);
    
    # Check the signals with subscribing for its change
    def handleSignal(value):
        print("received signal");
        print(value);
    sink_testbed2many_param_interface.on_sig1 += handleSignal
    
    # Play around executing your operations
    result = sink_testbed2many_param_interface.func1(0)
    await result
    print("method reuslt")
    print(result)    
    
    input("Press Enter to close")

    client.disconnect()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())

