"""
Program: test.py
Author: Ty Hobbs
Last date modified: 09/10/2019



The purpose of this program is to test the average() inputting three values and seeing if the returned value is what you would expect.
"""


from format_output import average_scores
import unittest
from unittest import mock


class MyTestCase(unittest.TestCase):

    def test_average(self):
        with mock.patch('builtins.input', side_effect=[70,75,80]):
            assert average_scores.average() == 75


if __name__ == '__main__':
    unittest.main()

"""
    The test with 70,75,80 will return a passed test because the average of these three scores is 75.
    When testing with 60,75,80 you get an AssertionError because the average of those three scores is not 75.  It should be 71.66.
"""
