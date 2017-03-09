from macros import *

def transform_layers(layer):
    if isinstance(layer, str):
        if "-" in layer:
            layer_split = layer.split("-")
            range_start = int(layer_split[0])
            range_end = int(layer_split[1])

            return list(range(range_start, range_end))

    return [0]

class pressed(object):
    def __init__(self, key, title, layers = "any"):
        self.key = key
        self.title = title
        self.layers = transform_layers(layers)

    def __call__(self, method):
        decorator_self = self
        self.method = method
        def wrappee( *args, **kwargs):
            Macros.register(self.key, self)
        return wrappee
