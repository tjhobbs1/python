"""
Program:  basic_list.py
Author:  Ty Hobbs
Last Day Modified:  10/08/2019

The purpose of the program is to create a list of numbers and return it to the user.

"""

def make_list():
    # This function calls another function called get_input() that gets user input for three numbers.
    # No Params
    # Returns a list of numbers
    list_of_numbers =[]  # stores a list of number to return back where the function was called.
    for i in range(3):
        returned_number = get_input()
        list_of_numbers.append(returned_number)

    return list_of_numbers


def get_input():
    # This function gets and checks user input for the make_list() function.
    # No Params
    # Returns user_input which should be a integer.
    user_input1 = True
    while True:
        try:
            # test that the user input is an number else throw a ValueError
            user_input = int(input("Enter a number: "))
            user_input1 = False
            user_input=str(user_input)
            return user_input
        except ValueError:
            # Show an error if the value is not a number and then ask for a new number.
            print("Error")
            user_input1 = True
            # Get new user input
            #user_input = int(input("Enter a number: "))
        except:
            print("Something worse happened!")
            raise #a worse error occurred, stops the program
    # Recast the input as a string
    user_input=str(user_input)

    return user_input


if __name__ == '__main__':
    print(make_list())

