"""
Program:  test_sort_and_search.py
Author:  Ty Hobbs
Last Day Modified:  10/08/2019

The purpose of the program is to test the functions in sort_and_search_list.py program.

"""

import unittest
import fun_with_lists.sort_and_search_list as sort_search

class TestList(unittest.TestCase):
    def setUp(self):
        self.initial_list = [10,7,8]
        self.expected = [7,8,10]
    def tearDown(self):
        self.initial_list = []
        self.expected = []
    def test_make_list(self):
        self.assertEqual(sort_search.sort_list(self.initial_list), self.expected)
    def test_make_list(self):
        self.assertEqual(sort_search.search_list(self.initial_list,10), 0)
    def test_make_list(self):
        self.assertEqual(sort_search.search_list(self.initial_list,57), -1)
    def test_make_list(self):
        self.assertEqual(sort_search.search_list(self.initial_list,8), 2)


if __name__ == '__main__':
    unittest.main()
