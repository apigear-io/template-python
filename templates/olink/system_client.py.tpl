from asyncio.queues import Queue
import asyncio
from olink.client import ClientNode
import websockets
import logging

{{ range .System.Modules }}
import {{snake .Name}}_olink
{{- end }}

# set default log level to WARNING and above
logging.basicConfig()
logging.getLogger().setLevel(logging.WARNING)

class Client:
    def __init__(self, node: ClientNode):
        self.send_queue = Queue()
        self.node = node
        self.node.on_write(self._write)
        self.conn = None

    def _write(self, data):
        self.send_queue.put_nowait(data)

    async def _writer(self):
        while True:
            data = await self.send_queue.get()
            if data is None:
                break
            logging.info("client send %s", data)
            await self.conn.send(data)

    async def _reader(self):
        while True:
            try:
                data = await self.conn.recv()
                logging.info("client recv %s", data)
                self.node.handle_message(data)
            except websockets.ConnectionClosed:
                break

    async def connect(self, addr):
        async with websockets.connect(addr) as conn:
            self.conn = conn
            reader = asyncio.create_task(self._reader())
            writer = asyncio.create_task(self._writer())
            try:
                _, pending = await asyncio.wait(
                    [reader, writer], return_when=asyncio.FIRST_COMPLETED
                )
                # cancel pending tasks
                self.send_queue.put_nowait(None)
                for task in pending:
                    task.cancel()
            except asyncio.CancelledError:
                pass
            

# create a client node
node = ClientNode()

# create our client ws adapter
client = Client(node)
{{ range .System.Modules }}
{{ $module := . }}
{{ range .Interfaces }}

# create and register sink for {{$module.Name}}.{{.Name}}
sink = {{snake $module.Name}}_olink.{{.Name}}Sink()
node.link_remote(sink.olink_object_name())
{{- end }}
{{- end }}


ADDR = 'ws://localhost:8000/ws'

async def main():
    await client.connect(ADDR)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
