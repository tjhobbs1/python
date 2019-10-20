"""
Program: payroll_calc.py
Author: Ty Hobbs
Last date modified: 09/30/2019



The purpose of this program is to take an employees name, the number of hours they work and their rate of pay.
It will then return the total amount of pay that employee will receive.
"""

def hourly_employee_input():
    # This function will get the users inputs of number of hours worked and hourly pay rate and print the paycheck amount.
    # :param
    # :returns: prints to the screen.
    # :raises ValueError: when input is not an int
    employee_name = ""
    hourly_rate = 0
    hours_worked = 0
# Get the employee's name.
    while employee_name == "":
        employee_name = input("Enter an Employee's Name: ")
        # Gets the user input of the rate of pay for the employee.
        while hourly_rate <= 0:
            try:
                hourly_rate = float(input("Enter employee's rate of pay"))
            except ValueError as err:  # Returns an error.
                print("Enter a positive numeric value")
                hourly_rate = float(input("Enter employee's rate of pay"))
    # Get the user input of the number of hours worked.
    while hours_worked <= 0:
        try:
            hours_worked = int(input("Enter the number of hours the employee worked: "))
        except ValueError as err:   # Returns an error.
            print("Enter a positive numeric value")
            hours_worked = int(input("Enter the number of hours the employee worked: "))
    total_pay = hourly_rate * hours_worked
    print(employee_name, "total pay is $",total_pay)


if __name__ == '__main__':
    try:  # check for ValueError
        hourly_employee_input()
    except ValueError as err:
        print("Enter a positive numeric value")
        hourly_employee_input()


