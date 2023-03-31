import asyncio
from asyncio.queues import Queue
from typing import Any

from olink.remote import RemoteNode, SourceAdapter
from olink.ws import run_server

import demo

# Counter service registration
counter_impl = demo.Counter()
counter_source = SourceAdapter("demo.Counter", counter_impl)
RemoteNode.register_source(counter_source)

if __name__ == "__main__":
    run_server("localhost", 8152)
