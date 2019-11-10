"""
Program:  test_packages.py
Author:  Ty Hobbs
Last Day Modified:  10/20/2019

The purpose of the program is to test the importing of packages.
"""

import definitions.dictionary_ops as dictionary , greeting as greeting,\
    set_ops as set_ops

#  Calls the greeting function
greeting.greeting()

#  Calls the author function
greeting.author()

# Creates a dictionary of Student IDs and Names to be passed
studentId ={
    101:"Ty",
    102:"Susan",
    103: "Jim",
    104: "Steve",
    105: "Kristi",
    106: "Miles"
}

# Calls the print_student_dict with passed studentsId dict.
dictionary.print_student_dict(studentId)


# Creates a set of foods to be passed into the function
foods = ("Banana","Apple","Pie","Cookie","Ham")

# Caled the print_food_set function with passed food set
set_ops.print_food_set(foods)


