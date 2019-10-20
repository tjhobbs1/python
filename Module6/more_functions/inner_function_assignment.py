"""
Program: inner_function_assignment.py
Author: Ty Hobbs
Last date modified: 09/30/2019



The purpose of this program is to take a one or two ore measurements and returns a perimeter and area.
"""
def measurement(measurement_list):
    # Takes a measurement list and sends it to a inner area function and perimeter function.
    # :param measurement_list takes a list of two measurements.
    # :calls to functions: final_area and final_perimeter
    final_area = area(measurement_list)
    final_perimeter = perimeter(measurement_list)

    return "Perimeter is: {final_perimeter} Area is: {final_area}" .format(final_perimeter = final_perimeter, final_area = final_area)

def area(a_list):
    # Takes a measurement list and calculates an area of the two measurments.
    # :param a_list takes a list of two measurements.
    # :returns the area of the measurements
    if len(a_list) < 2:
        length = a_list[0]
        width = a_list[0]
    else:
        length = a_list[0]
        width = a_list[1]
    area = length * width
    return area

def perimeter(a_list):
     # Takes a measurement list and calculates an perimeter of the two measurments.
    # :param a_list takes a list of two measurements.
    # :returns the perimeter of the measurements
    if len(a_list) < 2:
        length = a_list[0]
        width = a_list[0]
    else:
        length = a_list[0]
        width = a_list[1]
    perimeter = (2 * length) + (2 * width)
    return perimeter


if __name__ == '__main__':
    print(measurement([3,3]))
    print(measurement([3]))


