"""
Program: test_inner_functions.py
Author: Ty Hobbs
Last date modified: 09/30/2019



The purpose of this program is to test the measurement function of inner_function_assignment
"""

import unittest
from more_functions.inner_function_assignment import measurement


class MyTestCase(unittest.TestCase):
    def test_measurement(self):
        self.assertEqual(measurement([2.1,3.4]), "Perimeter is: 11.0 Area is: 7.14")
        self.assertEqual(measurement([3.5]), "Perimeter is: 14.0 Area is: 12.25")


if __name__ == '__main__':
    unittest.main()
