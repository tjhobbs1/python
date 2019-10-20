"""
Program:  my_definitions.py
Author:  Ty Hobbs
Last Day Modified:  10/20/2019

The purpose of the program is to create reusable functions that can be used in other programs.

"""


def greeting():
    """
    Displays a greeting
    :return: printed greeting
    """
    print("Hello, how are you?")


def author():
    """
    Prints the name of the author.
    :return: Prints the name of the author.
    """
    print("The Author is Ty Hobbs")


def print_student_dict(students):
    """
    Take a dictionary of students and then prints them out
    :param students: dictionary of student ID and student names
    :return: a print out of the student names and id
    """
    for k,v in students.items():
        print(k,':',v,)


def print_food_set(foods):
    """
    Takes a set of foods and prints them out.
    :param foods: A set of a foods
    :return:  Prints out the sets of foods, each on its own line.,
    """
    for elem in foods:
        print (elem)
