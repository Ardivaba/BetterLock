from decorators import *
from macros import *
from windows import *
from keys import *

Windows.start()

class Capslock:
    @staticmethod
    def start():
        while(True):
            if Windows.caps.has_events():
                Windows.caps.pop()
                key = Windows.caps.get_key()

                for _key, method in Macros.macros.items():
                    if key == keys[_key]:
                        method()
