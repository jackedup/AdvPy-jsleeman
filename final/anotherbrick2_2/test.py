import unittest
import os
import sys
import main as kattis
def Test(self, testin, testout):
        inputf = open(testin)
        input = inputf.read()
        actualout = ""
        firstline = True
        h =0
        w =0
        n =0
        for line in input.splitlines():
            if firstline:
                firstline = False
                liney = line.split()
                h = int(liney[0])
                w = int(liney[1])
                n = int(liney[2])
            else:
                result = str(kattis.eval(line, h, w, n))
                if (result != "None"): #python returns None as String?
                    actualout += str(result)
        expectedoutfile = open(testout)
        expectedout = expectedoutfile.read()
        inputf.close()
        expectedoutfile.close()
        self.assertEqual(expectedout,actualout)
class TestSecrets(unittest.TestCase):
    tests = [ ["test1.txt", "test1out.txt"],
                ["test2.txt", "test2out.txt"],
                ["test3.txt", "test3out.txt"]
             ]
    def test_all(self):
        for test in self.tests:
            Test(self, test[0],test[1])
    
if __name__ == '__main__':
    unittest.main()
