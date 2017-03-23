from windows import *
import time

"""
Responsible for managing macros
"""
class Macros:
    """Maps keyboard key to method"""
    @staticmethod
    def register(key, macro):
        for layer in macro.layers:
            Macros.macros[layer][key] = macro

# Initializes Macros static class
Macros.macros = [{}] * 10
Macros.layer = 0
