"""
Program:  customer_exception.py
Author:  Ty Hobbs
Last Day Modified:  11/12/2019

The purpose of the program is to build a reusable Customer class.  It will display how you can utilize custom exceptions in python.
"""
import re

class InvalidCustomerException(Exception):
    """
    This custom exception will throw an exception if the customer_id is not between 999 and 100000.
    """
    def __init__(self,message=None):
        if message==None:
            message = "You must enter a numeric value and a value greater 999 and less than 10000"
        super(InvalidCustomerException, self).__init__(message)

class InvalidNameException(Exception):
    """This custom exception will throw an exception error if the first or last name is not an alpha character."""
    def __init__(self,message=None):
        if message ==None:
            message = "You can only enter alpha characters"
        super(InvalidNameException,self).__init__(message)

class  InvalidPhoneNumberFormat(Exception):
    """This custom exception will throw an exception error if the number does not meet the 123-123-1234 format."""
    def __init__(self,message=None):
        if message ==None:
            print("you are here")
            message = "You must enter the phone number in a 123-123-1234 format "
        super(InvalidPhoneNumberFormat,self).__init__(message)



class Customer():
    """
    This class creates an object of a Customer.
    """
    def __init__(self,customer_id,last_name,first_name,phone_number):
        """
        Customer constructor
        :param customer_id: (int) the unique customer id.
        :param last_name: (string) the last name of the customer.
        :param first_name:  (string) the first name of the customer.
        :param phone_number: (string) the phone number of the customer.
        """
        customer_id = int(customer_id)
        if (customer_id < 1000) or (customer_id > 9999):
            raise InvalidCustomerException
        elif last_name.isalpha() ==False or first_name.isalpha()==False:
            raise InvalidNameException
        elif first_name.isalpha() ==False or first_name.isalpha()==False:
            raise InvalidNameException
        elif len(phone_number) <= 10 or not re.match("^[0-9]{3}-[0-9]{3}-[0-9]{4}$",phone_number):
            raise(InvalidPhoneNumberFormat)
        else:
            self.customer_id = customer_id
            self.last_name = last_name
            self.first_name = first_name
            self.phone_number = phone_number

    def change_customer_id(self, customer_id):
        """
        A setter for changing the customer_id
        :param customer_id: (int) a new customer id.
        :return: a new customer_id
        """
        if (customer_id < 1000) or (customer_id > 9999):
             raise InvalidCustomerException
        else:
            self.customer_id = customer_id

    def change_last_name(self, last_name):
        """
        Setter for changing the last name
        :param last_name: (string) new last name
        :return:  Changed last name.
        """
        if last_name.isalpha() ==False:
            raise InvalidNameException
        else:
            self.last_name = last_name

    def change_first_name(self, first_name):
        """
        Setter for changing the first_name
        :param first_name: (String)
        :return: A new first name
        """
        if first_name.isalpha()==False:
            raise InvalidNameException
        else:
            self.first_name = first_name

    def change_phone_number(self,phone_number):
        """
        A setter for changing the phone number
        :param phone_number: (String) a new phone number
        :return: a new phone number.
        """
        if len(phone_number) <= 10 or not re.match("^[0-9]{3}-[0-9]{3}-[0-9]{4}$",phone_number):
            raise(InvalidPhoneNumberFormat)
        else:
            self.phone_number = phone_number


    def __repr__(self):
        """
        Repr Method for the Customer Class
        :return: String of the Customer Class
        """
        return "Customer ID: {} \nCustomer Name: {},{}\nCustomer Phone: {}".format(self.customer_id,self.last_name,self.first_name,self.phone_number)

    def __str__(self):
        """
        The str method for the Customer Class.
        :param self:
        :return: A string object of the Customer.
        """
        return "Customer ID: {} \nCustomer Name: {},{}\nCustomer Phone: {}".format(self.customer_id,self.last_name,self.first_name,self.phone_number)

    def display(self):
        """
        A method to display the Customer Object.
        :param self:
        :return: A string object of the customer class.
        """
        return "Customer ID: {} \nCustomer Name: {},{}\nCustomer Phone: {}".format(self.customer_id,self.last_name,self.first_name,self.phone_number)





customer1 = Customer(4569,"Ty","Hobbs","319-330-6543")
print(customer1.display())
print(customer1)
# customer2 = Customer(4578,"Hobbs","Ty","3193309818")  # Throws an InvalidPhoneNumberFormat
# customer3 = Customer(12,"Ty","Hobbs","319-330-6543")   # Throws an InvalidCustomerException
# customer4 = Customer(1223,"1","Hobbs","319-330-6543")  # Throws an InvalidNameException on first_name
# customer5 = Customer(1223,"Ty","4","319-330-6543") # Throws an InvalidNameException on last_name




