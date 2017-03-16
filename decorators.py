from macros import *

"""
Takes layer string and converts it into array of numbers where each number
signifies seperate layer that the macro exists on
"""
def transform_layers(layer):
    if isinstance(layer, str):
        if "-" in layer:
            layer_split = layer.split("-")
            range_start = int(layer_split[0])
            range_end = int(layer_split[1])

            return list(range(range_start, range_end))

    return [0]

"""
Method decorator that registers a method as a hotkey
"""
class pressed(object):
    """
    When registering a hotkey we need to specify key that the hotkey gets
    executed on, title of the hotkey and a layer that it exists on
    """
    def __init__(self, key, title, layers = "any"):
        self.key = key
        self.title = title
        self.layers = transform_layers(layers)

    """
    Gets called when macro decoratod method is called. The actual method body
    isn't invoked but instead we register it's address as function behind key
    """
    def __call__(self, method):
        decorator_self = self
        self.method = method
        def wrappee( *args, **kwargs):
            Macros.register(self.key, self)
        return wrappee
