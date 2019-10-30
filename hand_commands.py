from jutils3.terminal import terminal as term
import jutils3.terminal.decorators as decorators
from jutils3.utils import utils

@decorators.description("When enabled, passes returned data between each command.")
def hand(terminal, arguments, data = None):
    if 'is_handed' in terminal.variables:
        terminal.output("Data is already being handed!")
        return
    def execute(raw_command):
        parsed_command = utils.parse_command(raw_command)
        command = terminal.commands.get(parsed_command[0], term.unknown)
        terminal.variables["handed_data"] = command(terminal, parsed_command[1], terminal.variables["handed_data"])
    terminal.variables["is_handed"] = True
    terminal.variables["handed_data"] = data
    terminal.old_execute = terminal.execute
    terminal.execute = execute

@decorators.description("Disables handing mode.")
def unhand(terminal, arguments, data = None):
    terminal.execute = terminal.old_execute
    del terminal.variables["is_handed"]
    del terminal.variables["handed_data"]
    del terminal.old_execute

@decorators.minimum_args(1)
@decorators.description("Stores data to be passed to the next command.")
def store(terminal, arguments, data = None):
    return arguments[0]
