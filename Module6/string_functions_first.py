"""
Program: string_function_first.py
Author: Ty Hobbs
Last date modified: 09/30/2019



The purpose of this program is to take a sting and int in as parameters into the function and return the string
the number of times that the int is set for.
"""

def multiply_string(entered_string, num_of_returns):
    # Takes a string input and multiplies it by the number of times that are passed in. It then prints it to the screen.
    # :param entered_string: The string that is passed in.
    # :param num_of_returns: The int that will be the number of times the string is multiplied by.
    # :returns the string the number of time that were passed.

    return entered_string * num_of_returns

if __name__ == '__main__':
    print(multiply_string("hi", 5))

