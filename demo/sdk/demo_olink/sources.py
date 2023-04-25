from olink.core.types import Name
from olink.remotenode import IObjectSource, RemoteNode
from demo_api import api
from typing import Any

class CounterSource(IObjectSource):
    impl: api.ICounter
    def __init__(self, impl: api.ICounter):
        self.impl = impl
        impl._notifier = self
        RemoteNode.register_source(self)

    def olink_object_name(self):
        return "demo.Counter"

    def olink_set_property(self, name: str, value: Any):
        path = Name.path_from_name(name)
        self.impl.set_property(path, value)

    def olink_invoke(self, name: str, args: list[Any]) -> Any:
        path = Name.path_from_name(name)
        func = getattr(self.impl, path)
        if not callable(func):
            raise Exception(f"not callable {name}")
        if args is None:
            return func()
        return func(*args)

    def olink_linked(self, name: str, node: "RemoteNode"):
        print('linked')

    def olink_collect_properties(self) -> object:
        props = {}
        props["value"] = self.impl.get_value()
        return props

    def notify_signal(self, symbol, args):
        RemoteNode.notify_signal(symbol, args)

    def notify_property(self, symbol, value):
        RemoteNode.notify_property_change(symbol, value)