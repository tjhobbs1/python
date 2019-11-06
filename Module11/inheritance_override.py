"""
Program:  inheritance_override.py
Author:  Ty Hobbs
Last Day Modified:  11/05/2019

The purpose of the program is to demo inheritance_override"""
import datetime
class Employee():
    """
    This is a class for making an Employee object.  It is the parent to SalariedEmployee and HourlyEmployee

    Attributes:
        lname (string): The last name of the employee.
        fname (string): The first name of the employee
        address (string):  The address of the employee
        phone (string):  The phone number of the employee
    """

    def __init__(self, lname, fname, address, phone):
        """
        The constructor for Employee class.

        Parameters:
           lname (string): The last name of the employee.
        fname (string): The first name of the employee
        address (string):  The address of the employee
        phone (string):  The phone number of the employee
        """
        self.last_name = lname
        self.first_name = fname
        self.emp_address = address
        self.emp_phone = phone

# Setters
    def change_last_name(self, lname):
        self.last_name = lname

    def change_first_name(self, fname):
        self.first_name = fname

    def change_address(self, address):
        self.emp_address = address

    def change_phone_number(self,phone):
        self.emp_phone = phone

    def display(self):
       """Returns a string of the object created by the Employee Class """
       return f'{self.last_name}, {self.first_name} \n{self.emp_address} \n{self.emp_phone}'


class SalariedEmployee(Employee):
     """
    This is a class for making an SalariedEmployee object. It inherits from the Employee Class

    Attributes:
        lname (string): The last name of the employee.
        fname (string): The first name of the employee
        address (string):  The address of the employee
        phone (string):  The phone number of the employee
        start_date(date object): The employee start date
        salary(float): The employees yearly salary
    """
     def __init__(self,lname, fname, address, phone,start_date,salary):
         """
        The constructor for SalariedEmployee class.

        Parameters:
        lname (string): The last name of the employee.
        fname (string): The first name of the employee
        address (string):  The address of the employee
        phone (string):  The phone number of the employee
        start_date(date object): The employee start date
        salary(float): The employees yearly salary

        """
         super().__init__(lname,fname,address,phone) # Call init on parent class
         self.start_date = start_date
         self.salary = salary

     def give_raise(self,new_pay_rate):
         """The function to set a pay raise.

            Parameters:
                new_pay_rate (float): The new rate of pay

            Returns:
                float: The new rate of pay """

         self.salary = new_pay_rate

     def display(self):
         """Return a string of the SalariedEmployee Object"""
         return str(self.last_name) + ", " + str(self.first_name) + "\n" + str(self.emp_address)\
               + "\nPhone: " + str(self.emp_phone) + "\n$" + str(self.salary) + "/year\nEmployee Start Date: " + str(self.start_date)

class HourlyEmployee(Employee):
    """
    This is a class for making an SalariedEmployee object. It inherits from the Employee Class

    Attributes:
        lname (string): The last name of the employee.
        fname (string): The first name of the employee
        address (string):  The address of the employee
        phone (string):  The phone number of the employee
        start_date(date object): The employee start date
        hourly_pay_rate(float): The employees hourly pay rate
    """
    def __init__(self,lname, fname, address, phone,start_date,hourly_pay_rate):
         """
        The constructor for HourlyEmployee class.

        Parameters:
        lname (string): The last name of the employee.
        fname (string): The first name of the employee
        address (string):  The address of the employee
        phone (string):  The phone number of the employee
        start_date(date object): The employee start date
        hourly_pay_rate(float): The employees yearly salary

        """
         super().__init__(lname,fname,address,phone) # Call init on parent class
         self.start_date = start_date
         self.hourly_pay_rate = hourly_pay_rate

    def give_raise(self,new_pay_rate):
          """The function to set a pay raise.

            Parameters:
                new_pay_rate (float): The new rate of pay

            Returns:
                float: The new rate of pay """

          self.salary = new_pay_rate
          self.hourly_pay_rate = new_pay_rate

    def display(self):
         """Returns a string of the HourlyEmployee Object"""
         return str(self.last_name) + ", " + str(self.first_name) + "\n" + str(self.emp_address)\
               + "\nPhone: " + str(self.emp_phone) + "\n$" + str(self.hourly_pay_rate) + "/hour\nEmployee Start Date: " + str(self.start_date)


current_date = datetime.datetime.today().strftime('%m-%d-%Y')

emply1 = SalariedEmployee('Hobbs','Ty','1409 NW Pine View Cr','5155557890',current_date,40000)
print(emply1.display())
print('\n')
emply1.give_raise(45000)
print(emply1.display())
print('\n')
emply2 =HourlyEmployee('Smith','Joe','1409 NW Pine View Cr','5155557890',current_date,10.00)
print(emply2.display())
print('\n')
emply2.give_raise(12.00)
print(emply2.display())

