# Python SDK Template for ApiGear

The python SDK template support http and object link client and server, based on the same service.

## Usage

```bash
apigear generate expert --input apis/counter.idl --output sdk --template apigear-io/template-python --features http,olink
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
      - http
      - olink
```

```bash
apigear generate solution demo.solution.yaml
```


## Features

* api: creates python interface files
* scaffold: create a full python project
* http: create a http client and http server
* olink: create ObjectLink client and server

## Run ObjectLink Server

Install requirements (pytest, fastapi, websockets, uvicorn)
```bash
pip install -r requirements.txt
```

Run the object link server

```bash
uvicorn olink_server:app
```

## Modify the service implementation

The implementation is in the module `{$module_name}_impl` folder. Each file contains one class that implements the service interface. All methods raise a not implemented exception. It is up to you to implement the service according to your needs.

