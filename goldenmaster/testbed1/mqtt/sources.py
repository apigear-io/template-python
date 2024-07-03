import apigear.mqtt
import utils.base_types
import testbed1.api
from utils.eventhook import EventHook
from typing import Any
import logging
class StructInterfaceServiceAdapter():
    def __init__(self, impl: testbed1.api.IStructInterface, service: apigear.mqtt.Service):
        self.service = service
        self.impl = impl
        self.impl.on_prop_bool_changed += self.notify_prop_bool_changed
        self.impl.on_prop_int_changed += self.notify_prop_int_changed
        self.impl.on_prop_float_changed += self.notify_prop_float_changed
        self.impl.on_prop_string_changed += self.notify_prop_string_changed
        self.impl.on_sig_bool += self.notify_sig_bool
        self.impl.on_sig_int += self.notify_sig_int
        self.impl.on_sig_float += self.notify_sig_float
        self.impl.on_sig_string += self.notify_sig_string
        self.service.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.service.subscribe_for_property("testbed1/StructInterface/set/propBool", self.__set_prop_bool)
        self.service.subscribe_for_property("testbed1/StructInterface/set/propInt", self.__set_prop_int)
        self.service.subscribe_for_property("testbed1/StructInterface/set/propFloat", self.__set_prop_float)
        self.service.subscribe_for_property("testbed1/StructInterface/set/propString", self.__set_prop_string)
        #TODO SUBSCRIBE FOR INVOKE TOPIC

    def __del__(self):
        self.service.on_connected -= self.subscribeForTopics
        self.service.unsubscribe("testbed1/StructInterface/set/propBool")
        self.service.unsubscribe("testbed1/StructInterface/set/propInt")
        self.service.unsubscribe("testbed1/StructInterface/set/propFloat")
        self.service.unsubscribe("testbed1/StructInterface/set/propString")
        #TODO UNSUBSCRIBE INVOKE TOPIC

    def notify_sig_bool(self, param_bool: testbed1.api.StructBool):
        _param_bool = testbed1.api.from_struct_bool(param_bool)
        args = [_param_bool]
        self.service.notify_signal("testbed1/StructInterface/sig/sigBool", args)

    def notify_sig_int(self, param_int: testbed1.api.StructInt):
        _param_int = testbed1.api.from_struct_int(param_int)
        args = [_param_int]
        self.service.notify_signal("testbed1/StructInterface/sig/sigInt", args)

    def notify_sig_float(self, param_float: testbed1.api.StructFloat):
        _param_float = testbed1.api.from_struct_float(param_float)
        args = [_param_float]
        self.service.notify_signal("testbed1/StructInterface/sig/sigFloat", args)

    def notify_sig_string(self, param_string: testbed1.api.StructString):
        _param_string = testbed1.api.from_struct_string(param_string)
        args = [_param_string]
        self.service.notify_signal("testbed1/StructInterface/sig/sigString", args)

    def notify_prop_bool_changed(self, value):
        v = testbed1.api.from_struct_bool(value)
        self.service.notify_property_change("testbed1/StructInterface/prop/propBool", v)

    def notify_prop_int_changed(self, value):
        v = testbed1.api.from_struct_int(value)
        self.service.notify_property_change("testbed1/StructInterface/prop/propInt", v)

    def notify_prop_float_changed(self, value):
        v = testbed1.api.from_struct_float(value)
        self.service.notify_property_change("testbed1/StructInterface/prop/propFloat", v)

    def notify_prop_string_changed(self, value):
        v = testbed1.api.from_struct_string(value)
        self.service.notify_property_change("testbed1/StructInterface/prop/propString", v)

    def __set_prop_bool(self, value: Any):
            v = testbed1.api.as_struct_bool(value)
            self.impl.set_prop_bool(v)

    def __set_prop_int(self, value: Any):
            v = testbed1.api.as_struct_int(value)
            self.impl.set_prop_int(v)

    def __set_prop_float(self, value: Any):
            v = testbed1.api.as_struct_float(value)
            self.impl.set_prop_float(v)

    def __set_prop_string(self, value: Any):
            v = testbed1.api.as_struct_string(value)
            self.impl.set_prop_string(v)
class StructArrayInterfaceServiceAdapter():
    def __init__(self, impl: testbed1.api.IStructArrayInterface, service: apigear.mqtt.Service):
        self.service = service
        self.impl = impl
        self.impl.on_prop_bool_changed += self.notify_prop_bool_changed
        self.impl.on_prop_int_changed += self.notify_prop_int_changed
        self.impl.on_prop_float_changed += self.notify_prop_float_changed
        self.impl.on_prop_string_changed += self.notify_prop_string_changed
        self.impl.on_sig_bool += self.notify_sig_bool
        self.impl.on_sig_int += self.notify_sig_int
        self.impl.on_sig_float += self.notify_sig_float
        self.impl.on_sig_string += self.notify_sig_string
        self.service.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.service.subscribe_for_property("testbed1/StructArrayInterface/set/propBool", self.__set_prop_bool)
        self.service.subscribe_for_property("testbed1/StructArrayInterface/set/propInt", self.__set_prop_int)
        self.service.subscribe_for_property("testbed1/StructArrayInterface/set/propFloat", self.__set_prop_float)
        self.service.subscribe_for_property("testbed1/StructArrayInterface/set/propString", self.__set_prop_string)
        #TODO SUBSCRIBE FOR INVOKE TOPIC

    def __del__(self):
        self.service.on_connected -= self.subscribeForTopics
        self.service.unsubscribe("testbed1/StructArrayInterface/set/propBool")
        self.service.unsubscribe("testbed1/StructArrayInterface/set/propInt")
        self.service.unsubscribe("testbed1/StructArrayInterface/set/propFloat")
        self.service.unsubscribe("testbed1/StructArrayInterface/set/propString")
        #TODO UNSUBSCRIBE INVOKE TOPIC

    def notify_sig_bool(self, param_bool: list[testbed1.api.StructBool]):
        _param_bool = [testbed1.api.api.from_struct_bool(_) for _ in param_bool]
        args = [_param_bool]
        self.service.notify_signal("testbed1/StructArrayInterface/sig/sigBool", args)

    def notify_sig_int(self, param_int: list[testbed1.api.StructInt]):
        _param_int = [testbed1.api.api.from_struct_int(_) for _ in param_int]
        args = [_param_int]
        self.service.notify_signal("testbed1/StructArrayInterface/sig/sigInt", args)

    def notify_sig_float(self, param_float: list[testbed1.api.StructFloat]):
        _param_float = [testbed1.api.api.from_struct_float(_) for _ in param_float]
        args = [_param_float]
        self.service.notify_signal("testbed1/StructArrayInterface/sig/sigFloat", args)

    def notify_sig_string(self, param_string: list[testbed1.api.StructString]):
        _param_string = [testbed1.api.api.from_struct_string(_) for _ in param_string]
        args = [_param_string]
        self.service.notify_signal("testbed1/StructArrayInterface/sig/sigString", args)

    def notify_prop_bool_changed(self, value):
        v = [testbed1.api.from_struct_bool(_) for _ in value]
        self.service.notify_property_change("testbed1/StructArrayInterface/prop/propBool", v)

    def notify_prop_int_changed(self, value):
        v = [testbed1.api.from_struct_int(_) for _ in value]
        self.service.notify_property_change("testbed1/StructArrayInterface/prop/propInt", v)

    def notify_prop_float_changed(self, value):
        v = [testbed1.api.from_struct_float(_) for _ in value]
        self.service.notify_property_change("testbed1/StructArrayInterface/prop/propFloat", v)

    def notify_prop_string_changed(self, value):
        v = [testbed1.api.from_struct_string(_) for _ in value]
        self.service.notify_property_change("testbed1/StructArrayInterface/prop/propString", v)

    def __set_prop_bool(self, value: Any):
            v = [testbed1.api.as_struct_bool(_) for _ in value]
            self.impl.set_prop_bool(v)

    def __set_prop_int(self, value: Any):
            v = [testbed1.api.as_struct_int(_) for _ in value]
            self.impl.set_prop_int(v)

    def __set_prop_float(self, value: Any):
            v = [testbed1.api.as_struct_float(_) for _ in value]
            self.impl.set_prop_float(v)

    def __set_prop_string(self, value: Any):
            v = [testbed1.api.as_struct_string(_) for _ in value]
            self.impl.set_prop_string(v)
