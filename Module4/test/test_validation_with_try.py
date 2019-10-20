"""
Program: test_validation_with_try.py
Author: Ty Hobbs
Last date modified: 09/18/2019



The purpose of this program is to test the average() inputting three values and seeing if the returned value is what you would expect.
"""


from input_validation import validation_with_try
import unittest
from unittest import mock


class MyTestCase(unittest.TestCase):


    def test_average_exception(self):
        with self.assertRaises(ValueError):
            validation_with_try.average_score(1,1,-1)




if __name__ == '__main__':
    unittest.main()

"""
    The test with 70,75,80 will return a passed test because the average of these three scores is 75.
    When testing with 60,75,80 you get an AssertionError because the average of those three scores is not 75.  It should be 71.66.
"""


