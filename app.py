from capslock import *

@pressed("p", "Print Hello World")
def print_hello_world():
    print("Hello world...")
print_hello_world()

Capslock.start()
