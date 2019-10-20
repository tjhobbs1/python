"""
Program: validation_with_try.py
Author: Ty Hobbs
Last date modified: 09/16/2019



The purpose of this program is to take a last name, first name and three test scores and return the average of those three scores.
It then displays the results to the user.
"""


def average_score():

    score1 = int(input("Enter the first score: "))
    score2 = int(input("Enter the second score: "))
    score3 = int(input("Enter the third score: "))
    try:
        if (score1 >= 0) and (score2 >= 0) and (score3 >= 0):
           return round((score1 + score2 + score3)/3, 2)
        else:
            raise ValueError
    except ValueError:
        print("You entered a negative test score.")





if __name__ == '__main__':

    last_name = input("Enter a last name: ")
    first_name = input("Enter a first name: ")

    score = average_score()

    print(last_name, ',', first_name, "- average grade:", score)



