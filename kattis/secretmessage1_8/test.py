import unittest
import os
import sys
import main as kattis
def Test(self, testin, testout):
        inputf = open(testin)
        input = inputf.read()
        
        firstline = True
        actualout = ""
        for line in input.splitlines():
            if firstline:
                kattis.eval(line)
                firstline = False
            else:
                actualout += str(kattis.eval(line)) + '\n'
        expectedoutfile = open(testout)
        expectedout = expectedoutfile.read()
        inputf.close()
        expectedoutfile.close()
        self.assertEqual(expectedout,actualout)
class TestSecrets(unittest.TestCase):
    tests = [ ["test1.txt", "test1out.txt"],
             ["test2.txt", "test2out.txt"],
             [ "test3.txt", "test3out.txt"]]
    def test_all(self):
        for test in self.tests:
            Test(self, test[0],test[1])
    
if __name__ == '__main__':
    unittest.main()
