import asyncio
import socket
import pytest
from apigear.mqtt import Client, Service


def _set_event(loop, event):
    def f():
        event.set()
    loop.call_soon_threadsafe(f)


@pytest.mark.asyncio
async def test_subscriptions_survive_network_reconnect():
    """A subscription made before a network disconnect should still deliver
    messages after paho-mqtt re-establishes the connection.

    Regression test for the dual TODOs in apigear/mqtt/base.py:
      - the connect-time `clean_start` choice, and
      - the on_connect handler re-subscribing all known topics.
    """
    topic = "tests/apigear/mqtt/base/reconnect/signal"
    client = Client("test-base-reconnect-client")
    service = Service("test-base-reconnect-service")

    loop = asyncio.get_event_loop()

    client_connected = asyncio.Event()
    service_connected = asyncio.Event()

    def _on_client_connected():
        _set_event(loop, client_connected)

    def _on_service_connected():
        _set_event(loop, service_connected)

    client.on_connected += _on_client_connected
    service.on_connected += _on_service_connected

    await client.connect("localhost", 1883)
    await service.connect("localhost", 1883)
    await asyncio.wait_for(client_connected.wait(), timeout=5.0)
    await asyncio.wait_for(service_connected.wait(), timeout=5.0)

    received = []
    received_event = asyncio.Event()

    def on_msg(payload):
        received.append(payload)
        _set_event(loop, received_event)

    subscribed = asyncio.Event()

    def on_sub(mid, codes):
        _set_event(loop, subscribed)

    client.on_subscribed += on_sub

    client.subscribe_for_signal(topic, on_msg)
    await asyncio.wait_for(subscribed.wait(), timeout=5.0)

    # baseline: prove the subscription works pre-disconnect
    service.notify_signal(topic, ["before-disconnect"])
    await asyncio.wait_for(received_event.wait(), timeout=5.0)
    received_event.clear()

    # force a TCP-level disconnect on the client side
    client_connected.clear()
    sock = client.client._sock
    assert sock is not None, "expected paho socket to be live before forced shutdown"
    sock.shutdown(socket.SHUT_RDWR)

    # wait for paho's built-in auto-reconnect to re-establish the TCP link
    await asyncio.wait_for(client_connected.wait(), timeout=15.0)
    # let any deferred SUBSCRIBE round-trips finish
    await asyncio.sleep(0.5)

    # publish a fresh signal — with the unfixed code the broker dropped
    # our session on disconnect (default Session-Expiry-Interval is 0 in
    # MQTTv5 CONNECT properties) and the on_connect handler does not
    # re-issue SUBSCRIBE, so this message is silently lost.
    service.notify_signal(topic, ["after-reconnect"])

    await asyncio.wait_for(received_event.wait(), timeout=5.0)
    assert ["after-reconnect"] in received

    client.disconnect()
    service.disconnect()
