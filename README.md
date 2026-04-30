# Python SDK Template for ApiGear

The python SDK template generates ObjectLink and MQTT client/server adapters from an ApiGear interface description, plus a runnable Python project skeleton you can extend with real behavior.

## Usage

```bash
apigear generate expert --input apis/counter.idl --output sdk --template apigear-io/template-python --features olink
```

Or using a solution document
```yaml
# demo.solution.yaml
schema: apigear.solution/1.0

layers:
  - name: demo
    inputs:
      - apis/counter.idl
    output: sdk
    template: appigear-io/template-python
    features:
      - olink
```

```bash
apigear generate solution demo.solution.yaml
```


## Features

* api: creates python interface files
* scaffold: create a full python project
* test_helpers: generates struct builders for tests
* olink: create ObjectLink client and server
* mqtt: create MQTT client and service adapters

## Run ObjectLink Server

Install requirements (pytest, websockets, uvicorn, starlette, olink-core)
```bash
pip install -r requirements.txt
```

Run the object link server

```bash
uvicorn olink_server:app
```

## Modify the service implementation

The implementation is in the module `{$module_name}_impl` folder. Each file contains one class that implements the service interface. All methods raise a not implemented exception. It is up to you to implement the service according to your needs.

