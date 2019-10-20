"""
Program:  basic_list.py
Author:  Ty Hobbs
Last Day Modified:  10/08/2019

The purpose of the program is test the functions in search_sort_list.py

"""

import unittest
from unittest.mock import patch
import fun_with_lists.search_sort_list as topic1


class TestList(unittest.TestCase):
    @patch('fun_with_lists.search_sort_list.get_input', return_value='ab')  # patch function for input
    def test_make_list_non_numeric(self, input):                        # pass input
        with self.assertRaises(ValueError):                             # this is familiar
            topic1.make_list()                                          # call the function!

    @patch('fun_with_lists.search_sort_list.get_input', return_value='#$')  # patch function for input
    def test_make_list_non_numeric(self, input):                        # pass input
        with self.assertRaises(ValueError):                             # this is familiar
            topic1.make_list()                                          # call the function!

    @patch('fun_with_lists.search_sort_list.get_input', return_value='1ww')  # patch function for input
    def test_make_list_non_numeric(self, input):                        # pass input
        with self.assertRaises(ValueError):                             # this is familiar
            topic1.make_list()                                          # call the function!


if __name__ == '__main__':
    unittest.main()
