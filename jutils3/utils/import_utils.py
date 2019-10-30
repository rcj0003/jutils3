from importlib import import_module

def import_object(target_module, attribute_name):
    module = import_module(target_module)
    return getattr(module, attribute_name)