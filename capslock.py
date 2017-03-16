from decorators import *
from macros import *
from windows import *
from keys import *
import os

# Change title of command line window so it's better distinguished from default
# command lines.
os.system("title BetterLock")

# Start windows class that deals with dll's and winapi
Windows.start()

"""Main class that glues everything together"""
class Capslock:
    """Starts capslock application"""
    @staticmethod
    def start():
        # If we have events, pop the event which we can then access through
        # .get_key() and .just_pressed()
        while(True):
            if Windows.caps.has_events():
                Windows.caps.pop()
                key = Windows.caps.get_key()

                # Now that we know which key was pressed we can loop through all
                # registered macros to see if there is macro with that key
                # registered.
                for _key, macro in Macros.macros[Macros.layer].items():
                    if key == keys[_key] and Macros.layer in macro.layers:
                        macro.method()
