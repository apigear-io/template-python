from olink.core.types import Name
from olink.remotenode import IObjectSource, RemoteNode
from org_objectapi_testbed.api import api
from typing import Any

class Interface1Source(IObjectSource):
    impl: api.IInterface1
    def __init__(self, impl: api.IInterface1):
        self.impl = impl
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "org.objectapi.testbed.Interface1"


    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        self.impl.set_property(path, value)

    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        func = getattr(self.impl, path)
        return func(*args)

    def olink_linked(self, name: str, node: "RemoteNode"):
        print('linked')

    def olink_collect_properties(self) -> object:
        props = ["prop1","prop2","prop3","prop4","prop5","prop6","prop7","prop10","prop11","prop12","prop14" ]
        return {k: getattr(self.impl, k) for k in props}

class Interface2Source(IObjectSource):
    impl: api.IInterface2
    def __init__(self, impl: api.IInterface2):
        self.impl = impl
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "org.objectapi.testbed.Interface2"


    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        self.impl.set_property(path, value)

    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        func = getattr(self.impl, path)
        return func(*args)

    def olink_linked(self, name: str, node: "RemoteNode"):
        print('linked')

    def olink_collect_properties(self) -> object:
        props = ["prop200","prop201","prop202","prop203","prop204","prop205" ]
        return {k: getattr(self.impl, k) for k in props}

