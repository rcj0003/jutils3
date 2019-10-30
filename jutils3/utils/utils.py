from jutils3.object.object_stream import Stream
import hashlib as sha
import datetime
import time
import traceback
import shlex

def try_parse(value, otherwise = 0):
    """Parses value to an integer, otherwise it returns the 0 or the second parameter."""
    try:
        return int(value)
    except:
        return otherwise

def replace_all(string, values):
    """Parses string to replace all values (%value%) with their corresponding dictionary value."""
    for x in values.keys():
        if values.get(x, None) != None:
            string = string.replace(f"%{x}%", str(values[x]))
    return string

def convert_string_to_hash(string):
    """Returns a SHA256 hash from a string."""
    return sha.sha256(string.encode(encoding="UTF-16")).hexdigest()

def log_traceback_to_file(filename):
    """Logs the most recent traceback to a file named 'filename'."""
    with open(filename, "a") as fileWrite:
        fileWrite.write(get_system_time_string() + "\n" + traceback.format_exc())

def get_system_time():
    """Returns the system time in milliseconds."""
    return int(round(time.time() * 1000))

def get_system_time_string():
    """Returns a string based on the current system time."""
    return getStringFromTimestamp(get_system_time())

def getStringFromTimestamp(time):
    """Converts a timestamp in milliseconds to a string."""
    return str(datetime.datetime.fromtimestamp(time / 1000))

def string_to_int_list(string):
    """Converts a string to an integer list. The elements correspond to the character code in the original string."""
    return Stream().map_data(lambda x: ord(x), string).get_results()

def int_list_to_string(intList):
    """Converts an integer list into a string."""
    return "".join(Stream().map_data(lambda x: chr(x), intList))

def xor_crypto(key, data):
    """Encrypts 'data' with 'key' using symmetric XOR encryption."""
    if type(data) is str:
        data = string_to_int_list(data)

    if type(key) is str:
        key = string_to_int_list(key)

    if type(data) is list:
        offset = 0
        for x in range(0, len(data)):
            data[x] ^= key[offset]
            offset = offset + 1 if offset + 1 < len(key) else 0
        
        return data

def parse_command(string):
    """Splits and parses a string into a useable command format in tuple form, with the first element being the main command, and the second being a list of arguments. "command test" would return ("command", ["test"])"""
    data = shlex.split(string)
    return ("", []) if len(data) == 0 else (data[0].lower(), data[1:] if len(data) >= 2 else [])

def get_parsed_input(dialog):
    """Returns a tuple with the primary command as the first element and the arguments (list form) as the second element."""
    while True:
        commandInput = input(dialog)
        if len(commandInput.replace(" ", "")) == 0:
            continue
        return parse_command(commandInput)

def create_embedded_list(keys, values):
    """Creates an embedded list, using each key as the first element and each value as the second element in each sub-list."""
    return list(map(lambda x, y: [x, y], keys, values))

def create_tuple_list(keys, values):
    """Creates a tuple list, using each key as the first element and each value as the second element in each tuple."""
    return list(map(lambda x, y: (x, y), keys, values))

def createDictionary(keys, values):
    """Creates a dictionary given keys and values."""
    return dict(map(lambda x, y: (x, y), keys, values))