"""
Program:  test_basic_list.py
Author:  Ty Hobbs
Last Day Modified:  10/08/2019

The purpose of the program is to test the functions of the basic_list.py program.

"""

import unittest
from unittest.mock import patch
import fun_with_lists.basic_list as topic1


class TestList(unittest.TestCase):
    @patch('fun_with_lists.basic_list.get_input', return_value='5')
    def test_make_list(self, input):
        self.assertEqual(topic1.make_list(), ['5','5','5'])
    @patch('fun_with_lists.basic_list.get_input', return_value='4')
    def test_make_list(self, input):
        self.assertEqual(topic1.make_list(), ['4','4','4'])
    @patch('fun_with_lists.basic_list.get_input', return_value='7')
    def test_make_list(self, input):
        self.assertEqual(topic1.make_list(), ['7','7','7'])


if __name__ == '__main__':
    unittest.main()
