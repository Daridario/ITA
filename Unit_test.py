import unittest

def division(a, b):
    return a / b

class TestDivision(unittest.TestCase):
    def test_divisionByZero(self):
        self.assertRaises(ZeroDivisionError, division, 1, 0)
        
    def test_isString(self):
        self.assertRaises(TypeError, division, "a", "b")
    
    
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestDivision("test_isString"))
    suite.addTest(TestDivision("test_divisionByZero"))
    return suite

mySuite = suite()

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())