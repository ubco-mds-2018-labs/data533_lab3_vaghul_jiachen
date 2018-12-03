import unittest

try:
    from unittests.teststats import TestStats
    from unittests.testodbc import TestODBC
except ImportError:
    from .unittests.teststats import TestStats
    from .unittests.testodbc import TestODBC

def testSuite():
    print("\n\n###################################################")
    print("EXECUTING XUEBADB TEST-SUITE")
    print("###################################################\n")
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestODBC))
    suite.addTest(unittest.makeSuite(TestStats))
    runner = unittest.TextTestRunner()
    print(f"\nRESULTS: [{runner.run(suite)}]")
    print("\n###################################################")
    print("###################################################")
