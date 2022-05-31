

## Using

The API is created inside the api folder.

In the examples folder is a usable example project with tests. You can run the example using

Note: The api and example folder will always be cleaned and re-written. So don't modify the files or your changes will get lost.

cd example && python main.py

Test can be run using pytest

cd example && pytest

You can start create your own project from scratch or just copy the example folder inside the root folder and start modifying the content

Please copy the content of the example folder into your root folder and use this as starting

## Updates

When you change the origin API the api and example folder will change during the generator run. You can check in the changes in the examples folder into git to see the diff between to runs and adapt your project code accordingly. Changes can be the API has changed or you use a newer version of the templates and technical details might have changed.



## Features

## HTTP Client and Server

## WAMP Client and Service


### Example

Server is in `wampserver.py`. 

To implement a service just implement the `wampservice.py` inside the WAMP module folder.

