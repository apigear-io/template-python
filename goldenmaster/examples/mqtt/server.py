import asyncio
import logging
import os
import sys

#add context - paths to modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import apigear.mqtt
import counter.api
import counter.impl
import counter.mqtt
import custom_types.api
import custom_types.impl
import custom_types.mqtt
import extern_types.api
import extern_types.impl
import extern_types.mqtt
import tb_empty.api
import tb_empty.impl
import tb_empty.mqtt
import tb_enum.api
import tb_enum.impl
import tb_enum.mqtt
import tb_names.api
import tb_names.impl
import tb_names.mqtt
import tb_same1.api
import tb_same1.impl
import tb_same1.mqtt
import tb_same2.api
import tb_same2.impl
import tb_same2.mqtt
import tb_simple.api
import tb_simple.impl
import tb_simple.mqtt
import testbed1.api
import testbed1.impl
import testbed1.mqtt
import testbed2.api
import testbed2.impl
import testbed2.mqtt
import vector3d.vector


# set default log level to INFO and above
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

# REMEMBER TO RUN A BROKER OF YOUR CHOICE
async def main():
    service = apigear.mqtt.Service("uniqueServiceIdTestIntProperty")
    source_testbed2_many_param_interface = testbed2.impl.ManyParamInterface()
    serviceAdapter_testbed2_many_param_interface = testbed2.mqtt.ManyParamInterfaceServiceAdapter(source_testbed2_many_param_interface, service)
    source_testbed2_nested_struct1_interface = testbed2.impl.NestedStruct1Interface()
    serviceAdapter_testbed2_nested_struct1_interface = testbed2.mqtt.NestedStruct1InterfaceServiceAdapter(source_testbed2_nested_struct1_interface, service)
    source_testbed2_nested_struct2_interface = testbed2.impl.NestedStruct2Interface()
    serviceAdapter_testbed2_nested_struct2_interface = testbed2.mqtt.NestedStruct2InterfaceServiceAdapter(source_testbed2_nested_struct2_interface, service)
    source_testbed2_nested_struct3_interface = testbed2.impl.NestedStruct3Interface()
    serviceAdapter_testbed2_nested_struct3_interface = testbed2.mqtt.NestedStruct3InterfaceServiceAdapter(source_testbed2_nested_struct3_interface, service)

    source_tb_enum_enum_interface = tb_enum.impl.EnumInterface()
    serviceAdapter_tb_enum_enum_interface = tb_enum.mqtt.EnumInterfaceServiceAdapter(source_tb_enum_enum_interface, service)

    source_tb_same1_same_struct1_interface = tb_same1.impl.SameStruct1Interface()
    serviceAdapter_tb_same1_same_struct1_interface = tb_same1.mqtt.SameStruct1InterfaceServiceAdapter(source_tb_same1_same_struct1_interface, service)
    source_tb_same1_same_struct2_interface = tb_same1.impl.SameStruct2Interface()
    serviceAdapter_tb_same1_same_struct2_interface = tb_same1.mqtt.SameStruct2InterfaceServiceAdapter(source_tb_same1_same_struct2_interface, service)
    source_tb_same1_same_enum1_interface = tb_same1.impl.SameEnum1Interface()
    serviceAdapter_tb_same1_same_enum1_interface = tb_same1.mqtt.SameEnum1InterfaceServiceAdapter(source_tb_same1_same_enum1_interface, service)
    source_tb_same1_same_enum2_interface = tb_same1.impl.SameEnum2Interface()
    serviceAdapter_tb_same1_same_enum2_interface = tb_same1.mqtt.SameEnum2InterfaceServiceAdapter(source_tb_same1_same_enum2_interface, service)

    source_tb_same2_same_struct1_interface = tb_same2.impl.SameStruct1Interface()
    serviceAdapter_tb_same2_same_struct1_interface = tb_same2.mqtt.SameStruct1InterfaceServiceAdapter(source_tb_same2_same_struct1_interface, service)
    source_tb_same2_same_struct2_interface = tb_same2.impl.SameStruct2Interface()
    serviceAdapter_tb_same2_same_struct2_interface = tb_same2.mqtt.SameStruct2InterfaceServiceAdapter(source_tb_same2_same_struct2_interface, service)
    source_tb_same2_same_enum1_interface = tb_same2.impl.SameEnum1Interface()
    serviceAdapter_tb_same2_same_enum1_interface = tb_same2.mqtt.SameEnum1InterfaceServiceAdapter(source_tb_same2_same_enum1_interface, service)
    source_tb_same2_same_enum2_interface = tb_same2.impl.SameEnum2Interface()
    serviceAdapter_tb_same2_same_enum2_interface = tb_same2.mqtt.SameEnum2InterfaceServiceAdapter(source_tb_same2_same_enum2_interface, service)

    source_tb_simple_void_interface = tb_simple.impl.VoidInterface()
    serviceAdapter_tb_simple_void_interface = tb_simple.mqtt.VoidInterfaceServiceAdapter(source_tb_simple_void_interface, service)
    source_tb_simple_simple_interface = tb_simple.impl.SimpleInterface()
    serviceAdapter_tb_simple_simple_interface = tb_simple.mqtt.SimpleInterfaceServiceAdapter(source_tb_simple_simple_interface, service)
    source_tb_simple_simple_array_interface = tb_simple.impl.SimpleArrayInterface()
    serviceAdapter_tb_simple_simple_array_interface = tb_simple.mqtt.SimpleArrayInterfaceServiceAdapter(source_tb_simple_simple_array_interface, service)
    source_tb_simple_no_properties_interface = tb_simple.impl.NoPropertiesInterface()
    serviceAdapter_tb_simple_no_properties_interface = tb_simple.mqtt.NoPropertiesInterfaceServiceAdapter(source_tb_simple_no_properties_interface, service)
    source_tb_simple_no_operations_interface = tb_simple.impl.NoOperationsInterface()
    serviceAdapter_tb_simple_no_operations_interface = tb_simple.mqtt.NoOperationsInterfaceServiceAdapter(source_tb_simple_no_operations_interface, service)
    source_tb_simple_no_signals_interface = tb_simple.impl.NoSignalsInterface()
    serviceAdapter_tb_simple_no_signals_interface = tb_simple.mqtt.NoSignalsInterfaceServiceAdapter(source_tb_simple_no_signals_interface, service)

    source_testbed1_struct_interface = testbed1.impl.StructInterface()
    serviceAdapter_testbed1_struct_interface = testbed1.mqtt.StructInterfaceServiceAdapter(source_testbed1_struct_interface, service)
    source_testbed1_struct_array_interface = testbed1.impl.StructArrayInterface()
    serviceAdapter_testbed1_struct_array_interface = testbed1.mqtt.StructArrayInterfaceServiceAdapter(source_testbed1_struct_array_interface, service)

    source_tb_names_nam_es = tb_names.impl.NamEs()
    serviceAdapter_tb_names_nam_es = tb_names.mqtt.NamEsServiceAdapter(source_tb_names_nam_es, service)



    source_counter_counter = counter.impl.Counter()
    serviceAdapter_counter_counter = counter.mqtt.CounterServiceAdapter(source_counter_counter, service)

    source_tb_empty_empty_interface = tb_empty.impl.EmptyInterface()
    serviceAdapter_tb_empty_empty_interface = tb_empty.mqtt.EmptyInterfaceServiceAdapter(source_tb_empty_empty_interface, service)


    await service.connect("localhost", 1883)
    # do some actions here, wait for messages, send messages like:
    
    # You can add local handlers for property handling
    def handleProperty(value):
        print("property changed");
        print(value);
    source_testbed2_many_param_interface.on_prop1_changed += handleProperty
    # Set property, the change will be sent to all clients, and local handlers
    # Have in mind that the value should be different than current (which probably is default) for the message to be sent
    local_prop1 = 0;
    source_testbed2_many_param_interface.set_prop1(local_prop1);
    
    # Emit the signal, it will be sent to all clients
    def handleSignal(value):
        print("received signal");
        print(value);
    source_testbed2_many_param_interface.on_sig1 += handleSignal
    source_testbed2_many_param_interface._sig1(0)
    
    input("Press Enter to close")
    service.disconnect()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())

