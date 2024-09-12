import apigear.mqtt
import utils.base_types
import testbed2.api
from utils.eventhook import EventHook
from typing import Any
import logging
class ManyParamInterfaceServiceAdapter():
    def __init__(self, impl: testbed2.api.IManyParamInterface, service: apigear.mqtt.Service):
        self.service = service
        self.impl = impl
        self.impl.on_prop1_changed += self.notify_prop1_changed
        self.impl.on_prop2_changed += self.notify_prop2_changed
        self.impl.on_prop3_changed += self.notify_prop3_changed
        self.impl.on_prop4_changed += self.notify_prop4_changed
        self.impl.on_sig1 += self.notify_sig1
        self.impl.on_sig2 += self.notify_sig2
        self.impl.on_sig3 += self.notify_sig3
        self.impl.on_sig4 += self.notify_sig4
        self.service.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.service.subscribe_for_property("testbed2/ManyParamInterface/set/prop1", self.__set_prop1)
        self.service.subscribe_for_property("testbed2/ManyParamInterface/set/prop2", self.__set_prop2)
        self.service.subscribe_for_property("testbed2/ManyParamInterface/set/prop3", self.__set_prop3)
        self.service.subscribe_for_property("testbed2/ManyParamInterface/set/prop4", self.__set_prop4)
        self.service.subscribe_for_invoke_req("testbed2/ManyParamInterface/rpc/func1", self.__invoke_func1)
        self.service.subscribe_for_invoke_req("testbed2/ManyParamInterface/rpc/func2", self.__invoke_func2)
        self.service.subscribe_for_invoke_req("testbed2/ManyParamInterface/rpc/func3", self.__invoke_func3)
        self.service.subscribe_for_invoke_req("testbed2/ManyParamInterface/rpc/func4", self.__invoke_func4)

    def __del__(self):
        self.service.on_connected -= self.subscribeForTopics
        self.service.unsubscribe("testbed2/ManyParamInterface/set/prop1")
        self.service.unsubscribe("testbed2/ManyParamInterface/set/prop2")
        self.service.unsubscribe("testbed2/ManyParamInterface/set/prop3")
        self.service.unsubscribe("testbed2/ManyParamInterface/set/prop4")
        self.service.unsubscribe("testbed2/ManyParamInterface/rpc/func1")
        self.service.unsubscribe("testbed2/ManyParamInterface/rpc/func2")
        self.service.unsubscribe("testbed2/ManyParamInterface/rpc/func3")
        self.service.unsubscribe("testbed2/ManyParamInterface/rpc/func4")
        self.impl.on_prop1_changed -= self.notify_prop1_changed
        self.impl.on_prop2_changed -= self.notify_prop2_changed
        self.impl.on_prop3_changed -= self.notify_prop3_changed
        self.impl.on_prop4_changed -= self.notify_prop4_changed
        self.impl.on_sig1 -= self.notify_sig1
        self.impl.on_sig2 -= self.notify_sig2
        self.impl.on_sig3 -= self.notify_sig3
        self.impl.on_sig4 -= self.notify_sig4

    def notify_sig1(self, param1: int):
        _param1 = utils.base_types.from_int(param1)
        args = [_param1]
        self.service.notify_signal("testbed2/ManyParamInterface/sig/sig1", args)

    def notify_sig2(self, param1: int, param2: int):
        _param1 = utils.base_types.from_int(param1)
        _param2 = utils.base_types.from_int(param2)
        args = [_param1, _param2]
        self.service.notify_signal("testbed2/ManyParamInterface/sig/sig2", args)

    def notify_sig3(self, param1: int, param2: int, param3: int):
        _param1 = utils.base_types.from_int(param1)
        _param2 = utils.base_types.from_int(param2)
        _param3 = utils.base_types.from_int(param3)
        args = [_param1, _param2, _param3]
        self.service.notify_signal("testbed2/ManyParamInterface/sig/sig3", args)

    def notify_sig4(self, param1: int, param2: int, param3: int, param4: int):
        _param1 = utils.base_types.from_int(param1)
        _param2 = utils.base_types.from_int(param2)
        _param3 = utils.base_types.from_int(param3)
        _param4 = utils.base_types.from_int(param4)
        args = [_param1, _param2, _param3, _param4]
        self.service.notify_signal("testbed2/ManyParamInterface/sig/sig4", args)

    def notify_prop1_changed(self, value):
        v = utils.base_types.from_int(value)
        self.service.notify_property_change("testbed2/ManyParamInterface/prop/prop1", v)

    def notify_prop2_changed(self, value):
        v = utils.base_types.from_int(value)
        self.service.notify_property_change("testbed2/ManyParamInterface/prop/prop2", v)

    def notify_prop3_changed(self, value):
        v = utils.base_types.from_int(value)
        self.service.notify_property_change("testbed2/ManyParamInterface/prop/prop3", v)

    def notify_prop4_changed(self, value):
        v = utils.base_types.from_int(value)
        self.service.notify_property_change("testbed2/ManyParamInterface/prop/prop4", v)

    def __set_prop1(self, value: Any):
            v = utils.base_types.as_int(value)
            self.impl.set_prop1(v)

    def __set_prop2(self, value: Any):
            v = utils.base_types.as_int(value)
            self.impl.set_prop2(v)

    def __set_prop3(self, value: Any):
            v = utils.base_types.as_int(value)
            self.impl.set_prop3(v)

    def __set_prop4(self, value: Any):
            v = utils.base_types.as_int(value)
            self.impl.set_prop4(v)

    def __invoke_func1(self, args: list[Any]) -> Any:
        param1 = utils.base_types.as_int(args[0])
        reply = self.impl.func1(param1)
        return utils.base_types.from_int(reply)

    def __invoke_func2(self, args: list[Any]) -> Any:
        param1 = utils.base_types.as_int(args[0])
        param2 = utils.base_types.as_int(args[1])
        reply = self.impl.func2(param1, param2)
        return utils.base_types.from_int(reply)

    def __invoke_func3(self, args: list[Any]) -> Any:
        param1 = utils.base_types.as_int(args[0])
        param2 = utils.base_types.as_int(args[1])
        param3 = utils.base_types.as_int(args[2])
        reply = self.impl.func3(param1, param2, param3)
        return utils.base_types.from_int(reply)

    def __invoke_func4(self, args: list[Any]) -> Any:
        param1 = utils.base_types.as_int(args[0])
        param2 = utils.base_types.as_int(args[1])
        param3 = utils.base_types.as_int(args[2])
        param4 = utils.base_types.as_int(args[3])
        reply = self.impl.func4(param1, param2, param3, param4)
        return utils.base_types.from_int(reply)
class NestedStruct1InterfaceServiceAdapter():
    def __init__(self, impl: testbed2.api.INestedStruct1Interface, service: apigear.mqtt.Service):
        self.service = service
        self.impl = impl
        self.impl.on_prop1_changed += self.notify_prop1_changed
        self.impl.on_sig1 += self.notify_sig1
        self.service.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.service.subscribe_for_property("testbed2/NestedStruct1Interface/set/prop1", self.__set_prop1)
        self.service.subscribe_for_invoke_req("testbed2/NestedStruct1Interface/rpc/func1", self.__invoke_func1)

    def __del__(self):
        self.service.on_connected -= self.subscribeForTopics
        self.service.unsubscribe("testbed2/NestedStruct1Interface/set/prop1")
        self.service.unsubscribe("testbed2/NestedStruct1Interface/rpc/func1")
        self.impl.on_prop1_changed -= self.notify_prop1_changed
        self.impl.on_sig1 -= self.notify_sig1

    def notify_sig1(self, param1: testbed2.api.NestedStruct1):
        _param1 = testbed2.api.from_nested_struct1(param1)
        args = [_param1]
        self.service.notify_signal("testbed2/NestedStruct1Interface/sig/sig1", args)

    def notify_prop1_changed(self, value):
        v = testbed2.api.from_nested_struct1(value)
        self.service.notify_property_change("testbed2/NestedStruct1Interface/prop/prop1", v)

    def __set_prop1(self, value: Any):
            v = testbed2.api.as_nested_struct1(value)
            self.impl.set_prop1(v)

    def __invoke_func1(self, args: list[Any]) -> Any:
        param1 = testbed2.api.as_nested_struct1(args[0])
        reply = self.impl.func1(param1)
        return testbed2.api.from_nested_struct1(reply)
class NestedStruct2InterfaceServiceAdapter():
    def __init__(self, impl: testbed2.api.INestedStruct2Interface, service: apigear.mqtt.Service):
        self.service = service
        self.impl = impl
        self.impl.on_prop1_changed += self.notify_prop1_changed
        self.impl.on_prop2_changed += self.notify_prop2_changed
        self.impl.on_sig1 += self.notify_sig1
        self.impl.on_sig2 += self.notify_sig2
        self.service.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.service.subscribe_for_property("testbed2/NestedStruct2Interface/set/prop1", self.__set_prop1)
        self.service.subscribe_for_property("testbed2/NestedStruct2Interface/set/prop2", self.__set_prop2)
        self.service.subscribe_for_invoke_req("testbed2/NestedStruct2Interface/rpc/func1", self.__invoke_func1)
        self.service.subscribe_for_invoke_req("testbed2/NestedStruct2Interface/rpc/func2", self.__invoke_func2)

    def __del__(self):
        self.service.on_connected -= self.subscribeForTopics
        self.service.unsubscribe("testbed2/NestedStruct2Interface/set/prop1")
        self.service.unsubscribe("testbed2/NestedStruct2Interface/set/prop2")
        self.service.unsubscribe("testbed2/NestedStruct2Interface/rpc/func1")
        self.service.unsubscribe("testbed2/NestedStruct2Interface/rpc/func2")
        self.impl.on_prop1_changed -= self.notify_prop1_changed
        self.impl.on_prop2_changed -= self.notify_prop2_changed
        self.impl.on_sig1 -= self.notify_sig1
        self.impl.on_sig2 -= self.notify_sig2

    def notify_sig1(self, param1: testbed2.api.NestedStruct1):
        _param1 = testbed2.api.from_nested_struct1(param1)
        args = [_param1]
        self.service.notify_signal("testbed2/NestedStruct2Interface/sig/sig1", args)

    def notify_sig2(self, param1: testbed2.api.NestedStruct1, param2: testbed2.api.NestedStruct2):
        _param1 = testbed2.api.from_nested_struct1(param1)
        _param2 = testbed2.api.from_nested_struct2(param2)
        args = [_param1, _param2]
        self.service.notify_signal("testbed2/NestedStruct2Interface/sig/sig2", args)

    def notify_prop1_changed(self, value):
        v = testbed2.api.from_nested_struct1(value)
        self.service.notify_property_change("testbed2/NestedStruct2Interface/prop/prop1", v)

    def notify_prop2_changed(self, value):
        v = testbed2.api.from_nested_struct2(value)
        self.service.notify_property_change("testbed2/NestedStruct2Interface/prop/prop2", v)

    def __set_prop1(self, value: Any):
            v = testbed2.api.as_nested_struct1(value)
            self.impl.set_prop1(v)

    def __set_prop2(self, value: Any):
            v = testbed2.api.as_nested_struct2(value)
            self.impl.set_prop2(v)

    def __invoke_func1(self, args: list[Any]) -> Any:
        param1 = testbed2.api.as_nested_struct1(args[0])
        reply = self.impl.func1(param1)
        return testbed2.api.from_nested_struct1(reply)

    def __invoke_func2(self, args: list[Any]) -> Any:
        param1 = testbed2.api.as_nested_struct1(args[0])
        param2 = testbed2.api.as_nested_struct2(args[1])
        reply = self.impl.func2(param1, param2)
        return testbed2.api.from_nested_struct1(reply)
class NestedStruct3InterfaceServiceAdapter():
    def __init__(self, impl: testbed2.api.INestedStruct3Interface, service: apigear.mqtt.Service):
        self.service = service
        self.impl = impl
        self.impl.on_prop1_changed += self.notify_prop1_changed
        self.impl.on_prop2_changed += self.notify_prop2_changed
        self.impl.on_prop3_changed += self.notify_prop3_changed
        self.impl.on_sig1 += self.notify_sig1
        self.impl.on_sig2 += self.notify_sig2
        self.impl.on_sig3 += self.notify_sig3
        self.service.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.service.subscribe_for_property("testbed2/NestedStruct3Interface/set/prop1", self.__set_prop1)
        self.service.subscribe_for_property("testbed2/NestedStruct3Interface/set/prop2", self.__set_prop2)
        self.service.subscribe_for_property("testbed2/NestedStruct3Interface/set/prop3", self.__set_prop3)
        self.service.subscribe_for_invoke_req("testbed2/NestedStruct3Interface/rpc/func1", self.__invoke_func1)
        self.service.subscribe_for_invoke_req("testbed2/NestedStruct3Interface/rpc/func2", self.__invoke_func2)
        self.service.subscribe_for_invoke_req("testbed2/NestedStruct3Interface/rpc/func3", self.__invoke_func3)

    def __del__(self):
        self.service.on_connected -= self.subscribeForTopics
        self.service.unsubscribe("testbed2/NestedStruct3Interface/set/prop1")
        self.service.unsubscribe("testbed2/NestedStruct3Interface/set/prop2")
        self.service.unsubscribe("testbed2/NestedStruct3Interface/set/prop3")
        self.service.unsubscribe("testbed2/NestedStruct3Interface/rpc/func1")
        self.service.unsubscribe("testbed2/NestedStruct3Interface/rpc/func2")
        self.service.unsubscribe("testbed2/NestedStruct3Interface/rpc/func3")
        self.impl.on_prop1_changed -= self.notify_prop1_changed
        self.impl.on_prop2_changed -= self.notify_prop2_changed
        self.impl.on_prop3_changed -= self.notify_prop3_changed
        self.impl.on_sig1 -= self.notify_sig1
        self.impl.on_sig2 -= self.notify_sig2
        self.impl.on_sig3 -= self.notify_sig3

    def notify_sig1(self, param1: testbed2.api.NestedStruct1):
        _param1 = testbed2.api.from_nested_struct1(param1)
        args = [_param1]
        self.service.notify_signal("testbed2/NestedStruct3Interface/sig/sig1", args)

    def notify_sig2(self, param1: testbed2.api.NestedStruct1, param2: testbed2.api.NestedStruct2):
        _param1 = testbed2.api.from_nested_struct1(param1)
        _param2 = testbed2.api.from_nested_struct2(param2)
        args = [_param1, _param2]
        self.service.notify_signal("testbed2/NestedStruct3Interface/sig/sig2", args)

    def notify_sig3(self, param1: testbed2.api.NestedStruct1, param2: testbed2.api.NestedStruct2, param3: testbed2.api.NestedStruct3):
        _param1 = testbed2.api.from_nested_struct1(param1)
        _param2 = testbed2.api.from_nested_struct2(param2)
        _param3 = testbed2.api.from_nested_struct3(param3)
        args = [_param1, _param2, _param3]
        self.service.notify_signal("testbed2/NestedStruct3Interface/sig/sig3", args)

    def notify_prop1_changed(self, value):
        v = testbed2.api.from_nested_struct1(value)
        self.service.notify_property_change("testbed2/NestedStruct3Interface/prop/prop1", v)

    def notify_prop2_changed(self, value):
        v = testbed2.api.from_nested_struct2(value)
        self.service.notify_property_change("testbed2/NestedStruct3Interface/prop/prop2", v)

    def notify_prop3_changed(self, value):
        v = testbed2.api.from_nested_struct3(value)
        self.service.notify_property_change("testbed2/NestedStruct3Interface/prop/prop3", v)

    def __set_prop1(self, value: Any):
            v = testbed2.api.as_nested_struct1(value)
            self.impl.set_prop1(v)

    def __set_prop2(self, value: Any):
            v = testbed2.api.as_nested_struct2(value)
            self.impl.set_prop2(v)

    def __set_prop3(self, value: Any):
            v = testbed2.api.as_nested_struct3(value)
            self.impl.set_prop3(v)

    def __invoke_func1(self, args: list[Any]) -> Any:
        param1 = testbed2.api.as_nested_struct1(args[0])
        reply = self.impl.func1(param1)
        return testbed2.api.from_nested_struct1(reply)

    def __invoke_func2(self, args: list[Any]) -> Any:
        param1 = testbed2.api.as_nested_struct1(args[0])
        param2 = testbed2.api.as_nested_struct2(args[1])
        reply = self.impl.func2(param1, param2)
        return testbed2.api.from_nested_struct1(reply)

    def __invoke_func3(self, args: list[Any]) -> Any:
        param1 = testbed2.api.as_nested_struct1(args[0])
        param2 = testbed2.api.as_nested_struct2(args[1])
        param3 = testbed2.api.as_nested_struct3(args[2])
        reply = self.impl.func3(param1, param2, param3)
        return testbed2.api.from_nested_struct1(reply)
