
from tb_simple_api import api
from tb_simple_impl import EmptyInterface
from tb_simple_olink import EmptyInterfaceSource, EmptyInterfaceSink
from olink.client import ClientNode
from olink.remote import RemoteNode
import pytest

@pytest.fixture()
def olink_objects():
    impl = EmptyInterface()
    EmptyInterfaceSource(impl)
    remote_node = RemoteNode()
    client_node = ClientNode()

    remote_node.on_write(client_node.handle_message)
    client_node.on_write(remote_node.handle_message)

    sink = EmptyInterfaceSink()
    client_node.link_remote(sink.olink_object_name())
    yield impl, sink

class TestOLinkEmptyInterface:
    pass
    pass
    pass
