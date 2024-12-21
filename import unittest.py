import unittest
from class1 import func1, func2, func3
from io import StringIO
import sys

class TestClass1Functions(unittest.TestCase):

    def setUp(self):
        # Redirect stdout to capture print statements
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        # Reset redirect.
        sys.stdout = sys.__stdout__

    def test_func1(self):
        func1(51)
        self.assertEqual(self.held_output.getvalue().strip(), "a")
        self.held_output.truncate(0)
        self.held_output.seek(0)
        
        func1(50)
        self.assertEqual(self.held_output.getvalue().strip(), "Hello, World!")
        self.held_output.truncate(0)
        self.held_output.seek(0)

    def test_func2(self):
        func2(71)
        self.assertEqual(self.held_output.getvalue().strip(), "b")
        self.held_output.truncate(0)
        self.held_output.seek(0)
        
        func2(70)
        self.assertEqual(self.held_output.getvalue().strip(), "c")
        self.held_output.truncate(0)
        self.held_output.seek(0)

    def test_func3(self):
        func3(11)
        self.assertEqual(self.held_output.getvalue().strip(), "groesser 10")
        self.held_output.truncate(0)
        self.held_output.seek(0)
        
        func3(10)
        self.assertEqual(self.held_output.getvalue().strip(), "")

if __name__ == '__main__':
    unittest.main()