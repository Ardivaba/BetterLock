import unittest
from macros import Macros

class BetterLockTests(unittest.TestCase):
    def test_macro_method_registered(self):
        Macros.initialize()
        Macros.register("d", None)
        self.assertEqual(len(Macros.macros[0]), 1)

unittest.main()
