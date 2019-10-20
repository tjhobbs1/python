"""
Program: input_while.py
Author: Ty Hobbs
Last date modified: 09/24/2019

The purpose of this program is to use a while loop to take check a users data entered into the program and keep going
till the correct range of the number(1-100) is entered or if the Sentinel Value is entered.

"""

SENTINEL_VALUE = -99
list_of_numbers = []
user_input = int(input("Enter a number: or -99 to quit"))

while user_input != SENTINEL_VALUE:
    list_of_numbers.append(user_input)
    while not user_input in range(1, 101):
        print("Bad Input")
        print("inwhile")
        if user_input == -99:
            break
        else:
            list_of_numbers.pop()
            break
    user_input = int(input("Enter a number or -99 to stop"))

print(list_of_numbers)

"""
Test 1:  1,2,3,999,4,-99 : [1,2,3,4]
Test 2: 0,4,5,6,456,3,-99 : [4, 5, 6, 3]
Test 3: 6, 3435, 3, 324234,7, -99 :  [6, 3, 4, 7]
Test 4: -7, 8 ,-4, 8, 9, -8, -99 :  [8, 8, 9]

"""
