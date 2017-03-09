from windows import *
import time

class Macros:
    @staticmethod
    def register(key, method):
        Macros.macros[key] = method

Macros.macros = {}
