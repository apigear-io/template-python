from olink.remotenode import RemoteNode

from demo_api import api



class CounterService(object):
    def __init__(self):
        super().__init__()
        self.value = 0

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value != self.value:
            self.value = value
            RemoteNode.notify_property_change('demo.Counter/value', value)
    def increment(self):
        raise NotImplementedError()
    def decrement(self):
        raise NotImplementedError()

    async def run(self):
        pass