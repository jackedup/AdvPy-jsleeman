import unittest
import os
import sys
import main as kattis
def Test(self, testin, testout):
        inputf = open(testin)
        input = inputf.read()
        
        actualout = ""
        for line in input.splitlines():
                actualout += str(kattis.eval(line)) + '\n'
        expectedoutfile = open(testout)
        expectedout = expectedoutfile.read()
        inputf.close()
        expectedoutfile.close()
        self.assertEqual(expectedout,actualout)
class TestSecrets(unittest.TestCase):
    def test_easytest(self):
        actualout = kattis.eval("4,2,2")
        self.assertEqual(actualout, 14522)
    def test_mediumtest(self):
        actualout = kattis.eval("9,,2")
        self.assertEqual(actualout, 32402)
    def test_hardtest(self):
        actualout = kattis.eval("3,2,,")
        self.assertEqual(actualout, 655200)
    
if __name__ == '__main__':
    unittest.main()
