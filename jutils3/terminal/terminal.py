from jutils3.utils import utils

def unknown(terminal, arguments, data = None):
    terminal.output("Unknown command.")

class Terminal():
    def __init__(self, title, terminal_input, terminal_output, cursor = "> "):
        self.title = title
        self.terminal_input = terminal_input
        self.terminal_output = terminal_output
        self.cursor = cursor
        self.variables = {}
        self.commands = {}
        self.running = False

    def __getitem__(self, variable_name):
        return self.variables.get(variable_name, None)

    def output(self, *message):
        for line in message:
            self.terminal_output(line)

    def run(self):
        self.running = True
        self.output(*self.title)
        while self.running:
            self.execute(self.terminal_input(self.cursor))
    
    def exit(self):
        self.running = False
    
    def register_command(self, command):
        if command.__name__ not in self.commands:
            self.commands[command.__name__] = command

    def execute(self, raw_command):
        parsed_command = utils.parse_command(raw_command)
        command = self.commands.get(parsed_command[0], unknown)
        command(self, parsed_command[1])