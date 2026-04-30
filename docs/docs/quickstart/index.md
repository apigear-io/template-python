---
sidebar_position: 2
---
import QuickStartCommon from "@site/docs/_quickstart_common.md"

# Quick-Start

The Quick-Start guide explains how to, in few steps, get from an API to a functional *Python* plugin.
Steps 1 and 3 are universal for other technologies. In the step 2 you will choose a concrete *Python* template.
For more general information about first steps with ApiGear [First Steps](/docs/guide/quick-start)

The quick start enables only the basic features: the `api` generation and the `scaffold` skeleton with stub implementations you can fill in.
For all available features check the [overview](../features/features.md).

<QuickStartCommon />

## 5. Use the generated Python project

### Project folder structure
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
It contains both features generated: the `api` and the `scaffold` skeleton with stub implementations.

:::note
Make sure you have *Python* in at least 3.11 version and pip package installer for python. 
:::
The generated code provides *Python* implementations. The following paragraphs show how you can use it.
Start with installing all the requirements in `requirements.txt` file in top level directory with command
`pip install --upgrade -r requirements.txt`
:::tip
It is recommended to install the dependencies in a virtual environment(venv).
:::

The `api.py` contains all definitions of the enums and structs for your module, as well as the abstract base classes for your interfaces.
From now on you can simply import the `api` module or the scaffolded implementation modules and use them.
For more details on the generated features see the [features overview](../features/features.md).

:::tip
Check the extended features to see how to use your API over the network.
:::

:::note
For simulation, see the [`olink` feature](../features/features.md#extended), which provides a middle layer on your code side, and the [simulation docs](/docs/scripting/backends/intro).
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
