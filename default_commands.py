from jutils3.terminal import terminal as term
import jutils3.terminal.decorators as decorators
from jutils3.utils import utils
import jutils3.utils.compatibility as compat
import os

@decorators.description("Provides information about the running instance of jutils3.")
def jutils(terminal, arguments, data = None):
    terminal.output("[jutils3 by rcj0003]", "Running Version Information:", compat.get_version_string())
    return None

@decorators.description("Prints a list of commands and their descriptions.")
def help(terminal, arguments, data = None):
    terminal.output("Commands", "---")
    for command_name, command in terminal.commands.items():
        terminal.output(f"'{command_name}'")
        command(terminal, ["--desc"])
        terminal.output("")

@decorators.description("Provides information about the running instance of jutils3.")
def clear(terminal, arguments, data = None):
    os.system('cls||clear')
    return None

@decorators.minimum_args(1)
@decorators.description("Defines a variable based on provided arguments or passed data.")
def define(terminal, arguments, data = None):
    terminal.variables[arguments[0]] = data
    return None

@decorators.description("Exits the terminal.")
def quit(terminal, arguments, data = None):
    terminal.exit()
    return True

@decorators.description("Prints out provided arguments.")
def print(terminal, arguments, data = None):
    if '--data' in arguments:
        terminal.output(data)
    else:
        terminal.output(*arguments)
    return None

@decorators.description("Waits the specified time in milliseconds.")
def wait(terminal, arguments, data = None):
    start = utils.get_system_time()
    time = 1000 if len(arguments) == 0 else utils.try_parse(arguments[0], 1000)
    while start + time > utils.get_system_time():
        pass