from os import environ
import asyncio

from org_objectapi_testbed.api import api
from . import shared
from . import service



### Proxy Service

class Interface1Proxy(shared.Interface1EventListener):
    def __init__(self, session, service):
        self.session = session
        self.service = service
        self.service._set_listener(self)

    def op1(self):
        resp = self.service.op1()
        self._publish_state()
        return resp

    def op2(self, step: int):
        resp = self.service.op2(step)
        self._publish_state()
        return resp

    def op3(self):
        resp = self.service.op3()
        self._publish_state()
        return resp

    def notifySig1(self):
        if self.session:
            self.session.publish('org.objectapi.testbed.Interface1.sig1', )

    def notifySig2(self, step: int):
        if self.session:
            self.session.publish('org.objectapi.testbed.Interface1.sig2', step)

    def notifySig3(self):
        if self.session:
            self.session.publish('org.objectapi.testbed.Interface1.sig3', )

    def _get_state(self):
        return self.service._get_state().dict()

    def _set_state(self, **msg):
        self.service._set_state(**msg)
        self._publish_state()

    def _publish_state(self):
        self.session.publish('org.objectapi.testbed.Interface1', **self.service._get_state().dict())

class Interface1Adapter(object):
    def __init__(self, proxy):
        self.proxy = proxy

    def register(self, session, module):
        self.session = session
        self.module = module
        session.register(self.proxy._get_state, f"org.objectapi.testbed.Interface1._get")
        session.register(self.proxy._set_state, f"org.objectapi.testbed.Interface1._set")
        session.register(self.proxy.op1, f"org.objectapi.testbed.Interface1.op1")
        session.register(self.proxy.op2, f"org.objectapi.testbed.Interface1.op2")
        session.register(self.proxy.op3, f"org.objectapi.testbed.Interface1.op3")



### Proxy Service

class Interface2Proxy(shared.Interface2EventListener):
    def __init__(self, session, service):
        self.session = session
        self.service = service
        self.service._set_listener(self)

    def _get_state(self):
        return self.service._get_state().dict()

    def _set_state(self, **msg):
        self.service._set_state(**msg)
        self._publish_state()

    def _publish_state(self):
        self.session.publish('org.objectapi.testbed.Interface2', **self.service._get_state().dict())

class Interface2Adapter(object):
    def __init__(self, proxy):
        self.proxy = proxy

    def register(self, session, module):
        self.session = session
        self.module = module
        session.register(self.proxy._get_state, f"org.objectapi.testbed.Interface2._get")
        session.register(self.proxy._set_state, f"org.objectapi.testbed.Interface2._set")


def register(session):

    # Interface1
    instance = service.Interface1Service()
    proxy = Interface1Proxy(session, instance)
    adapter = Interface1Adapter(proxy)
    adapter.register(session, 'org.objectapi.testbed.Interface1')
    asyncio.create_task(instance.run())

    # Interface2
    instance = service.Interface2Service()
    proxy = Interface2Proxy(session, instance)
    adapter = Interface2Adapter(proxy)
    adapter.register(session, 'org.objectapi.testbed.Interface2')
    asyncio.create_task(instance.run())
