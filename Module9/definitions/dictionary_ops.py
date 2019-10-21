"""
Program:  dictionary_ops.py
Author:  Ty Hobbs
Last Day Modified:  10/20/2019

The purpose of the program is to create a reusable function that prints a dictionary of student
names and ids

"""

def print_student_dict(students):
    """
    Take a dictionary of students and then prints them out
    :param students: dictionary of student ID and student names
    :return: a print out of the student names and id
    """
    for k,v in students.items():
        print(k,':',v,)
