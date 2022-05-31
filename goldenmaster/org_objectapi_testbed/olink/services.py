from olink.remotenode import RemoteNode

from org_objectapi_testbed.api import api
from . import shared

class Interface1Service(object):
    prop1=False
    prop2=0
    prop3=0.0
    prop4=str()
    prop5=[]
    prop6={}
    prop7=0
    prop10=[]
    prop11=[]
    prop12=[]
    prop14=[]

    def set_property(self, name, value):    
        if value != getattr(self, name):
            setattr(self, name, value)
            RemoteNode.notify_property_change(f'org.objectapi.testbed.Interface1/{name}', value)

    def op1(self):
        raise NotImplementedError()

    def op2(self, step: int):
        raise NotImplementedError()

    def op3(self):
        raise NotImplementedError()

    def sig1(self):
        RemoteNode.notify_signal('org.objectapi.testbed.Interface1/sig1', [])

    def sig2(self, step: int):
        RemoteNode.notify_signal('org.objectapi.testbed.Interface1/sig2', [step])

    def sig3(self):
        RemoteNode.notify_signal('org.objectapi.testbed.Interface1/sig3', [])

    # service logic can be handled here
    async def run(self):
        pass

class Interface2Service(object):
    prop200=0
    prop201=0
    prop202=0
    prop203=0.0
    prop204=0.0
    prop205=str()

    def set_property(self, name, value):    
        if value != getattr(self, name):
            setattr(self, name, value)
            RemoteNode.notify_property_change(f'org.objectapi.testbed.Interface2/{name}', value)

    # service logic can be handled here
    async def run(self):
        pass
