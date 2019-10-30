import jutils3.terminal.decorators as decorators
from jutils3.utils.config_utils import load_config, save_config
import json

@decorators.description("Loads a file into a string. The string is passable as data to other commands.")
@decorators.minimum_args(1)
def load_file(terminal, args, data = None):
    try:
        with open(args[0], 'r') as file:
            return file.read()
    except:
        terminal.output("An error occurred while trying to load the file.")

@decorators.description("Saves a string into a file. Passed data can be saved with the '--savedata' argument.")
@decorators.minimum_args(1)
def save_file(terminal, args, data = None):
    try:
        with open(args.pop(0), 'w') as file:
            if '--savedata' in args:
                file.write(data)
            else:
                file.writelines(args)
    except:
        terminal.output("An error occurred while trying to load the file.")

@decorators.description("Saves JSON data into a file. Passed data can be saved with the '--savedata' argument.")
@decorators.minimum_args(1)
def load_json(terminal, args, data = None):
    try:
        return load_config(args[0])
    except:
        terminal.output("An error occurred while trying to load the JSON data.")

@decorators.description("Saves JSON data into a file. The first argument must be the same of the file. Passed data can be saved with the '--savedata' argument.")
@decorators.minimum_args(2)
def save_json(terminal, args, data = None):
    try:
        json_data = None
        if '--savedata' in args:
            json_data = data
        else:
            json_data = json.loads(args[1])
        save_config(json_data, args[0])
    except:
        terminal.output("An error occurred while trying to load the JSON data.")