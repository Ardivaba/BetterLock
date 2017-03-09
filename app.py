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

Capslock.start()
