import unittest # The unittest module

# Create a test case by subclassing unittest.TestCase
class MyTestCase(unittest.TestCase):
    def test_addition(self):
        result = 2 + 2
        self.assertEqual(result, 4)

    def test_subtraction(self):
        result = 5 - 3
        self.assertEqual(result, 9)

# Create a test suite to group multiple test cases
suite = unittest.TestSuite()
suite.addTest(MyTestCase('test_addition'))
suite.addTest(MyTestCase('test_subtraction'))

# Create a test runner and run the test suite
runner = unittest.TextTestRunner()
runner.run(suite)