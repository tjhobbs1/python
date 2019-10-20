"""
Program:  sort_and_search.py
Author:  Ty Hobbs
Last Day Modified:  10/08/2019

The purpose of the program is to create a list of numbers and return it to the user.

"""


def search_list(passed_list, search_value):
    # This function takes in a list and number to search for.
    # Param: passed_list is the list that is passed from the main.
    # Param: search_value is the number that is passed in to search for
    # Return:  Returns the position of the searched number or a -1 if it cant be found.
    try:
       return passed_list.index(search_value)
    except ValueError:
        # Returns -1 if the value can't be found.
        return -1


def sort_list(passed_list):
    # This function takes in a list and sorts it.
    # Param:  passed_list is the list that is passed in to be sorted.
    # Return:  returns the sorted list.

    passed_list.sort()
    return passed_list


def get_input():
    # This function gets and checks user input to be returned for use by other functions. It loops through till -1 is entered by the user.
    # No Params
    # Returns a list of numbers.

    list_of_numbers = []
    user_input = 0

    while user_input != -1:
        try:
            # test that the user input is an number else throw a ValueError
            user_input = int(input("Enter a number or -1 to stop: "))
            list_of_numbers.append(user_input)
        except ValueError:
            # Show an error if the value is not a number and then ask for a new number.
            print("Error")
            user_input = int(input("Enter a number or -1 to stop: "))
        except:
            print("Something worse happened!")
            raise #a worse error occurred, now we kill it

    list_of_numbers.pop()
    return list_of_numbers

""" 
I used the return to pass the sorted list because then it allows the user to do something else with the list if needed
versus just printing it out. 

"""

if __name__ == '__main__':
    list_of_numbers = [9,2,15,7,188,55]

    print(search_list(list_of_numbers,15))
    print(search_list(list_of_numbers,8))
    print(sort_list(list_of_numbers))

    list_of_numbers = get_input()
    print(search_list(list_of_numbers,5))
    print(sort_list(list_of_numbers))





