"""
Program: test_loop.py
Author: Ty Hobbs
Last date modified: 09/24/2019



The purpose of this program is to test the average function from the test score average program.
"""
import unittest
from input_loops.average_input_scores import average


class MyTest(unittest.TestCase):

    def test_average(self):
        self.assertEqual(75, average([100,50]))
        self.assertEqual(78.6, average([90,60,76,79,88]))
        self.assertEqual(71.83, average([100,56,89,99,67,20]))
        self.assertEqual(79.33, average([88,77,56,99,89,67]))
        self.assertEqual(50, average([50]))


if __name__ == '__main__':
    unittest.main()


