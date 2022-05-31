from os import environ
import asyncio
from org_objectapi_testbed.api import api
from . import shared

class Interface1Service(object):
    def __init__(self, session):
        self._session = session
        self._listener = None
        self._state = shared.Interface1State(
            prop1=False,
            prop2=0,
            prop3=0.0,
            prop4=str(),
            prop5=[],
            prop6={},
            prop7=0,
            prop10=[],
            prop11=[],
            prop12=[],
            prop14=[]
        )

    def _set_listener(self, listener: shared.Interface1EventListener):
        self._listener = listener

    async def _call(self, op: str, *args, **kwargs):
        # call a remote procedure
        return await self._session.call(f'org.objectapi.testbed.Interface1.{op}', *args, **kwargs)

    def _on_state_event(self, msg):
        # handle remote state change
        self._state = shared.Interface1State.parse_obj(msg)

    def _on_sig1(self, msg):
        # notify listener
        print('on sig1', msg)
        if self._listener:
            self._listener.sig1(**msg)

    def _on_sig2(self, msg):
        # notify listener
        print('on sig2', msg)
        if self._listener:
            self._listener.sig2(**msg)

    def _on_sig3(self, msg):
        # notify listener
        print('on sig3', msg)
        if self._listener:
            self._listener.sig3(**msg)

    async def _register(self):
        # register all signals and state changed
        await self._session.subscribe(self._on_state_event, 'org.objectapi.testbed.Interface1')
        await self._session.subscribe(self._on_sig1, 'org.objectapi.testbed.Interface1.sig1')
        await self._session.subscribe(self._on_sig2, 'org.objectapi.testbed.Interface1.sig2')
        await self._session.subscribe(self._on_sig3, 'org.objectapi.testbed.Interface1.sig3')

    @property
    def prop1(self):
        return self._state.prop1

    @property
    def prop2(self):
        return self._state.prop2

    @property
    def prop3(self):
        return self._state.prop3

    @property
    def prop4(self):
        return self._state.prop4

    @property
    def prop5(self):
        return self._state.prop5

    @property
    def prop6(self):
        return self._state.prop6

    @property
    def prop7(self):
        return self._state.prop7

    @property
    def prop10(self):
        return self._state.prop10

    @property
    def prop11(self):
        return self._state.prop11

    @property
    def prop12(self):
        return self._state.prop12

    @property
    def prop14(self):
        return self._state.prop14

    async def op1(self):
        return await self._call('op1')

    async def op2(self, step: int):
        return await self._call('op2', step)

    async def op3(self):
        return await self._call('op3')

class Interface2Service(object):
    def __init__(self, session):
        self._session = session
        self._listener = None
        self._state = shared.Interface2State(
            prop200=0,
            prop201=0,
            prop202=0,
            prop203=0.0,
            prop204=0.0,
            prop205=str()
        )

    def _set_listener(self, listener: shared.Interface2EventListener):
        self._listener = listener

    async def _call(self, op: str, *args, **kwargs):
        # call a remote procedure
        return await self._session.call(f'org.objectapi.testbed.Interface2.{op}', *args, **kwargs)

    def _on_state_event(self, msg):
        # handle remote state change
        self._state = shared.Interface2State.parse_obj(msg)

    async def _register(self):
        # register all signals and state changed
        await self._session.subscribe(self._on_state_event, 'org.objectapi.testbed.Interface2')

    @property
    def prop200(self):
        return self._state.prop200

    @property
    def prop201(self):
        return self._state.prop201

    @property
    def prop202(self):
        return self._state.prop202

    @property
    def prop203(self):
        return self._state.prop203

    @property
    def prop204(self):
        return self._state.prop204

    @property
    def prop205(self):
        return self._state.prop205
