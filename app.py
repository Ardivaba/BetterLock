from capslock import *
import os
import time
import keys

#@pressed("", "")
#def method():
#    os.system("")
#method()

@pressed("w", "Open white noise website")
def open_white_noise_website():
    os.system("explorer http://onlinetonegenerator.com/432Hz.html")
open_white_noise_website()

@pressed("i", "Open a super important book")
def open_a_super_important_book():
    os.system("explorer C:\\Users\\Kasutaja\\Desktop\\Books\\How to Win Friends and Influence People")
open_a_super_important_book()

@pressed("y", "Print")
def print_something():
    print("Hey, here's something")
print_something()

@pressed("p", "Print Hello World")
def print_hello_world():
    print("Hello world...")
print_hello_world()

@pressed("r", "Open ruby documentation")
def open_ruby_documentation():
    os.system("explorer http://ruby-doc.org/")
open_ruby_documentation()

@pressed("g", "Open google")
def open_google():
    os.system("explorer http://google.com/")
open_google()

@pressed("c", "Open cmd")
def open_cmd():
    os.system("start cmd.exe")
open_cmd()

@pressed("e", "Edit macros")
def edit_macros():
    os.system("atom C:/Users/Kasutaja/Desktop/BetterLock/app.py")
edit_macros()

@pressed("p", "Open project folder")
def open_project_folder():
    os.system("explorer C:\\Users\\Desktop\\Chat")
open_project_folder()

@pressed("o", "Open my timetable")
def open_ois():
    os.system("explorer http://itcollege.ois.ee/")
open_ois()

@pressed("a", "Open bracket")
def open_bracket():
    time.sleep(1)
    Capslock.press_key("alt")
    Capslock.press_key("f4")
open_bracket()

@pressed("f1", "Set macro layers to 0")
def macro_layer_to_0():
    macros.set_layer(0)
macro_layer_to_0()

@pressed("f2", "Set macro layers to 1")
def macro_layer_to_1():
    macros.set_layer(1)
macro_layer_to_1()

# Third optional argument is set to 1-3 which means that this macro only works
# on layers 1 through 3
@pressed("p", "Print memes", "1-3")
def print_memes():
    print("A Cat.")
print_memes()

Capslock.start()
