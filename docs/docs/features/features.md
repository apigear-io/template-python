import CodeBlock from '@theme/CodeBlock';
import helloWorldModuleComponent from '!!raw-loader!./data/helloworld.module.yaml';
import Figure from '../figure'

# Features

This guide explains how to use the generated code, what are the available features and  their benefits.

## Get started

This template generates code for [*Python*](https://www.python.org/) projects. In order to successfully compile and use the code, you need to have the *Python* installed (at least 3.12). Check [the Python website](https://www.python.org/downloads/) for downloads.
Basic understanding of *Python* is required.

### Code generation
Follow the documentation for the [code generation](/docs/start/first_steps) in general and [CLI](/docs/cli/generate) or the [Studio](/docs/studio/intro) tools.
Or try first the [quick start guide](../quickstart/index.md) which shows how to prepare api and generate code out of it.

:::tip
For questions regarding this template please go to our [discussions page](https://github.com/orgs/apigear-io/discussions). For feature requests or bug reports please use the [issue tracker](https://github.com/apigear-io/template-python/issues).
:::

### Example API

The following code snippet contains the *API* which is used throughout this guide to demonstrate the generated code and its usage in *Python*.

<details>
    <summary>Hello World API (click to expand)</summary>
    <CodeBlock language="yaml" showLineNumbers>{helloWorldModuleComponent}</CodeBlock>
</details>

## Features

### Core
Features generate a view model for the `api`. This can be used to implement a working service and directly use it in your UI project.
- [api] TBD - generates abstract base interface and a basic implementation for data types
- [stubs] TBD - adds a basic stubs for the `api`, you'll get classes that can be instantiated and have some default behavior.

### Extended
Features can be used in combination with `api` and add more functionality on top, like the simulation
- [olink] TBD - provides a client and server adapters for each interface, that can be connected to any of the other technology templates with support for [ObjectLink](/docs/advanced/objectlink/intro). Use this feature to connect with ApiGear simulation tools.
- [MQTT] TBD - provides minimal working adapters for MQTT client and service side for each interfaces. Check also MQTT in other technology templates that supports it. Also examples are provided:
    - `examples/mqtt/server.py` that shows usage of your services in mqtt server adapter.
    - `examples/mqtt/client.py` that shows usage of your interfaces in mqtt client adapter.

There is also an *internal* feature `apigear`, which is generated for the *extended* features, its usage is explained with the extended features.
Each feature can be selected using the solution file or via command line tool.
:::note
*Features are case sensitive, make sure to always **use lower-case.** *
:::
:::tip
The *meta* feature `all` enables all specified features of the template. If you want to see the full extent of the generated code `all` is easiest solution.
Please note, `all` is part of the code generator and not explicitly used within templates.
:::
## Folder structure

This graph shows the full folder structure which is generated for `all` features enabled.
 Generated features are encapsulated in separate folders inside the module folder, here `io_world` or for the common features like `examples` and the internal helper feature `apigear`, a level above, in the `generation layer` level, here `qt_hello_world`. For more details visit the documentation for each feature. 

```bash
📂hello-world
 ┣ 📂apigear
 ┃ ┣ 📜helloworld.solution.yaml
 ┃ ┗ 📜helloworld.module.yaml
 ┣ 📂py_hello_world
 ┃ ┣ 📂apigear
 ┃ ┣ 📂examples
 ┃ ┃ ┣ 📂mqtt
 ┃ ┃ ┗ 📂olink
 # highlight-next-line
 ┃ ┣ 📂io_world
 ┃ ┃ ┣ 📂api
 ┃ ┃ ┣ 📂impl
 ┃ ┃ ┣ 📂mqtt
 ┃ ┃ ┗ 📂olink
 ┃ ┣ 📂utlis
 ┃ ┗ 📜requirements.txt
```
