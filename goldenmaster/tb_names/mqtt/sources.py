import apigear.mqtt
import utils.base_types
import tb_names.api
from utils.eventhook import EventHook
from typing import Any
import logging
class NamEsServiceAdapter():
    def __init__(self, impl: tb_names.api.INamEs, service: apigear.mqtt.Service):
        self.service = service
        self.impl = impl
        self.impl.on_switch_changed += self.notify_switch_changed
        self.impl.on_some_property_changed += self.notify_some_property_changed
        self.impl.on_some_poperty2_changed += self.notify_some_poperty2_changed
        self.impl.on_some_signal += self.notify_some_signal
        self.impl.on_some_signal2 += self.notify_some_signal2
        self.service.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.service.subscribe_for_property("tb.names/Nam_Es/set/Switch", self.__set_switch)
        self.service.subscribe_for_property("tb.names/Nam_Es/set/SOME_PROPERTY", self.__set_some_property)
        self.service.subscribe_for_property("tb.names/Nam_Es/set/Some_Poperty2", self.__set_some_poperty2)
        #TODO SUBSCRIBE FOR INVOKE TOPIC

    def __del__(self):
        self.service.on_connected -= self.subscribeForTopics
        self.service.unsubscribe("tb.names/Nam_Es/set/Switch")
        self.service.unsubscribe("tb.names/Nam_Es/set/SOME_PROPERTY")
        self.service.unsubscribe("tb.names/Nam_Es/set/Some_Poperty2")
        #TODO UNSUBSCRIBE INVOKE TOPIC

    def notify_some_signal(self, some_param: bool):
        _some_param = utils.base_types.from_bool(some_param)
        args = [_some_param]
        self.service.notify_signal("tb.names/Nam_Es/sig/SOME_SIGNAL", args)

    def notify_some_signal2(self, some_param: bool):
        _some_param = utils.base_types.from_bool(some_param)
        args = [_some_param]
        self.service.notify_signal("tb.names/Nam_Es/sig/Some_Signal2", args)

    def notify_switch_changed(self, value):
        v = utils.base_types.from_bool(value)
        self.service.notify_property_change("tb.names/Nam_Es/prop/Switch", v)

    def notify_some_property_changed(self, value):
        v = utils.base_types.from_int(value)
        self.service.notify_property_change("tb.names/Nam_Es/prop/SOME_PROPERTY", v)

    def notify_some_poperty2_changed(self, value):
        v = utils.base_types.from_int(value)
        self.service.notify_property_change("tb.names/Nam_Es/prop/Some_Poperty2", v)

    def __set_switch(self, value: Any):
            v = utils.base_types.as_bool(value)
            self.impl.set_switch(v)

    def __set_some_property(self, value: Any):
            v = utils.base_types.as_int(value)
            self.impl.set_some_property(v)

    def __set_some_poperty2(self, value: Any):
            v = utils.base_types.as_int(value)
            self.impl.set_some_poperty2(v)
