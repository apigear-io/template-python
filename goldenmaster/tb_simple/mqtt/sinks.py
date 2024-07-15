import asyncio
from typing import Any
import apigear.mqtt
from utils.eventhook import EventHook
import utils.base_types
import tb_simple.api
import logging

class VoidInterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self.on_sig_void = EventHook()
        self.client.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.client.subscribe_for_signal("tb.simple/VoidInterface/sig/sigVoid",  self.__on_sig_void_signal)
        #TODO SUBSCRIBE FOR INVOKE RESP TOPIC

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.unsubscribe("tb.simple/VoidInterface/sig/sigVoid")
        #TODO UNSUBSCRIBE INVOKE RESP TOPIC

    # internal functions on message handle

    def __on_sig_void_signal(self, args: list[Any]):
        self.on_sig_void.fire()
        return

class SimpleInterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self._prop_bool = False
        self.on_prop_bool_changed = EventHook()
        self._prop_int = 0
        self.on_prop_int_changed = EventHook()
        self._prop_int32 = 0
        self.on_prop_int32_changed = EventHook()
        self._prop_int64 = 0
        self.on_prop_int64_changed = EventHook()
        self._prop_float = 0.0
        self.on_prop_float_changed = EventHook()
        self._prop_float32 = 0.0
        self.on_prop_float32_changed = EventHook()
        self._prop_float64 = 0.0
        self.on_prop_float64_changed = EventHook()
        self._prop_string = ""
        self.on_prop_string_changed = EventHook()
        self.on_sig_bool = EventHook()
        self.on_sig_int = EventHook()
        self.on_sig_int32 = EventHook()
        self.on_sig_int64 = EventHook()
        self.on_sig_float = EventHook()
        self.on_sig_float32 = EventHook()
        self.on_sig_float64 = EventHook()
        self.on_sig_string = EventHook()
        self.client.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.client.subscribe_for_property("tb.simple/SimpleInterface/prop/propBool", self.__set_prop_bool)
        self.client.subscribe_for_property("tb.simple/SimpleInterface/prop/propInt", self.__set_prop_int)
        self.client.subscribe_for_property("tb.simple/SimpleInterface/prop/propInt32", self.__set_prop_int32)
        self.client.subscribe_for_property("tb.simple/SimpleInterface/prop/propInt64", self.__set_prop_int64)
        self.client.subscribe_for_property("tb.simple/SimpleInterface/prop/propFloat", self.__set_prop_float)
        self.client.subscribe_for_property("tb.simple/SimpleInterface/prop/propFloat32", self.__set_prop_float32)
        self.client.subscribe_for_property("tb.simple/SimpleInterface/prop/propFloat64", self.__set_prop_float64)
        self.client.subscribe_for_property("tb.simple/SimpleInterface/prop/propString", self.__set_prop_string)
        self.client.subscribe_for_signal("tb.simple/SimpleInterface/sig/sigBool",  self.__on_sig_bool_signal)
        self.client.subscribe_for_signal("tb.simple/SimpleInterface/sig/sigInt",  self.__on_sig_int_signal)
        self.client.subscribe_for_signal("tb.simple/SimpleInterface/sig/sigInt32",  self.__on_sig_int32_signal)
        self.client.subscribe_for_signal("tb.simple/SimpleInterface/sig/sigInt64",  self.__on_sig_int64_signal)
        self.client.subscribe_for_signal("tb.simple/SimpleInterface/sig/sigFloat",  self.__on_sig_float_signal)
        self.client.subscribe_for_signal("tb.simple/SimpleInterface/sig/sigFloat32",  self.__on_sig_float32_signal)
        self.client.subscribe_for_signal("tb.simple/SimpleInterface/sig/sigFloat64",  self.__on_sig_float64_signal)
        self.client.subscribe_for_signal("tb.simple/SimpleInterface/sig/sigString",  self.__on_sig_string_signal)
        #TODO SUBSCRIBE FOR INVOKE RESP TOPIC

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.unsubscribe("tb.simple/SimpleInterface/prop/propBool")
        self.client.unsubscribe("tb.simple/SimpleInterface/prop/propInt")
        self.client.unsubscribe("tb.simple/SimpleInterface/prop/propInt32")
        self.client.unsubscribe("tb.simple/SimpleInterface/prop/propInt64")
        self.client.unsubscribe("tb.simple/SimpleInterface/prop/propFloat")
        self.client.unsubscribe("tb.simple/SimpleInterface/prop/propFloat32")
        self.client.unsubscribe("tb.simple/SimpleInterface/prop/propFloat64")
        self.client.unsubscribe("tb.simple/SimpleInterface/prop/propString")
        self.client.unsubscribe("tb.simple/SimpleInterface/sig/sigBool")
        self.client.unsubscribe("tb.simple/SimpleInterface/sig/sigInt")
        self.client.unsubscribe("tb.simple/SimpleInterface/sig/sigInt32")
        self.client.unsubscribe("tb.simple/SimpleInterface/sig/sigInt64")
        self.client.unsubscribe("tb.simple/SimpleInterface/sig/sigFloat")
        self.client.unsubscribe("tb.simple/SimpleInterface/sig/sigFloat32")
        self.client.unsubscribe("tb.simple/SimpleInterface/sig/sigFloat64")
        self.client.unsubscribe("tb.simple/SimpleInterface/sig/sigString")
        #TODO UNSUBSCRIBE INVOKE RESP TOPIC

    def set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        topic = "tb.simple/SimpleInterface/set/propBool"
        self.client.set_remote_property(topic, utils.base_types.from_bool(value))

    def get_prop_bool(self):
        return self._prop_bool

    def set_prop_int(self, value):
        if self._prop_int == value:
            return
        topic = "tb.simple/SimpleInterface/set/propInt"
        self.client.set_remote_property(topic, utils.base_types.from_int(value))

    def get_prop_int(self):
        return self._prop_int

    def set_prop_int32(self, value):
        if self._prop_int32 == value:
            return
        topic = "tb.simple/SimpleInterface/set/propInt32"
        self.client.set_remote_property(topic, utils.base_types.from_int32(value))

    def get_prop_int32(self):
        return self._prop_int32

    def set_prop_int64(self, value):
        if self._prop_int64 == value:
            return
        topic = "tb.simple/SimpleInterface/set/propInt64"
        self.client.set_remote_property(topic, utils.base_types.from_int64(value))

    def get_prop_int64(self):
        return self._prop_int64

    def set_prop_float(self, value):
        if self._prop_float == value:
            return
        topic = "tb.simple/SimpleInterface/set/propFloat"
        self.client.set_remote_property(topic, utils.base_types.from_float(value))

    def get_prop_float(self):
        return self._prop_float

    def set_prop_float32(self, value):
        if self._prop_float32 == value:
            return
        topic = "tb.simple/SimpleInterface/set/propFloat32"
        self.client.set_remote_property(topic, utils.base_types.from_float32(value))

    def get_prop_float32(self):
        return self._prop_float32

    def set_prop_float64(self, value):
        if self._prop_float64 == value:
            return
        topic = "tb.simple/SimpleInterface/set/propFloat64"
        self.client.set_remote_property(topic, utils.base_types.from_float64(value))

    def get_prop_float64(self):
        return self._prop_float64

    def set_prop_string(self, value):
        if self._prop_string == value:
            return
        topic = "tb.simple/SimpleInterface/set/propString"
        self.client.set_remote_property(topic, utils.base_types.from_string(value))

    def get_prop_string(self):
        return self._prop_string

    # internal functions on message handle

    def __set_prop_bool(self, data):
        value =  utils.base_types.as_bool(data)
        if self._prop_bool == value:
            return
        self._prop_bool = value
        self.on_prop_bool_changed.fire(self._prop_bool)

    def __set_prop_int(self, data):
        value =  utils.base_types.as_int(data)
        if self._prop_int == value:
            return
        self._prop_int = value
        self.on_prop_int_changed.fire(self._prop_int)

    def __set_prop_int32(self, data):
        value =  utils.base_types.as_int32(data)
        if self._prop_int32 == value:
            return
        self._prop_int32 = value
        self.on_prop_int32_changed.fire(self._prop_int32)

    def __set_prop_int64(self, data):
        value =  utils.base_types.as_int64(data)
        if self._prop_int64 == value:
            return
        self._prop_int64 = value
        self.on_prop_int64_changed.fire(self._prop_int64)

    def __set_prop_float(self, data):
        value =  utils.base_types.as_float(data)
        if self._prop_float == value:
            return
        self._prop_float = value
        self.on_prop_float_changed.fire(self._prop_float)

    def __set_prop_float32(self, data):
        value =  utils.base_types.as_float32(data)
        if self._prop_float32 == value:
            return
        self._prop_float32 = value
        self.on_prop_float32_changed.fire(self._prop_float32)

    def __set_prop_float64(self, data):
        value =  utils.base_types.as_float64(data)
        if self._prop_float64 == value:
            return
        self._prop_float64 = value
        self.on_prop_float64_changed.fire(self._prop_float64)

    def __set_prop_string(self, data):
        value =  utils.base_types.as_string(data)
        if self._prop_string == value:
            return
        self._prop_string = value
        self.on_prop_string_changed.fire(self._prop_string)

    def __on_sig_bool_signal(self, args: list[Any]):
        param_bool =  utils.base_types.as_bool(args[0])
        self.on_sig_bool.fire(param_bool)
        return

    def __on_sig_int_signal(self, args: list[Any]):
        param_int =  utils.base_types.as_int(args[0])
        self.on_sig_int.fire(param_int)
        return

    def __on_sig_int32_signal(self, args: list[Any]):
        param_int32 =  utils.base_types.as_int32(args[0])
        self.on_sig_int32.fire(param_int32)
        return

    def __on_sig_int64_signal(self, args: list[Any]):
        param_int64 =  utils.base_types.as_int64(args[0])
        self.on_sig_int64.fire(param_int64)
        return

    def __on_sig_float_signal(self, args: list[Any]):
        param_float =  utils.base_types.as_float(args[0])
        self.on_sig_float.fire(param_float)
        return

    def __on_sig_float32_signal(self, args: list[Any]):
        param_float32 =  utils.base_types.as_float32(args[0])
        self.on_sig_float32.fire(param_float32)
        return

    def __on_sig_float64_signal(self, args: list[Any]):
        param_float64 =  utils.base_types.as_float64(args[0])
        self.on_sig_float64.fire(param_float64)
        return

    def __on_sig_string_signal(self, args: list[Any]):
        param_string =  utils.base_types.as_string(args[0])
        self.on_sig_string.fire(param_string)
        return

class SimpleArrayInterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self._prop_bool = []
        self.on_prop_bool_changed = EventHook()
        self._prop_int = []
        self.on_prop_int_changed = EventHook()
        self._prop_int32 = []
        self.on_prop_int32_changed = EventHook()
        self._prop_int64 = []
        self.on_prop_int64_changed = EventHook()
        self._prop_float = []
        self.on_prop_float_changed = EventHook()
        self._prop_float32 = []
        self.on_prop_float32_changed = EventHook()
        self._prop_float64 = []
        self.on_prop_float64_changed = EventHook()
        self._prop_string = []
        self.on_prop_string_changed = EventHook()
        self._prop_read_only_string = ""
        self.on_prop_read_only_string_changed = EventHook()
        self.on_sig_bool = EventHook()
        self.on_sig_int = EventHook()
        self.on_sig_int32 = EventHook()
        self.on_sig_int64 = EventHook()
        self.on_sig_float = EventHook()
        self.on_sig_float32 = EventHook()
        self.on_sig_float64 = EventHook()
        self.on_sig_string = EventHook()
        self.client.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.client.subscribe_for_property("tb.simple/SimpleArrayInterface/prop/propBool", self.__set_prop_bool)
        self.client.subscribe_for_property("tb.simple/SimpleArrayInterface/prop/propInt", self.__set_prop_int)
        self.client.subscribe_for_property("tb.simple/SimpleArrayInterface/prop/propInt32", self.__set_prop_int32)
        self.client.subscribe_for_property("tb.simple/SimpleArrayInterface/prop/propInt64", self.__set_prop_int64)
        self.client.subscribe_for_property("tb.simple/SimpleArrayInterface/prop/propFloat", self.__set_prop_float)
        self.client.subscribe_for_property("tb.simple/SimpleArrayInterface/prop/propFloat32", self.__set_prop_float32)
        self.client.subscribe_for_property("tb.simple/SimpleArrayInterface/prop/propFloat64", self.__set_prop_float64)
        self.client.subscribe_for_property("tb.simple/SimpleArrayInterface/prop/propString", self.__set_prop_string)
        self.client.subscribe_for_property("tb.simple/SimpleArrayInterface/prop/propReadOnlyString", self.__set_prop_read_only_string)
        self.client.subscribe_for_signal("tb.simple/SimpleArrayInterface/sig/sigBool",  self.__on_sig_bool_signal)
        self.client.subscribe_for_signal("tb.simple/SimpleArrayInterface/sig/sigInt",  self.__on_sig_int_signal)
        self.client.subscribe_for_signal("tb.simple/SimpleArrayInterface/sig/sigInt32",  self.__on_sig_int32_signal)
        self.client.subscribe_for_signal("tb.simple/SimpleArrayInterface/sig/sigInt64",  self.__on_sig_int64_signal)
        self.client.subscribe_for_signal("tb.simple/SimpleArrayInterface/sig/sigFloat",  self.__on_sig_float_signal)
        self.client.subscribe_for_signal("tb.simple/SimpleArrayInterface/sig/sigFloat32",  self.__on_sig_float32_signal)
        self.client.subscribe_for_signal("tb.simple/SimpleArrayInterface/sig/sigFloat64",  self.__on_sig_float64_signal)
        self.client.subscribe_for_signal("tb.simple/SimpleArrayInterface/sig/sigString",  self.__on_sig_string_signal)
        #TODO SUBSCRIBE FOR INVOKE RESP TOPIC

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/prop/propBool")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/prop/propInt")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/prop/propInt32")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/prop/propInt64")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/prop/propFloat")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/prop/propFloat32")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/prop/propFloat64")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/prop/propString")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/prop/propReadOnlyString")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/sig/sigBool")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/sig/sigInt")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/sig/sigInt32")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/sig/sigInt64")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/sig/sigFloat")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/sig/sigFloat32")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/sig/sigFloat64")
        self.client.unsubscribe("tb.simple/SimpleArrayInterface/sig/sigString")
        #TODO UNSUBSCRIBE INVOKE RESP TOPIC

    def set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        topic = "tb.simple/SimpleArrayInterface/set/propBool"
        self.client.set_remote_property(topic, [utils.base_types.from_bool(_) for _ in value])

    def get_prop_bool(self):
        return self._prop_bool

    def set_prop_int(self, value):
        if self._prop_int == value:
            return
        topic = "tb.simple/SimpleArrayInterface/set/propInt"
        self.client.set_remote_property(topic, [utils.base_types.from_int(_) for _ in value])

    def get_prop_int(self):
        return self._prop_int

    def set_prop_int32(self, value):
        if self._prop_int32 == value:
            return
        topic = "tb.simple/SimpleArrayInterface/set/propInt32"
        self.client.set_remote_property(topic, [utils.base_types.from_int32(_) for _ in value])

    def get_prop_int32(self):
        return self._prop_int32

    def set_prop_int64(self, value):
        if self._prop_int64 == value:
            return
        topic = "tb.simple/SimpleArrayInterface/set/propInt64"
        self.client.set_remote_property(topic, [utils.base_types.from_int64(_) for _ in value])

    def get_prop_int64(self):
        return self._prop_int64

    def set_prop_float(self, value):
        if self._prop_float == value:
            return
        topic = "tb.simple/SimpleArrayInterface/set/propFloat"
        self.client.set_remote_property(topic, [utils.base_types.from_float(_) for _ in value])

    def get_prop_float(self):
        return self._prop_float

    def set_prop_float32(self, value):
        if self._prop_float32 == value:
            return
        topic = "tb.simple/SimpleArrayInterface/set/propFloat32"
        self.client.set_remote_property(topic, [utils.base_types.from_float32(_) for _ in value])

    def get_prop_float32(self):
        return self._prop_float32

    def set_prop_float64(self, value):
        if self._prop_float64 == value:
            return
        topic = "tb.simple/SimpleArrayInterface/set/propFloat64"
        self.client.set_remote_property(topic, [utils.base_types.from_float64(_) for _ in value])

    def get_prop_float64(self):
        return self._prop_float64

    def set_prop_string(self, value):
        if self._prop_string == value:
            return
        topic = "tb.simple/SimpleArrayInterface/set/propString"
        self.client.set_remote_property(topic, [utils.base_types.from_string(_) for _ in value])

    def get_prop_string(self):
        return self._prop_string

    def get_prop_read_only_string(self):
        return self._prop_read_only_string

    # internal functions on message handle

    def __set_prop_bool(self, data):
        value = [utils.base_types.as_bool(_) for _ in data]
        if self._prop_bool == value:
            return
        self._prop_bool = value
        self.on_prop_bool_changed.fire(self._prop_bool)

    def __set_prop_int(self, data):
        value = [utils.base_types.as_int(_) for _ in data]
        if self._prop_int == value:
            return
        self._prop_int = value
        self.on_prop_int_changed.fire(self._prop_int)

    def __set_prop_int32(self, data):
        value = [utils.base_types.as_int32(_) for _ in data]
        if self._prop_int32 == value:
            return
        self._prop_int32 = value
        self.on_prop_int32_changed.fire(self._prop_int32)

    def __set_prop_int64(self, data):
        value = [utils.base_types.as_int64(_) for _ in data]
        if self._prop_int64 == value:
            return
        self._prop_int64 = value
        self.on_prop_int64_changed.fire(self._prop_int64)

    def __set_prop_float(self, data):
        value = [utils.base_types.as_float(_) for _ in data]
        if self._prop_float == value:
            return
        self._prop_float = value
        self.on_prop_float_changed.fire(self._prop_float)

    def __set_prop_float32(self, data):
        value = [utils.base_types.as_float32(_) for _ in data]
        if self._prop_float32 == value:
            return
        self._prop_float32 = value
        self.on_prop_float32_changed.fire(self._prop_float32)

    def __set_prop_float64(self, data):
        value = [utils.base_types.as_float64(_) for _ in data]
        if self._prop_float64 == value:
            return
        self._prop_float64 = value
        self.on_prop_float64_changed.fire(self._prop_float64)

    def __set_prop_string(self, data):
        value = [utils.base_types.as_string(_) for _ in data]
        if self._prop_string == value:
            return
        self._prop_string = value
        self.on_prop_string_changed.fire(self._prop_string)

    def __set_prop_read_only_string(self, data):
        value =  utils.base_types.as_string(data)
        if self._prop_read_only_string == value:
            return
        self._prop_read_only_string = value
        self.on_prop_read_only_string_changed.fire(self._prop_read_only_string)

    def __on_sig_bool_signal(self, args: list[Any]):
        param_bool = [utils.base_types.as_bool(_) for _ in args[0]]
        self.on_sig_bool.fire(param_bool)
        return

    def __on_sig_int_signal(self, args: list[Any]):
        param_int = [utils.base_types.as_int(_) for _ in args[0]]
        self.on_sig_int.fire(param_int)
        return

    def __on_sig_int32_signal(self, args: list[Any]):
        param_int32 = [utils.base_types.as_int32(_) for _ in args[0]]
        self.on_sig_int32.fire(param_int32)
        return

    def __on_sig_int64_signal(self, args: list[Any]):
        param_int64 = [utils.base_types.as_int64(_) for _ in args[0]]
        self.on_sig_int64.fire(param_int64)
        return

    def __on_sig_float_signal(self, args: list[Any]):
        param_float = [utils.base_types.as_float(_) for _ in args[0]]
        self.on_sig_float.fire(param_float)
        return

    def __on_sig_float32_signal(self, args: list[Any]):
        param_floa32 = [utils.base_types.as_float32(_) for _ in args[0]]
        self.on_sig_float32.fire(param_floa32)
        return

    def __on_sig_float64_signal(self, args: list[Any]):
        param_float64 = [utils.base_types.as_float64(_) for _ in args[0]]
        self.on_sig_float64.fire(param_float64)
        return

    def __on_sig_string_signal(self, args: list[Any]):
        param_string = [utils.base_types.as_string(_) for _ in args[0]]
        self.on_sig_string.fire(param_string)
        return

class NoPropertiesInterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self.on_sig_void = EventHook()
        self.on_sig_bool = EventHook()
        self.client.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.client.subscribe_for_signal("tb.simple/NoPropertiesInterface/sig/sigVoid",  self.__on_sig_void_signal)
        self.client.subscribe_for_signal("tb.simple/NoPropertiesInterface/sig/sigBool",  self.__on_sig_bool_signal)
        #TODO SUBSCRIBE FOR INVOKE RESP TOPIC

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.unsubscribe("tb.simple/NoPropertiesInterface/sig/sigVoid")
        self.client.unsubscribe("tb.simple/NoPropertiesInterface/sig/sigBool")
        #TODO UNSUBSCRIBE INVOKE RESP TOPIC

    # internal functions on message handle

    def __on_sig_void_signal(self, args: list[Any]):
        self.on_sig_void.fire()
        return

    def __on_sig_bool_signal(self, args: list[Any]):
        param_bool =  utils.base_types.as_bool(args[0])
        self.on_sig_bool.fire(param_bool)
        return

class NoOperationsInterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self._prop_bool = False
        self.on_prop_bool_changed = EventHook()
        self._prop_int = 0
        self.on_prop_int_changed = EventHook()
        self.on_sig_void = EventHook()
        self.on_sig_bool = EventHook()
        self.client.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.client.subscribe_for_property("tb.simple/NoOperationsInterface/prop/propBool", self.__set_prop_bool)
        self.client.subscribe_for_property("tb.simple/NoOperationsInterface/prop/propInt", self.__set_prop_int)
        self.client.subscribe_for_signal("tb.simple/NoOperationsInterface/sig/sigVoid",  self.__on_sig_void_signal)
        self.client.subscribe_for_signal("tb.simple/NoOperationsInterface/sig/sigBool",  self.__on_sig_bool_signal)
        #TODO SUBSCRIBE FOR INVOKE RESP TOPIC

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.unsubscribe("tb.simple/NoOperationsInterface/prop/propBool")
        self.client.unsubscribe("tb.simple/NoOperationsInterface/prop/propInt")
        self.client.unsubscribe("tb.simple/NoOperationsInterface/sig/sigVoid")
        self.client.unsubscribe("tb.simple/NoOperationsInterface/sig/sigBool")
        #TODO UNSUBSCRIBE INVOKE RESP TOPIC

    def set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        topic = "tb.simple/NoOperationsInterface/set/propBool"
        self.client.set_remote_property(topic, utils.base_types.from_bool(value))

    def get_prop_bool(self):
        return self._prop_bool

    def set_prop_int(self, value):
        if self._prop_int == value:
            return
        topic = "tb.simple/NoOperationsInterface/set/propInt"
        self.client.set_remote_property(topic, utils.base_types.from_int(value))

    def get_prop_int(self):
        return self._prop_int

    # internal functions on message handle

    def __set_prop_bool(self, data):
        value =  utils.base_types.as_bool(data)
        if self._prop_bool == value:
            return
        self._prop_bool = value
        self.on_prop_bool_changed.fire(self._prop_bool)

    def __set_prop_int(self, data):
        value =  utils.base_types.as_int(data)
        if self._prop_int == value:
            return
        self._prop_int = value
        self.on_prop_int_changed.fire(self._prop_int)

    def __on_sig_void_signal(self, args: list[Any]):
        self.on_sig_void.fire()
        return

    def __on_sig_bool_signal(self, args: list[Any]):
        param_bool =  utils.base_types.as_bool(args[0])
        self.on_sig_bool.fire(param_bool)
        return

class NoSignalsInterfaceClientAdapter():
    def __init__(self, client: apigear.mqtt.Client):
        self.client = client
        self._prop_bool = False
        self.on_prop_bool_changed = EventHook()
        self._prop_int = 0
        self.on_prop_int_changed = EventHook()
        self.client.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.client.subscribe_for_property("tb.simple/NoSignalsInterface/prop/propBool", self.__set_prop_bool)
        self.client.subscribe_for_property("tb.simple/NoSignalsInterface/prop/propInt", self.__set_prop_int)
        #TODO SUBSCRIBE FOR INVOKE RESP TOPIC

    def __del__(self):
        self.client.on_connected -= self.subscribeForTopics
        self.client.unsubscribe("tb.simple/NoSignalsInterface/prop/propBool")
        self.client.unsubscribe("tb.simple/NoSignalsInterface/prop/propInt")
        #TODO UNSUBSCRIBE INVOKE RESP TOPIC

    def set_prop_bool(self, value):
        if self._prop_bool == value:
            return
        topic = "tb.simple/NoSignalsInterface/set/propBool"
        self.client.set_remote_property(topic, utils.base_types.from_bool(value))

    def get_prop_bool(self):
        return self._prop_bool

    def set_prop_int(self, value):
        if self._prop_int == value:
            return
        topic = "tb.simple/NoSignalsInterface/set/propInt"
        self.client.set_remote_property(topic, utils.base_types.from_int(value))

    def get_prop_int(self):
        return self._prop_int

    # internal functions on message handle

    def __set_prop_bool(self, data):
        value =  utils.base_types.as_bool(data)
        if self._prop_bool == value:
            return
        self._prop_bool = value
        self.on_prop_bool_changed.fire(self._prop_bool)

    def __set_prop_int(self, data):
        value =  utils.base_types.as_int(data)
        if self._prop_int == value:
            return
        self._prop_int = value
        self.on_prop_int_changed.fire(self._prop_int)
