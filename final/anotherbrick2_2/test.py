import unittest
import os
import sys
import main as kattis
class TestBricks(unittest.TestCase):
    def test_uno(self):
        h = 2
        w = 10
        n = 10
        result = str(kattis.eval("2 2 2 2 2 2 2 2 2 2", h, w, n))
        self.assertEqual(result, "YES")
    def test_dos(self):
        h = 4
        w = 10
        n = 8
        result = str(kattis.eval("5 3 8 1 3 4 1 2", h, w, n))
        self.assertEqual(result, "NO")
    def test_tres(self):
        h = 2
        w = 100
        n = 10
        result = str(kattis.eval("100 10 20 10 10 10 10 10 10 10", h, w, n))
        self.assertEqual(result, "YES")
if __name__ == '__main__':
    unittest.main()
