from windows import Windows
from decorators import *

@pressed("i", "Maps i to up")
def map_i_to_up():
    print("Hello?")
    Windows.unlock_keyboard()
    Windows.press_key("up")
    Windows.release_key("up")
    Windows.lock_keyboard()
map_i_to_up()
