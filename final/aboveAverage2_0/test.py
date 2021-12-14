import unittest
import os
import sys
import main as kattis
class TestAverage(unittest.TestCase):
        def test_uno(self):
                actualout = kattis.eval("""5\n5 44 88 74 43 100\n7 110 30 33 55 44 88 90\n3 3 88 33\n3 33 99 66\n9 100 100 0 4 33 70 88 44 44""")
                self.assertEqual(actualout, """60.000%\n42.857%\n33.333%\n33.333%\n44.444%\n""")
        def test_dos(self):
                actualout = kattis.eval("""1\n5 33 88\n 66 99 105\n""")
                self.assertEqual(actualout, """60.000%\n""")
        def test_tres(self):
                actualout = kattis.eval("""2\n2 50 75\n4 177 6 55 86""")
                self.assertEqual(actualout, """50.000%\n50.000%\n""")
         
if __name__ == '__main__':
    unittest.main()
