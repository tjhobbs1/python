"""
Program:  sort_and_search_array.py
Author:  Ty Hobbs
Last Day Modified:  10/08/2019

The purpose of the program is demo arrays in python.
"""
from array import array


def search_array(passed_list, search_value):
    # Takes in an array list and a value and searches the array and returns the index else it returns - 1
    # Param:  passed_list takes in an array
    # Param :  search_value  takes in the value to be searched.
    # Return:  Returns the index of the value or -1 if it can not find it.
    try:
        return passed_list.index(search_value)
    except ValueError:
        return -1


def sort_array(passed_list):
    # This will sort an given array.
    # Param:  passed_list is a passed array list to be sorted.
    #  Returns a sorted array.

    passed_list = passed_list.tolist()
    passed_list.sort()
    return passed_list


if __name__ == '__main__':

    array_entry = array('i',[77,66,23,6,7,4,6,10])

    print(search_array(array_entry,66))

    print(sort_array(array_entry))
