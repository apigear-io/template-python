from os import environ
import asyncio

from org_objectapi_testbed.api import api
from . import shared

class Interface1Service(object):
    def __init__(self):
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

    def _get_state(self):
        return self._state

    def _set_state(self, **msg):
        try:
            # if all properties were transferred set them at once
            self._state = shared.Interface1State.parse_obj(msg)
        except:
            # if a property is missing try partial updates
            if 'prop1' in msg:
                self._state.prop1 = msg['prop1']
            if 'prop2' in msg:
                self._state.prop2 = msg['prop2']
            if 'prop3' in msg:
                self._state.prop3 = msg['prop3']
            if 'prop4' in msg:
                self._state.prop4 = msg['prop4']
            if 'prop5' in msg:
                self._state.prop5 = msg['prop5']
            if 'prop6' in msg:
                self._state.prop6 = msg['prop6']
            if 'prop7' in msg:
                self._state.prop7 = msg['prop7']
            if 'prop10' in msg:
                self._state.prop10 = msg['prop10']
            if 'prop11' in msg:
                self._state.prop11 = msg['prop11']
            if 'prop12' in msg:
                self._state.prop12 = msg['prop12']
            if 'prop14' in msg:
                self._state.prop14 = msg['prop14']

    def op1(self) -> None:
        raise NotImplementedError("Not implemented Interface1.op1")

    def op2(self, step: int) -> None:
        raise NotImplementedError("Not implemented Interface1.op2")

    def op3(self) -> int:
        raise NotImplementedError("Not implemented Interface1.op3")

    def sig1(self):
        if self._listener:
            self._listener.notifySig1()

    def sig2(self, step: int):
        if self._listener:
            self._listener.notifySig2(step)

    def sig3(self):
        if self._listener:
            self._listener.notifySig3()

    # service logic can be handled here
    async def run(self):
        pass

class Interface2Service(object):
    def __init__(self):
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

    def _get_state(self):
        return self._state

    def _set_state(self, **msg):
        try:
            # if all properties were transferred set them at once
            self._state = shared.Interface2State.parse_obj(msg)
        except:
            # if a property is missing try partial updates
            if 'prop200' in msg:
                self._state.prop200 = msg['prop200']
            if 'prop201' in msg:
                self._state.prop201 = msg['prop201']
            if 'prop202' in msg:
                self._state.prop202 = msg['prop202']
            if 'prop203' in msg:
                self._state.prop203 = msg['prop203']
            if 'prop204' in msg:
                self._state.prop204 = msg['prop204']
            if 'prop205' in msg:
                self._state.prop205 = msg['prop205']

    # service logic can be handled here
    async def run(self):
        pass
