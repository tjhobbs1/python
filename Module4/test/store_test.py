"""
Program: store_test.py
Author: Ty Hobbs
Last date modified: 09/17/2019



The purpose of this program is to test the test_price_under() method in the store front program.
"""

from store import store_front
import unittest

from store.store_front import calculate_order


class MyTestCase(unittest.TestCase):

     def test_price_under_10(self):
          self.assertEqual(calculate_order(8,0,0),14.43)
          self.assertEqual(calculate_order(8,0,.1),13.58)
          self.assertEqual(calculate_order(8,0,.15),13.16)
          self.assertEqual(calculate_order(8,0,.2),12.73)
          self.assertEqual(calculate_order(8,5,0),9.13)
          self.assertEqual(calculate_order(8,5,.1),8.81)
          self.assertEqual(calculate_order(8,5,.15),8.65)
          self.assertEqual(calculate_order(8,5,.2),8.49)
          self.assertEqual(calculate_order(8,10,0),3.83)
          self.assertEqual(calculate_order(8,10,.1),4.04)
          self.assertEqual(calculate_order(8,10,.15),4.15)
          self.assertEqual(calculate_order(8,10,.2),4.25)
          self.assertEqual(calculate_order(25,0,0),34.45)
          self.assertEqual(calculate_order(25,0,.1),31.80)
          self.assertEqual(calculate_order(25,0,.20),29.15)
          self.assertEqual(calculate_order(25,5,0),29.15)
          self.assertEqual(calculate_order(25,5,.10),27.03)
          self.assertEqual(calculate_order(25,5,.15),25.97)
          self.assertEqual(calculate_order(25,5,.20),24.91)
          self.assertEqual(calculate_order(45,0,0),59.65)
          self.assertEqual(calculate_order(45,0,.1),54.88)
          self.assertEqual(calculate_order(45,0,.2),50.11)
          self.assertEqual(calculate_order(75,0,0),79.50)
          self.assertEqual(calculate_order(75,5,.1),66.78)
          self.assertEqual(calculate_order(75,10,0),68.90)
          self.assertEqual(calculate_order(75,10,.2),55.12)



if __name__ == '__main__':
    unittest.main()
