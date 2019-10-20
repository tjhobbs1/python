"""
Program: test_string_function.py
Author: Ty Hobbs
Last date modified: 09/30/2019



The purpose of this program is to test the multiply_string function from the string_function program.
"""

import unittest
from more_functions.string_functions import multiply_string


class MyTestCase(unittest.TestCase):
    def test_string_multiplyer(self):
        self.assertEqual(multiply_string("python",1), "python")
        self.assertEqual(multiply_string("python",3), "pythonpythonpython")
        self.assertEqual(multiply_string("python",6), "pythonpythonpythonpythonpythonpython")

if __name__ == '__main__':
    unittest.main()
