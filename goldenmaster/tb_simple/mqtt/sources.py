import apigear.mqtt
import utils.base_types
import tb_simple.api
from utils.eventhook import EventHook
from typing import Any
import logging
class VoidInterfaceServiceAdapter():
    def __init__(self, impl: tb_simple.api.IVoidInterface, service: apigear.mqtt.Service):
        self.service = service
        self.impl = impl
        self.impl.on_sig_void += self.notify_sig_void
        self.service.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.service.subscribe_for_invoke_req("tb.simple/VoidInterface/rpc/funcVoid", self.__invoke_func_void)

    def __del__(self):
        self.service.on_connected -= self.subscribeForTopics
        self.service.unsubscribe("tb.simple/VoidInterface/rpc/funcVoid")

    def notify_sig_void(self):
        args = []
        self.service.notify_signal("tb.simple/VoidInterface/sig/sigVoid", args)

    def __invoke_func_void(self, args: list[Any]) -> Any:
        reply = self.impl.func_void()
        return utils.base_types.from_int(0)
class SimpleInterfaceServiceAdapter():
    def __init__(self, impl: tb_simple.api.ISimpleInterface, service: apigear.mqtt.Service):
        self.service = service
        self.impl = impl
        self.impl.on_prop_bool_changed += self.notify_prop_bool_changed
        self.impl.on_prop_int_changed += self.notify_prop_int_changed
        self.impl.on_prop_int32_changed += self.notify_prop_int32_changed
        self.impl.on_prop_int64_changed += self.notify_prop_int64_changed
        self.impl.on_prop_float_changed += self.notify_prop_float_changed
        self.impl.on_prop_float32_changed += self.notify_prop_float32_changed
        self.impl.on_prop_float64_changed += self.notify_prop_float64_changed
        self.impl.on_prop_string_changed += self.notify_prop_string_changed
        self.impl.on_sig_bool += self.notify_sig_bool
        self.impl.on_sig_int += self.notify_sig_int
        self.impl.on_sig_int32 += self.notify_sig_int32
        self.impl.on_sig_int64 += self.notify_sig_int64
        self.impl.on_sig_float += self.notify_sig_float
        self.impl.on_sig_float32 += self.notify_sig_float32
        self.impl.on_sig_float64 += self.notify_sig_float64
        self.impl.on_sig_string += self.notify_sig_string
        self.service.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.service.subscribe_for_property("tb.simple/SimpleInterface/set/propBool", self.__set_prop_bool)
        self.service.subscribe_for_property("tb.simple/SimpleInterface/set/propInt", self.__set_prop_int)
        self.service.subscribe_for_property("tb.simple/SimpleInterface/set/propInt32", self.__set_prop_int32)
        self.service.subscribe_for_property("tb.simple/SimpleInterface/set/propInt64", self.__set_prop_int64)
        self.service.subscribe_for_property("tb.simple/SimpleInterface/set/propFloat", self.__set_prop_float)
        self.service.subscribe_for_property("tb.simple/SimpleInterface/set/propFloat32", self.__set_prop_float32)
        self.service.subscribe_for_property("tb.simple/SimpleInterface/set/propFloat64", self.__set_prop_float64)
        self.service.subscribe_for_property("tb.simple/SimpleInterface/set/propString", self.__set_prop_string)
        self.service.subscribe_for_invoke_req("tb.simple/SimpleInterface/rpc/funcNoReturnValue", self.__invoke_func_no_return_value)
        self.service.subscribe_for_invoke_req("tb.simple/SimpleInterface/rpc/funcBool", self.__invoke_func_bool)
        self.service.subscribe_for_invoke_req("tb.simple/SimpleInterface/rpc/funcInt", self.__invoke_func_int)
        self.service.subscribe_for_invoke_req("tb.simple/SimpleInterface/rpc/funcInt32", self.__invoke_func_int32)
        self.service.subscribe_for_invoke_req("tb.simple/SimpleInterface/rpc/funcInt64", self.__invoke_func_int64)
        self.service.subscribe_for_invoke_req("tb.simple/SimpleInterface/rpc/funcFloat", self.__invoke_func_float)
        self.service.subscribe_for_invoke_req("tb.simple/SimpleInterface/rpc/funcFloat32", self.__invoke_func_float32)
        self.service.subscribe_for_invoke_req("tb.simple/SimpleInterface/rpc/funcFloat64", self.__invoke_func_float64)
        self.service.subscribe_for_invoke_req("tb.simple/SimpleInterface/rpc/funcString", self.__invoke_func_string)

    def __del__(self):
        self.service.on_connected -= self.subscribeForTopics
        self.service.unsubscribe("tb.simple/SimpleInterface/set/propBool")
        self.service.unsubscribe("tb.simple/SimpleInterface/set/propInt")
        self.service.unsubscribe("tb.simple/SimpleInterface/set/propInt32")
        self.service.unsubscribe("tb.simple/SimpleInterface/set/propInt64")
        self.service.unsubscribe("tb.simple/SimpleInterface/set/propFloat")
        self.service.unsubscribe("tb.simple/SimpleInterface/set/propFloat32")
        self.service.unsubscribe("tb.simple/SimpleInterface/set/propFloat64")
        self.service.unsubscribe("tb.simple/SimpleInterface/set/propString")
        self.service.unsubscribe("tb.simple/SimpleInterface/rpc/funcNoReturnValue")
        self.service.unsubscribe("tb.simple/SimpleInterface/rpc/funcBool")
        self.service.unsubscribe("tb.simple/SimpleInterface/rpc/funcInt")
        self.service.unsubscribe("tb.simple/SimpleInterface/rpc/funcInt32")
        self.service.unsubscribe("tb.simple/SimpleInterface/rpc/funcInt64")
        self.service.unsubscribe("tb.simple/SimpleInterface/rpc/funcFloat")
        self.service.unsubscribe("tb.simple/SimpleInterface/rpc/funcFloat32")
        self.service.unsubscribe("tb.simple/SimpleInterface/rpc/funcFloat64")
        self.service.unsubscribe("tb.simple/SimpleInterface/rpc/funcString")

    def notify_sig_bool(self, param_bool: bool):
        _param_bool = utils.base_types.from_bool(param_bool)
        args = [_param_bool]
        self.service.notify_signal("tb.simple/SimpleInterface/sig/sigBool", args)

    def notify_sig_int(self, param_int: int):
        _param_int = utils.base_types.from_int(param_int)
        args = [_param_int]
        self.service.notify_signal("tb.simple/SimpleInterface/sig/sigInt", args)

    def notify_sig_int32(self, param_int32: int):
        _param_int32 = utils.base_types.from_int32(param_int32)
        args = [_param_int32]
        self.service.notify_signal("tb.simple/SimpleInterface/sig/sigInt32", args)

    def notify_sig_int64(self, param_int64: int):
        _param_int64 = utils.base_types.from_int64(param_int64)
        args = [_param_int64]
        self.service.notify_signal("tb.simple/SimpleInterface/sig/sigInt64", args)

    def notify_sig_float(self, param_float: float):
        _param_float = utils.base_types.from_float(param_float)
        args = [_param_float]
        self.service.notify_signal("tb.simple/SimpleInterface/sig/sigFloat", args)

    def notify_sig_float32(self, param_float32: float):
        _param_float32 = utils.base_types.from_float32(param_float32)
        args = [_param_float32]
        self.service.notify_signal("tb.simple/SimpleInterface/sig/sigFloat32", args)

    def notify_sig_float64(self, param_float64: float):
        _param_float64 = utils.base_types.from_float64(param_float64)
        args = [_param_float64]
        self.service.notify_signal("tb.simple/SimpleInterface/sig/sigFloat64", args)

    def notify_sig_string(self, param_string: str):
        _param_string = utils.base_types.from_string(param_string)
        args = [_param_string]
        self.service.notify_signal("tb.simple/SimpleInterface/sig/sigString", args)

    def notify_prop_bool_changed(self, value):
        v = utils.base_types.from_bool(value)
        self.service.notify_property_change("tb.simple/SimpleInterface/prop/propBool", v)

    def notify_prop_int_changed(self, value):
        v = utils.base_types.from_int(value)
        self.service.notify_property_change("tb.simple/SimpleInterface/prop/propInt", v)

    def notify_prop_int32_changed(self, value):
        v = utils.base_types.from_int32(value)
        self.service.notify_property_change("tb.simple/SimpleInterface/prop/propInt32", v)

    def notify_prop_int64_changed(self, value):
        v = utils.base_types.from_int64(value)
        self.service.notify_property_change("tb.simple/SimpleInterface/prop/propInt64", v)

    def notify_prop_float_changed(self, value):
        v = utils.base_types.from_float(value)
        self.service.notify_property_change("tb.simple/SimpleInterface/prop/propFloat", v)

    def notify_prop_float32_changed(self, value):
        v = utils.base_types.from_float32(value)
        self.service.notify_property_change("tb.simple/SimpleInterface/prop/propFloat32", v)

    def notify_prop_float64_changed(self, value):
        v = utils.base_types.from_float64(value)
        self.service.notify_property_change("tb.simple/SimpleInterface/prop/propFloat64", v)

    def notify_prop_string_changed(self, value):
        v = utils.base_types.from_string(value)
        self.service.notify_property_change("tb.simple/SimpleInterface/prop/propString", v)

    def __set_prop_bool(self, value: Any):
            v = utils.base_types.as_bool(value)
            self.impl.set_prop_bool(v)

    def __set_prop_int(self, value: Any):
            v = utils.base_types.as_int(value)
            self.impl.set_prop_int(v)

    def __set_prop_int32(self, value: Any):
            v = utils.base_types.as_int32(value)
            self.impl.set_prop_int32(v)

    def __set_prop_int64(self, value: Any):
            v = utils.base_types.as_int64(value)
            self.impl.set_prop_int64(v)

    def __set_prop_float(self, value: Any):
            v = utils.base_types.as_float(value)
            self.impl.set_prop_float(v)

    def __set_prop_float32(self, value: Any):
            v = utils.base_types.as_float32(value)
            self.impl.set_prop_float32(v)

    def __set_prop_float64(self, value: Any):
            v = utils.base_types.as_float64(value)
            self.impl.set_prop_float64(v)

    def __set_prop_string(self, value: Any):
            v = utils.base_types.as_string(value)
            self.impl.set_prop_string(v)

    def __invoke_func_no_return_value(self, args: list[Any]) -> Any:
        param_bool = utils.base_types.as_bool(args[0])
        reply = self.impl.func_no_return_value(param_bool)
        return utils.base_types.from_int(0)

    def __invoke_func_bool(self, args: list[Any]) -> Any:
        param_bool = utils.base_types.as_bool(args[0])
        reply = self.impl.func_bool(param_bool)
        return utils.base_types.from_bool(reply)

    def __invoke_func_int(self, args: list[Any]) -> Any:
        param_int = utils.base_types.as_int(args[0])
        reply = self.impl.func_int(param_int)
        return utils.base_types.from_int(reply)

    def __invoke_func_int32(self, args: list[Any]) -> Any:
        param_int32 = utils.base_types.as_int32(args[0])
        reply = self.impl.func_int32(param_int32)
        return utils.base_types.from_int32(reply)

    def __invoke_func_int64(self, args: list[Any]) -> Any:
        param_int64 = utils.base_types.as_int64(args[0])
        reply = self.impl.func_int64(param_int64)
        return utils.base_types.from_int64(reply)

    def __invoke_func_float(self, args: list[Any]) -> Any:
        param_float = utils.base_types.as_float(args[0])
        reply = self.impl.func_float(param_float)
        return utils.base_types.from_float(reply)

    def __invoke_func_float32(self, args: list[Any]) -> Any:
        param_float32 = utils.base_types.as_float32(args[0])
        reply = self.impl.func_float32(param_float32)
        return utils.base_types.from_float32(reply)

    def __invoke_func_float64(self, args: list[Any]) -> Any:
        param_float = utils.base_types.as_float64(args[0])
        reply = self.impl.func_float64(param_float)
        return utils.base_types.from_float64(reply)

    def __invoke_func_string(self, args: list[Any]) -> Any:
        param_string = utils.base_types.as_string(args[0])
        reply = self.impl.func_string(param_string)
        return utils.base_types.from_string(reply)
class SimpleArrayInterfaceServiceAdapter():
    def __init__(self, impl: tb_simple.api.ISimpleArrayInterface, service: apigear.mqtt.Service):
        self.service = service
        self.impl = impl
        self.impl.on_prop_bool_changed += self.notify_prop_bool_changed
        self.impl.on_prop_int_changed += self.notify_prop_int_changed
        self.impl.on_prop_int32_changed += self.notify_prop_int32_changed
        self.impl.on_prop_int64_changed += self.notify_prop_int64_changed
        self.impl.on_prop_float_changed += self.notify_prop_float_changed
        self.impl.on_prop_float32_changed += self.notify_prop_float32_changed
        self.impl.on_prop_float64_changed += self.notify_prop_float64_changed
        self.impl.on_prop_string_changed += self.notify_prop_string_changed
        self.impl.on_prop_read_only_string_changed += self.notify_prop_read_only_string_changed
        self.impl.on_sig_bool += self.notify_sig_bool
        self.impl.on_sig_int += self.notify_sig_int
        self.impl.on_sig_int32 += self.notify_sig_int32
        self.impl.on_sig_int64 += self.notify_sig_int64
        self.impl.on_sig_float += self.notify_sig_float
        self.impl.on_sig_float32 += self.notify_sig_float32
        self.impl.on_sig_float64 += self.notify_sig_float64
        self.impl.on_sig_string += self.notify_sig_string
        self.service.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.service.subscribe_for_property("tb.simple/SimpleArrayInterface/set/propBool", self.__set_prop_bool)
        self.service.subscribe_for_property("tb.simple/SimpleArrayInterface/set/propInt", self.__set_prop_int)
        self.service.subscribe_for_property("tb.simple/SimpleArrayInterface/set/propInt32", self.__set_prop_int32)
        self.service.subscribe_for_property("tb.simple/SimpleArrayInterface/set/propInt64", self.__set_prop_int64)
        self.service.subscribe_for_property("tb.simple/SimpleArrayInterface/set/propFloat", self.__set_prop_float)
        self.service.subscribe_for_property("tb.simple/SimpleArrayInterface/set/propFloat32", self.__set_prop_float32)
        self.service.subscribe_for_property("tb.simple/SimpleArrayInterface/set/propFloat64", self.__set_prop_float64)
        self.service.subscribe_for_property("tb.simple/SimpleArrayInterface/set/propString", self.__set_prop_string)
        self.service.subscribe_for_property("tb.simple/SimpleArrayInterface/set/propReadOnlyString", self.__set_prop_read_only_string)
        self.service.subscribe_for_invoke_req("tb.simple/SimpleArrayInterface/rpc/funcBool", self.__invoke_func_bool)
        self.service.subscribe_for_invoke_req("tb.simple/SimpleArrayInterface/rpc/funcInt", self.__invoke_func_int)
        self.service.subscribe_for_invoke_req("tb.simple/SimpleArrayInterface/rpc/funcInt32", self.__invoke_func_int32)
        self.service.subscribe_for_invoke_req("tb.simple/SimpleArrayInterface/rpc/funcInt64", self.__invoke_func_int64)
        self.service.subscribe_for_invoke_req("tb.simple/SimpleArrayInterface/rpc/funcFloat", self.__invoke_func_float)
        self.service.subscribe_for_invoke_req("tb.simple/SimpleArrayInterface/rpc/funcFloat32", self.__invoke_func_float32)
        self.service.subscribe_for_invoke_req("tb.simple/SimpleArrayInterface/rpc/funcFloat64", self.__invoke_func_float64)
        self.service.subscribe_for_invoke_req("tb.simple/SimpleArrayInterface/rpc/funcString", self.__invoke_func_string)

    def __del__(self):
        self.service.on_connected -= self.subscribeForTopics
        self.service.unsubscribe("tb.simple/SimpleArrayInterface/set/propBool")
        self.service.unsubscribe("tb.simple/SimpleArrayInterface/set/propInt")
        self.service.unsubscribe("tb.simple/SimpleArrayInterface/set/propInt32")
        self.service.unsubscribe("tb.simple/SimpleArrayInterface/set/propInt64")
        self.service.unsubscribe("tb.simple/SimpleArrayInterface/set/propFloat")
        self.service.unsubscribe("tb.simple/SimpleArrayInterface/set/propFloat32")
        self.service.unsubscribe("tb.simple/SimpleArrayInterface/set/propFloat64")
        self.service.unsubscribe("tb.simple/SimpleArrayInterface/set/propString")
        self.service.unsubscribe("tb.simple/SimpleArrayInterface/set/propReadOnlyString")
        self.service.unsubscribe("tb.simple/SimpleArrayInterface/rpc/funcBool")
        self.service.unsubscribe("tb.simple/SimpleArrayInterface/rpc/funcInt")
        self.service.unsubscribe("tb.simple/SimpleArrayInterface/rpc/funcInt32")
        self.service.unsubscribe("tb.simple/SimpleArrayInterface/rpc/funcInt64")
        self.service.unsubscribe("tb.simple/SimpleArrayInterface/rpc/funcFloat")
        self.service.unsubscribe("tb.simple/SimpleArrayInterface/rpc/funcFloat32")
        self.service.unsubscribe("tb.simple/SimpleArrayInterface/rpc/funcFloat64")
        self.service.unsubscribe("tb.simple/SimpleArrayInterface/rpc/funcString")

    def notify_sig_bool(self, param_bool: list[bool]):
        _param_bool = [utils.base_types.api.from_bool(_) for _ in param_bool]
        args = [_param_bool]
        self.service.notify_signal("tb.simple/SimpleArrayInterface/sig/sigBool", args)

    def notify_sig_int(self, param_int: list[int]):
        _param_int = [utils.base_types.api.from_int(_) for _ in param_int]
        args = [_param_int]
        self.service.notify_signal("tb.simple/SimpleArrayInterface/sig/sigInt", args)

    def notify_sig_int32(self, param_int32: list[int]):
        _param_int32 = [utils.base_types.api.from_int32(_) for _ in param_int32]
        args = [_param_int32]
        self.service.notify_signal("tb.simple/SimpleArrayInterface/sig/sigInt32", args)

    def notify_sig_int64(self, param_int64: list[int]):
        _param_int64 = [utils.base_types.api.from_int64(_) for _ in param_int64]
        args = [_param_int64]
        self.service.notify_signal("tb.simple/SimpleArrayInterface/sig/sigInt64", args)

    def notify_sig_float(self, param_float: list[float]):
        _param_float = [utils.base_types.api.from_float(_) for _ in param_float]
        args = [_param_float]
        self.service.notify_signal("tb.simple/SimpleArrayInterface/sig/sigFloat", args)

    def notify_sig_float32(self, param_floa32: list[float]):
        _param_floa32 = [utils.base_types.api.from_float32(_) for _ in param_floa32]
        args = [_param_floa32]
        self.service.notify_signal("tb.simple/SimpleArrayInterface/sig/sigFloat32", args)

    def notify_sig_float64(self, param_float64: list[float]):
        _param_float64 = [utils.base_types.api.from_float64(_) for _ in param_float64]
        args = [_param_float64]
        self.service.notify_signal("tb.simple/SimpleArrayInterface/sig/sigFloat64", args)

    def notify_sig_string(self, param_string: list[str]):
        _param_string = [utils.base_types.api.from_string(_) for _ in param_string]
        args = [_param_string]
        self.service.notify_signal("tb.simple/SimpleArrayInterface/sig/sigString", args)

    def notify_prop_bool_changed(self, value):
        v = [utils.base_types.from_bool(_) for _ in value]
        self.service.notify_property_change("tb.simple/SimpleArrayInterface/prop/propBool", v)

    def notify_prop_int_changed(self, value):
        v = [utils.base_types.from_int(_) for _ in value]
        self.service.notify_property_change("tb.simple/SimpleArrayInterface/prop/propInt", v)

    def notify_prop_int32_changed(self, value):
        v = [utils.base_types.from_int32(_) for _ in value]
        self.service.notify_property_change("tb.simple/SimpleArrayInterface/prop/propInt32", v)

    def notify_prop_int64_changed(self, value):
        v = [utils.base_types.from_int64(_) for _ in value]
        self.service.notify_property_change("tb.simple/SimpleArrayInterface/prop/propInt64", v)

    def notify_prop_float_changed(self, value):
        v = [utils.base_types.from_float(_) for _ in value]
        self.service.notify_property_change("tb.simple/SimpleArrayInterface/prop/propFloat", v)

    def notify_prop_float32_changed(self, value):
        v = [utils.base_types.from_float32(_) for _ in value]
        self.service.notify_property_change("tb.simple/SimpleArrayInterface/prop/propFloat32", v)

    def notify_prop_float64_changed(self, value):
        v = [utils.base_types.from_float64(_) for _ in value]
        self.service.notify_property_change("tb.simple/SimpleArrayInterface/prop/propFloat64", v)

    def notify_prop_string_changed(self, value):
        v = [utils.base_types.from_string(_) for _ in value]
        self.service.notify_property_change("tb.simple/SimpleArrayInterface/prop/propString", v)

    def notify_prop_read_only_string_changed(self, value):
        v = utils.base_types.from_string(value)
        self.service.notify_property_change("tb.simple/SimpleArrayInterface/prop/propReadOnlyString", v)

    def __set_prop_bool(self, value: Any):
            v = [utils.base_types.as_bool(_) for _ in value]
            self.impl.set_prop_bool(v)

    def __set_prop_int(self, value: Any):
            v = [utils.base_types.as_int(_) for _ in value]
            self.impl.set_prop_int(v)

    def __set_prop_int32(self, value: Any):
            v = [utils.base_types.as_int32(_) for _ in value]
            self.impl.set_prop_int32(v)

    def __set_prop_int64(self, value: Any):
            v = [utils.base_types.as_int64(_) for _ in value]
            self.impl.set_prop_int64(v)

    def __set_prop_float(self, value: Any):
            v = [utils.base_types.as_float(_) for _ in value]
            self.impl.set_prop_float(v)

    def __set_prop_float32(self, value: Any):
            v = [utils.base_types.as_float32(_) for _ in value]
            self.impl.set_prop_float32(v)

    def __set_prop_float64(self, value: Any):
            v = [utils.base_types.as_float64(_) for _ in value]
            self.impl.set_prop_float64(v)

    def __set_prop_string(self, value: Any):
            v = [utils.base_types.as_string(_) for _ in value]
            self.impl.set_prop_string(v)

    def __set_prop_read_only_string(self, value: Any):
            pass

    def __invoke_func_bool(self, args: list[Any]) -> Any:
        param_bool = [utils.base_types.as_bool(_) for _ in args[0]]
        reply = self.impl.func_bool(param_bool)
        return [utils.base_types.from_bool(_) for _ in reply]

    def __invoke_func_int(self, args: list[Any]) -> Any:
        param_int = [utils.base_types.as_int(_) for _ in args[0]]
        reply = self.impl.func_int(param_int)
        return [utils.base_types.from_int(_) for _ in reply]

    def __invoke_func_int32(self, args: list[Any]) -> Any:
        param_int32 = [utils.base_types.as_int32(_) for _ in args[0]]
        reply = self.impl.func_int32(param_int32)
        return [utils.base_types.from_int32(_) for _ in reply]

    def __invoke_func_int64(self, args: list[Any]) -> Any:
        param_int64 = [utils.base_types.as_int64(_) for _ in args[0]]
        reply = self.impl.func_int64(param_int64)
        return [utils.base_types.from_int64(_) for _ in reply]

    def __invoke_func_float(self, args: list[Any]) -> Any:
        param_float = [utils.base_types.as_float(_) for _ in args[0]]
        reply = self.impl.func_float(param_float)
        return [utils.base_types.from_float(_) for _ in reply]

    def __invoke_func_float32(self, args: list[Any]) -> Any:
        param_float32 = [utils.base_types.as_float32(_) for _ in args[0]]
        reply = self.impl.func_float32(param_float32)
        return [utils.base_types.from_float32(_) for _ in reply]

    def __invoke_func_float64(self, args: list[Any]) -> Any:
        param_float = [utils.base_types.as_float64(_) for _ in args[0]]
        reply = self.impl.func_float64(param_float)
        return [utils.base_types.from_float64(_) for _ in reply]

    def __invoke_func_string(self, args: list[Any]) -> Any:
        param_string = [utils.base_types.as_string(_) for _ in args[0]]
        reply = self.impl.func_string(param_string)
        return [utils.base_types.from_string(_) for _ in reply]
class NoPropertiesInterfaceServiceAdapter():
    def __init__(self, impl: tb_simple.api.INoPropertiesInterface, service: apigear.mqtt.Service):
        self.service = service
        self.impl = impl
        self.impl.on_sig_void += self.notify_sig_void
        self.impl.on_sig_bool += self.notify_sig_bool
        self.service.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.service.subscribe_for_invoke_req("tb.simple/NoPropertiesInterface/rpc/funcVoid", self.__invoke_func_void)
        self.service.subscribe_for_invoke_req("tb.simple/NoPropertiesInterface/rpc/funcBool", self.__invoke_func_bool)

    def __del__(self):
        self.service.on_connected -= self.subscribeForTopics
        self.service.unsubscribe("tb.simple/NoPropertiesInterface/rpc/funcVoid")
        self.service.unsubscribe("tb.simple/NoPropertiesInterface/rpc/funcBool")

    def notify_sig_void(self):
        args = []
        self.service.notify_signal("tb.simple/NoPropertiesInterface/sig/sigVoid", args)

    def notify_sig_bool(self, param_bool: bool):
        _param_bool = utils.base_types.from_bool(param_bool)
        args = [_param_bool]
        self.service.notify_signal("tb.simple/NoPropertiesInterface/sig/sigBool", args)

    def __invoke_func_void(self, args: list[Any]) -> Any:
        reply = self.impl.func_void()
        return utils.base_types.from_int(0)

    def __invoke_func_bool(self, args: list[Any]) -> Any:
        param_bool = utils.base_types.as_bool(args[0])
        reply = self.impl.func_bool(param_bool)
        return utils.base_types.from_bool(reply)
class NoOperationsInterfaceServiceAdapter():
    def __init__(self, impl: tb_simple.api.INoOperationsInterface, service: apigear.mqtt.Service):
        self.service = service
        self.impl = impl
        self.impl.on_prop_bool_changed += self.notify_prop_bool_changed
        self.impl.on_prop_int_changed += self.notify_prop_int_changed
        self.impl.on_sig_void += self.notify_sig_void
        self.impl.on_sig_bool += self.notify_sig_bool
        self.service.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.service.subscribe_for_property("tb.simple/NoOperationsInterface/set/propBool", self.__set_prop_bool)
        self.service.subscribe_for_property("tb.simple/NoOperationsInterface/set/propInt", self.__set_prop_int)

    def __del__(self):
        self.service.on_connected -= self.subscribeForTopics
        self.service.unsubscribe("tb.simple/NoOperationsInterface/set/propBool")
        self.service.unsubscribe("tb.simple/NoOperationsInterface/set/propInt")

    def notify_sig_void(self):
        args = []
        self.service.notify_signal("tb.simple/NoOperationsInterface/sig/sigVoid", args)

    def notify_sig_bool(self, param_bool: bool):
        _param_bool = utils.base_types.from_bool(param_bool)
        args = [_param_bool]
        self.service.notify_signal("tb.simple/NoOperationsInterface/sig/sigBool", args)

    def notify_prop_bool_changed(self, value):
        v = utils.base_types.from_bool(value)
        self.service.notify_property_change("tb.simple/NoOperationsInterface/prop/propBool", v)

    def notify_prop_int_changed(self, value):
        v = utils.base_types.from_int(value)
        self.service.notify_property_change("tb.simple/NoOperationsInterface/prop/propInt", v)

    def __set_prop_bool(self, value: Any):
            v = utils.base_types.as_bool(value)
            self.impl.set_prop_bool(v)

    def __set_prop_int(self, value: Any):
            v = utils.base_types.as_int(value)
            self.impl.set_prop_int(v)
class NoSignalsInterfaceServiceAdapter():
    def __init__(self, impl: tb_simple.api.INoSignalsInterface, service: apigear.mqtt.Service):
        self.service = service
        self.impl = impl
        self.impl.on_prop_bool_changed += self.notify_prop_bool_changed
        self.impl.on_prop_int_changed += self.notify_prop_int_changed
        self.service.on_connected += self.subscribeForTopics

    def subscribeForTopics(self):
        self.service.subscribe_for_property("tb.simple/NoSignalsInterface/set/propBool", self.__set_prop_bool)
        self.service.subscribe_for_property("tb.simple/NoSignalsInterface/set/propInt", self.__set_prop_int)
        self.service.subscribe_for_invoke_req("tb.simple/NoSignalsInterface/rpc/funcVoid", self.__invoke_func_void)
        self.service.subscribe_for_invoke_req("tb.simple/NoSignalsInterface/rpc/funcBool", self.__invoke_func_bool)

    def __del__(self):
        self.service.on_connected -= self.subscribeForTopics
        self.service.unsubscribe("tb.simple/NoSignalsInterface/set/propBool")
        self.service.unsubscribe("tb.simple/NoSignalsInterface/set/propInt")
        self.service.unsubscribe("tb.simple/NoSignalsInterface/rpc/funcVoid")
        self.service.unsubscribe("tb.simple/NoSignalsInterface/rpc/funcBool")

    def notify_prop_bool_changed(self, value):
        v = utils.base_types.from_bool(value)
        self.service.notify_property_change("tb.simple/NoSignalsInterface/prop/propBool", v)

    def notify_prop_int_changed(self, value):
        v = utils.base_types.from_int(value)
        self.service.notify_property_change("tb.simple/NoSignalsInterface/prop/propInt", v)

    def __set_prop_bool(self, value: Any):
            v = utils.base_types.as_bool(value)
            self.impl.set_prop_bool(v)

    def __set_prop_int(self, value: Any):
            v = utils.base_types.as_int(value)
            self.impl.set_prop_int(v)

    def __invoke_func_void(self, args: list[Any]) -> Any:
        reply = self.impl.func_void()
        return utils.base_types.from_int(0)

    def __invoke_func_bool(self, args: list[Any]) -> Any:
        param_bool = utils.base_types.as_bool(args[0])
        reply = self.impl.func_bool(param_bool)
        return utils.base_types.from_bool(reply)
