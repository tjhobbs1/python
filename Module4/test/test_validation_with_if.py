"""
Program: test_validation_with_if.py
Author: Ty Hobbs
Last date modified: 09/18/2019



The purpose of this program is to test the average() inputting three values and seeing if the returned value is what you would expect.
It also checks for when a negative number is passed in as a score.
"""


from input_validation import validation_with_if
import unittest
from unittest import mock


class MyTestCase(unittest.TestCase):

    # Test the average test score function.

    def test_average(self):
        with mock.patch('builtins.input', side_effect=[70, 75, 80]):
            assert validation_with_if.average() == 75
        with mock.patch('builtins.input', side_effect=[70, 80, 90]):
            assert validation_with_if.average() == 80
        with mock.patch('builtins.input', side_effect=[55, 67, 90]):
            assert validation_with_if.average() == 70.67
        with mock.patch('builtins.input', side_effect=[68, 100, 97]):
            assert validation_with_if.average() == 88.33
    # Test the results if a negative number is passed in as a test score.

    def test_neg_score(self):
        with mock.patch('builtins.input', side_effect=[-70, 75, 80]):
            assert validation_with_if.average() == -1
        with mock.patch('builtins.input', side_effect=[70, -75, 80]):
            assert validation_with_if.average() == -1
        with mock.patch('builtins.input', side_effect=[70, 75, -80]):
            assert validation_with_if.average() == -1
        with mock.patch('builtins.input', side_effect=[-70, -75, 80]):
            assert validation_with_if.average() == -1
        with mock.patch('builtins.input', side_effect=[-70, -75, -80]):
            assert validation_with_if.average() == -1
        with mock.patch('builtins.input', side_effect=[-70, 75, -80]):
            assert validation_with_if.average() == -1
        with mock.patch('builtins.input', side_effect=[70, -75, -80]):
            assert validation_with_if.average() == -1





if __name__ == '__main__':
    unittest.main()
"""
    The test with 70,75,80 will return a passed test because the average of these three scores is 75.
    When testing with 60,75,80 you get an AssertionError because the average of those three scores is not 75.  It should be 71.66.
"""
