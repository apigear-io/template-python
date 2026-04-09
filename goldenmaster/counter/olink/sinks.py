import asyncio
from typing import Any
from olink.core import Name
from olink.client import IObjectSink, ClientNode
from utils.eventhook import EventHook
import utils.base_types
import counter.api
import logging
import custom_types.api
import extern_types.api
import vector3d.vector

class CounterSink(IObjectSink):
    def __init__(self):
        super().__init__()
        self._vector = custom_types.api.Vector3D()
        self.on_vector_changed = EventHook()
        self._extern_vector = vector3d.vector.Vector()
        self.on_extern_vector_changed = EventHook()
        self._vector_array = []
        self.on_vector_array_changed = EventHook()
        self._extern_vector_array = []
        self.on_extern_vector_array_changed = EventHook()
        self.on_value_changed = EventHook()
        self._on_is_ready= EventHook()
        self.client = ClientNode.register_sink(self)

    def _set_vector(self, value):
        if self._vector == value:
            return
        self._vector = value
        self.on_vector_changed.fire(self._vector)

    def set_vector(self, value):
        if self._vector == value:
            return
        self.client.set_remote_property('counter.Counter/vector', custom_types.api.from_vector3_d(value))

    def get_vector(self):
        return self._vector

    def _set_extern_vector(self, value):
        if self._extern_vector == value:
            return
        self._extern_vector = value
        self.on_extern_vector_changed.fire(self._extern_vector)

    def set_extern_vector(self, value):
        if self._extern_vector == value:
            return
        self.client.set_remote_property('counter.Counter/extern_vector', extern_types.api.from_vector3d_vector_vector(value))

    def get_extern_vector(self):
        return self._extern_vector

    def _set_vector_array(self, value):
        if self._vector_array == value:
            return
        self._vector_array = value
        self.on_vector_array_changed.fire(self._vector_array)

    def set_vector_array(self, value):
        if self._vector_array == value:
            return
        self.client.set_remote_property('counter.Counter/vectorArray', [custom_types.api.from_vector3_d(_) for _ in value])

    def get_vector_array(self):
        return self._vector_array

    def _set_extern_vector_array(self, value):
        if self._extern_vector_array == value:
            return
        self._extern_vector_array = value
        self.on_extern_vector_array_changed.fire(self._extern_vector_array)

    def set_extern_vector_array(self, value):
        if self._extern_vector_array == value:
            return
        self.client.set_remote_property('counter.Counter/extern_vectorArray', [extern_types.api.from_vector3d_vector_vector(_) for _ in value])

    def get_extern_vector_array(self):
        return self._extern_vector_array

    async def increment(self, vec: vector3d.vector.Vector):
        _vec = extern_types.api.from_vector3d_vector_vector(vec)
        args = [_vec]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(extern_types.api.as_vector3d_vector_vector(result.value))
        self.client.invoke_remote(f"counter.Counter/increment", args, func)
        return await asyncio.wait_for(future, 500)

    async def increment_array(self, vec: list[vector3d.vector.Vector]):
        _vec = [extern_types.api.from_vector3d_vector_vector(my_vector3_d) for my_vector3_d in vec]
        args = [_vec]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            array_res = result.value
            return future.set_result([extern_types.api.as_vector3d_vector_vector(_) for _ in array_res])
        self.client.invoke_remote(f"counter.Counter/incrementArray", args, func)
        return await asyncio.wait_for(future, 500)

    async def decrement(self, vec: custom_types.api.Vector3D):
        _vec = custom_types.api.from_vector3_d(vec)
        args = [_vec]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            return future.set_result(custom_types.api.as_vector3_d(result.value))
        self.client.invoke_remote(f"counter.Counter/decrement", args, func)
        return await asyncio.wait_for(future, 500)

    async def decrement_array(self, vec: list[custom_types.api.Vector3D]):
        _vec = [custom_types.api.from_vector3_d(vector3_d) for vector3_d in vec]
        args = [_vec]
        future = asyncio.get_running_loop().create_future()
        def func(result):
            array_res = result.value
            return future.set_result([custom_types.api.as_vector3_d(_) for _ in array_res])
        self.client.invoke_remote(f"counter.Counter/decrementArray", args, func)
        return await asyncio.wait_for(future, 500)

    def olink_object_name(self):
        return 'counter.Counter'

    def olink_on_init(self, name: str, props: object, node: "ClientNode"):
        self.client = ClientNode.register_sink(self)
        for k in props:
            if k == "vector":
                v =  custom_types.api.as_vector3_d(props[k])
                self._set_vector(v)
            elif k == "extern_vector":
                v =  extern_types.api.as_vector3d_vector_vector(props[k])
                self._set_extern_vector(v)
            elif k == "vectorArray":
                v = [custom_types.api.as_vector3_d(_) for _ in props[k]]
                self._set_vector_array(v)
            elif k == "extern_vectorArray":
                v = [extern_types.api.as_vector3d_vector_vector(_) for _ in props[k]]
                self._set_extern_vector_array(v)
        self._on_is_ready.fire()

    def olink_on_property_changed(self, name: str, value: Any) -> None:
        path = Name.path_from_name(name)
        if path == "vector":
            v =  custom_types.api.as_vector3_d(value)
            self._set_vector(v)
            return
        elif path == "extern_vector":
            v =  extern_types.api.as_vector3d_vector_vector(value)
            self._set_extern_vector(v)
            return
        elif path == "vectorArray":
            v = [custom_types.api.as_vector3_d(_) for _ in value]
            self._set_vector_array(v)
            return
        elif path == "extern_vectorArray":
            v = [extern_types.api.as_vector3d_vector_vector(_) for _ in value]
            self._set_extern_vector_array(v)
            return
        logging.error("unknown property: %s", name)

    def olink_on_signal(self, name: str, args: list[Any]):
        path = Name.path_from_name(name)
        if path == "valueChanged":
            vector =  custom_types.api.as_vector3_d(args[0])
            extern_vector =  extern_types.api.as_vector3d_vector_vector(args[1])
            vector_array = [custom_types.api.as_vector3_d(_) for _ in args[2]]
            extern_vector_array = [extern_types.api.as_vector3d_vector_vector(_) for _ in args[3]]
            self.on_value_changed.fire(vector, extern_vector, vector_array, extern_vector_array)
            return
        logging.error("unknown signal: %s", name)
