"""
Program:  search_sort_list.py
Author:  Ty Hobbs
Last Day Modified:  10/08/2019

The purpose of the program is to create a list of numbers and return it to the user. It will be used for testing
Basic List Exceptions
"""

def make_list():
    # This function will run a for loop calling the get_input function to get three numbers
    # Params: none
    # Returns a list of numbers for display to the user.  Throws a ValueError if non-numeric number is caught.

    list_of_numbers =[]  # Empty list to store numbers in.
    for i in range(3):
        returned_number = get_input()
        try:
            returned_number = int(returned_number)  # Trys and set the value to an int
            list_of_numbers.append(returned_number)  # If no error is caught it will append it to the list.
        except ValueError:
            raise ValueError        # Raises a ValueError if the variable can't be changed to an int.
    return list_of_numbers


def get_input():
    #  This function gets the user's inputs and returns it back to the make_list() function.
    # Params:  None
    # Returns a value back to the make_list() function in the form of a string.

    user_input = input("Enter a number: ")
    print(user_input)

    return user_input


if __name__ == '__main__':
    print(make_list())

