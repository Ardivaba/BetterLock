from capslock import *
import os

#@pressed("", "")
#def method():
#    os.system("")
#method()

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

# Vision

# Maps left side keys to right side keys
# map_keys(['i', 'j', 'k', 'l'], ['up arrow', 'left arrow', 'down arrow', 'right arrow'])

@pressed("f1", "Set macro layers to 0", "any")
def macro_layer_to_0():
    macros.set_layer(0)
macro_layer_to_0()

@pressed("f2", "Set macro layers to 1", "any")
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









# EOF
