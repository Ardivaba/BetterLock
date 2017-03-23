from capslock import *
import os
import time
import keys
from windows import Windows

@pressed("e", "Edit macros - Opens Atom editor with app.py")
def edit_macros():
    os.system("atom C:/Users/Kasutaja/Desktop/BetterLock/app.py")
edit_macros()

# Map arrow ijkl to arrow keys
@pressed("i", "Maps i to up")
def map_i_to_up():
    Windows.unlock_keyboard()
    Windows.press_key("up")
    Windows.release_key("up")
    Windows.lock_keyboard()
map_i_to_up()

@pressed("k", "Maps k to down")
def map_k_to_down():
    Windows.unlock_keyboard()
    Windows.press_key("down")
    Windows.release_key("down")
    Windows.lock_keyboard()
map_k_to_down()

@pressed("j", "Maps j to left")
def map_j_to_left():
    Windows.unlock_keyboard()
    Windows.press_key("left")
    Windows.release_key("left")
    Windows.lock_keyboard()
map_j_to_left()

@pressed("l", "Maps l to left")
def map_l_to_right():
    Windows.unlock_keyboard()
    Windows.press_key("right")
    Windows.release_key("right")
    Windows.lock_keyboard()
map_l_to_right()

@pressed("u", "Maps u to backspace")
def map_u_to_backspace():
    Windows.unlock_keyboard()
    Windows.press_key("backspace")
    Windows.release_key("backspace")
    Windows.lock_keyboard()
map_u_to_backspace()

@pressed("o", "Maps o to backspace")
def map_o_to_tab():
    Windows.unlock_keyboard()
    Windows.press_key("tab")
    Windows.release_key("tab")
    Windows.lock_keyboard()
map_o_to_tab()

Capslock.start()
