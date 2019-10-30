import json

def save_config(config, file_name):
    with open(file_name, 'w') as file:
        json.dump(config, file)

def load_config(file_name):
    data = {}
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data