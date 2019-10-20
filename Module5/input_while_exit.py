"""
Program: input_while.py
Author: Ty Hobbs
Last date modified: 09/24/2019

The purpose of this program is to use a while loop to take check a users data entered into the program and keep going
till the correct range of the number(1-100) is entered or if the Sentinel Value is entered. 

"""

SENTINEL_VALUE = "-99"
SENTINEL_VALUE_QUIT= "Quit"
list_of_numbers = []
user_input = input("Enter a number: or -99 to stop or type quit to end the program")

while user_input != SENTINEL_VALUE or user_input != SENTINEL_VALUE_QUIT:
    int(user_input)
    list_of_numbers.append(user_input)
    while not user_input in range(1, 101):
        print("Bad Input")
        if user_input == -99:
            break
        else:
            list_of_numbers.pop()
            break
    user_input = int(input("Enter a number or -99 to stop"))

print(list_of_numbers)
