"""
Program:  employee.py
Author:  Ty Hobbs
Last Day Modified:  10/28/2019

The purpose of the program is to build a reusable Employee class.  It will display how to use the init method to build an Employee object and return the info to the user.
"""
import datetime
class Employee():

    def __init__(self, lname, fname, address, phone,is_salaried,start_date, salary):
         self.last_name = lname
         self.first_name = fname
         self.emp_address = address
         self.emp_phone = phone
         self.change_salaried = is_salaried
         self.emp_start_date = start_date
         self.emp_salary = '%.2f' % float(salary)


    def change_last_name(self, lname):
        self.last_name = lname

    def change_first_name(self, fname):
        self.first_name = fname

    def change_address(self, address):
        self.emp_address = address

    def change_phone_number(self,phone):
        self.emp_phone = phone

    def change_salaried(self,is_salaried):
        self.change_salaried = is_salaried

    def change_start_date(self,start_date):
        self.emp_start_date = start_date

    def change_salary(self,salary):
        self.emp_salary = salary



    def display(self):
        if self.change_salaried == True:
             return str(self.last_name) + ", " + str(self.first_name) + "\n" + str(self.emp_address)\
               + "\nPhone: " + str(self.emp_phone) + "\nSalaried Employee: " \
               + "$" + str(self.emp_salary) + "/year\nEmployee Start Date: " + str(self.emp_start_date)
        else:
            return str(self.last_name) + ", " + str(self.first_name) + "\n" + str(self.emp_address)\
               + "\nPhone: " + str(self.emp_phone) + "\nHourly Employee: " \
               + "$" + str(self.emp_salary) + "/hour\nEmployee Start Date: " + str(self.emp_start_date)



# Driver
emp = Employee('Matt',"Ruiz","111 Main St, Des Moines, IA","5151234567",True,datetime.date(2002,5,5),300000.1256)   # call the construtor, needs to have a first and last name in parameter
emp1 = Employee('Jeff',"Smith","123 North St, Ankeny, IA","5151234567",False,datetime.date(1999,4,18),21.368)
# emp.change_first_name()
# emp.change_last_name()
# emp.change_address()
# emp.change_phone_number()
# emp.change_salaried()
# emp.change_start_date("Date")
# emp.change_salary()
print(emp.display())                # display returns a str, so print the information
print(emp1.display())
del emp                             # clean up!
