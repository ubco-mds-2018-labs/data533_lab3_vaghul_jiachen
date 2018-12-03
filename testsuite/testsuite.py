import unittest
from unittests.teststats import TestStats

def testSuite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestStats))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
    
testSuite()
