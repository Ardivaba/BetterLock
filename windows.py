from ctypes import *

class Windows:
    @staticmethod
    def start():
        caps = cdll.LoadLibrary("./BetterLock/Debug/BetterLock.dll")
        caps.start()
        Windows.caps = caps

    @staticmethod
    def send_string(string):
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys(string)

#while(True):
#    if c.has_events():
#        c.pop()
#        print(c.get_key())
