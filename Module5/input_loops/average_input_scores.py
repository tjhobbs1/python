"""
Program: average_input_scores.py
Author: Ty Hobbs
Last date modified: 09/24/2019



The purpose of this program is to take a last name, first name and as many test scores as the user wants to input and then
return the average of those scores.
It then displays the results to the user.
The loop is terminated by entering the sentinel value of -1.
"""


def average(list_of_student_scores):
    sum_of_test_scores = 0
    total_number_of_scores = float(len(list_of_student_scores))

    for x in list_of_student_scores:
        sum_of_test_scores = sum_of_test_scores + x

    final_test_score_average = round(sum_of_test_scores / total_number_of_scores, 2)
    return final_test_score_average


if __name__ == '__main__':
    student_last_name = input("Enter Students Last Name: ")
    student_first_name = input("Enter Students First Name: ")

    score_list = []
    student_score = 0

    while student_score != -1:
        try:
            student_score = float(input("Enter Student Score or -1 to end: "))
            if (student_score >= -1) and (student_score <= 100):
                score_list.append(student_score)
            else:
                raise ValueError
        except ValueError:
            print("Please enter a positive number.")

    score_list.pop()

    avg_score = average(score_list)
    print(student_last_name, ",", student_first_name, "grade:", avg_score)
