"""
Program:  multiple_inheritance.py
Author:  Ty Hobbs
Last Day Modified:  11/05/2019

The purpose of the program is to demonstrate the use of multiple inheritance in Python. """
import datetime


class Employee():
    """
    This is a class for making an Employee object.  It is the parent to SalariedEmployee and HourlyEmployee

    Attributes:
        start_date (datetime): The start date of the employee
        salary (float):  The salary of the employee

    """

    def __init__(self, start_date, salary):
        """
        The constructor for Employee class.

        Parameters:
        start_date (datetime): The start date of the employee
        salary (float):  The salary of the employee

        """
        self.start_date = start_date
        self.salary = salary

    def __str__(self):
        return f'{self.last_name} {self.start_date} {self.salary}'

    def __repr__(self):
         return f'{self.last_name} {self.start_date} {self.salary}'

    # Setters
    def change_last_name(self, lname):
        self.last_name = lname

    def change_start_date(self, new_date):
        self.start_date = new_date

    def give_raise(self, new_pay_rate):
        self.salary = new_pay_rate

    """Returns a string of the Employee Class"""

    def display(self):
        """Returns a string of the object created by the Employee Class """
        return f'{self.last_name}, {self.first_name} \n{self.emp_address} \n{self.emp_phone}'


class Person:
    """
       The constructor for Person class.

       Parameters:
       lname (String):  The last name of the person
       fname (String):  The first name of the person
       address (String):  The address of the person
       phone (String):  The phone number of the person.

       """

    def __init__(self, lname, fname, address, phone):
        """
        The constructor for Person class.

        Parameters:
           lname (string): The last name of the employee.
            fname (string): The first name of the employee
            address (string):  The address of the employee
            phone (string):  The phone number of the employee
        """
        # Checks for char in name.
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self.address = address
        self.last_name = lname
        self.first_name = fname
        self.phone = phone

    def __repr__(self):
        return f'{self.first_name} {self.last_name} {self.address} {self.phone}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}\n' \
               f'{self.address}\n' \
               f'{self.phone}'

    # Setters for Person Class
    def change_last_name(self, name):
        self.last_name = name

    def change_first_name(self, name):
        self.first_name = name

    def change_address(self, address):
        self.address = address

    def change_phone(self, phone):
        self.phone = phone

    """Returns a string object of the Person Class """

    def display(self):
        return self.last_name + ", " + self.first_name + ":" + self.address + ":" + self.phone


class Manager(Employee, Person):
    """
   This is a class for making an Manager object.  It inherits from both the Employee and the Person Class.

   Attributes:
       department (string): The managers department
       direct_reports (list):  A list of direct report employees

   """

    def __init__(self, lname, fname, start_date, salary, department, direct_reports=[], address="", phone=""):
        """
        The constructor for Manager class.

        Parameters:
        start_date (datetime):  The start date of the employee
        salary (float):  The salary of the employee.
        """
        Employee.__init__(self, start_date, salary)
        Person.__init__(self, lname, fname, address, phone)
        self.department = department
        self.direct_reports = direct_reports

    # Setters for the manager class
    def add_direct_reports(self, membmer):
        self.direct_reports.append(membmer)

    def give_raise(self, new_pay_rate):
        self.salary = new_pay_rate

    def display(self):
        """Returns a display of the Manager"""
        return f'Name: {self.first_name} {self.last_name}\n' \
               f'Department: {self.department}\n' \
               f'Salary: {self.salary}\n' \
               f'Start Date: {self.start_date}\n' \
               f'List of Direct Reports: {self.direct_reports}'


current_date = datetime.datetime.today().strftime('%m-%d-%Y')

print('No Direct Reports added')
manager1 = Manager('Hobbs', 'Ty', current_date, 250000, "IT")
print(manager1.display())
print('Direct Reports added\n')
manager1.add_direct_reports('Joe')
manager1.add_direct_reports('Kara')
manager1.add_direct_reports('Sue')
print(manager1.display())
print('Raise added\n')
manager1.give_raise(300000)
print(manager1.display())
