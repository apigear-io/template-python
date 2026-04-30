"""Pytest configuration for the generated SDK tests.

Adds session-scope hygiene for the MQTT broker: retained property
messages from prior test runs persist at the broker across client
disconnects. Without cleanup they pre-populate a sink's local cache
on subscribe, causing `set_propX(value)` calls to short-circuit
when the cache already happens to match — silently breaking tests
that wait on `on_*_changed` events.

Set APIGEAR_MQTT_SKIP_CLEAN=1 to disable (e.g., when pointing at a
shared broker you don't own). Override the broker via
MQTT_BROKER_HOST / MQTT_BROKER_PORT env vars (default localhost:1883).
"""
import os
import time

import pytest

try:
    import paho.mqtt.client as _mqtt
    _MQTT_AVAILABLE = True
except ImportError:
    _MQTT_AVAILABLE = False


@pytest.fixture(scope="session", autouse=True)
def _clear_mqtt_retained_at_session_start():
    if not _MQTT_AVAILABLE:
        yield
        return
    if os.environ.get("APIGEAR_MQTT_SKIP_CLEAN"):
        yield
        return

    host = os.environ.get("MQTT_BROKER_HOST", "localhost")
    port = int(os.environ.get("MQTT_BROKER_PORT", "1883"))

    seen = set()

    def on_message(client, userdata, msg):
        if msg.retain and len(msg.payload) > 0:
            seen.add(msg.topic)

    client_id = f"pytest-retained-cleaner-{int(time.time())}"
    client = _mqtt.Client(protocol=_mqtt.MQTTv5, client_id=client_id)
    client.on_message = on_message

    try:
        client.connect(host, port)
    except Exception:
        # broker not reachable — MQTT tests will fail/skip on their own
        yield
        return

    client.subscribe("#", 0)
    client.loop_start()
    time.sleep(0.5)
    client.loop_stop()

    for topic in seen:
        client.publish(topic, b"", qos=0, retain=True)

    time.sleep(0.3)
    client.disconnect()
    yield
