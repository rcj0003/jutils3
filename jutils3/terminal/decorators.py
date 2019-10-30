from functools import wraps

def minimum_args(minimum_arguments):
    def inner(command_function):
        @wraps(command_function)
        def command(terminal, arguments, data = None):
            if len(arguments) < minimum_arguments:
                terminal.output(f"Expected {minimum_arguments} arguments, got {len(arguments)}.")
                return None
            return command_function(terminal, arguments, data)
        return command
    return inner

def description(*description):
    def inner(command_function):
        @wraps(command_function)
        def command(terminal, arguments, data = None):
            if '--desc' in arguments:
                terminal.output(*description)
                return None
            return command_function(terminal, arguments, data)
        return command
    return inner

def requires_data(data_type):
    def inner(command_function):
        @wraps(command_function)
        def command(terminal, arguments, data = None):
            if data == None or not isinstance(data, data_type):
                terminal.output("Passed data type is not valid.")
                return None
            return command_function(terminal, arguments, data)
        return command
    return inner