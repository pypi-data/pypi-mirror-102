# PyEasyEmbed

PyEasyEmbed is a little framework to integrate python code into other applications using shell commands. Instead of multiple arguments, a EasyEmbed app expects one JSON-Object to deal with. PyEasyEmbed is written in pure Python3.

## Usage

PyEasyEmbed uses a Server object which dispatches commands.

```python
import EasyEmbed as EE

# The version number is the number of your application which can be used by your main app to determine if the embedded app is compatible
ser = EE.CommandServer(version = "0.1")

# A command responder which returns the input JSON Object, the name of the command is determined by the name of the function
@ser.command
def echo(data):
    return data

# Call the execute function to dispatch the input to the available commands
ser.execute()
```

## Command structure 

A PyEasyEmbed command has always one or two arguments. The first is the name of the called command, the second is a JSON-Object which is parsed and deliverd as a parameter to the command function. Depending on your shell interface you may need to escape quotes. If no JSON-Object is provided, the data paramter will be `None`.

Example call
```
python example.py echo "{\"hello\":\"world\"}"
```

The command server has a standard `info` command which prints the version number of your app, the python version running etc.

### Response structure
To the command call from above the response would be the following:
```json
{
    "status": 0,
    "response": {"hello":"world"}
}
```
In case an exception occured during the command function, the following is returned:
```json
{
    "status": 1,
    "message": "Exception occured while executing command!",
    "exception": Traceback String
}
```
In case the command is not defined:
```json
{
    "status": -1,
    "message": "Command does not exist!"
}
```
In case the JSON-Object could not be parsed:
```json
{
    "status": -3,
    "message": "JSON data could not be parsed!"
}
```