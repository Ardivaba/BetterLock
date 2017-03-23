# BetterLock

Capslock is one of the mose useles yet accessible keys on the keyboard. The aim of BetterLock is to make capslock useful by making it into
a modifier key like alt, shift, ctrl etc.
With BetterLock you can create hotkeys that run Python scripts when capslock and one of the keyboard keys are pressed at the same time.

# Installation

```cmd
git clone https://github.com/Ardivaba/BetterLock/
```

# Usage

First import neccessary scripts
```python
from capslock import *
import os # To access os.system
from windows import Windows # If you want to map keys to other keys
```

To create a hotkey you must decorate a method with @pressed decorator. It takes 2 arguments: The key that activated a hotkey and the
description of the hotkey. Define a method itself with arbitrary name and then call the function. *Calling the function registers the
hotkey instead of invoking it, it's the limitation of Python decorators.*

To create a hotkey that opens your hotkeys Python script write it like that:
```python
@pressed("e", "Edit macros - Opens Atom editor with app.py")
def edit_macros():
    os.system("atom your/path/to/app.py")
edit_macros()
```

And then finally start capslock script
```python
Capslock.start()
```
