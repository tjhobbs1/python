"""
Program: test_function.py
Author: Ty Hobbs
Last date modified: 09/01/2019



The purpose of this program is to test the function camper_age_input.
"""

import unittest
from main import camper_age_input

class FunctionTestCase(unittest.TestCase):
    def test_increase(self):
        self.assertEqual(2, camper_age_input.convert_to_months(24))


if __name__ == '__main__':
    unittest.main()
