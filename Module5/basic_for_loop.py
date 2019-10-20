"""
Program: basic_for_loop.py
Author: Ty Hobbs
Last date modified: 09/24/2019


The purpose of this program is to demonstrate the use of for loops.
"""

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

print("First Section")

for n in numbers:
    print(n)

print("Second Section")

for x in reversed(range(33, 100, 3)):
    print(x)
