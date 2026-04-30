---
sidebar_position: 4
---
import CodeBlock from '@theme/CodeBlock';
import helloWorldModuleComponent from '!!raw-loader!./data/helloworld.module.yaml';

# HTTP

:::caution
The HTTP feature is intentionally minimal: a synchronous client and a [FastAPI](https://fastapi.tiangolo.com/) server, one POST route per operation, no auth, no retries, no async client. It is suitable for local development, scripted tests, and simple service-to-service calls. For production-grade scenarios — back-pressure, streaming property updates, reconnect logic, fan-out — prefer the [`olink`](/docs/protocols/objectlink/intro) or [`mqtt`](mqtt.md) features.
:::

This feature exposes your interfaces over plain HTTP. It generates two halves:

- A **server adapter** built on FastAPI that mounts one POST route per interface operation and wires it to a local interface implementation.
- A **client adapter** built on the [`requests`](https://pypi.org/project/requests/) library that calls those routes and exposes the same `I<Interface>` shape your local code uses.

Operation responses include both the operation `result` and a snapshot of the interface `state` (current property values) so the client can keep its local view of properties up to date after each call.

### Before start

The HTTP libraries need to be installed separately. Make sure you have installed all the libraries listed in `requirements.txt`:

```bash
pip install --upgrade -r requirements.txt
```

When the `http` feature is enabled, `requirements.txt` includes `fastapi`. The server example also needs an ASGI runner such as `uvicorn`.

## File overview for module

With an example API

<details>
  <summary>Hello World API (click to expand)</summary>
  <CodeBlock language="yaml" showLineNumbers>{helloWorldModuleComponent}</CodeBlock>
</details>

the following file structure is generated:

```bash {3,8}
📂hello-world
 ┣ 📂py_hello_world
 ┃ ┣ 📂http
 ┃ ┃ ┗ 📜server.py
 ┃ ┣ 📂io_world
 ┃ ┃ ┣ 📂api
 ┃ ┃ ┣ 📂impl
 ┃ ┃ ┣ 📂http
 ┃ ┃ ┃ ┣ 📜client.py
 ┃ ┃ ┃ ┣ 📜routes.py
 ┃ ┃ ┃ ┣ 📜shared.py
 ┃ ┃ ┃ ┗ 📜__init__.py
 ...
```

- `📜http/server.py` — top-level FastAPI app. It mounts one router per generated module under a prefix that matches the module name.
- `📜io_world/http/routes.py` — the per-module FastAPI `APIRouter`. Defines one POST endpoint per interface operation.
- `📜io_world/http/shared.py` — pydantic request and response models for every operation, plus a `<Interface>State` model that mirrors the interface properties.
- `📜io_world/http/client.py` — synchronous client classes implementing `I<Interface>` by posting to the matching routes.

### Routes

Every operation maps to a single POST route at:

```
POST /{module}/{module}/{interface}/{operation}
```

The leading `/{module}` prefix comes from `server.py` mounting the router; the inner path comes from `routes.py`. For the example above, the `Hello.say` operation is reachable at `POST /io.world/io_world/hello/say`.

Each request body is the matching `<Interface><Operation>Request` pydantic model, and each response body is `<Interface><Operation>Response` containing:

- `result` — the operation's return value (typed to the IDL return type, or `None` for `void`).
- `state` — the current values of the interface's properties at the time the response was built.

:::note
The HTTP routes do not push property changes. Properties are only refreshed on the client when an operation response carries a fresh `state`. If you need real-time property updates, use the `olink` or `mqtt` feature instead.
:::

## HTTP Server Adapter

`📜io_world/http/routes.py` instantiates one local interface object per interface (using the implementation from the `scaffold` feature) and binds each operation to a FastAPI handler. The handler:

1. Deserializes the incoming pydantic request model.
2. Calls the matching method on the local implementation.
3. Reads back all property values to build a `<Interface>State` snapshot.
4. Returns the `result` plus the `state` snapshot.

`📜http/server.py` is the entry point. It instantiates `app = FastAPI()` and includes one router per module:

```python
from fastapi import FastAPI
import io_world.http

app = FastAPI()
app.include_router(io_world.http.routes.router, prefix="/io.world")
```

Run the server with any ASGI runner. Using `uvicorn`:

```bash
uvicorn http.server:app --host 0.0.0.0 --port 8000
```

:::tip
The generated server uses the implementation classes from your `{module}/impl/` folder. Edit those files to change behavior — the routes layer does not need to be regenerated.
:::

## HTTP Client Adapter

`📜io_world/http/client.py` contains one class per interface, named after the interface (for example `Hello`). Each class:

- Implements `I<Interface>` (the abstract base from the `api` feature), so it is drop-in compatible with code that already uses your interface.
- Stores the server URL on construction (defaults to `http://localhost:8000`).
- Holds a local cache of property values, refreshed from the `state` field of every operation response.
- Calls `requests.post(...)` synchronously inside each operation method.

#### Properties

Property getters return the locally cached value. Property setters update the local cache only — they do **not** call the server. Property values on the client are refreshed when an operation response includes a new `state`.

:::caution
There is no remote setter, no property-change notification, and no polling endpoint. The HTTP client's view of properties is only as fresh as the last operation response.
:::

#### Operations

Operation methods are synchronous (`requests` is a blocking library). Calling an operation issues a `POST`, parses the JSON response, refreshes the local property cache from `state`, and returns the `result`.

#### Signals

Signals are not delivered over HTTP. If your interface defines signals and you need to consume them, use `olink` or `mqtt` instead.

### Use the HTTP client

```python
import io_world.api
import io_world.http

# point at the running FastAPI server
hello = io_world.http.client.Hello(url="http://localhost:8000")

# call an operation: posts to /io.world/io_world/hello/say and returns the result
message = io_world.api.Message()
message.content = "Hello over HTTP"
result = hello.say(message, io_world.api.When.NOW)
print("method result:", result)

# property cache is up to date with the server's state after the operation returned
print("last:", hello.get_last())
```

:::note
The client is synchronous. If you need to call operations from `async` code, run them in a worker thread (for example with `asyncio.to_thread`).
:::

## Scope and known limitations

The HTTP feature is deliberately small. Notable limitations:

- **Sync only.** The generated client uses `requests`. There is no async client.
- **No authentication.** No token, header, or session helpers are generated. Bring your own middleware on the FastAPI side and your own auth on the `requests.post` call.
- **No retry or backoff.** Network failures raise; you must wrap calls yourself.
- **No streaming or signals.** Property changes and signals are not pushed; only operation responses carry property snapshots.
- **One process per module.** `server.py` mounts every module on the same FastAPI app under a per-module prefix.

For richer transport — bidirectional updates, signals, reconnect handling — use the [`olink`](/docs/protocols/objectlink/intro) or [`mqtt`](mqtt.md) features.
