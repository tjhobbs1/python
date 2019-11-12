"""
Program:  test_customer_exceptions.py
Author:  Ty Hobbs
Last Day Modified:  11/12/2019

The purpose of the program is used to test the Customer Class exceptions.
"""
import unittest
from custom_exceptions.customer_exceptions import Customer as cust
from custom_exceptions.customer_exceptions import InvalidCustomerException, InvalidNameException, \
    InvalidPhoneNumberFormat


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.customer1 = cust(1234,"Hobbs","Ty","319-330-1234")

    def tearDown(self):
        del self.customer1

    def test_initial_value_required_attributes(self):
        """
        Test that the customer1 object has the correct attributes set
        :return: Pass or fail test
        """
        self.assertEqual(self.customer1.customer_id,1234)
        self.assertEqual(self.customer1.last_name, 'Hobbs')
        self.assertEqual(self.customer1.first_name, 'Ty')
        self.assertEqual(self.customer1.phone_number,'319-330-1234')

    def test_inital_all_attributes(self):
        """
        Test that all initial values are set
        :return: Pass of fail of the test
        """
        customer = cust(6789,"Smith","Jane","515-555-5555")
        assert customer.customer_id == 6789
        assert customer.last_name == 'Smith'
        assert customer.first_name == 'Jane'
        assert customer.phone_number == '515-555-5555'

    def InvalidCustomerException(self):
        """
        Test that the InvalidCustomerException is thrown when a customer_id does not meet the criteria.
        :return: Pass or fail test.
        """
        with self.assertRaises(InvalidCustomerException):
            customer3 = cust(123, 'Hobbs','Ty','515-456-7890')
            customer4 = cust(123456, 'Hobbs','Ty','515-456-7890')

    def InvalidNameException(self):
        """
        Test that the InvalidNameException is thrown when a first and last name does not meet the criteria.
        :return: Pass or fail test.
        """
        with self.assertRaises(InvalidNameException):
            customer5 = cust(1234, '123','Ty','515-456-7890')
            customer6 = cust(1234, 'Hobbs','123','515-456-7890')

    def InvalidPhoneNumberFormat(self):
        """
        Test that the correct phone number format is inputted.
        :return: Pass or fail test.
        """
        with self.assertRaises(InvalidPhoneNumberFormat):
            customer7 = cust(123, 'Hobbs','Ty','5-456-7890')
            customer8 = cust(123, 'Hobbs','Ty','515-45a-7890')
            customer9 = cust(123, 'Hobbs','Ty','515-456-7')
            customer10 = cust(123, 'Hobbs','Ty','515-987-7654')


if __name__ == '__main__':
    unittest.main()

