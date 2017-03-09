from windows import *
import time

class Macros:
    @staticmethod
    def register(key, macro):
        for layer in macro.layers:
            Macros.macros[layer][key] = macro

Macros.macros = [{}] * 10

Macros.layer = 0
