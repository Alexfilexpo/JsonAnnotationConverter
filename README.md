# JsonAnnotationConverter
Small package for converting Annotell JSON Annotations to OpenLabel JSON Annotations

# Structure
Package build using Python 3.8 and FastApi

# Prerequirements
Create virtual environment. Run in terminal:<br/>
  ```sh build_environment.sh```
  
# How to
If you need to use API - run this script in terminal:<br/>
```sh run_api.sh```<br/>
Server will run on 127.0.0.1:8000.
FastAPI provides API client for requests.
Using this client you can send your Annotell json data and OpenLabel will be received as a response.

If you need to run Converter locally as standalone - run this script in terminal:<br/>
```sh run_standalone.sh```<br/>
It will run standalone_example.py script where local Annotell json file is read and parsed to convert it as OpenLabel json data output. 
