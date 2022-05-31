from os import environ
import asyncio
from autobahn.asyncio.component import Component, run
import org_objectapi_testbed.wamp.adapter


WAMP_SERVER=u'ws://127.0.0.1:8080/ws'
WAMP_REALM=u"realm1"

comp = Component(
    transports=WAMP_SERVER,
    realm=WAMP_REALM,
)

@comp.on_join
async def joined(session, details):
    org_objectapi_testbed.wamp.adapter.register(session)


if __name__ == '__main__':
    run([comp])
