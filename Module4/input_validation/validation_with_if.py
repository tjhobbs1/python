"""
Program: validation_with_if.py
Author: Ty Hobbs
Last date modified: 09/18/2019



The purpose of this program is to take a last name, first name and three test scores and return the average of those three scores.
It then displays the results to the user.  If the user puts in a negative test score it will return a -1.
"""


def average():

    score1 = int(input("Enter the first score: "))
    score2 = int(input("Enter the second score: "))
    score3 = int(input("Enter the third score: "))

    if score1 < 0:
        return -1
    elif score2 < 0:
        return -1
    elif score3 < 0:
        return -1
    else:
        average_score = (score1 + score2 + score3)/3

        return round(average_score, 2)


if __name__ == '__main__':

    last_name = input("Enter a last name: ")
    first_name = input("Enter a first name: ")
    scores = average()

    print(last_name, ',', first_name, "- average grade:", scores)
