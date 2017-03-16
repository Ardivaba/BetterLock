from ctypes import *
from keys import *
# import os
# import win32com

"""Enables communication with WinAPI"""
class Windows:
    """Loads BetterLock dll"""
    @staticmethod
    def start():
        caps = cdll.LoadLibrary("./BetterLock/Debug/BetterLock.dll")
        caps.start()
        Windows.caps = caps

    """Doesn't work"""
    @staticmethod
    def send_string(string):
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys(string)

    @staticmethod
    def lock_keyboard():
        Windows.caps.lock_keyboard()

    @staticmethod
    def unlock_keyboard():
        Windows.caps.unlock_keyboard()
        
    """Sends key_press event to WinAPI"""
    @staticmethod
    def press_key(key_code):
        Windows.caps.press_key(keys[key_code])

    """Sends key_released event to WinAPI"""
    @staticmethod
    def release_key(key_code):
        Windows.caps.release_key(keys[key_code])

if __name__ == "__main__":
    Windows.start()
    Windows.press_key("w")
    Windows.release_key("w")
