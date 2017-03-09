from macros import *

class pressed(object):
    def __init__(self, key, title):
        self.key = key
        self.title = title
    def __call__(self, original_func):
        decorator_self = self
        def wrappee( *args, **kwargs):
            Macros.register(self.key, original_func)
        return wrappee
