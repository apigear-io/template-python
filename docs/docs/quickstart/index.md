---
sidebar_position: 2
---

# Quick-Start

The Quick-Start guide explains how to, in few steps, get from an API to a functional *Python* plugin.
Steps 1 and 3 are universal for other technologies. In the step 2 you will choose a concrete *Python* template.
For more general information about first steps with ApiGear [First Steps](/docs/start/first_steps)

The quick start enables only basic features: the api(TBD) generation and simple stub(TBD) implementation.
For all available features check the [overview](features/features.md).

## 1. Install the code generator

Get the [ApiGear Studio](https://github.com/apigear-io/studio/releases) or [ApiGear CLI](https://github.com/apigear-io/cli/releases). For more information check the [ApiGear documentation](/docs/start/install).

## 2. Get the template

There are several options to get the template. Installation via the *Studio* or the *CLI*. Alternatively it is possible to clone or download from github.

### Installation via CLI

When using the *CLI* only the highlighted line is imported. You can always check whether the installation was successful via the `template list` command.
```bash
$ apigear template list
list of templates from registry and cache
name                       | installed | registry | url
apigear-io/template-python | false     | true     | https://github.com/apigear-io/template-python.git
...
# highlight-next-line
$ apigear template install apigear-io/template-python
$ apigear template list
list of templates from registry and cache
name                       | installed | registry | url
apigear-io/template-python | true      | true     | https://github.com/apigear-io/template-python.git
...
```

### Installation via Studio

From within the studio the installation is really simple.

1. Open an existing project or create an new one
2. Go to the `Templates` tab
3. Click `Install` on the `apigear-io/template-python` entry

### Clone from github

In case you want to check or modify the source code of the template, it is easier to clone or download the repository. The repository does not need to be part of the project, but can be stored anywhere on the computer.
```bash
$ git clone https://github.com/apigear-io/template-python.git
```

## 3. Set up project

For a project we usually need two files. The solution which specifies what `APIs` and which template to use for it. And at least one `API` module file.
Both should ideally be in a folder called `apigear` next to each other.

Alternatively, you can also use the *Studio* to create a new project and modify the two example files.

### Solution file
Create a [solution](/docs/start/first_steps#create-a-solution) file.
The example below specifies
* module files in *line 8*, here the `helloworld.module.yaml` module with `Hello` API
* the output directory for generated files in *line 9*
* a template used to generate the code in *line 10*, here the `apigear-ui/template-python` template. This can also be a path to a local copy of the template.
* the enabled features of the template in *line 13*, here the `stubs` feature, a simple implementation of interfaces. For all available features check the [overview](features/features.md).

```yaml title="helloworld.solution.yaml" showLineNumbers
schema: "apigear.solution/1.0"
name: hello_world_example
version: "0.1.0"

targets:
  - name: hello_world
    inputs:
      - helloworld.module.yaml
    output: ../py_hello_world
    template: apigear-io/template-python
    force: true
    features:
      - stubs
```
:::tip Targets
You can extend this solution file with other targets, each for the different technology with  different template. The module.yaml is technology independent and may be used for any template.
:::

:::note
Set the force parameter to true if you want to always override all the generated files. With option set to false some files, like implementation (stub feature) won't be updated. All the API files are always updated.
:::

### API module file
Use your favorite text editor to create the `helloworld.module.yaml` with the example content:

```yaml title="helloworld.module.yaml" showLineNumbers
schema: apigear.module/1.0
name: io.world
version: "1.0.0"

interfaces:
  - name: Hello
    properties:
      - { name: last, type: Message }
    operations:
      - name: say
        params:
          - { name: msg, type: Message }
          - { name: when, type: When }
        return:
          type: int
    signals:
      - name: justSaid
        params:
          - { name: msg, type: Message }
enums:
  - name: When
    members:
      - { name: Now, value: 0 }
      - { name: Soon, value: 1 }
      - { name: Never, value: 2 }
structs:
  - name: Message
    fields:
      - { name: content, type: string }
```

## 4. Generate code

With the output directory set as in example, both *ApiGear* files reside in an `apigear` subfolder next to the generated files.
In this case the folder structure should look similar to this
```bash
📂hello-world
 ┣ 📂apigear
 ┃ ┣ 📜helloworld.solution.yaml
 ┃ ┗ 📜helloworld.module.yaml
 ┣ 📂py_hello_world
 # highlight-next-line
 ┃ ┣ 📂io_world
 ┃ ┃ ┣ 📂api
 ┃ ┃ ┗ 📂implementation
 ┃ ┗ 📜CMakeLists.txt
```

Using the solution file from the previous paragraph the code will be generated in the `py_hello_world` folder. 
With subfolder for each module, here `io_world` as the name of module (defined in line 2 of `helloworld.module.yaml`).
It contains both features generated: a basic api and a stub implementation.

### Generate via CLI

The following snippet shows how the CLI can be run.

```bash
$ apigear generate solution apigear/helloworld.solution.yaml 
10:52:20 INF generated 38 files in 65ms. (22 write, 0 skip, 16 copy) topic=gen
```
* `generate` tells the CLI that it should generate code
* `solution` specifies that we want to run a solution file
  

### Generate via Studio

1. Open the project
2. Go to the `Solutions` tab
3. Click `Run` on the `helloworld.solution.yaml` entry

## 5. Use the generated Python project.

:::note
Make sure you have *Python* in at least 3.11 version and pip package installer for python. 
:::
The generated code provides *Python* implementations. The following paragraphs show how you can use it.
Start with installing all the requirements in `requirements.txt` file in top level directory with command
`pip install --upgrade -r requirements.txt`
:::tip
It is recommended to install the dependencies in a virtual environment(venv).
:::

The 'api.py' contains all definitions of the enums and structs for your module, as well as the abstract base classes for your Interfaces.
From now on you can simply import the api or the stub implementation modules and use it.
For more details on generated features please check api(TBD), stubs (TBD). 

:::tip
Check the extended features to see how to use your API over the network.
:::

:::note
For the simulation check the olink feature(TBD) which provides middle layer on your code side and the [simulation](/docs/advanced/simulation/intro) explained.
:::

### Create and run an example

Prepare an `examples` folder in the `hello-world/py_hello_world` directory with a main. like this:
```python
import asyncio
import os
import sys

#add context - path to modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import io_world.api
import io_world.impl

def main():
    myHelloInstance = io_world.impl.Hello()

    # Try out properties: subscribe for changes
    def handle_last_changed(message):
         print("last property changed ")
         print(message)
    myHelloInstance.on_last_changed += handle_last_changed
    
    # and ask for change.
    messageForProperty = io_world.api.Message()
    messageForProperty.content = "New message";
    myHelloInstance.set_last(messageForProperty);

    # Check the signals with subscribing for its change
    def handle_just_said(message):
         print("justSaid signal emitted ")
         print(message)
    myHelloInstance.on_just_said += handle_just_said

    # and emit one.
    messageForSignal = io_world.api.Message()
    messageForSignal.content = "Message from signal";
    myHelloInstance._just_said(messageForSignal);

    # Play around executing operations, maybe they emit signals? or change the properties?
    method_result = myHelloInstance.say(io_world.api.Message(), io_world.api.When.NOW);
    print("Method result")
    print(method_result)
    myHelloInstance.on_last_changed -= handle_last_changed
    myHelloInstance.on_just_said -= handle_just_said

if __name__ == '__main__':
    main()

}
```
You can run it e.g from console. Open a terminal, navigate to generated code (`py_hello_world`) and run the example with command `python examples/example.py`.
