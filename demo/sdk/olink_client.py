from olink.clientnode import ClientNode
from olink.ws.client import Client

import demo

node = ClientNode()
client = Client(node)
node.link_remote('demo.Counter')
demo.olink.sinks.CounterSink()

if __name__ == "__main__":

    repl = REPL()
    repl.cmdloop()