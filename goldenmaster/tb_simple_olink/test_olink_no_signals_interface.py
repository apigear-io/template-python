
from tb_simple_api import api
from tb_simple_impl import NoSignalsInterface
from tb_simple_olink import NoSignalsInterfaceSource, NoSignalsInterfaceSink
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest

@pytest.fixture()
def olink_objects():
    impl = NoSignalsInterface()
    source = NoSignalsInterfaceSource(impl)
    remote_node = RemoteNode()
    client_node = ClientNode()

    remote_node.on_write(client_node.handle_message)
    client_node.on_write(remote_node.handle_message)

    sink = NoSignalsInterfaceSink()
    client_node.link_remote(sink.olink_object_name())
    yield impl, sink

class TestOLinkNoSignalsInterface:
    pass
