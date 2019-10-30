from jutils3.terminal import terminal
from jutils3.utils.config_utils import load_config
from jutils3.utils.import_utils import import_object

try:
    print("Loading configuration...")
    config = load_config("config.json")
except:
    print("Failed to load, using fallback configuration.")
    config = {
        "commands": {
            "default_commands": [
                "jutils",
                "help",
                "quit",
                "print",
                "clear",
                "wait",
                "define"
            ],
            "hand_commands": [
                "hand",
                "unhand",
                "store"
            ],
            "file_commands": [
                "load_file",
                "save_file",
                "load_json",
                "save_json"
            ],
            "table_commands": [
                "dicloadinf",
                "csvloadinf",
                "dlsloadinf",
                "fromtbl",
                "peek",
                "select",
                "search",
                "limit",
                "results",
            ]
        }
    }

terminal = terminal.Terminal(["[jutils3 by rcj0003] Created @ 2019", ""], input, print, cursor = config.get("cursor", ": "))

try:
    print("Loading commands...")
    for module, commands in config["commands"].items():
        for command in commands:
            terminal.register_command(import_object(module, command))
except:
    print("There was an error while loading commands! Check your configuration and ensure that you are pointing to valid commands! The terminal will terminate.")

terminal.execute("clear")
terminal.run()