"""
Program: cast_to_integer.py
Author: Ty Hobbs
Last date modified: 08/30/2019



The purpose of this program is to accept any input,
convert to a integer type and output the integer.
"""

integer_input = int(input("Enter a integer: "))
float_input = float(input("Enter a float: "))
string_input = input("Enter a string: ")

print(integer_input)
print(int(float_input))
int(string_input)
print(string_input)

# The String input will throw an error when casting as an int.


