"""
Program:  set_ops.py
Author:  Ty Hobbs
Last Day Modified:  10/20/2019

The purpose of the program is to create a reusable function that prints a set of foods.

"""

def print_food_set(foods):
    """
    Takes a set of foods and prints them out.
    :param foods: A set of a foods
    :return:  Prints out the sets of foods, each on its own line.,
    """
    for elem in foods:
        print (elem)
