import unittest
import os
import sys
import main as kattis

class TestNumbers(unittest.TestCase):
    def test_one(self):
        actualout = kattis.eval("4,2,2")
        self.assertEqual(actualout, 14522)
    def test_two(self):
        actualout = kattis.eval("9,,2")
        self.assertEqual(actualout, 32402)
    def test_three(self):
        actualout = kattis.eval("3,2,,")
        self.assertEqual(actualout, 655200)
    
if __name__ == '__main__':
    unittest.main()
